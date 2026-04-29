---
layout: default
title: Exercises
---

# Exercise Menu

Every workshop has one core exercise; every async week offers a deep-dive menu at varying time commitments. This page consolidates them for quick reference. The full setup, prompts, and discussion questions live on each weekly module page.

- <span class="tag tag-light">Light</span> ~30 minutes
- <span class="tag tag-standard">Standard</span> ~90 minutes
- <span class="tag tag-deep">Deep</span> ~3 hours

## Stage 1 — Text (Weeks 1–4)

### Workshop 1 (May 13) — Build our own ELIZA

<span class="tag tag-standard">Standard</span> **Build a Claude Artifact in the spirit of Weizenbaum's 1966 ELIZA — together.** Group exercise. Open Claude, prompt it to construct a Rogerian-style chatbot Artifact. Style and tone are yours: a snarky librarian, a doom-prophet, a noir detective, a Rogerian therapist. Compare to the [masswerk web ELIZA](https://www.masswerk.at/eliza/). Notice where the ELIZA effect kicks in, sixty years on.

*Source: `HumanitiesAI/weekone.md` (Three Conversations).*

### Week 2 (async) — Claude interface deep-dive

- <span class="tag tag-light">Light</span> **Settings tour + reflection.** Walk through every settings panel in Claude. Set defaults that fit your work. Write a paragraph about what surprised you and what you wish were adjustable.
- <span class="tag tag-standard">Standard</span> **Iterate a poem in an Artifact.** Pick a form (haiku, sonnet, ghazal, blackout, cento). Iterate ten times in Claude Sonnet. Publish the final as a Claude Artifact. *Source: `HumanitiesAI/weektwo.md`.*
- <span class="tag tag-deep">Deep</span> **Three-models comparison.** Run the same teaching question through Opus / Sonnet / Haiku in one Project. Track depth, hedging, hallucination rate, time. Write a one-page model-selection memo.

### Workshop 2 (May 27) — Distant reading + copyright

<span class="tag tag-standard">Standard</span> **Build a small corpus, read it across.** Bring three to ten texts in your discipline. Upload to a Claude Project. Run the distant-reading sequence: stopword filter → bag-of-words → key phrases → character or theme network → comparative read. End with an Artifact summarizing the patterns. **Plus**: write one paragraph on the copyright status of your corpus.

*Source: `HumanitiesAI/weekfour.md`; `CriticalMaking2026/exercises/eight_analysis.md`.*

### Week 4 (async) — Distant reading + Skills

- <span class="tag tag-light">Light</span> **One Project Gutenberg book.** Pick a single text, run the basic distant-reading prompts in a Project, generate a word cloud and character network. *Source: `HumanitiesAI/weekfour.md`.*
- <span class="tag tag-standard">Standard</span> **Build your first Claude Skill.** Use the **skill-creator** skill to scaffold a citation-style, alt-text, lecture-note, or syllabus-drafting skill. Save and test on a fresh conversation. *Source: `HumanitiesAI/weekfifteen.md`.*
- <span class="tag tag-deep">Deep</span> **Design an exercise for your students.** Adapt a workflow from W3 or W4 into a 60–90-minute classroom exercise. Write the prompt, scaffolding, deliverable, and rubric.

---

## Stage 2 — Visual and Multimodal (Weeks 5–6)

### Workshop 3 (June 10) — Image analysis with Projects + Artifacts

<span class="tag tag-standard">Standard</span> **Image-to-text translation set, two tools.** Five to ten images you have rights to use. **Part A** in a Project: alt-text, metadata table, three patterns across the set. **Part B** in an Artifact: a comparative gallery, grid, or typology. **Part C**: critique what each tool surfaced and missed.

*Source: `HumanitiesAI/weeksix.md`; `CriticalMaking2026/exercises/four_maps.md`.*

### Week 6 (async) — Multimodal AI

- <span class="tag tag-light">Light</span> **Infographic with Gemini Nano Banana or OpenAI Images 2.0.** Take a concept easier to *show* than *say*. Generate it in two different tools. Compare what each reaches for first.
- <span class="tag tag-standard">Standard</span> **Slide deck with Claude Design.** Take notes from a lecture, paper abstract, or workshop. Prompt Claude to build a deck via the Design / Artifact slide-deck mode. Iterate three rounds. Compare to building it by hand.
- <span class="tag tag-deep">Deep</span> **Build your own voice interface in an Artifact.** Web Speech API, prompt-driven. Compare to Claude's built-in voice mode.

---

## Stage 3 — Code Web (Weeks 7–10)

### Workshop 4 (June 24) — Agentic AI + GitHub Pages, two paths

<span class="tag tag-standard">Standard</span> **Pick a path. Both deploy to GitHub Pages.**
- *Path A — CV → ePortfolio.* Bring a CV / syllabus / project description. Claude Code Web reads it, builds a one-page site, deploys to Pages.
- *Path B — Dataset → visualization.* Bring a CSV / JSON. Claude Code Web reads it, proposes three visualization approaches, deploys the chosen one.

*Source: `HumanitiesAI/weekeleven.md`; `CriticalMaking2026/exercises/ten_visualization.md`.*

### Week 8 (async) — Multiple small projects

Pick two or three. Each is small. Each ends in a deployed URL.

- <span class="tag tag-light">Light</span> **Polish the W7 site.** Two passes: accessibility (alt-text, contrast, headings) and content (any errors).
- <span class="tag tag-standard">Standard</span> **Static handout → interactive page.** Convert a paper handout (glossary, timeline, bibliography) into a one-page interactive site.
- <span class="tag tag-standard">Standard</span> **Recommender or "find your X" tool.** Build a JSON dataset (100 books / 50 films / 30 archives) plus a minimal interactive front end. *Source: `HumanitiesAI/weeknine.md`.*
- <span class="tag tag-standard">Standard</span> **Public scholarship one-pager.** Summarize a piece of your scholarship for a non-specialist audience.
- <span class="tag tag-standard">Standard</span> **Interactive worksheet for one assignment.** Walk a student through one of your assignments in an interactive page with localStorage save.
- <span class="tag tag-light">Light</span> **Debug-with-Claude practice.** Deliberately break one of the above; fix it only by talking to Claude.

### Workshop 5 (July 8) — Course games, planning mode, AI policy

<span class="tag tag-standard">Standard</span> **Two halves, both required.**
- *Build with planning mode* — a small game or playful tool around a concept from your course. Open with: *"Enter plan mode. Do not exit plan mode until I confirm the plan is ready."* Iterate the plan before letting Claude build.
- *Draft a course AI policy* — one page, addressing copyright, attribution, accessibility, equity of access, labor, UDL, and the *agentic* question. Frame as invitation, not prohibition.

*Source: `HumanitiesAI/weeknine.md`, `weektwelve.md`; `CriticalMaking2026/exercises/six_game.md`.*

### Week 10 (async) — UDL + AI policy, by your discipline

- <span class="tag tag-light">Light</span> **Policy A/B.** Use Claude in a Project to identify three UDL-aligned revisions to an existing AI policy.
- <span class="tag tag-standard">Standard</span> **Accessibility audit + fix in Code Web.** Run W7 site through WAVE or axe DevTools. Use planning mode in Claude Code Web to fix the top three issues.
- <span class="tag tag-deep">Deep</span> **Full syllabus integration.** Revise a syllabus to integrate AI policy, signature assignment, and at least one AI-aware exercise. Anchor in CAST UDL framework.

---

## Stage 4 — Agentic Futures (Weeks 11–12)

### Workshop 6 (July 22) — Demo + write your `CLAUDE.md`

<span class="tag tag-light">Light</span> **Watch the demo, write a `CLAUDE.md`.** This session is mostly demo (Cowork, Claude CLI, MCP, Superpowers). Your hands-on portion: in a text editor, draft a `CLAUDE.md` describing your research domain, typical workflows, preferences, and boundaries. No installation required.

*Source: `DHSI_DH_AI_2026/dhsi-2026-course-packet.md` (context engineering).*

### Week 12 (async) — Course proposal / course update

- <span class="tag tag-light">Light</span> **Final reflection (500 words).** What did you build, what surprised you, what will you carry into fall? *Source pattern: `HumanitiesAI/finalreflection.md`.*
- <span class="tag tag-standard">Standard</span> **Course proposal / syllabus revision in a Claude Project.** Upload syllabus / proposal + your AI policy + one artifact + your `CLAUDE.md`. Iterate as a critical-reader conversation. Specifically check learning-outcome alignment and draft a 250-word public-facing summary.
- <span class="tag tag-deep">Deep</span> **One CLI or Cowork session on a personal machine.** Optional. Install [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code), run one Brainstorm → Spec → Plan → Implementation cycle on a small project (could be your fall course site).

---

## Bring-along checklist (workshop weeks)

| Workshop | What to bring |
|----------|----------------|
| W1 (May 13) — Introducing AI | A laptop. A document, conversation, or short piece of writing for your first prompt. |
| W3 (May 27) — Textual Analysis | A small corpus (3–10 texts) you have rights to use. |
| W5 (June 10) — Visual Analysis | An image set (5–10 images you have rights to). |
| W7 (June 24) — Web Applications | A CV / syllabus *or* a dataset (CSV / JSON). A free GitHub account. |
| W9 (July 8) — Playful + Policy | A concept from your course. A draft AI policy paragraph. The W7 site URL. |
| W11 (July 22) — Agentic Futures | All your artifacts (W7, W9, AI policy, Skill from W4). Optional: a personal laptop with admin access. |
