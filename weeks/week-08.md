---
week: 8
title: "Rebuilding a Handout (Asynchronous)"
kind: async
theme: "Code Web reinforcement: rebuild a static handout"
starts: 2026-06-29
---

A reinforcement week for Code Web. The *Signature Assignment* for ENG 6813 is due Sunday, July 5, so this week is intentionally light on new content — pick the depth you have time for. There is no in-person session and no required deliverable. Save deeper Code Web work for the next workshop on July 8.

<div class="async-callout" markdown="1">
**Asynchronous deep-dive.** Light by design. ENG 6813 students: focus on the Signature Assignment due July 5. Use the exercises here as a way to prototype something for that deliverable if it helps.
</div>

## Reading Menu

- <span class="tag tag-light">Light</span> Farrell, Henry. ["After Software Eats the World, What Comes Out the Other End?"](https://www.programmablemutter.com/p/after-software-eats-the-world-what) October 3, 2024. (~25 min) Helpful framing for what you just did in W7.
- <span class="tag tag-light">Light</span> Cohen, Dan. ["The Index and the Vector."](https://newsletter.dancohen.org) *Humane Ingenuity.* (~15 min) The DH-specific framing of what Code Web changes for archives and reference work.
- <span class="tag tag-standard">Standard</span> Littman, *Code to Joy*, Chapters 2–3 (The What of Programming; Sequencing Commands). (~90 min) The most accessible introduction to programming concepts; a useful counterpoint to vibe-coding hype.
- <span class="tag tag-standard">Standard</span> Willison, Simon. ["Beyond Vibe Coding."](https://simonwillison.net/2025/Sep/4/beyond-vibe-coding/) September 4, 2025. (~30 min) When the chat-driven model breaks down, and what to do.

## Exercise Menu

- <span class="tag tag-light">Light</span> **Iterate the W7 site (~30 min).** Open your W7 ePortfolio in Claude Code Web. Two passes: (1) accessibility — alt-text on images, contrast check, heading structure; (2) content — fix any error you noticed in the first deploy. Push the changes; check the live URL.
- <span class="tag tag-standard">Standard</span> **Static handout → interactive page (~90 min).** Pick a paper handout you currently give students — a glossary, a timeline of a movement or period, a list of resources, an annotated bibliography. Use Claude Code Web to convert it into a one-page interactive site (clickable timeline, filterable list, structured glossary). Deploy via GitHub Pages. *Source: adapted from `HumanitiesAI/weekeleven.md`.*
- <span class="tag tag-deep">Deep</span> **Recommender or Buzzfeed-style tool (~3 hr).** Build a JSON dataset relevant to your discipline (100 books, 50 films, 30 archives, 40 primary documents) plus a minimal interactive front end that lets a user rate or filter the set and gets a recommendation back. *Source: `HumanitiesAI/weeknine.md`.*

## Useful Reference for the Hands-On Work

For all three exercises, the same shape works:

```
1. Initialize a fresh GitHub repo.
2. Upload any source files (handouts, JSON, images) directly to the repo.
3. Open Claude Code Web, select the repo.
4. Prompt: describe the goal, the audience, and the constraints (e.g., "deploy on GitHub Pages, use only HTML/CSS/JS, no build step").
5. Iterate. Push. Check the live URL. Iterate again.
```

If you hit something that breaks — a build error, a deploy failure — paste the error back into Claude Code Web and ask. Most issues resolve in one or two prompts.

## Cross-references

- Companion ENG 6813 module: [Week 8](../../InterdisciplinaryTeaching-main/InterdisciplinaryTeaching-main/weeks/week-08.md) (Signature Assignment due July 5).
- Source materials: `HumanitiesAI/weekeleven.md`, `weeknine.md`; `DistantCoding/transcript.md`.
