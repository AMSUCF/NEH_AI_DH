---
week: 8
title: "Multiple Small Projects (Asynchronous)"
kind: async
theme: "Confidence-building with GitHub / Claude Code Web / GitHub Pages"
starts: 2026-06-29
summary: |
  To build confidence with the GitHub / Claude Code Web / GitHub Pages workflow, try multiple small projects this week. Exercise prompts include both pedagogical practices and potential assignments, such as building an eportfolio, creating an interactive worksheet, or developing online public scholarship resources. Remember that you can use Claude itself to debug any problems with GitHub and GitHub Pages as you go.
---

<div class="async-callout" markdown="1">
**Asynchronous deep-dive.** This week is *deliberately wide*. Pick two or three small projects from the menu below — the goal is repetition until the GitHub / Code Web / Pages loop becomes muscle memory. There is no right number; finish what feels useful.
</div>

## The Same Loop, Different Projects

For every exercise this week, the same shape works:

```
1. Initialize a fresh GitHub repo (Public, with a README).
2. Upload any source files (handouts, JSON, images, datasets).
3. Open Claude Code Web; select the repo.
4. Prompt: describe the goal, the audience, the constraints
   (e.g. "deploy on GitHub Pages, HTML/CSS/JS only, no build step").
5. Iterate. Push. Check the live URL. Iterate again.
```

If you hit something that breaks — a build error, a deploy failure, a layout issue — paste the error or screenshot back into Claude Code Web and ask. **Most issues resolve in one or two prompts.** That habit (debug *with* Claude rather than around it) is worth building this week.

## Reading Menu

- <span class="tag tag-light">Light</span> Farrell, Henry. ["After Software Eats the World, What Comes Out the Other End?"](https://www.programmablemutter.com/p/after-software-eats-the-world-what) October 3, 2024. (~25 min) Helpful framing for what you just did in W7.
- <span class="tag tag-light">Light</span> Cohen, Dan. ["The Index and the Vector."](https://newsletter.dancohen.org) *Humane Ingenuity.* (~15 min) The DH-specific framing of what Code Web changes for archives and reference work.
- <span class="tag tag-standard">Standard</span> Littman, *Code to Joy*, Chapters 2–3 (The What of Programming; Sequencing Commands). (~90 min) The most accessible introduction to programming concepts; a useful counterpoint to vibe-coding hype.
- <span class="tag tag-standard">Standard</span> Willison, Simon. ["Beyond Vibe Coding."](https://simonwillison.net/2025/Sep/4/beyond-vibe-coding/) September 4, 2025. (~30 min) When the chat-driven model breaks down, and what to do.

## Exercise Menu — Pick Two or Three

Each is small. Each ends in a deployed URL. Stack them.

### A. Polish the W7 site (~30 min)

Open your W7 ePortfolio or visualization in Claude Code Web. Two passes: (1) **accessibility** — alt-text on images, contrast check, heading structure, keyboard navigation; (2) **content** — fix any error you noticed in the first deploy. Push the changes; check the live URL.

### B. Static handout → interactive page (~90 min)

Pick a paper handout you currently give students — a glossary, a timeline of a movement or period, a list of resources, an annotated bibliography. Use Claude Code Web to convert it into a one-page interactive site (clickable timeline, filterable list, structured glossary). Deploy via GitHub Pages.

*Source: adapted from `HumanitiesAI/weekeleven.md`.*

### C. Recommender or "find your X" tool (~2 hr)

Build a JSON dataset relevant to your discipline (100 books, 50 films, 30 archives, 40 primary documents, 25 paintings) plus a minimal interactive front end that lets a user filter or rate the set and gets a recommendation back.

*Source: `HumanitiesAI/weeknine.md`.*

### D. Public scholarship one-pager (~2 hr)

Pick a small piece of scholarship you've done — a conference paper, a book chapter, a dissertation chapter, a public talk. Use Claude Code Web to build a one-page public-scholarship site that summarizes it for a non-specialist audience. Include: a clear one-paragraph hook, the argument in three bullets, a citation, and a link to the full version (if available). Deploy.

### E. Interactive worksheet for one assignment (~2 hr)

Pick a single assignment you give. Build a one-page interactive worksheet that walks the student through it: prompts, structured input fields, a "save my answers" button (`localStorage` is fine), and printable output. The point is to model what scaffolding looks like in this medium.

### F. Debug-with-Claude practice (~30 min, repeatable)

Take any of the above and *deliberately break it* — delete a file, mis-set the GitHub Pages branch, paste in malformed JSON. Then debug it back to working *only by talking to Claude*. The point is to build the muscle of pasting an error message back and asking what it means.

## What to Carry Into Workshop 5

Bring a **dataset or topic** for a small interactive tool (a course concept you'd turn into a game, a corpus you'd turn into a quiz, a collection you'd turn into a generator). And bring **a paragraph of AI policy from your current syllabus**, even one paragraph — if you don't have one, bring a syllabus and a willingness to draft.

## Cross-references

- Source materials: `HumanitiesAI/weekeleven.md` (GitHub Pages deploy), `weeknine.md` (recommender), `weektwelve.md` (agentic Code Web with planning mode).
