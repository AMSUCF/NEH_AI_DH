# Session Recap Pages — Design

**Date:** 2026-07-14
**Status:** Approved

## Purpose

Each live workshop in the NEH AI+DH series is recorded on Zoom. After each session, a
public-facing recap page is added to the site so people who missed the workshop can read
what happened, sticking as close as possible to what was actually said, illustrated with
screenshots pulled from the recording. Recaps are linked from each week's page, directly
under the slide deck link.

The first recap covers Workshop 1 (May 13, 2026), presented by Mel Stanfill.

## Source material

Zoom exports live in `videos/` at the repo root — the standing drop-zone for each week's
files, **never committed** (the mp4 alone is 380 MB):

- `*_Recording_1920x1040.mp4` — the recording (source for screenshots)
- `*_Recording.transcript.vtt` — timestamped transcript (source for quotes; timecodes
  align with the video)
- `*_RecordingnewChat.txt` — Zoom chat log
- `*_Recording.m4a` — audio only (unused)

`videos/` is added to `.gitignore`.

## Decisions (from brainstorming)

1. **Privacy — presenters only, by name.** Only the presenter(s) are quoted and named.
   Participant questions and chat comments are paraphrased without names ("a participant
   noted…"). Screenshots favor slides/screen-share; no attendee gallery or webcam strips.
2. **Format — narrative walkthrough.** Prose recap following the session chronologically,
   with direct presenter quotes woven in and roughly one screenshot per major segment
   (6–10 images). No timestamps in the page body; no link to the recording for now.
3. **Presenter attribution.** Zoom's speaker labels are unreliable (the W1 transcript tags
   every line to the host account). Workshop 1 was presented by Mel Stanfill. For future
   weeks with multiple or different presenters, confirming who presented (and who said
   what, via the video where needed) is an explicit per-week checklist step — ask
   Anastasia before attributing quotes.
4. **Approach — editorial pass with documented conventions**, not a parsing/scaffolding
   script. The repeatable parts are conventions plus an ffmpeg one-liner; the selection of
   quotes, frames, and structure is editorial judgment each week.

## Components

### 1. Recap page: `weeks/week-NN-recap.md`

Front matter: `title: "Workshop N Recap: <short title>"` (default layout applies via
`_config.yml` defaults). Body structure:

- **Header block** — workshop date, "Led by <presenter>", one-paragraph summary of the
  session.
- **One section per major segment** as it actually unfolded (the week page's "Session
  Outline" is scaffolding, but the transcript's real order wins). Each section: faithful
  prose recap, 1–3 direct presenter quotes, one screenshot with descriptive alt text.
- **Participant voice** — paraphrased, anonymous, woven in where it shaped the session.
- **Closing** — pointer to the week's core exercise for those who missed the session.
- **Footer note** — quotes are lightly edited for filler words/false starts only.

### 2. Link from the week page

In `weeks/week-NN.md`, inside the existing `workshop-callout` div, a second button line
under the slide deck link:

```markdown
[Session recap →](week-NN-recap.md){:.btn}
```

`jekyll-relative-links` rewrites the `.md` href to the rendered URL, matching existing
site conventions.

### 3. Screenshots: `assets/recaps/wNN/`

- Extracted from the mp4 with ffmpeg at timestamps chosen from the transcript.
- Naming: `NN-slug.jpg` in section order (e.g. `01-eliza-demo.jpg`).
- Sizing: 1200 px wide, JPEG quality ~85 — keeps a full week's images well under
  ~1.5 MB committed.
- Extraction command pattern:
  `ffmpeg -ss HH:MM:SS -i <mp4> -frames:v 1 -vf scale=1200:-2 -q:v 4 <out.jpg>`
- **Privacy screen:** every frame is visually reviewed before use. Prefer full-frame
  slide/demo captures; if a webcam thumbnail or attendee gallery appears, crop it out or
  pick a different frame.

### 4. Workflow doc: `docs/recap-workflow.md`

The per-week checklist so weeks 2–12 follow identically:

1. Drop Zoom exports into `videos/` (gitignored).
2. Confirm presenter(s) with Anastasia — never trust Zoom speaker labels.
3. Read the full transcript; map segments against the week page outline.
4. Select quotes (faithful, lightly cleaned) and paraphrase participant contributions
   anonymously.
5. Extract frames at chosen timestamps; privacy-review each; save to `assets/recaps/wNN/`.
6. Write `weeks/week-NN-recap.md`; add the recap button to `weeks/week-NN.md`.
7. Build/preview check, then commit page + images (never the videos).

## Error handling / edge cases

- **Transcript/video timecode drift:** VTT times matched the video in W1; spot-check one
  frame against its quote each week before extracting the full set.
- **No usable people-free frame for a segment:** crop, or skip the screenshot for that
  segment rather than publish attendee faces.
- **Ambiguous speaker on a key quote:** verify against the video/audio; if still unclear,
  paraphrase instead of quoting.

## Testing

- `bundle exec jekyll build` (or serve) succeeds; recap page renders with images and the
  week-page button links correctly.
- `git status` confirms `videos/` is ignored.
- Visual pass over every committed screenshot for privacy.
