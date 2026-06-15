---
week: 7
title: "Workshop 4: Web and Interactive Applications"
kind: workshop
theme: "Agentic AI, GitHub Pages, and Claude Code Web"
starts: 2026-06-22
summary: |
  This week, we will be looking at how classic digital humanities pedagogical tasks (such as the creation of an eportfolio or the annotation and presentation of an image collection) can change with the addition of agentic AI tools. We'll define what agentic AI currently means and how it works, introduce GitHub and GitHub pages as a free method for students to build web-based projects; and introduce the Claude Code Web interface, comparing it with the local Claude Code Desktop workflow.
workshop:
  title: "Workshop 4: Web and Interactive Applications"
  date: 2026-06-24
  time: "10 AM - noon"
  location: CHDR
---

By the end of the session, every participant will have a live URL to either a deployed ePortfolio *or* a deployed, annotated image slideshow, in their voice, in roughly 90 minutes.

<div class="workshop-callout" markdown="1">
**NEH Workshop 4 — Wednesday, June 24, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community.

[Open the slide deck →]({{ '/slides/web/w07/' | relative_url }}){:.btn}
</div>

## What to Bring

- A free [GitHub account](https://github.com/) — created ahead of time if possible, but we will walk through signup at the start of the session for anyone who is new. Use your `.edu` email so you can apply for [GitHub Education](https://education.github.com/) benefits.
- **One** of the following, depending on which path you want to take:
  - **ePortfolio path:** your CV, a course syllabus, a project description, or a short bio paragraph in `.docx`, `.pdf`, or `.md`.
  - **Image-slideshow path:** a small set of images you have rights to use (5–15) — your own photographs, public-domain scans, or Creative Commons images. Examples: documentation of your fieldwork or making, a teaching image set, a small selection from an archive.
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
3. **From Artifact to Code Web.** What persists, what changes. Why a real GitHub repository matters even for a one-page site (version history, attribution, sharing). What Claude Code Web can and cannot do compared to **Claude Code Desktop** — the local app I demo alongside it today and that we tour fully in Workshop 6 (W11).
4. **Live demo: two builds, in Claude Code Desktop.** I run both builds in **Claude Code Desktop** (the version that lives on your own machine) so you can compare it with the browser workflow you'll do hands-on:
   - **CV → ePortfolio**: plan, build, and deploy a single-page personal site.
   - **Image set → annotated slideshow**: generate alt text for each image, rename the files to match their contents, and build a slideshow.
   Both ship to GitHub Pages within the demo. We watch the URLs go live, we iterate visibly, and we name what's different between the local (Desktop) and browser (Code Web) workflows.
5. **Hands-on: your document or your images.** Pick a path. Each participant follows the demo on their own materials, in Claude Code Web. Roving help, pair support encouraged.
6. **Discussion: assignment design.** Open Q&A on how AI fits into the assignments and projects you are building. What changes when "build a website" becomes a 90-minute exercise instead of a semester project? What gets *added* to the assignment to keep it pedagogical?
7. **Wrap.** What broke today? What surprised you?

## Core Exercise

**Both paths build and deploy agentically in [Claude Code Web](https://claude.ai/code) — plan, iterate, deploy to GitHub Pages, straight from the browser with no local setup. Pick one.** In the live demo I run the same two builds in **Claude Code Desktop** (the local app) so you can watch the difference between the browser workflow you'll use here and the local-files-plus-Desktop workflow we tour properly in Workshop 6.

> **If the GitHub connector asks for a token:** Code Web's GitHub connection sometimes needs a personal access token (PAT) rather than one-click authorize. If it does: GitHub → *Settings → Developer settings → Personal access tokens → Fine-grained tokens*, give it read/write on your repository, and paste it when Code Web prompts. We'll walk through this together if it comes up.

### Path A — CV to ePortfolio (deployed)

1. **Create a fresh GitHub repository.** From your GitHub home page, click the green *New* button. Name it descriptively (`my-eportfolio`, `firstname-lastname-cv`). Set it to *Public*. Check *Add a README*.
2. **Upload your document.** From the repo page, click *Add file → Upload files* and drag the CV / syllabus / description in. Click *Commit changes*.
3. **Open [Claude Code Web](https://claude.ai/code).** Connect the GitHub repository.
4. **Plan before you build.** Prompt: *"Enter plan mode. This repository has my [CV / syllabus / project description]. Read it, then propose a plan for a fun-but-professional single-page website appropriate to the work it represents. Don't build until I confirm the plan."*
5. **Confirm, then build.** Once the plan looks right: *"Build it using the content from the document. Put the website in a subfolder called `/site`. Make it deploy-ready for GitHub Pages."*
6. **Iterate.** Color, layout, sections. The conversation is the workflow.
7. **Deploy via GitHub Pages.** *Settings → Pages*, source `main` branch, folder `/site` (or `/(root)`). Wait two minutes; the live URL appears.
8. **Save the URL.** Bring it to W9.

### Path B — Image set to annotated slideshow (deployed)

*Adapted from the* Image Metadata with Claude Code *demo in [DHSI 2026](https://anastasiasalter.net/DHSI_DH_AI_2026/).*

1. **Create a fresh GitHub repository.** Same as above — *Public*, *Add a README*.
2. **Upload your images.** *Add file → Upload files*, drag in the 5–15 images you have rights to use, *Commit changes*.
3. **Open [Claude Code Web](https://claude.ai/code).** Connect the repository.
4. **Plan before you build.** Prompt: *"Enter plan mode. This repository has a set of images. Plan a workflow to (1) generate descriptive alt text for each image, (2) rename each file to match its contents, and (3) build a single-page slideshow that presents the images with their alt text as captions. Put the slideshow in a `/site` subfolder and make it deploy-ready for GitHub Pages. Don't build until I confirm the plan."*
5. **Confirm, then build and iterate.** Let Claude do the renames and write the slideshow. Read the alt text — fix anything it got wrong or thin; that judgment is the point. Ask for navigation, captions, a credits line.
6. **Deploy via GitHub Pages.** *Settings → Pages*, source `main` branch, folder `/site` (or `/(root)`). Wait two minutes; the live URL appears.
7. **Save the URL.** Bring it to W9.

**While you build, watch the comparison.** The demo runs both of these in Claude Code Desktop — same agentic loop (plan → build → deploy), same Pages target, but the files live on my machine and I commit through GitHub Desktop instead of the browser. Notice where the two workflows diverge: setup, where your files live, how you connect to GitHub, what persists between sessions. That contrast is the on-ramp to the CLI tour in Workshop 6.

## Pedagogical Note

This is the workshop where some participants will feel the strongest dissonance: *I just made a website without writing any code.* The honest answer is yes — and also: you wrote prose, you made design decisions, you reviewed the output, you committed changes. That is a literacy, even if it is not the literacy you grew up calling "programming." Read Martin's *PMLA* essay before the session if you want a frame for the conversation it will provoke.

For your own teaching: this is a high-leverage assignment design, but it is also one where students can use the tool poorly. Scaffold by requiring (a) at least three iteration cycles documented in the conversation history, (b) a reflection on at least one design decision the student overrode, and (c) attribution of AI use in the README.

## Cross-references

- Source materials: [HumanitiesAI/weekeleven](https://anastasiasalter.net/HumanitiesAI/weekeleven.html) (GitHub Pages deploy), [HumanitiesAI/weekfour](https://anastasiasalter.net/HumanitiesAI/weekfour.html) (distant reading visualization with Claude Code), [CriticalMaking2026/exercises/ten_visualization](https://anastasiasalter.net/CriticalMaking2026/exercises/ten_visualization.html) (P5.js + Claude Code prototyping).
