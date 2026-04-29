"""Render a reveal.js deck from a manifest JSON.

Manifest schema (annotated):
{
  "week": "w01",
  "title": "Workshop 1: Introducing AI for DH Pedagogy",
  "subtitle": "...",
  "session": {"date": "...", "time": "...", "location": "..."},
  "slides": [
    { "layout": "cover", "title": "...", "subtitle": "...", "image": {"src": "x.webp"} },
    { "layout": "section", "kicker": "Part 1", "title": "..." },
    { "layout": "image-bullets",
      "title": "...",
      "bullets": ["...", "..."],
      "image": {"src": "x.webp", "alt": "..."},
      "media": [{"source": "AI_Week_One", "file": "image9.png", "as": "x", "kind": "image"}] },
    { "layout": "quote", "quote": "...", "attribution": "...", "image": {...} },
    { "layout": "video", "title": "...", "video": {"src": "demo.webm"}, "caption": "..." },
    { "layout": "demo-slot", "title": "Live demo", "note": "..." },
    { "layout": "two-col", "title": "...", "left": "...", "right": "..." },
    { "layout": "exercise", "title": "...", "prompt": "...", "steps": ["...", "..."] },
    { "layout": "closing", "title": "...", "links": [{"label": "...", "url": "..."}] }
  ]
}

The renderer:
- Calls optimize.py logic on every `media` entry to produce assets/slides/<week>/.
- Emits slides/web/<week>/index.html using reveal.js via jsDelivr CDN.
- Pulls in /assets/css/style.css to inherit the modern-quilt color tokens
  and font families, then layers a small reveal-specific override block.
"""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

from PIL import Image
import imageio_ffmpeg


REPO_ROOT = Path(__file__).resolve().parents[2]
EXTRACTED = REPO_ROOT / "slides" / "_extracted"
ASSETS_OUT = REPO_ROOT / "assets" / "slides"
DECK_OUT = REPO_ROOT / "slides" / "web"

IMAGE_MAX_WIDTH = 1600
WEBP_QUALITY = 82
VIDEO_MAX_BYTES = 10 * 1024 * 1024


def optimize_image(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
        else:
            im = im.convert("RGB")
        if im.width > IMAGE_MAX_WIDTH:
            new_h = round(im.height * (IMAGE_MAX_WIDTH / im.width))
            im = im.resize((IMAGE_MAX_WIDTH, new_h), Image.LANCZOS)
        im.save(dst, format="WEBP", quality=WEBP_QUALITY, method=6)


def optimize_video(src: Path, dst: Path) -> bool:
    if src.stat().st_size > VIDEO_MAX_BYTES:
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg, "-y", "-loglevel", "error",
        "-i", str(src),
        "-vf", "scale=640:-2",
        "-c:v", "libvpx-vp9",
        "-b:v", "0", "-crf", "36",
        "-an", "-pix_fmt", "yuv420p",
        str(dst),
    ]
    subprocess.run(cmd, check=True)
    return True


def process_media(manifest: dict, out_dir: Path) -> dict:
    """Walk every slide's `media` entries and produce optimized assets.

    Returns {as_slug: {"path": "x.webp"|"x.webm", "kind": "image"|"video", "skipped": bool}}.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, dict] = {}
    for slide in manifest.get("slides", []):
        for m in slide.get("media", []):
            slug = m["as"]
            kind = m.get("kind", "image")
            # Either {"path": "hal.jpg"} relative to the repo root,
            # or {"source": "<deck>", "file": "imageN.png"} pulled from extraction.
            if "path" in m:
                src = REPO_ROOT / m["path"]
            else:
                src = EXTRACTED / m["source"] / "media" / m["file"]
            if not src.exists():
                rel = src.relative_to(REPO_ROOT) if src.is_relative_to(REPO_ROOT) else src
                print(f"  MISSING: {rel}", file=sys.stderr)
                continue
            label = m.get("path") or f"{m.get('source')}/{m.get('file')}"
            if kind == "image":
                dst = out_dir / f"{slug}.webp"
                optimize_image(src, dst)
                results[slug] = {"path": dst.name, "kind": "image", "skipped": False}
                print(f"  img  {label} -> {dst.name}")
            elif kind == "video":
                dst = out_dir / f"{slug}.webm"
                ok = optimize_video(src, dst)
                results[slug] = {
                    "path": dst.name if ok else None,
                    "kind": "video",
                    "skipped": not ok,
                }
                tag = "video" if ok else "skip "
                size_mb = src.stat().st_size // 1024 // 1024
                print(f"  {tag} {label} ({size_mb} MB) -> {dst.name if ok else '(skipped)'}")
            else:
                dst = out_dir / f"{slug}{src.suffix}"
                shutil.copy2(src, dst)
                results[slug] = {"path": dst.name, "kind": "other", "skipped": False}
    return results


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def md_inline(s: str) -> str:
    """Tiny inline-markdown converter for **bold**, *italic*, [link](url), `code`."""
    if not s:
        return ""
    import re
    s = esc(s)
    # links first (since they contain bracket/paren chars)
    def _link(m: "re.Match[str]") -> str:
        return f'<a href="{site_url(m.group(2))}">{m.group(1)}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", _link, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


# Decks live at slides/web/<week>/index.html — three levels deep from repo root.
SITE_ROOT_REL = "../../.."


def site_url(path: str) -> str:
    """Convert a repo-root-relative path (starting with /) to a path relative
    to the deck's index.html, so the deck works under GitHub Pages baseurl
    without Jekyll processing. External URLs are returned unchanged.
    """
    if not path:
        return path
    if path.startswith(("http://", "https://", "mailto:", "#")):
        return path
    if path.startswith("/"):
        return SITE_ROOT_REL + path
    return path


def img_tag(image: dict | None, week: str) -> str:
    if not image:
        return ""
    src = site_url(f"/assets/slides/{week}/{image['src']}")
    alt = esc(image.get("alt", ""))
    return f'<img src="{src}" alt="{alt}" loading="lazy">'


def video_tag(video: dict | None, week: str) -> str:
    if not video:
        return ""
    src = site_url(f"/assets/slides/{week}/{video['src']}")
    poster = ""
    if "poster" in video:
        poster = f' poster="{site_url(f"/assets/slides/{week}/{video["poster"]}")}"'
    return f'<video src="{src}"{poster} autoplay muted loop playsinline></video>'


def render_slide(slide: dict, week: str) -> str:
    layout = slide.get("layout", "image-bullets")
    title = slide.get("title", "")
    sid = slide.get("id", "")
    sec_attrs = f' id="{esc(sid)}"' if sid else ""

    if layout == "cover":
        return dedent(f"""\
        <section class="slide-cover"{sec_attrs}>
          {img_tag(slide.get("image"), week)}
          <div class="cover-text">
            <h1>{md_inline(title)}</h1>
            {f'<p class="subtitle">{md_inline(slide.get("subtitle",""))}</p>' if slide.get("subtitle") else ''}
            {f'<p class="cover-meta">{md_inline(slide.get("meta",""))}</p>' if slide.get("meta") else ''}
          </div>
        </section>""")

    if layout == "section":
        return dedent(f"""\
        <section class="slide-section"{sec_attrs}>
          {f'<p class="kicker">{md_inline(slide.get("kicker",""))}</p>' if slide.get("kicker") else ''}
          <h2>{md_inline(title)}</h2>
          {f'<p class="lead">{md_inline(slide.get("lead",""))}</p>' if slide.get("lead") else ''}
        </section>""")

    if layout == "quote":
        no_img = " no-image" if not slide.get("image") else ""
        q = slide["quote"]
        if isinstance(q, list):
            quote_inner = "".join(f"<p>{md_inline(p)}</p>" for p in q)
            long_cls = " long-quote" if len(q) >= 3 else ""
        else:
            quote_inner = md_inline(q)
            long_cls = ""
        return dedent(f"""\
        <section class="slide-quote{no_img}{long_cls}"{sec_attrs}>
          {img_tag(slide.get("image"), week)}
          <div class="quote-text">
            <blockquote>{quote_inner}</blockquote>
            {f'<p class="attribution">— {md_inline(slide.get("attribution",""))}</p>' if slide.get("attribution") else ''}
          </div>
        </section>""")

    if layout == "image-bullets":
        bullets = slide.get("bullets", [])
        bullet_html = "\n".join(f"<li>{md_inline(b)}</li>" for b in bullets)
        no_img = " no-image" if not slide.get("image") else ""
        kicker = slide.get("kicker", "")
        kicker_html = f'<p class="kicker">{md_inline(kicker)}</p>' if kicker else ''
        caption = slide.get("caption", "")
        caption_html = f'<p class="caption">{md_inline(caption)}</p>' if caption else ''
        return dedent(f"""\
        <section class="slide-image-bullets{no_img}"{sec_attrs}>
          <div class="bullets-text">
            {kicker_html}
            <h2>{md_inline(title)}</h2>
            {f'<ul>{bullet_html}</ul>' if bullets else ''}
            {caption_html}
          </div>
          {img_tag(slide.get("image"), week)}
        </section>""")

    if layout == "image-only":
        return dedent(f"""\
        <section class="slide-image-only"{sec_attrs}>
          {img_tag(slide.get("image"), week)}
          {f'<p class="caption">{md_inline(slide.get("caption",""))}</p>' if slide.get("caption") else ''}
        </section>""")

    if layout == "video":
        return dedent(f"""\
        <section class="slide-video"{sec_attrs}>
          {f'<h2>{md_inline(title)}</h2>' if title else ''}
          {video_tag(slide.get("video"), week)}
          {f'<p class="caption">{md_inline(slide.get("caption",""))}</p>' if slide.get("caption") else ''}
        </section>""")

    if layout == "demo-slot":
        return dedent(f"""\
        <section class="slide-demo-slot"{sec_attrs}>
          <p class="kicker">Live demo</p>
          <h2>{md_inline(title)}</h2>
          {f'<p>{md_inline(slide.get("note",""))}</p>' if slide.get("note") else ''}
        </section>""")

    if layout == "exercise":
        steps = slide.get("steps", [])
        step_html = "\n".join(f"<li>{md_inline(s)}</li>" for s in steps)
        return dedent(f"""\
        <section class="slide-exercise"{sec_attrs}>
          <p class="kicker">Exercise</p>
          <h2>{md_inline(title)}</h2>
          {f'<p class="prompt">{md_inline(slide.get("prompt",""))}</p>' if slide.get("prompt") else ''}
          {f'<ol>{step_html}</ol>' if steps else ''}
        </section>""")

    if layout == "two-col":
        return dedent(f"""\
        <section class="slide-two-col"{sec_attrs}>
          {f'<h2>{md_inline(title)}</h2>' if title else ''}
          <div class="cols">
            <div class="col"><h3>{md_inline(slide.get("left_title",""))}</h3>{md_inline(slide.get("left",""))}</div>
            <div class="col"><h3>{md_inline(slide.get("right_title",""))}</h3>{md_inline(slide.get("right",""))}</div>
          </div>
        </section>""")

    if layout == "closing":
        links = slide.get("links", [])
        link_html = "\n".join(f'<li><a href="{esc(site_url(l["url"]))}">{md_inline(l["label"])}</a></li>' for l in links)
        return dedent(f"""\
        <section class="slide-closing"{sec_attrs}>
          <h2>{md_inline(title)}</h2>
          {f'<p class="lead">{md_inline(slide.get("lead",""))}</p>' if slide.get("lead") else ''}
          {f'<ul class="links">{link_html}</ul>' if links else ''}
        </section>""")

    raise ValueError(f"Unknown layout: {layout}")


HEAD_TEMPLATE = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css" id="reveal-theme">
<link rel="stylesheet" href="../../../assets/css/style.css">
<style>
:root {{
  --slide-pad: clamp(1.25rem, 3vw, 3rem);
}}
.reveal {{
  font-family: 'Inter', -apple-system, system-ui, sans-serif;
  color: var(--ink, #141414);
  background: var(--bone, #faf6ec);
}}
.reveal .slides {{ text-align: left; }}
.reveal .slides section {{
  padding: var(--slide-pad);
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  box-sizing: border-box;
}}
.reveal h1, .reveal h2, .reveal h3 {{
  font-family: 'Bricolage Grotesque', 'Inter', serif;
  color: var(--ink, #141414);
  text-transform: none;
  letter-spacing: -0.01em;
  margin: 0 0 0.5em;
  line-height: 1.05;
}}
.reveal h1 {{ font-size: clamp(2.4rem, 6vw, 4.2rem); }}
.reveal h2 {{ font-size: clamp(2rem, 5vw, 3.4rem); }}
.reveal h3 {{ font-size: clamp(1.4rem, 3.5vw, 2rem); }}
.reveal p, .reveal li {{ font-size: clamp(1.1rem, 2.4vw, 1.6rem); line-height: 1.4; }}
.reveal a {{ color: var(--cobalt, #1545c4); }}
.reveal code {{ font-family: 'JetBrains Mono', 'Courier New', monospace; background: rgba(0,0,0,0.06); padding: 0.05em 0.25em; border-radius: 3px; font-size: 0.9em; }}
.reveal blockquote {{ border-left: 4px solid var(--coral, #ff5a4e); padding: 0.25em 0 0.25em 1rem; margin: 0; font-size: clamp(1.2rem, 2.8vw, 1.9rem); font-style: normal; line-height: 1.35; width: auto; box-shadow: none; }}
.reveal .kicker {{ font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--coral, #ff5a4e); margin: 0 0 0.5rem; }}
.reveal .attribution {{ font-size: 1rem; color: var(--muted, #5a5a5a); margin-top: 0.5rem; }}
.reveal .caption {{ font-size: 1rem; color: var(--muted, #5a5a5a); margin-top: 0.75rem; }}
.reveal .lead {{ font-size: clamp(1.2rem, 2.6vw, 1.8rem); color: var(--muted, #5a5a5a); }}

.reveal img, .reveal video {{ max-width: 100%; max-height: 60vh; object-fit: contain; border-radius: 6px; }}

/* Cover */
.reveal .slide-cover {{ background: var(--ink, #141414); color: var(--bone, #faf6ec); position: relative; overflow: hidden; }}
.reveal .slide-cover img {{ position: absolute; inset: 0; width: 100%; height: 100%; max-height: none; object-fit: cover; opacity: 0.35; border-radius: 0; }}
.reveal .slide-cover .cover-text {{ position: relative; z-index: 1; }}
.reveal .slide-cover h1 {{ color: var(--bone, #faf6ec); }}
.reveal .slide-cover .subtitle {{ font-family: 'Bricolage Grotesque', serif; font-size: clamp(1.4rem, 3vw, 2rem); color: var(--mustard, #e8b53a); margin: 0.5rem 0 1.5rem; }}
.reveal .slide-cover .cover-meta {{ font-family: 'JetBrains Mono', monospace; font-size: 1rem; color: var(--bone, #faf6ec); opacity: 0.85; }}

/* Section divider */
.reveal .slide-section {{ background: var(--coral, #ff5a4e); color: var(--ink, #141414); }}
.reveal .slide-section h2 {{ font-size: clamp(2.5rem, 7vw, 5rem); }}
.reveal .slide-section .kicker {{ color: var(--ink, #141414); }}
.reveal .slide-section .lead {{ color: var(--ink, #141414); max-width: 60ch; }}

/* Image-bullets */
.reveal .slide-image-bullets {{ display: grid !important; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; }}
.reveal .slide-image-bullets.no-image {{ display: block !important; max-width: 70ch; margin-left: auto !important; margin-right: auto !important; }}
.reveal .slide-image-bullets img {{ max-height: 75vh; }}
.reveal .slide-image-bullets ul {{ list-style: none; padding: 0; margin: 0; }}
.reveal .slide-image-bullets li {{ padding-left: 1.5em; position: relative; margin-bottom: 0.7rem; }}
.reveal .slide-image-bullets li::before {{ content: ""; position: absolute; left: 0; top: 0.55em; width: 0.7em; height: 0.7em; background: var(--coral, #ff5a4e); border-radius: 2px; transform: rotate(45deg); }}
@media (max-width: 800px) {{ .reveal .slide-image-bullets {{ grid-template-columns: 1fr; }} }}

/* Image-only */
.reveal .slide-image-only {{ align-items: center; text-align: center; }}
.reveal .slide-image-only img {{ max-height: 80vh; }}

/* Quote */
.reveal .slide-quote {{ display: grid !important; grid-template-columns: 1fr 1.4fr; gap: 2rem; align-items: center; background: var(--bone, #faf6ec); }}
.reveal .slide-quote.no-image {{ display: block !important; max-width: 60ch; margin-left: auto !important; margin-right: auto !important; }}
.reveal .slide-quote.no-image blockquote {{ font-size: clamp(1.6rem, 3.4vw, 2.4rem); }}
.reveal .slide-quote blockquote p {{ margin: 0 0 0.7em; }}
.reveal .slide-quote blockquote p:last-child {{ margin-bottom: 0; }}
.reveal .slide-quote.long-quote.no-image {{ max-width: 70ch; }}
.reveal .slide-quote.long-quote blockquote {{ font-size: clamp(1rem, 1.9vw, 1.3rem); line-height: 1.45; }}
.reveal .slide-quote.long-quote blockquote code {{ font-size: 0.95em; }}
.reveal .slide-quote img {{ max-height: 70vh; }}
@media (max-width: 800px) {{ .reveal .slide-quote {{ grid-template-columns: 1fr; }} }}

/* Video */
.reveal .slide-video video {{ width: 100%; max-height: 65vh; }}

/* Demo slot */
.reveal .slide-demo-slot {{ background: var(--mustard, #e8b53a); color: var(--ink, #141414); }}
.reveal .slide-demo-slot .kicker {{ color: var(--ink, #141414); }}

/* Exercise */
.reveal .slide-exercise {{ background: var(--sage, #7a8f4a); color: var(--ink, #141414); }}
.reveal .slide-exercise .kicker {{ color: var(--ink, #141414); }}
.reveal .slide-exercise ol {{ counter-reset: ex; padding-left: 0; list-style: none; }}
.reveal .slide-exercise ol li {{ counter-increment: ex; padding-left: 2.5em; position: relative; margin-bottom: 0.7rem; }}
.reveal .slide-exercise ol li::before {{ content: counter(ex); position: absolute; left: 0; top: 0; font-family: 'Bricolage Grotesque', serif; font-weight: 700; font-size: 1.4em; color: var(--ink, #141414); }}
.reveal .slide-exercise .prompt {{ font-style: italic; max-width: 60ch; }}

/* Two-col */
.reveal .slide-two-col .cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }}
@media (max-width: 800px) {{ .reveal .slide-two-col .cols {{ grid-template-columns: 1fr; }} }}

/* Closing */
.reveal .slide-closing {{ background: var(--plum, #5d2e5f); color: var(--bone, #faf6ec); }}
.reveal .slide-closing h2 {{ color: var(--bone, #faf6ec); }}
.reveal .slide-closing a {{ color: var(--mustard, #e8b53a); }}
.reveal .slide-closing .lead {{ color: var(--bone, #faf6ec); opacity: 0.9; }}
.reveal .slide-closing .links {{ list-style: none; padding: 0; }}
.reveal .slide-closing .links li {{ margin-bottom: 0.5rem; }}

/* Progress bar / controls in coral */
.reveal .progress {{ color: var(--coral, #ff5a4e); }}
.reveal .controls {{ color: var(--coral, #ff5a4e); }}

/* Back-to-workshop link, fixed top-right of every deck */
.deck-back {{
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 100;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: var(--bone, #faf6ec);
  color: var(--ink, #141414);
  text-decoration: none;
  padding: 0.4rem 0.8rem;
  border: 2px solid var(--ink, #141414);
  box-shadow: 2px 2px 0 var(--ink, #141414);
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}}
.deck-back:hover {{
  transform: translate(-1px, -1px);
  box-shadow: 3px 3px 0 var(--ink, #141414);
  background: var(--coral, #ff5a4e);
}}
.deck-back:active {{
  transform: translate(1px, 1px);
  box-shadow: 0 0 0 var(--ink, #141414);
}}
@media print {{ .deck-back {{ display: none; }} }}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">
"""

FOOT_TEMPLATE = """\
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    center: false,
    width: 1280,
    height: 800,
    margin: 0.04,
    transition: 'fade',
    controlsTutorial: false
  });
</script>
</body>
</html>
"""


def render_deck(manifest_path: Path) -> Path:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    week = manifest["week"]
    print(f"\n[render] {week}")

    asset_dir = ASSETS_OUT / week
    process_media(manifest, asset_dir)

    deck_dir = DECK_OUT / week
    deck_dir.mkdir(parents=True, exist_ok=True)

    # Map deck slug "wNN" -> week page "/weeks/week-NN.html"
    week_num = week.lstrip("w").lstrip("0") or "0"
    week_page = site_url(f"/weeks/week-{week_num.zfill(2)}.html")
    back_link = f'<a class="deck-back" href="{week_page}" title="Back to workshop page">← Workshop</a>\n'

    body = "\n".join(render_slide(s, week) for s in manifest["slides"])
    head = HEAD_TEMPLATE.format(title=esc(manifest["title"]))
    # Inject back_link as a direct child of <body>, outside <div class="reveal">,
    # so position:fixed isn't broken by reveal's transformed ancestor.
    head = head.replace("<body>\n", f"<body>\n{back_link}", 1)
    html_out = head + body + "\n" + FOOT_TEMPLATE

    out = deck_dir / "index.html"
    out.write_text(html_out, encoding="utf-8")
    print(f"  -> {out.relative_to(REPO_ROOT)} ({len(manifest['slides'])} slides)")
    return out


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("manifests", nargs="+", type=Path)
    args = p.parse_args(argv)
    for m in args.manifests:
        render_deck(m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
