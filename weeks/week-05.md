---
week: 5
title: "Workshop 3: AI for Visual Analysis"
kind: workshop
theme: "Visual analysis with Claude Projects, Artifacts, and Cowork"
starts: 2026-06-08
summary: |
  Image generation (and multimodal AI more broadly) is among the most contested forms of AI usage, raising questions of copyright and ethics that we'll address in this week's discussions. Our exercises will focus on image analysis and the ways AI is reshaping how we work with visual culture broadly, with pragmatic tasks such as alt-text and metadata alongside image analysis. We'll use Claude Projects, Claude Artifacts, and Claude Cowork in this week's exercises.
workshop:
  title: "Workshop 3: AI for Visual Analysis"
  date: 2026-06-10
  time: "10 AM - noon"
  location: CHDR
---

By the end of the session, every participant will have an Artifact gallery from their own image set with alt-text, structured metadata, and at least one comparative reading.

<div class="workshop-callout" markdown="1">
**NEH Workshop 3 — Wednesday, June 10, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community.

[Open the slide deck →]({{ '/slides/web/w05/' | relative_url }}){:.btn}

[Read the session recap →](week-05-recap.md){:.btn}
</div>

## What to Bring

- The same setup: laptop, Claude Pro subscription.
- **An image set.** Five to ten images you have rights to use. Possibilities: your own photos, archival scans you work with regularly, [Library of Congress Pictures](https://www.loc.gov/pictures/), [Internet Archive image collections](https://archive.org/details/image), Creative Commons material, comic covers from public domain, museum open-access collections. They should share a connection — same photographer, same archive, same theme, same period.
- A working understanding of what alt-text is and why it matters. We will revisit this, but the more familiar the better.

## Pre-Workshop Reading

- Crawford, Kate, and Trevor Paglen. ["Excavating AI."](https://excavating.ai/) (~30 min) A useful critical introduction to what training datasets look like under the hood.
- Demsky, Ian. ["My Month with Midjourney."](https://electronicbookreview.com/publications/my-month-with-midjourney/) *Electronic Book Review*, April 2, 2023. (~25 min) A useful piece on iteration as method in image generation.
- Coverage of the copyright fights: pick one — [*Andersen v. Stability AI*](https://www.courtlistener.com/docket/66732129/andersen-v-stability-ai-ltd/), [*New York Times v. OpenAI*](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html), or [Getty Images v. Stability AI](https://www.theguardian.com/technology/2025/nov/04/getty-images-loses-most-copyright-claims-against-stability-ai-in-uk-court).

Optional:

- Mitchell, *Artificial Intelligence*, Part II: Looking and Seeing.
- Jebb, Louis. ["On Process: Refik Anadol."](https://www.theartnewspaper.com/2024/04/05/on-process-refik-anadol-seeks-to-demystify-ai-art-by-showing-how-it-is-put-together) *The Art Newspaper*, April 2024.

## Session Outline (120 minutes)

1. **Two paradigms in one session.** Image *generation* (text-to-image) versus image *analysis* (image-to-text, alt-text, multi-image comparison). Most people think of generation when they think of AI — but *both* are forms of data visualization, and that is the lens we bring to each.
2. **AI images as information visualization.** Every generated image is a picture of its training data. We look at what search engines and generators reveal about defaults and bias: Safiya Noble's "professor style" results, the way tools return the same man for "a professor," the "make it more" drift toward stereotype, and the *Washington Post*'s ["This is how AI image generators see the world"](https://www.washingtonpost.com/technology/interactive/2023/ai-generated-images-bias-racism-sexism-stereotypes/) interactive ("toys in Iraq," "a house" by country). Crawford & Paglen's "Excavating AI" is the structural critique. Warm-up exercises run throughout: "make it *more*," "draw my life," and generic-then-specific prompting.
3. **The copyright and ethics conversation.** Where the lawsuits stand, what training data was scraped, what we can and can't responsibly generate or analyze, and what working with local models changes about sending images to someone else's server.
4. **Visualizing images with AI (hands-on).** Each participant uploads their five-to-ten image set to a **Claude Project**: alt-text for each image, a metadata table, three patterns across the set, and an **Artifact** that visualizes the set in a meaningful relationship. Then we try the same workflow in **Claude Cowork**.
5. **Critical reflection.** What did Claude *see* that you did not? What did it miss? Where does its visual reading reproduce the biases discussed earlier? What's it doing with images of people, in particular?
6. **Discussion: where this fits in your teaching.** An accessibility tool? A scaffolded close-reading exercise? An archival metadata workflow? A copyright trap? All of the above?

## Core Exercise

**Image-to-text translation set.** Using your five-to-ten image set:

1. Upload all images to a **Claude Project**.
2. Generate descriptive alt-text for each, applying accessibility standards.
3. Build a metadata table covering: image, key features, period or context, observations.
4. Ask Claude to surface three patterns across the set.
5. Ask Claude to build an **Artifact** that visualizes the set in a meaningful relationship — a grid, a comparative table, a typology. Iterate on the layout and captions, then publish and save the URL.
6. Critique the alt-text. Where does Claude's vision fail or flatten? What's it doing with images of people, in particular? What would you tell a student to watch for?
7. If you have access, try the same workflow in **Claude Cowork**.

## Pedagogical Note

For accessibility-minded readers: AI-generated alt-text is *a draft.* It is faster than writing alt-text from scratch, and it is consistently worse than alt-text written by a human who knows the context. Use it as scaffolding for students learning to write alt-text, not as a finished artifact. The same applies to metadata: AI accelerates a draft; human curation is the work.

For the copyright conversation: there is no current legal answer, only a moving target. The honest pedagogical move is to teach students to ask the question — what was this trained on, what gives us the right to use this image, who is harmed if we get it wrong — not to give them a stable answer. Working with local models instead of web-based products like Claude can remove one piece of the problem: sending images to someone else's server. We'll discuss this more as we get into Claude Code.

## Cross-references

- Source materials: [HumanitiesAI/weeksix](https://anastasiasalter.net/HumanitiesAI/weeksix.html) (image-to-text translation); [CriticalMaking2026/exercises/four_maps](https://anastasiasalter.net/CriticalMaking2026/exercises/four_maps.html) (visual ideation), [CriticalMaking2026/exercises/one_selfie](https://anastasiasalter.net/CriticalMaking2026/exercises/one_selfie.html) (filters, beautification, bias).
