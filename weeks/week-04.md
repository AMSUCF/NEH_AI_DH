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
**Asynchronous deep-dive.** Pick one option from each menu below, or skip — Workshop 3 (June 10) shifts to visual analysis and does not require completion of these. The Skills exercise is the new tool to learn this week if you have time for one thing.
</div>

## What's New This Week: Claude Skills

A **Skill** is a reusable instruction-set Claude loads on demand — think of it as a custom system-prompt module you can build once and apply to any conversation or Project. Anthropic publishes a [skill-creator](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/skill-creator) skill that helps you write your own. Skills live in **Settings → Capabilities → Skills**.

Two examples that work well for humanities pedagogy:

- A **citation-style skill** that consistently formats references in MLA / Chicago / APA without you re-prompting.
- A **discipline-specific glossary** skill that primes Claude to use the vocabulary your field actually uses (rhetoric, archaeology, art history, etc.) rather than a generic gloss.

Building one from scratch is the closest thing this series has to "writing code" — and you don't write code. You write Markdown.

## Reading Menu

- <span class="tag tag-light">Light</span> Cohen, Dan. ["The Writing Is on the Wall for Handwriting Recognition."](https://newsletter.dancohen.org/archive/the-writing-is-on-the-wall-for-handwriting-recognition/) *Humane Ingenuity.* If you missed this for W3, read it now — it grounds the rest of the series in a longer history of computational reading in archives.
- <span class="tag tag-light">Light</span> Anthropic. ["Introducing Skills."](https://www.anthropic.com/news/skills) (~10 min) The official launch context for what Skills are designed to do.
- <span class="tag tag-standard">Standard</span> Underwood, Ted. ["A Genealogy of Distant Reading."](http://digitalhumanities.org:8081/dhq/vol/11/2/000317/000317.html) *DHQ* 11.2 (2017). The canonical history.
- <span class="tag tag-standard">Standard</span> Bender & Hanna, *The AI Con*, Chapter 3: Leisure for Me, Gig Work for Thee. The labor critique to balance the practitioner-blog enthusiasm.

## Exercise Menu

- <span class="tag tag-light">Light</span> **Single-text Project Gutenberg run (~30 min).** Pick one text from [Project Gutenberg](https://www.gutenberg.org/). Upload to a fresh Project. Run the basic distant-reading prompts (preprocessing, bag-of-words, word cloud, character network). Compare to a Voyant or text-frequency baseline if you have one. *Source: [HumanitiesAI/weekfour](https://anastasiasalter.net/HumanitiesAI/weekfour.html).*
- <span class="tag tag-standard">Standard</span> **Build your first Skill (~90 min).** In Claude, open **Settings → Capabilities → Skills**. Enable the **skill-creator** skill. Then prompt Claude: *"Use the skill-creator skill to help me create a new skill for [your task — citation formatting, alt-text writing, lecture-note structuring, syllabus drafting, etc.]. Ask me clarifying questions about my preferences before you draft the skill."* Save the resulting Skill, upload it via Settings, and test it on a fresh conversation. Document what changed in the defaults. Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (PDF) is the companion reference for this exercise — it's the same guide demoed in Workshop 2. *Source: [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (Option One).*
- <span class="tag tag-deep">Deep</span> **Design an exercise for your students (~3 hr).** Take the workflow from W3 (or one of the exercises above) and adapt it into a 60–90-minute classroom exercise for your own discipline. Write the prompt, the scaffolding, the deliverable, and the rubric. Test it yourself end-to-end before you assign it. The point is to model the *iteration* you'll ask of students. Save it as a markdown file you can edit; consider sharing it back in W12.

## What to Carry Into Workshop 3

If you do nothing else this week, **assemble five to ten images you might want to analyze together** — archival scans, art, photographs, comic covers, hand-written documents, illustrations from a book you teach. Use materials you have rights to (your own photos, public domain, Creative Commons, [Library of Congress Pictures](https://www.loc.gov/pictures/), [Internet Archive Images](https://archive.org/details/image)). Have them ready as a folder for upload on June 10.

## Cross-references

- Source materials: [HumanitiesAI/weekfour](https://anastasiasalter.net/HumanitiesAI/weekfour.html) (distant reading), [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (Skills walkthrough), [HumanitiesAI/weekfourteen](https://anastasiasalter.net/HumanitiesAI/weekfourteen.html) (Code Web for distant reading).
