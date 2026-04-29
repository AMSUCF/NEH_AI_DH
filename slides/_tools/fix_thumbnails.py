"""Replace speaker-camera thumbnail images in manifests with real slide content.

In the source PowerPoints, Anastasia's recorded camera overlay leaves a
640×360 PNG thumbnail (~675 KB) embedded in nearly every slide. When the
extractor's per-slide media list contains both that thumbnail and a real
content image (article screenshot, diagram, photo), I sometimes picked the
thumbnail. This tool walks every manifest's `media` entry, locates the
*source slide* the picked file lives on (via slides.json), and swaps the
file reference for the largest non-thumbnail image on that same slide.

Usage:
    python slides/_tools/fix_thumbnails.py            # dry-run, show planned swaps
    python slides/_tools/fix_thumbnails.py --apply    # write the swaps back

After --apply, re-run render.py on the affected manifests.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image


REPO_ROOT = Path(__file__).resolve().parents[2]
EXTRACTED = REPO_ROOT / "slides" / "_extracted"
MANIFEST_DIR = REPO_ROOT / "slides" / "_tools" / "manifests"

SPEAKER_DIM = (640, 360)
SPEAKER_SIZE_BYTES_TOLERANCE = 0.10  # ±10% of the canonical thumbnail size


def is_speaker_thumbnail(path: Path, canonical_size: int | None = None) -> bool:
    """640×360 PNGs that match (or nearly match) the deck's speaker-thumbnail
    file size are speaker-camera overlays from the recorded PowerPoint.
    """
    try:
        with Image.open(path) as im:
            if (im.width, im.height) != SPEAKER_DIM:
                return False
    except Exception:
        return False
    if canonical_size is None:
        return True  # all 640×360 PNGs treated as speaker
    actual = path.stat().st_size
    return abs(actual - canonical_size) / canonical_size < SPEAKER_SIZE_BYTES_TOLERANCE


def find_speaker_canonical_size(media_dir: Path) -> int | None:
    """Find the most common file size among 640×360 PNGs in this deck.
    That's almost certainly the speaker thumbnail."""
    sizes: dict[int, int] = {}
    for p in media_dir.glob("image*.png"):
        try:
            with Image.open(p) as im:
                if (im.width, im.height) != SPEAKER_DIM:
                    continue
        except Exception:
            continue
        s = p.stat().st_size
        sizes[s] = sizes.get(s, 0) + 1
    if not sizes:
        return None
    return max(sizes.items(), key=lambda kv: kv[1])[0]


def best_image_for_slide(deck: str, slide_idx: int) -> str | None:
    """Return the filename of the best content image on this slide, or None."""
    media_dir = EXTRACTED / deck / "media"
    slides = json.loads((EXTRACTED / deck / "slides.json").read_text(encoding="utf-8"))
    speaker_size = find_speaker_canonical_size(media_dir)
    for s in slides:
        if s["index"] != slide_idx:
            continue
        candidates: list[tuple[int, str]] = []
        for fname in s["media"]:
            if not fname.lower().endswith((".png", ".jpg", ".jpeg")):
                continue
            p = media_dir / fname
            if not p.exists():
                continue
            if is_speaker_thumbnail(p, speaker_size):
                continue
            try:
                with Image.open(p) as im:
                    area = im.width * im.height
            except Exception:
                continue
            candidates.append((area, fname))
        if not candidates:
            return None
        candidates.sort(reverse=True)
        return candidates[0][1]
    return None


def find_source_slide(deck: str, file_name: str) -> int | None:
    """Find the slide a given media filename lives on. Returns 1-based index."""
    slides = json.loads((EXTRACTED / deck / "slides.json").read_text(encoding="utf-8"))
    for s in slides:
        if file_name in s["media"]:
            return s["index"]
    return None


def fix_manifest(manifest_path: Path, apply: bool) -> tuple[int, int]:
    text = manifest_path.read_text(encoding="utf-8")
    manifest = json.loads(text)
    media_dir_for = lambda deck: EXTRACTED / deck / "media"

    swaps: list[tuple[str, str, str, str, int]] = []
    drops: list[tuple[str, str, str, int]] = []
    for slide in manifest.get("slides", []):
        sid = slide.get("id", "?")
        new_media: list[dict] = []
        drop_image = False
        for m in slide.get("media", []):
            if m.get("kind", "image") != "image":
                new_media.append(m)
                continue
            deck = m["source"]
            old_file = m["file"]
            old_path = media_dir_for(deck) / old_file
            if not old_path.exists():
                print(f"  [{sid}] MISSING source file: {deck}/{old_file}", file=sys.stderr)
                new_media.append(m)
                continue
            speaker_size = find_speaker_canonical_size(media_dir_for(deck))
            if not is_speaker_thumbnail(old_path, speaker_size):
                new_media.append(m)
                continue
            slide_idx = find_source_slide(deck, old_file)
            if slide_idx is None:
                print(f"  [{sid}] no source slide for {deck}/{old_file}", file=sys.stderr)
                new_media.append(m)
                continue
            new_file = best_image_for_slide(deck, slide_idx)
            if new_file is None:
                drops.append((sid, deck, old_file, slide_idx))
                drop_image = True
                continue  # remove this media entry entirely
            if new_file == old_file:
                new_media.append(m)
                continue
            swaps.append((sid, deck, old_file, new_file, slide_idx))
            if apply:
                m["file"] = new_file
            new_media.append(m)
        if apply:
            slide["media"] = new_media
            if drop_image and "image" in slide:
                del slide["image"]

    for sid, deck, old, new, idx in swaps:
        print(f"  [{sid}] {deck} slide {idx}: {old} -> {new}")
    for sid, deck, old, idx in drops:
        print(f"  [{sid}] {deck} slide {idx}: drop {old} (no content image; quote will render text-only)")

    if apply and (swaps or drops):
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return len(swaps), len(drops)


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    p.add_argument("--manifest", type=Path, action="append", help="specific manifest(s); defaults to all")
    args = p.parse_args(argv)

    paths = args.manifest or sorted(MANIFEST_DIR.glob("w*.json"))
    total_swaps = 0
    total_drops = 0
    for path in paths:
        print(f"\n[{path.name}]")
        s, d = fix_manifest(path, args.apply)
        total_swaps += s
        total_drops += d
        print(f"  {s} swap(s), {d} drop(s){' applied' if args.apply else ' planned (dry run)'}")
    print(f"\nTotal: {total_swaps} swap(s), {total_drops} drop(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
