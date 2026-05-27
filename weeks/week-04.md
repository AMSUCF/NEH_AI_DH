---
week: 4
title: "Distant Reading and Skills (Asynchronous)"
kind: async
theme: "Claude Projects + Skills for text work"
starts: 2026-06-01
summary: |
  This week's exercises are designed to let you explore the capacity of Claude Projects and Skills on your own, with a focus on working with either other people's text or across your own files. Consider trying to build your own exercise with your students in mind, thinking about the ways of working modeled in the examples.
---

<div class="async-callout" markdown="1">
**Asynchronous expectations.** Read the **Required** items in the menu below and complete **at least one** of the three exercises. **Post the results of that exercise back in the cohort Discord** — a screenshot, a Skill file, a link to your Project, or a short reflection on what surprised you. The Discord post is the deliverable. Also begin assembling your image set for Workshop 3 (see "What to Carry" below). Building your own Skill is the new move to try this week if you only have time for one thing.
</div>

## What's New This Week: Building Your Own Skill

Skills themselves aren't new — you used them in Workshop 2, and you've been brushing up against pre-built ones (like skill-creator) since the start of the series. What's new this week is **writing your own**. A Skill is a reusable instruction-set Claude loads on demand — a custom system-prompt module you build once and apply to any conversation or Project. Anthropic publishes a [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) skill that helps you draft your own; Skills live in **Settings → Capabilities → Skills**.

Building one from scratch is the closest thing this series has to "writing code" — and you don't write code. You write Markdown.

## Reading Menu

- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Cohen, Dan. ["The Writing Is on the Wall for Handwriting Recognition."](https://newsletter.dancohen.org/archive/the-writing-is-on-the-wall-for-handwriting-recognition/) *Humane Ingenuity.* If you missed this for W3, read it now — it grounds the rest of the series in a longer history of computational reading in archives.
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Anthropic. ["Introducing Skills."](https://claude.com/blog/skills) (~10 min) The official launch context for what Skills are designed to do.
- <span class="tag tag-required">Required</span> <span class="tag tag-standard">Standard</span> Willison, Simon. ["Notes on the Vatican's encyclical on AI."](https://simonwillison.net/2026/May/25/encyclical-on-ai/) A practitioner reading of Leo XIV's encyclical — useful as a bridge between the labor critique and the daily-use perspective.
- <span class="tag tag-required">Required</span> <span class="tag tag-standard">Standard</span> *Religion Dispatches.* ["Leo XIV Links AI Histories to Enslavement and Exploitation."](https://religiondispatches.org/2026/05/26/leo-xiv-links-ai-histories-enslavement-and-exploitation) Pairs with Bender & Hanna; situates the labor and extraction critique inside a longer moral genealogy.
- <span class="tag tag-standard">Standard</span> Underwood, Ted. ["A Genealogy of Distant Reading."](https://dhq.digitalhumanities.org/vol/11/2/000317/000317.html) *DHQ* 11.2 (2017). The canonical history.
- <span class="tag tag-standard">Standard</span> Bender & Hanna, *The AI Con*, Chapter 3: Leisure for Me, Gig Work for Thee. The labor critique to balance the practitioner-blog enthusiasm.

## Exercise Menu

- <span class="tag tag-light">Light</span> **Wrangle something messier than plain text (~45 min).** Take a source that *isn't* already clean text — a PDF with an awkward layout, a screenshot, a photo of your own handwritten notes, a scan of a manuscript page, slides exported as images. Upload to a fresh Project and prompt Claude either to (a) convert it to clean markdown or (b) pull the text out as a transcript. Iterate: spot-check the output against the original, prompt for corrections on uncertain passages, ask Claude to flag what it could not read. The goal is *usable* material — something you could now feed into a distant-reading workflow next week. Pay attention to where Claude hallucinates versus where it accurately marks uncertainty.
- <span class="tag tag-standard">Standard</span> **Build your first Skill (~90 min).** In Claude, open **Settings → Capabilities → Skills**. Enable the **skill-creator** skill. Then prompt Claude: *"Use the skill-creator skill to help me create a new skill for [your task]. Ask me clarifying questions about my preferences before you draft the skill."* Two suggested directions, both responding to defaults you've probably noticed by now:
  - An **aesthetic-control skill** that defines a visual identity for any HTML artifact Claude generates, so you're not stuck with the default Anthropic look. Pick a reference point — Geocities-retro-web, brutalist, your discipline's print conventions, a specific artist's site, the look of a journal you publish in — and encode it. (My own working example is a Geocities-retro-web skill.)
  - A **text-analysis pipeline skill** that bundles the workflow we ran in Workshop 2 (preprocessing → bag-of-words → key phrases → comparative passages → thematic network) into one reusable instruction set, so you can repeat the same analysis across new corpora without re-prompting each step.

  Save the resulting Skill, upload it via Settings, and test it on a fresh conversation. Document what changed in the defaults. Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (PDF) is the companion reference — the same guide demoed in Workshop 2. *Source: [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (Option One).*
- <span class="tag tag-deep">Deep</span> **Scale up in Claude Cowork (~3 hr, advanced).** Take the Workshop 2 textual-analysis workflow and rerun it inside **Claude Cowork** — Claude working alongside you in a desktop session with read/write access to a local folder. *Critical setup:* create a **new, empty folder**, add only the materials you want analyzed (or operated on), and point Cowork at that folder — never a broad personal directory. Use it to rerun the in-class workflow at a larger scale than the chat interface comfortably handles. This pattern is the right shape for **repeat cases** you'll want to do over and over: cleaning up successive weeks of lecture captions, normalizing a recurring set of student submissions, processing each new batch of fieldnotes as it comes in. You'll see another Cowork demo in Workshop 4 (W11); this is a chance to try it ahead of time on a workflow you already know.

## What to Carry Into Workshop 3

Two things to bring back:

1. **A Discord post on at least one exercise.** Whichever exercise you choose, share the result in the cohort Discord — a screenshot, the Skill markdown file, a link to your Project, the transcript you wrangled, or a short note on what surprised you and where Claude got it wrong. The post is the deliverable; the exchange is where the cohort learning happens.
2. **Five to ten images for the live workshop.** Assemble images you might want to analyze together — archival scans, art, photographs, comic covers, hand-written documents, illustrations from a book you teach. Use materials you have rights to (your own photos, public domain, Creative Commons, [Library of Congress Pictures](https://www.loc.gov/pictures/), [Internet Archive Images](https://archive.org/details/image)). Have them ready as a folder for upload on June 10.

## Cross-references

- Source materials: [HumanitiesAI/weekfour](https://anastasiasalter.net/HumanitiesAI/weekfour.html) (distant reading), [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (Skills walkthrough), [HumanitiesAI/weekfourteen](https://anastasiasalter.net/HumanitiesAI/weekfourteen.html) (Code Web for distant reading).
