# slides/_tools

Tooling for extracting media + text from the source PowerPoints (which are
gitignored at `slides/*.pptx`) into the gitignored work area `slides/_extracted/`.

## Setup

```bash
python -m pip install -r slides/_tools/requirements.txt
```

## Extract everything

```bash
python slides/_tools/extract.py slides/*.pptx
```

Per source deck this writes:

- `slides/_extracted/<deck-stem>/media/` — every embedded image/video, original filenames preserved
- `slides/_extracted/<deck-stem>/slides.json` — `[{index, title, body, notes, media[]}]`
- `slides/_extracted/<deck-stem>/inventory.md` — human-readable summary used to build the week mapping

The `_extracted/` tree is large (multi-GB) and gitignored. Re-running is idempotent.

## Optimize images for the web

(See `slides/_tools/optimize.py` if/when added — not part of the current
extraction step. For now, hand-pick the images each reveal deck needs from
`_extracted/<deck>/media/` and run a one-shot `Pillow` resize/convert.)
