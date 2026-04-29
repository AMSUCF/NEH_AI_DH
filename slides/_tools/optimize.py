"""Optimize selected media into assets/slides/wXX/ for the reveal.js decks.

Usage (from repo root):
    python slides/_tools/optimize.py --week w01 --manifest slides/_tools/manifests/w01.json

Manifest schema (JSON):
    {
      "week": "w01",
      "slides": [
        {
          "id": "title",
          "source": "AI_Week_One",
          "source_slide": 1,
          "media": [
            {"file": "image1.png", "as": "title-cover", "kind": "image"}
          ]
        },
        {
          "id": "eliza-history",
          "source": "AI_Week_One",
          "source_slide": 32,
          "media": [
            {"file": "media5.mp4", "as": "eliza-demo", "kind": "video"}
          ]
        }
      ]
    }

Behavior:
  - Images: resize to max 1600px wide, save as WebP @ Q82.
  - Videos: only if file size < 10MB; convert to looping .webm (VP9, no audio,
    640px wide). Larger videos are skipped — the deck slot is left as a
    placeholder for live demo per user direction.
  - Output filenames use the manifest's `as` slug + extension.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image
import imageio_ffmpeg


REPO_ROOT = Path(__file__).resolve().parents[2]
EXTRACTED = REPO_ROOT / "slides" / "_extracted"
ASSETS_OUT = REPO_ROOT / "assets" / "slides"

IMAGE_MAX_WIDTH = 1600
WEBP_QUALITY = 82
VIDEO_MAX_BYTES = 10 * 1024 * 1024  # 10 MB
VIDEO_TARGET_WIDTH = 640


def optimize_image(src: Path, dst: Path) -> None:
    """Resize to max width and save as WebP. Preserves aspect ratio."""
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
    print(f"  image: {src.name} -> {dst.relative_to(REPO_ROOT)} ({dst.stat().st_size // 1024} KB)")


def optimize_video(src: Path, dst: Path) -> bool:
    """Convert to small VP9 webm if under size threshold. Returns True if converted."""
    size = src.stat().st_size
    if size > VIDEO_MAX_BYTES:
        print(f"  video: {src.name} skipped ({size // 1024 // 1024} MB > 10 MB) — leave live-demo slot")
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg, "-y", "-loglevel", "error",
        "-i", str(src),
        "-vf", f"scale={VIDEO_TARGET_WIDTH}:-2",
        "-c:v", "libvpx-vp9",
        "-b:v", "0", "-crf", "36",
        "-an",
        "-pix_fmt", "yuv420p",
        str(dst),
    ]
    subprocess.run(cmd, check=True)
    print(f"  video: {src.name} -> {dst.relative_to(REPO_ROOT)} ({dst.stat().st_size // 1024} KB)")
    return True


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--week", required=True, help="e.g. w01")
    p.add_argument("--manifest", required=True, type=Path)
    args = p.parse_args(argv)

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    week = manifest["week"]
    if week != args.week:
        print(f"manifest week ({week}) != --week ({args.week})", file=sys.stderr)
        return 2

    out_dir = ASSETS_OUT / week
    out_dir.mkdir(parents=True, exist_ok=True)

    skipped_videos: list[dict] = []
    for slide in manifest.get("slides", []):
        sid = slide["id"]
        deck = slide["source"]
        deck_media = EXTRACTED / deck / "media"
        for m in slide.get("media", []):
            src = deck_media / m["file"]
            if not src.exists():
                print(f"  MISSING: {deck}/media/{m['file']}", file=sys.stderr)
                continue
            print(f"[{sid}] from {deck}/{m['file']}")
            if m["kind"] == "image":
                ext = ".webp"
                dst = out_dir / f"{m['as']}{ext}"
                optimize_image(src, dst)
            elif m["kind"] == "video":
                dst = out_dir / f"{m['as']}.webm"
                converted = optimize_video(src, dst)
                if not converted:
                    skipped_videos.append({"slide": sid, "source": f"{deck}/media/{m['file']}", "size_mb": src.stat().st_size // 1024 // 1024})
            else:
                # unknown -> just copy
                dst = out_dir / f"{m['as']}{src.suffix}"
                shutil.copy2(src, dst)

    if skipped_videos:
        print("\nSkipped videos (live-demo slots):")
        for s in skipped_videos:
            print(f"  - {s['slide']}: {s['source']} ({s['size_mb']} MB)")

    print(f"\nDone. {out_dir.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
