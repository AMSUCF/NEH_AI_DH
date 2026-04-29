---
week: 5
title: "Workshop 3: AI for Visual Analysis"
kind: workshop
theme: "Visual analysis with Claude Projects + Artifacts"
starts: 2026-06-08
summary: |
  Image generation (and multimodal AI more broadly) is among the most contested forms of AI usage, raising questions of copyright and ethics that we'll address in this week's discussions. Our exercises will focus on image analysis and the ways AI is reshaping how we work with visual culture broadly, with pragmatic tasks such as alt-text and metadata alongside image analysis. We'll use both Claude Projects and Claude Artifacts in this week's exercises.
workshop:
  title: "Workshop 3: AI for Visual Analysis"
  date: 2026-06-10
  time: "10 AM - noon"
  location: CHDR
---

By the end of the session, every participant will have an Artifact gallery from their own image set with alt-text, structured metadata, and at least one comparative reading.

<div class="workshop-callout" markdown="1">
**NEH Workshop 3 — Tuesday, June 10, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the broader NEH learning community.

[Open the slide deck →]({{ '/slides/web/w05/' | relative_url }}){:.btn}
</div>

## What to Bring

- The same setup: laptop, Claude Pro subscription.
- **An image set.** Five to ten images you have rights to use. Possibilities: your own photos, archival scans you work with regularly, [Library of Congress Pictures](https://www.loc.gov/pictures/), [Internet Archive image collections](https://archive.org/details/image), Creative Commons material, comic covers from public domain, museum open-access collections. They should share a connection — same photographer, same archive, same theme, same period.
- A working understanding of what alt-text is and why it matters. We will revisit this, but the more familiar the better.

## Pre-Workshop Reading

- Crawford, Kate, and Trevor Paglen. ["Excavating AI."](https://excavating.ai/) (~30 min) The single best critical introduction to what training datasets look like under the hood.
- Demsky, Ian. ["My Month with Midjourney."](https://electronicbookreview.com/publications/my-month-with-midjourney/) *Electronic Book Review*, April 2, 2023. (~25 min) The most useful single piece on iteration as method in image generation.
- Coverage of the copyright fights: pick one — [*Andersen v. Stability AI*](https://www.courtlistener.com/docket/66732129/andersen-v-stability-ai-ltd/), [*New York Times v. OpenAI*](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html), or [Getty Images v. Stability AI](https://www.theguardian.com/technology/2025/nov/04/getty-images-loses-most-copyright-claims-against-stability-ai-in-uk-court).

Optional:

- Mitchell, *Artificial Intelligence*, Part II: Looking and Seeing.
- Jebb, Louis. ["On Process: Refik Anadol."](https://www.theartnewspaper.com/2024/04/05/on-process-refik-anadol-seeks-to-demystify-ai-art-by-showing-how-it-is-put-together) *The Art Newspaper*, April 2024.

## Session Outline (120 minutes)

1. **Two paradigms in one session.** Image *generation* (text-to-image) versus image *analysis* (image-to-text, alt-text, multi-image comparison). The workshop is about both, but we lead with the analytical work because that's where the pedagogical leverage is.
2. **The copyright and ethics conversation.** Where the lawsuits stand, what training data was scraped, what we can and can't responsibly generate or analyze. The Crawford & Paglen reading is the structural critique; the lawsuits are the live news.
3. **Live demo: archival comic covers in two tools.** I upload a small set to Claude Sonnet two ways — first to a **Project** (for batch metadata work across many files, with persistent context) and then to a fresh **Artifact** conversation (for the publishable visualization). We walk: describe → alt-text → key features → comparative metadata → relational visualization as an Artifact.
4. **Hands-on: your image set.** Each participant uploads their five-to-ten image set:
   - In a **Project** — generate alt-text for each image, build a metadata table, ask Claude for three patterns across the set.
   - In an **Artifact** — generate a comparative-description gallery (a grid, a typology, a timeline) you can share by URL.
5. **Critical reflection.** What did Claude *see* that you did not? What did it miss? Where does its visual reading reproduce the biases discussed in Crawford & Paglen? What's it doing with images of people, in particular?
6. **Discussion: where this fits in your teaching.** An accessibility tool? A scaffolded close-reading exercise? An archival metadata workflow? A copyright trap? All of the above?

## Core Exercise

**Image-to-text translation set, two tools.** Using your image set:

**Part A — In a Claude Project (the batch work):**

1. Create a fresh Project. Upload all images.
2. Generate descriptive alt-text for each, applying accessibility standards.
3. Build a metadata table covering: image, key features, period or context, observations.
4. Ask Claude to surface three patterns across the set.

**Part B — In a Claude Artifact (the shareable output):**

5. Open a new conversation; ask Claude to build an Artifact that visualizes the set in a meaningful relationship — a grid, a comparative table, a typology.
6. Iterate on the Artifact: change the layout, add captions from your alt-text, fix what's flat.
7. Publish it. Save the URL.

**Part C — The critique:**

8. Where does Claude's vision fail or flatten? Where did the Project handle scale better than the Artifact, or vice versa? What would you tell a student to watch for?

## Pedagogical Note

For accessibility-minded readers: AI-generated alt-text is *a draft.* It is faster than writing alt-text from scratch, and it is consistently worse than alt-text written by a human who knows the context. Use it as scaffolding for students learning to write alt-text, not as a finished artifact. The same applies to metadata: AI accelerates a draft; human curation is the work.

For the copyright conversation: there is no current legal answer, only a moving target. The honest pedagogical move is to teach students to ask the question — what was this trained on, what gives us the right to use this image, who is harmed if we get it wrong — not to give them a stable answer.

## Cross-references

- Source materials: `HumanitiesAI/weeksix.md` (image-to-text translation); `CriticalMaking2026/exercises/four_maps.md` (visual ideation), `CriticalMaking2026/exercises/one_selfie.md` (filters, beautification, bias).
