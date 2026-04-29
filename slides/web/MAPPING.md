# Source-deck → NEH live-session mapping

**Status:** draft for review. Once you sign off, I build the six reveal.js decks.

This document maps the 16 source-class PowerPoints (in `slides/_extracted/`,
gitignored) to the six NEH workshop **live-session** weeks. The async weeks
(W2, W4, W6, W8, W10, W12) keep using their existing markdown pages and are
intentionally out of scope.

The cross-references baked into each `weeks/week-XX.md` ("Source materials:
`HumanitiesAI/weekone.md`…") drove the primary mapping. I've added secondary
decks where the source structure suggests good supporting material.

## Source-class structure (recap)

| File | Opening title (slide 1) |
|---|---|
| `AI_Week_One` | Textual — Histories |
| `AI_Week_Two` | Textual — Generation |
| `AI_Week_Three` | TeXT — Sources, Origins |
| `AI_Week_Four` | textual — reading |
| `AI_Week_Five` | Images |
| `AI_WeekSix` | Visual — Art and Creativity |
| `AI_Week_Seven` | The Desert of the Real |
| `AI_WeekEight` | Visual — Perception |
| `AI_WeekNine` | Procedural — Code and Rules |
| `AI_WeekTen` | Procedural — Digital Humanities |
| `AI_WeekEleven` | procedural art & play |
| `AI_Week_Twelve` | Procedural: Hypertext & the Web |
| `AI_WeekThirteen` | Local Futures |
| `AI_Week_Fourteen` | Revisiting Text (and Labor) |
| `AI_Week_Fifteen` | Closing Thoughts |
| `AI_VisualCulture` | GenAI, Visual Culture, and "The Algorithm" |

The class moves textual → visual → procedural → futures/labor/closing. The
NEH workshop reorganises that arc into six bigger sessions; that's why each
NEH week pulls from one to three source decks.

## A note on videos (~485 across all decks)

Each source deck has roughly one short embedded video per slide — most are
small UI/chat demo clips, screen captures, or what look like converted GIFs.
**Uploading 485 videos to YouTube/Vimeo is not the move.** Recommended
defaults for each chosen slide:

- **Decorative / UI animation (small, < 10 MB):** convert to looping `.webm`
  or `.gif` and commit to `assets/slides/wXX/` (still small).
- **Content-bearing demo / talk excerpt (large, > 20 MB):** upload to
  YouTube/Vimeo, paste URL into the `Video URL` slot below.
- **Otherwise:** drop. Most slides have a fallback image already.

I'll tag each video below with my recommendation. You override during review.

---

## NEH Workshop 1 (Week 1) — Introducing AI for DH Pedagogy

**Cross-ref in `weeks/week-01.md`:** `HumanitiesAI/weekone.md` (ELIZA),
`HumanitiesAI/weektwo.md` (interfaces, Kirschenbaum).

**Primary source decks:**

- `AI_Week_One` (Textual — Histories) — Weizenbaum/ELIZA, hype/anti-hype,
  Bender & Hanna's *AI Con* arguments. Maps directly to the workshop's
  "field-clearing" framing.
- `AI_Week_Two` (Textual — Generation) — RACTER, intelligence-as-measure
  critique, where text generation came from. Pairs with the Kirschenbaum
  reading.

**Secondary (optional pull-ins):**

- `AI_Week_Three` slides 5–13 (ML basics, symbolic vs. subsymbolic, Turing
  imitation game) for the workshop's "what an LLM actually is" section.

**Slide selection (target ~18 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_Week_One` | 1, 5, 8, 10, 15, 32, 34 | Title, "AI is a marketing term," hype/anti-hype, Weizenbaum-Minsky split, Bender/Hanna purpose |
| `AI_Week_Two` | 1, 25, 26, 27 | Title, RACTER history, intelligence ranking critique |
| `AI_Week_Three` | 5, 8, 10, 13, 17, 22 | ML/deep learning, symbolic-subsymbolic, Turing, industrial-revolution Luddites |

**Media to optimize → `assets/slides/w01/`:** see `slides/_extracted/AI_Week_One/inventory.md` for `image1.png`–`image75.png`; pick those associated with the slides above (the inventory's "Media:" line shows which `imageN.png` belongs to each slide).

**Videos for W1:** the `media1.mp4`–`media38.mp4` set in Week_One almost
certainly includes ELIZA-style chat demo clips. Recommend keeping ≤ 3:
- `AI_Week_One/media/media1.mp4` (24 MB) — likely opening clip; **convert to webm**.
- One ELIZA / Weizenbaum demo, if any — **YouTube embed if > 20 MB.**
- Drop the rest.

---

## NEH Workshop 2 (Week 3) — AI for Textual Analysis

**Cross-ref in `weeks/week-03.md`:** `HumanitiesAI/weekfour.md` (distant
reading); `DistantCodingUMKC` Example 2; `CriticalMaking2026/exercises/eight_analysis`.

**Primary source decks:**

- `AI_Week_Four` (textual — reading) — closest to the distant-reading
  workshop. Slides on legal/medical/student LLM-reading examples set up
  the "critique what AI gets wrong" through-line.

**Secondary:**

- `AI_Week_Three` slides 23–27 (the "AI is killing the web" + Anthropic
  settlement + hidden-labor sections) — useful context for the labor and
  attribution conversation in W3's discussion.

**Slide selection (target ~14 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_Week_Four` | 1, 5, 7, 9, 11, 14, 25 | Title, legal/medical/student LLM-reading vignettes, "saving image discussions for next week" transition (cut), homework cheating |
| `AI_Week_Three` | 23, 26, 27 | Web-killing, Anthropic class action, hidden Kenyan-labor passage |

**Videos for W3:** Week_Four's `media1.mp4` (20.8 MB) is likely a legal-AI
demo; check it. Keep ≤ 2 videos; convert small UI clips to webm; YouTube
for any longer demo.

---

## NEH Workshop 3 (Week 5) — AI for Visual Analysis

**Cross-ref in `weeks/week-05.md`:** `HumanitiesAI/weeksix.md` (image-to-text
translation); `DistantCodingUMKC` Example 3 (butterflies);
`CriticalMaking2026/exercises/four_maps.md`.

**Primary source decks:**

- `AI_VisualCulture` — already a public-talk-shaped deck on GenAI + visual
  culture. **Strongest fit for the Crawford & Paglen "Excavating AI"
  reading anchor.** Slides 18, 24, 35 are explicit exercises ("Make it
  More," "Make it You," "Exercise Three") that map onto the workshop's
  hands-on alt-text / metadata sequence.
- `AI_WeekSix` (Visual — Art and Creativity) — GAN history, paperclip-
  maximizer thought experiment, Anthropic SB-53 endorsement, 2018 GAN
  examples (slide 29).

**Secondary:**

- `AI_Week_Five` (Images) — opening "Images" framing slide; pull as a
  section divider only.

**Slide selection (target ~18 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_VisualCulture` | 1, 2, 4, 5, 18, 24, 30, 35 | Title, presenter, "what is GenAI", matrix-keywords prompt critique, three exercises, Washington Post bias article |
| `AI_WeekSix` | 1, 4, 6, 17, 29 | Visual title, paperclip maximizer, SB-53, *Science* paper, 2018 GAN examples |
| `AI_Week_Five` | 1 | Section divider for "Images" |

**Videos for W5:** Smallest video volume across all decks — `AI_VisualCulture`
has only 2 (`media1.mp4` 24 MB, `media2.mp4` 8 MB). Both very likely
content-bearing (presenter intro / generative-art clip). **Recommend YouTube
upload for `media1.mp4`, webm-convert + commit `media2.mp4`.**

---

## NEH Workshop 4 (Week 7) — Web and Interactive Applications

**Cross-ref in `weeks/week-07.md`:** `DistantCodingUMKC/index.md` (Example 1,
ePortfolio); `HumanitiesAI/weekeleven.md` (GitHub Pages deploy);
`DistantCoding/transcript.md` (vibe-coding framing).

**Primary source decks:**

- `AI_WeekEleven` (procedural art & play) — closest to the workshop's
  hands-on "ship a CV/syllabus to GitHub Pages" arc, since the source week
  was where Anastasia first walked the class through Pages.

**Secondary:**

- `AI_Week_Twelve` (Procedural: Hypertext & the Web) — slide 3 references a
  JavaScript variables/datatypes primer; useful for the section on what
  Code Web actually does under the hood.
- `AI_WeekTen` (Procedural — Digital Humanities) — slide 1 is a clean
  section divider / framing for the DH-pedagogy through-line.

**Slide selection (target ~16 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_WeekEleven` | 1, plus the GitHub Pages walkthrough cluster (~10 slides) | Workshop's CV-to-ePortfolio core |
| `AI_Week_Twelve` | 1, 3 | "Hypertext & the Web" framing + JS primer link |
| `AI_WeekTen` | 1 | Procedural DH section divider |

**Videos for W7:** Likely a screen-capture of a Code Web run-through. Keep
1 worth-it walkthrough video; **YouTube** for any > 20 MB; drop the rest.

---

## NEH Workshop 5 (Week 9) — Playful Approaches and Creative Code, AI Policy

**Cross-ref in `weeks/week-09.md`:** `HumanitiesAI/weeknine.md` (recommender);
`HumanitiesAI/weektwelve.md` (agentic Code Web);
`CriticalMaking2026/exercises/eight_analysis.md`, `nine_generation.md`,
`eleven_narrative.md`.

**Primary source decks:**

- `AI_WeekNine` (Procedural — Code and Rules) — opens with "the road so
  far: textual / visual / procedural," exactly the framing W9 needs to
  close the loop after the visual workshop.
- `AI_Week_Twelve` (Procedural: Hypertext & the Web) — agentic Code Web
  examples; pair with the playful-tool build.

**Secondary:**

- `AI_WeekTen` (Procedural — DH) — for the "what counts as DH work" thread
  that supports the AI-policy conversation.

**Slide selection (target ~16 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_WeekNine` | 1, 2, 3, 4, 5, plus recommender-build cluster | Title, "the road so far," recommender exercise |
| `AI_Week_Twelve` | 1, 3, plus Code-Web agentic demo cluster | Hypertext framing, agentic examples |

**AI-policy section (the second half of the workshop) is mostly fresh
content** — there's no source-class deck that drafted UDL-aligned policy
language. Built from scratch driven by the W9 .md outline.

**Videos for W9:** Procedural decks (`AI_WeekNine` 32 vids, `AI_Week_Twelve`
30) are very likely loops of Code-Web building. Keep 2–3 best build videos
as YouTube embeds; drop the rest.

---

## NEH Workshop 6 (Week 11) — Agentic Futures, Curricular Sustainability

**Cross-ref in `weeks/week-11.md`:** `DistantCodingUMKC/index.md` (Days 2–4 —
CLI, MCP, skills, Superpowers); `HumanitiesAI/weekthirteen.md` (local models),
`weekfourteen.md` (Code Web for distant reading), `weekfifteen.md` (skills,
subagents, fine-tuning); `dhsi.md`.

**Primary source decks:**

- `AI_WeekThirteen` (Local Futures) — local-model framing for the
  "agentic horizon" tour.
- `AI_Week_Fourteen` (Revisiting Text and Labor) — labor frame; pairs with
  the Underwood "Marionette Theater" reading.
- `AI_Week_Fifteen` (Closing Thoughts) — natural source for the workshop's
  closing-Q&A and `CLAUDE.md` exercise framing.

**Slide selection (target ~18 slides):**

| Source | Slides | Why |
|---|---|---|
| `AI_WeekThirteen` | 1, plus local-model demo cluster | "Local Futures" opener, local CLI demo |
| `AI_Week_Fourteen` | 1, 4, 5 | "Revisiting Text and Labor", Altman-on-jobs, Graeber empty-room |
| `AI_Week_Fifteen` | 1, plus closing reflections | "Closing Thoughts" framing |

**Videos for W11:** Keep one CLI/Cowork demo as YouTube embed (most useful
for participants who want to see what "agentic" actually looks like). Drop
the rest.

---

## What's not used (asynchronous weeks / unused source decks)

`AI_WeekEight` (Visual — Perception) — could enrich async W6 (Visual AI in
the Wild) if the user later wants async-week decks; out of scope for now.

Decks not pulled into any live workshop above:
- `AI_WeekEight` — async W6 fit
- Most of `AI_Week_Five` — image-history depth not needed in 120 min
- `AI_Week_Seven` (Desert of the Real) — interesting but doesn't fit a
  single workshop's spine; the "AI realism" question is touched on in W5
  via VisualCulture instead.

---

## Open questions before Phase 5

1. **Videos:** is the "drop most, YouTube the few content-bearing demos,
   convert small UI clips to webm" strategy OK? If you'd rather keep more
   videos, say so and I'll commit larger optimized clips to
   `assets/slides/wXX/videos/`.
2. **Slide-count target:** I've sized each deck at 14–18 slides assuming
   a 120-min session split between lecture / demo / hands-on. If you want
   bigger decks (more lecture density), I can pull more.
3. **Anything I miscategorised?** The cross-refs in `weeks/week-XX.md`
   were the spine of this mapping; if any are stale (e.g., "I actually
   want W11 to lean on Week_Fourteen, not Week_Thirteen"), tell me here.
