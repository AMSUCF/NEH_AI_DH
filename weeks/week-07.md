---
week: 7
title: "Workshop 4: Web and Interactive Applications"
kind: workshop
theme: "Agentic AI, GitHub Pages, and Claude Code Web"
starts: 2026-06-22
summary: |
  This week, we will be looking at how classic digital humanities pedagogical tasks (such as the creation of an eportfolio or the visualization of a dataset) can change with the addition of agentic AI tools. We'll define what agentic AI currently means and how it works, introduce GitHub and GitHub pages as a free method for students to build web-based projects; and introduce the Claude Code Web interface.
workshop:
  title: "Workshop 4: Web and Interactive Applications"
  date: 2026-06-24
  time: "10 AM - noon"
  location: CHDR
---

By the end of the session, every participant will have a live URL to either a deployed ePortfolio *or* a deployed dataset visualization, in their voice, in roughly 90 minutes.

<div class="workshop-callout" markdown="1">
**NEH Workshop 4 — Tuesday, June 24, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the broader NEH learning community.

[Open the slide deck →]({{ '/slides/web/w07/' | relative_url }}){:.btn}
</div>

## What to Bring

- A free [GitHub account](https://github.com/) — created ahead of time if possible, but we will walk through signup at the start of the session for anyone who is new. Use your `.edu` email so you can apply for [GitHub Education](https://education.github.com/) benefits.
- **One** of the following, depending on which path you want to take:
  - **ePortfolio path:** your CV, a course syllabus, a project description, or a short bio paragraph in `.docx`, `.pdf`, or `.md`.
  - **Dataset visualization path:** a small dataset relevant to your work — a CSV, a JSON file, a list. Examples: a course's reading list with metadata, a chronology of works in a movement, the texts you analyzed in W3, a small archive index.
- Claude Pro subscription with access to **Claude Code Web** at [claude.ai/code](https://claude.ai/code).
- No prior GitHub or web-deployment experience is assumed.

## Pre-Workshop Reading

- Martin, Meredith. ["Command Lines for the Humanities."](https://www.cambridge.org/core/journals/pmla/article/command-lines-for-the-humanities/097F959E6971063D05B085E698354BA2) *PMLA* 139.3 (2024): 541–547. (~30 min) The conceptual frame for why command-line and code work belongs in humanities pedagogy.
- Willison, Simon. *[How Coding Agents Work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/).* Read the section "What is an agent?" (~10 min) The plainest current definition.
- Evans, Julia. [*So You Want to Be a Wizard.*](https://wizardzines.com/zines/wizard/) Free zine. (~20 min flip-through.) The right tone for entering this work.

Optional:

- Ford, Paul. ["Timing My Vibe Coding."](https://ftrain.com/aboard-podcast-timing-my-vibe-coding) *The Aboard Podcast.* (~25 min listen)
- Littman, *Code to Joy*, Chapter 1: Telling Computers What to Do.

## Session Outline (120 minutes)

1. **What "agentic AI" actually means.** Tool use (the model can call functions you give it), planning (the model decides what to do next, in what order, when to stop), and subagents (the model can spawn helper instances of itself). An *agent* is the loop these compose into. Why this is a meaningful shift from chat-only Claude — and why everything we did in W1–W6 is still the substrate.
2. **GitHub and GitHub Pages, from scratch.** Walk through, together: creating an account, what a *repository* is, what a *commit* is in plain language, what *main* means, and what GitHub Pages does (a free public URL pointed at the contents of your repo). Anyone who needs to sign up does it now; everyone leaves this section with a working account and one empty repository.
3. **From Artifact to Code Web.** What persists, what changes. Why a real GitHub repository matters even for a one-page site (version history, attribution, sharing). What Claude Code Web can and cannot do compared to the desktop CLI we will tour in W11.
4. **Live demo: two paths.** I open Code Web and demo both:
   - **CV → ePortfolio**: prompt Claude to design and deploy a single-page personal site.
   - **Data → visualization**: prompt Claude to read a CSV / JSON, propose three visualizations, and deploy the chosen one as an interactive page.
   Both ship to GitHub Pages within the demo. We watch the URLs go live. We iterate visibly.
5. **Hands-on: your document or dataset.** Pick a path. Each participant follows the demo on their own materials. Roving help, pair support encouraged.
6. **Discussion: assignment design.** Open Q&A on how AI fits into the assignments and projects you are building. What changes when "build a website" becomes a 90-minute exercise instead of a semester project? What gets *added* to the assignment to keep it pedagogical?
7. **Wrap.** What broke today? What surprised you?

## Core Exercise

**Pick one path. Both deploy to GitHub Pages.**

### Path A — CV to ePortfolio (deployed)

1. **Create a fresh GitHub repository.** From your GitHub home page, click the green *New* button. Name it descriptively (`my-eportfolio`, `firstname-lastname-cv`). Set it to *Public*. Check *Add a README*.
2. **Upload your document.** From the repo page, click *Add file → Upload files* and drag the CV / syllabus / description in. Click *Commit changes*.
3. **Open [Claude Code Web](https://claude.ai/code).** Authorize the GitHub connection. Select the repository.
4. **Prompt:** *"This repository has my [CV / syllabus / project description] in it. Read it, then build a fun-but-professional single-page website appropriate to the type of work it represents. Use the content from the document. Put the website in a subfolder called `/site`. Make it deploy-ready for GitHub Pages."*
5. **Iterate.** Color, layout, sections. The conversation is the workflow.
6. **Deploy via GitHub Pages.** *Settings → Pages*, source `main` branch, folder `/site` (or `/(root)`). Wait two minutes; the live URL appears.
7. **Save the URL.** Bring it to W9.

### Path B — Dataset to visualization (deployed)

1. **Create a fresh GitHub repository.** Same process as above.
2. **Upload your dataset** (CSV, JSON, or a list).
3. **Open [Claude Code Web](https://claude.ai/code).** Authorize, select repo.
4. **Prompt:** *"This repository has a dataset of [describe what it is and what each column means]. I'd like to make it explorable as a single-page website. Read the data, propose three visualization approaches, and ask me which one to build. Use HTML / CSS / JS only — no build step. Deploy-ready for GitHub Pages."*
5. **Pick one. Iterate.** Ask Claude to add filters, change the color palette, fix mobile layout, add captions or notes.
6. **Deploy via GitHub Pages.** Same process.
7. **Save the URL.** Bring it to W9.

## Pedagogical Note

This is the workshop where some participants will feel the strongest dissonance: *I just made a website without writing any code.* The honest answer is yes — and also: you wrote prose, you made design decisions, you reviewed the output, you committed changes. That is a literacy, even if it is not the literacy you grew up calling "programming." Read Martin's *PMLA* essay before the session if you want a frame for the conversation it will provoke.

For your own teaching: this is a high-leverage assignment design, but it is also one where students can use the tool poorly. Scaffold by requiring (a) at least three iteration cycles documented in the conversation history, (b) a reflection on at least one design decision the student overrode, and (c) attribution of AI use in the README.

## Cross-references

- Source materials: `HumanitiesAI/weekeleven.md` (GitHub Pages deploy), `weekfour.md` (distant reading visualization with Claude Code), `CriticalMaking2026/exercises/ten_visualization.md` (P5.js + Claude Code prototyping).
