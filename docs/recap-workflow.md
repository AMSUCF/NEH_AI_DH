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
   no attendee faces, names, or webcam strips, and no browser chrome showing URL bars with share links or tokens, personal emails, or private tab titles — crop browser chrome when in doubt — re-extract nearby, crop, or drop.
   Approved frames go to `assets/recaps/wNN/`; keep the week under ~1.5 MB
   (6–10 images).
4. **Write `weeks/week-NN-recap.md`.** Narrative walkthrough in the session's
   actual order (use `weeks/week-01-recap.md` as the template): front-matter
   title only; header line with date/location/presenter; one section per
   segment with faithful prose, lightly-cleaned verbatim quotes, and one
   screenshot with descriptive alt text; participants paraphrased anonymously;
   closing "Try It Yourself" pointer to the week's core exercise; footer note
   disclosing quote cleanup. No timestamps, no recording link.
   Obvious auto-caption transcription errors in quotes (e.g. "Cloud" → Claude, "ELISA" → ELIZA) may be corrected to what was actually said; the footer note must disclose both filler removal and these corrections.
5. **Verify fidelity.** Re-check each quote against its VTT cue; grep the page
   for participant names (expect none).
6. **Link it.** Add under the slide deck button in `weeks/week-NN.md`:
   `[Read the session recap →](week-NN-recap.md){:.btn}`
7. **Build check and commit** page + images (never `videos/`).
