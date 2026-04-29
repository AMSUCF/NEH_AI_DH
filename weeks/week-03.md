---
week: 3
title: "Workshop 2: AI for Textual Analysis"
kind: workshop
theme: "Distant reading and corpus work with Claude Projects"
starts: 2026-05-25
summary: |
  This week, we'll explore distant reading and computational text analysis across disciplines. Bring a set of texts to play with: we'll discuss the copyright implications of what we work with, and dive into how we work using Claude Projects to handle larger numbers of files.
workshop:
  title: "Workshop 2: AI for Textual Analysis"
  date: 2026-05-27
  time: "10 AM - noon"
  location: CHDR
---

<div class="workshop-callout" markdown="1">
**NEH Workshop 2 — Tuesday, May 27, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the broader NEH learning community.

[Open the slide deck →]({{ '/slides/web/w03/' | relative_url }}){:.btn}
</div>

## What to Bring

- The same setup as Workshop 1: laptop, Claude Pro subscription.
- **A small corpus.** Three to ten texts you have rights to use or that are public-domain. Plain text (.txt) or PDF. They can be chapters, articles, primary sources, student work samples (with permission), interview transcripts, government documents — whatever your discipline reads at scale. They should share a meaningful connection so comparative analysis means something.
- The reflections / frustrations from your W2 settings tour, if you did it.

## Pre-Workshop Reading

- Houston, Natalie M. ["Text Analysis."](https://digitalpedagogy.hcommons.org/keyword/Text-Analysis/) *Digital Pedagogy in the Humanities.* (~20 min) Frames text analysis as a teachable practice.
- Underwood, Ted. ["A More Interesting Upside of AI."](https://tedunderwood.com/2025/07/02/a-more-interesting-upside-of-ai/) *The Stone and the Shell*, July 2, 2025. (~15 min) The most useful single piece on what AI changes for distant reading.
- Walsh, Melanie, and Maria Antoniak. ["The Goodreads 'Classics': A Computational Study of Readers, Amazon, and Crowdsourced Amateur Criticism."](https://post45.org/2021/04/the-goodreads-classics-a-computational-study-of-readers-amazon-and-crowdsourced-amateur-criticism/) *Post45*, 2021. (~25 min) A model of distant reading at scale, well-written for non-specialists.

On copyright (skim before the discussion):

- Authors Guild et al. v. Anthropic settlement coverage: ["Authors celebrate historic settlement."](https://arstechnica.com/tech-policy/2025/08/authors-celebrate-historic-settlement-coming-soon-in-anthropic-class-action/) *Ars Technica*, August 2025. (~10 min)
- *Bartz v. Anthropic*: brief background on the case and what it does and doesn't establish about training-data copyright.

## Session Outline (120 minutes)

1. **Distant reading, three traditions.** Moretti's literary system at scale, Underwood's stylometrics, the Voyant classroom tradition. What Claude Projects adds: persistent context across multi-turn conversation, multi-file uploads, native handling of mixed formats, the ability to reason about *why* a pattern looks the way it does.
2. **The copyright conversation.** What Anthropic's settlement does (compensation for authors whose books were ingested) and doesn't (it does not establish a precedent that bars training on scraped text). What you can responsibly upload to a Project: your own writing, your students' work with permission, public-domain corpora, openly-licensed texts. What gives us reasonable pause: copyrighted academic articles you have library access to. The discussion is part of the workshop, not a footnote.
3. **Live demo: a corpus I have not opened before.** I bring a small set of texts, upload them to a fresh Project, and walk through a sequence: preprocessing → bag-of-words → key phrases → comparative passages → thematic network. We critique what Claude gets right and where it confabulates. The iteration is the visible part.
4. **Hands-on: your corpus (largest single block of the session).** Each participant uploads their corpus to a Project. Run the same sequence on your own materials. Roving help; pair where useful.
5. **Building an Artifact summary.** End the analytical sequence by asking Claude to produce an Artifact — a small visual or interactive summary you can share with a colleague or a class.
6. **Discussion.** Where did Claude help? Where did it hallucinate? What would a student need to know before they used this for an assignment? What did the copyright question feel like in practice?

## Core Exercise

**Distant reading with Claude Projects.** Using the corpus you brought (or, if you could not attend, a three-to-ten-text set from [Project Gutenberg](https://www.gutenberg.org/), [HathiTrust](https://www.hathitrust.org/) public-domain holdings, or your own files):

1. Create a fresh Project. Upload all texts.
2. Run the analytical sequence: stopword filter → bag-of-words → key phrases → character or theme network → comparative read across the texts.
3. Ask Claude to generate an **Artifact** that visualizes one finding (a word cloud, a frequency chart, a network diagram, a comparative table).
4. Critique what you see. Compare to what you would have noticed in close reading. Document at least one place Claude got it wrong.
5. **Write one paragraph about the copyright status of your corpus.** *What did you upload, what gives you the right to upload it, and where would you draw the line?* This is the half of the assignment students often skip; do it for yourself first.

## Pedagogical Note

The point of this exercise is not the visualization. The point is the *iteration.* Notice when you have to push back, refine, ask Claude to reconsider. That iteration is the actual humanities work — and it is teachable. When you bring this exercise into a course, scaffold the iteration explicitly: "show me three prompts you tried before you got the result you used." And scaffold the copyright reflection: "tell me what you uploaded and why you had the right to."

## Cross-references

- Source materials: `HumanitiesAI/weekfour.md` (distant reading exercise); `CriticalMaking2026/exercises/eight_analysis.md` (Voyant + analysis pipeline).
