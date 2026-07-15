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
**NEH Workshop 2 — Wednesday, May 27, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community.

[Open the slide deck →]({{ '/slides/web/w03/' | relative_url }}){:.btn}

[Read the session recap →](week-03-recap.md){:.btn}
</div>

## What to Bring

- The same setup as Workshop 1: laptop, Claude Pro subscription.
- **A small corpus.** Three to ten texts you have rights to use or that are public-domain. Plain text (.txt) or PDF. They can be chapters, articles, primary sources, student work samples (with permission), interview transcripts, government documents — whatever your discipline reads at scale. They should share a meaningful connection so comparative analysis means something.
- The reflections / frustrations from your W2 settings tour, if you did it.

## Pre-Workshop Reading

- Houston, Natalie M. ["Text Analysis."](https://digitalpedagogy.hcommons.org/keyword/Text-Analysis/) *Digital Pedagogy in the Humanities.* Frames text analysis as a teachable practice.
- Underwood, Ted. ["A More Interesting Upside of AI."](https://tedunderwood.com/2025/07/02/a-more-interesting-upside-of-ai/) *The Stone and the Shell*, July 2, 2025. A useful piece on what AI changes for distant reading.
- Walsh, Melanie, and Maria Antoniak. ["The Goodreads 'Classics': A Computational Study of Readers, Amazon, and Crowdsourced Amateur Criticism."](https://post45.org/2021/04/the-goodreads-classics-a-computational-study-of-readers-amazon-and-crowdsourced-amateur-criticism/) *Post45*, 2021. A model of distant reading at scale, well-written for non-specialists.

On copyright (skim before the discussion):

- Authors Guild et al. v. Anthropic settlement coverage: ["Authors celebrate historic settlement."](https://arstechnica.com/tech-policy/2025/08/authors-celebrate-historic-settlement-coming-soon-in-anthropic-class-action/) *Ars Technica*, August 2025.
- *Bartz v. Anthropic* — NPR coverage of the September 2025 settlement: ["Anthropic settles authors' lawsuit over pirated chatbot training material."](https://www.npr.org/2025/09/05/g-s1-87367/anthropic-authors-settlement-pirated-chatbot-training-material) Brief background on the case and what it does and doesn't establish about training-data copyright. The full docket, including filings and orders, is on [CourtListener](https://www.courtlistener.com/docket/69058235/bartz-v-anthropic-pbc/).

## Session Outline (120 minutes)

1. **Contextualizing the AI text problem.** A cold open on the longer history: automation and the Luddites, the "textpocalypse" and the enshittified, AI-saturated web, and AI-generated fiction passing as human (the Granta / Commonwealth Prize case). Why read computationally at all, now that machines write and rewrite the web?
2. **How distant reading has been framed in DH and pedagogy.** The traditions we inherit: Moretti's literary system at scale, Underwood's stylometrics, the Voyant classroom tradition. What Claude Projects adds: persistent context across multi-turn conversation, multi-file uploads, native handling of mixed formats, and the ability to think through the difference between computational text analysis and human reading.
3. **Where AI is reading text right now.** Field scenes already in motion: law (the billable hour, hallucinated court filings, an "AI law student"), medicine, and the student-"cheating" frame — alongside where AI genuinely helps, like transcribing handwriting.
4. **Whose reading paid for this: labor and copyright.** The hidden labor behind "less toxic" models (the Kenyan data workers) and the training set as legal record (the Anthropic settlement). What the settlement does and doesn't establish, different types of fair and responsible use, the role of the UCF library, and classroom use cases.
5. **Live demo sequence: Projects → Artifacts → Skills, then hands-on (largest single block of the session).** I upload a small literary corpus I have not opened to a fresh Project and walk a sequence — preprocessing → bag-of-words → key phrases → comparative passages → thematic network — end the analysis in a shareable **Artifact**, then build a simple, reusable textual-analysis **Skill**. Participants run the sequence on their own corpus, including a NotebookLM comparison, while we critique what Claude gets right and where it confabulates.
6. **Discussion.** Where did Claude help? Where did it hallucinate? What would a student need to know before they used this for an assignment? What did the copyright question feel like in practice?

## Core Exercise

**Distant reading with Claude Projects.** Using the corpus you brought (or, if you could not attend, a three-to-ten-text set from [Project Gutenberg](https://www.gutenberg.org/), [HathiTrust](https://www.hathitrust.org/) public-domain holdings, or your own files):

1. Create a fresh Project. Upload all texts.
2. Run the analytical sequence: stopword filter → bag-of-words → key phrases → character or theme network → comparative read across the texts.
3. Ask Claude to generate **Artifacts** that visualize the findings — word clouds, frequency charts, network diagrams, comparative tables, thematic timelines. **We will generate at least five different artifacts and iterate** on the prompts and choices in between.
4. Critique what you see. Compare to what you would have noticed in close reading. Document at least one place Claude got it wrong.
5. **Replicate the same process with [Google NotebookLM](https://notebooklm.google.com/), and note the differences in workflow and in the visibility of the computational work:**
   - Create a new notebook and add the *same* texts as sources — NotebookLM accepts PDFs, `.txt`, `.docx`, EPUB, pasted text, and Google Drive or web links (up to 50 sources, 500,000 words each).
   - Ask the same analytical questions in the chat. Notice that NotebookLM answers *only* from your uploaded sources and footnotes every claim with an inline citation back to the exact passage.
   - Generate a Studio output — a Briefing Doc, Study Guide, Mind Map, or an Audio Overview — and set it beside the Artifact Claude produced.
   - Compare. Claude shows its reasoning and its *code* (the analysis tool, editable Artifacts) and will range beyond your texts when it thinks it should; NotebookLM hides the computation entirely and stays strictly grounded in your sources. Which felt more transparent? Which felt more trustworthy, and for which question?

## Pedagogical Note

Distant reading and computational text analysis have limitations, but they also give us insight into larger patterns — and into how humans process texts. Students have likely heard elsewhere that AI is good for *summary*. Can these methods push back against that kind of usage, and bring students into more complex, thoughtful ways of working through a text?

## Cross-references

- Source materials: [HumanitiesAI/weekfour](https://anastasiasalter.net/HumanitiesAI/weekfour.html) (distant reading exercise); [CriticalMaking2026/exercises/eight_analysis](https://anastasiasalter.net/CriticalMaking2026/exercises/eight_analysis.html) (Voyant + analysis pipeline).
