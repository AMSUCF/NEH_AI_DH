# Workshop Session Recap Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a public-facing recap page for Workshop 1 built from the Zoom recording/transcript/chat in `videos/`, linked under the slide deck button on the Week 1 page, plus the reusable workflow doc for weeks 2–12.

**Architecture:** Editorial pipeline, not code: gitignore the `videos/` drop-zone, mine the VTT transcript for structure and quotes, extract privacy-screened frames from the mp4 with ffmpeg into `assets/recaps/w01/`, write a narrative-walkthrough markdown page, and document the repeatable checklist.

**Tech Stack:** Jekyll (GitHub Pages, kramdown/GFM, jekyll-relative-links), ffmpeg 8.x, Zoom VTT/chat exports.

## Global Constraints

- **Privacy — presenters only, by name.** Only Mel Stanfill (W1 presenter) is quoted/named. Participants are paraphrased anonymously ("a participant asked…"). No attendee faces, names, or webcam strips in any committed screenshot.
- **Fidelity.** Quotes come verbatim from the VTT, cleaned only of filler words/false starts; the page footer discloses that editing. Prose recap must not put claims in the presenter's mouth that the transcript doesn't support.
- **Never commit `videos/`** (mp4 is 380 MB — over GitHub's hard limit).
- **Zoom speaker labels are unreliable** — the W1 VTT tags every line to one account. W1 attribution is confirmed (Mel Stanfill presented). Future weeks: confirm with Anastasia first.
- Images: 1200 px wide JPEG, ffmpeg `-q:v 4`, named `NN-slug.jpg`, ~6–10 per week, full week under ~1.5 MB.
- No timestamps in the page body; no recording link.
- Follow existing site conventions: default layout via `_config.yml` defaults (no explicit `layout:` needed), `.md` relative links (jekyll-relative-links rewrites them), `{:.btn}` for buttons.
- Repo paths below are relative to `C:\Users\anast\Documents\GitHub\NEH_AI_DH`. Source files: `videos/GMT20260513-135613_Recording_1920x1040.mp4`, `videos/GMT20260513-135613_Recording.transcript.vtt`, `videos/GMT20260513-135613_RecordingnewChat.txt`.

---

### Task 1: Gitignore the videos drop-zone

**Files:**
- Modify: `.gitignore` (append at end)

**Interfaces:**
- Produces: `videos/` permanently ignored; all later tasks may assume Zoom exports live there untracked.

- [ ] **Step 1: Append the ignore rule**

Add to the end of `.gitignore`:

```gitignore

# Zoom workshop recordings drop-zone (recap source material; mp4s exceed GitHub limits)
videos/
```

- [ ] **Step 2: Verify git ignores the folder**

Run: `git status --porcelain` and `git check-ignore -v videos/GMT20260513-135613_Recording_1920x1040.mp4`
Expected: `?? videos/` no longer appears in status; check-ignore prints the `.gitignore` rule line.

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "Ignore videos/ drop-zone for workshop recordings"
```

---

### Task 2: Mine the transcript — segment map and quote sheet (working notes, not committed)

**Files:**
- Read: `videos/GMT20260513-135613_Recording.transcript.vtt` (2,726 lines — read it all, in chunks), `videos/GMT20260513-135613_RecordingnewChat.txt`, `weeks/week-01.md` (Session Outline, lines 45–68)
- Create: `<scratchpad>/w01-recap-notes.md` (session scratchpad — never committed)

**Interfaces:**
- Produces: `w01-recap-notes.md` containing (a) a segment map — the session's real chronological segments, each with start/end `HH:MM:SS` from VTT cue times and a mapping to the week-01 outline item it corresponds to; (b) a quote sheet — for each segment, 1–3 verbatim quote candidates with their VTT timestamps; (c) participant moments to paraphrase (from transcript Q&A and the chat file, e.g. the 00:32:03 chat comment that ELIZA "mostly reiterates what you say"); (d) a screenshot shortlist — one timestamp per segment where the screen-share should show a slide/demo (typically mid-quote or right after a segment transition). Tasks 3 and 4 consume all four parts.

- [ ] **Step 1: Read the full VTT transcript** in sequential chunks (it is ~112 KB; use offset/limit reads). While reading, note segment boundaries (topic shifts: intro/logistics → ELIZA history/demo → how LLMs work → ChatGPT moment → landscape/agents → chatbot tour → Claude setup → build-an-ELIZA exercise → close) and copy out strong verbatim quote candidates with their cue timestamps. The actual segments found in the transcript override this expected list.

- [ ] **Step 2: Read the chat file** (`GMT20260513-135613_RecordingnewChat.txt`, 6 lines) and note which comments are worth paraphrasing anonymously.

- [ ] **Step 3: Write the notes file** to the session scratchpad as `w01-recap-notes.md` with the four sections named in Interfaces. Every quote must carry its `HH:MM:SS` timestamp; every screenshot-shortlist entry must name the segment slug it will illustrate (e.g. `02-eliza-demo`).

- [ ] **Step 4: Verify coverage**

Check: every major segment in the map has ≥1 quote candidate and exactly one shortlisted screenshot timestamp; intro logistics/small-talk (first ~13 min) explicitly marked "skip — not public-facing content."
Expected: 6–10 segments, each fully populated. No commit (nothing in the repo changed).

---

### Task 3: Extract and privacy-screen screenshots

**Files:**
- Create: `assets/recaps/w01/NN-slug.jpg` (one per shortlisted segment, 6–10 files)
- Consume: screenshot shortlist from `<scratchpad>/w01-recap-notes.md`

**Interfaces:**
- Consumes: Task 2's screenshot shortlist (segment slug + timestamp pairs).
- Produces: committed JPEGs at `assets/recaps/w01/NN-slug.jpg`; Task 4 references them as `{{ '/assets/recaps/w01/NN-slug.jpg' | relative_url }}`.

- [ ] **Step 1: Extract candidate frames to the scratchpad** (candidates first — not straight into the repo):

```bash
mkdir -p "<scratchpad>/frames"
ffmpeg -ss HH:MM:SS -i "videos/GMT20260513-135613_Recording_1920x1040.mp4" \
  -frames:v 1 -vf scale=1200:-2 -q:v 4 "<scratchpad>/frames/NN-slug.jpg"
```

One command per shortlist entry (they can run in one batch).

- [ ] **Step 2: Visually review every frame** with the Read tool (it renders images). Privacy screen per the Global Constraints: reject any frame showing attendee faces, names beyond the presenter's, or webcam gallery strips. Also reject blurry mid-transition frames. For rejects: either re-extract at a nearby timestamp (±5–30 s while the same slide is up) and re-review, or crop the offending region with `ffmpeg -i in.jpg -vf "crop=w:h:x:y" out.jpg` and re-review, or drop that segment's screenshot.

- [ ] **Step 3: Copy approved frames into the repo**

```bash
mkdir -p assets/recaps/w01
cp "<scratchpad>/frames/<approved>.jpg" assets/recaps/w01/
```

- [ ] **Step 4: Verify size budget**

Run: `du -sh assets/recaps/w01` and `ls -la assets/recaps/w01`
Expected: 6–10 files, total under ~1.5 MB. If over, re-encode the largest with `-q:v 6`.

- [ ] **Step 5: Commit**

```bash
git add assets/recaps/w01
git commit -m "Add Workshop 1 recap screenshots (privacy-screened)"
```

---

### Task 4: Write the Workshop 1 recap page

**Files:**
- Create: `weeks/week-01-recap.md`
- Consume: segment map, quote sheet, participant notes from `<scratchpad>/w01-recap-notes.md`; images from `assets/recaps/w01/`

**Interfaces:**
- Consumes: Task 2 notes (all content), Task 3 image filenames.
- Produces: the page Task 5 links to as `week-01-recap.md`.

- [ ] **Step 1: Write the page** with this skeleton (real content from the notes replaces the bracketed guidance; brackets must not survive into the file):

```markdown
---
title: "Workshop 1 Recap: Introducing AI for DH Pedagogy"
---

**Wednesday, May 13, 2026 · CHDR · Led by Mel Stanfill**

[One-paragraph summary of what the session covered and did, written from the
transcript — not copied from the week page.]

[← Back to Week 1](week-01.md)

## [Segment heading, e.g. "ELIZA and the ELIZA effect"]

[Faithful prose recap of what was said in this segment.]

> "[Verbatim quote from the transcript, lightly cleaned.]"

![Descriptive alt text of what the slide/demo shows]({{ '/assets/recaps/w01/NN-slug.jpg' | relative_url }})

[…repeat one section per segment, in the session's actual order…]

## Try It Yourself

[Pointer to the Week 1 core exercise (build-your-own-ELIZA) for readers who
missed the session, linking to week-01.md's Core Exercise section.]

---

*Quotes are drawn from the session transcript, lightly edited to remove filler
words and false starts. Participant comments are paraphrased without attribution.*
```

Rules while writing: every section's prose must be checkable against the transcript; participant contributions appear paraphrased and anonymous; each image gets descriptive alt text of the slide/demo content; no timestamps; no recording link.

- [ ] **Step 2: Verify fidelity** — for each quote in the page, re-open the matching VTT cue (by timestamp from the notes) and confirm the wording matches apart from filler removal. Confirm no participant name appears anywhere in the body.

Run: `grep -n -f <(cut -f2 videos/GMT20260513-135613_RecordingnewChat.txt | sort -u) weeks/week-01-recap.md` — simpler: grep the page for each chat-participant surname individually.
Expected: no matches for any participant name.

- [ ] **Step 3: Commit**

```bash
git add weeks/week-01-recap.md
git commit -m "Add Workshop 1 session recap"
```

---

### Task 5: Link the recap from the Week 1 page

**Files:**
- Modify: `weeks/week-01.md:23` (inside the `workshop-callout` div, after the slide deck button)

**Interfaces:**
- Consumes: `weeks/week-01-recap.md` from Task 4.

- [ ] **Step 1: Add the button.** In `weeks/week-01.md`, change:

```markdown
[Open the slide deck →]({{ '/slides/web/w01/' | relative_url }}){:.btn}
```

to:

```markdown
[Open the slide deck →]({{ '/slides/web/w01/' | relative_url }}){:.btn}

[Read the session recap →](week-01-recap.md){:.btn}
```

- [ ] **Step 2: Commit**

```bash
git add weeks/week-01.md
git commit -m "Link Workshop 1 recap from the week page"
```

---

### Task 6: Write the recap workflow doc

**Files:**
- Create: `docs/recap-workflow.md` (docs/ is excluded from the Jekyll build — internal doc, correct location)

**Interfaces:**
- Consumes: conventions proven by Tasks 1–5.

- [ ] **Step 1: Write the doc** — the per-week checklist from the spec, made concrete by what Tasks 2–5 actually did:

```markdown
# Session Recap Workflow

Per-week process for turning Zoom exports into a public recap page.
Spec: `docs/superpowers/specs/2026-07-14-session-recaps-design.md`.

## Inputs

Drop the week's Zoom exports into `videos/` (gitignored — never commit them):
`*_Recording_*.mp4`, `*_Recording.transcript.vtt`, `*_RecordingnewChat.txt`.

## Checklist

1. **Confirm presenter(s) with Anastasia.** Zoom speaker labels are unreliable
   (W1 tagged every line to one account). Never attribute a quote from labels
   alone; for multi-presenter sessions, verify who said what against the video.
2. **Read the full transcript.** Build a segment map (real chronological
   segments, VTT timestamps) against the week page's Session Outline; collect
   1–3 verbatim quote candidates per segment and participant moments to
   paraphrase. Read the chat file too. Skip pre-session logistics/small talk.
3. **Extract screenshots.** One per segment:
   `ffmpeg -ss HH:MM:SS -i <mp4> -frames:v 1 -vf scale=1200:-2 -q:v 4 <NN-slug.jpg>`
   Extract to a scratch folder first. **Privacy-review every frame visually**:
   no attendee faces, names, or webcam strips — re-extract nearby, crop, or drop.
   Approved frames go to `assets/recaps/wNN/`; keep the week under ~1.5 MB
   (6–10 images).
4. **Write `weeks/week-NN-recap.md`.** Narrative walkthrough in the session's
   actual order (use `weeks/week-01-recap.md` as the template): front-matter
   title only; header line with date/location/presenter; one section per
   segment with faithful prose, lightly-cleaned verbatim quotes, and one
   screenshot with descriptive alt text; participants paraphrased anonymously;
   closing "Try It Yourself" pointer to the week's core exercise; footer note
   disclosing quote cleanup. No timestamps, no recording link.
5. **Verify fidelity.** Re-check each quote against its VTT cue; grep the page
   for participant names (expect none).
6. **Link it.** Add under the slide deck button in `weeks/week-NN.md`:
   `[Read the session recap →](week-NN-recap.md){:.btn}`
7. **Build check and commit** page + images (never `videos/`).
```

- [ ] **Step 2: Commit**

```bash
git add docs/recap-workflow.md
git commit -m "Document the session recap workflow"
```

---

### Task 7: Build verification

**Files:**
- None modified.

- [ ] **Step 1: Jekyll build**

Run: `bundle exec jekyll build`
Expected: build succeeds. If bundler/jekyll isn't installed locally, fall back to structural checks: confirm `weeks/week-01-recap.md` front matter parses (title present), every `assets/recaps/w01/*.jpg` referenced in the page exists on disk, and the `week-01-recap.md` link target matches the filename exactly.

- [ ] **Step 2: Rendered check (if build succeeded)**

Run: `ls _site/weeks/week-01-recap.html` and grep it for `assets/recaps/w01`
Expected: file exists; image paths resolve with the `/NEH_AI_DH` baseurl prefix.

- [ ] **Step 3: Final status check**

Run: `git status --porcelain`
Expected: clean (or only `_site`-type ignored artifacts); `videos/` absent.
