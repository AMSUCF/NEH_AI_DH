---
week: 7
title: "Workshop 4: Web and Interactive Applications"
kind: workshop
theme: "Building interactive tools with Claude Code Web"
starts: 2026-06-22
workshop:
  title: "Workshop 4: Web and Interactive Applications"
  date: 2026-06-24
  time: "10 AM - noon"
  location: CHDR
---

This is the transition workshop: from chat-and-Artifacts to **Claude Code Web**. The change is meaningful — Code Web works against a real **GitHub** repository, can write and edit multiple files, and can deploy a real site through **GitHub Pages**. We assume most participants have not used either before, so this session introduces both from scratch: what GitHub is (a place to store and version your work, owned by you, not by Claude), what a repository is, what Pages does (turn the contents of a repo into a public website at a free URL). We then use Code Web to do something concrete: take a CV, a syllabus, or a project description and turn it into a deployed website. By the end of the session, every participant will have a live URL to a site they built, in their voice, in roughly 90 minutes.

<div class="workshop-callout" markdown="1">
**NEH Workshop 4 — Tuesday, June 24, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the broader NEH learning community.

[Open the slide deck →]({{ '/slides/web/w07/' | relative_url }}){:.btn}
</div>

## What to Bring

- A free [GitHub account](https://github.com/) — created ahead of time if possible, but we will walk through signup at the start of the session for anyone who is new. Use your `.edu` email so you can apply for [GitHub Education](https://education.github.com/) benefits.
- A document — your CV, a course syllabus, a project description, or even a short bio paragraph — in `.docx`, `.pdf`, or `.md`. Have a copy on your laptop ready to upload.
- Claude Pro subscription with access to **Claude Code Web** at [claude.ai/code](https://claude.ai/code).
- No prior GitHub or web-deployment experience is assumed.

## Pre-Workshop Reading

- Martin, Meredith. ["Command Lines for the Humanities."](https://www.cambridge.org/core/journals/pmla/article/command-lines-for-the-humanities/097F959E6971063D05B085E698354BA2) *PMLA* 139.3 (2024): 541–547. (~30 min) The conceptual frame for why command-line and code work belongs in humanities pedagogy.
- Ford, Paul. ["Timing My Vibe Coding."](https://ftrain.com/aboard-podcast-timing-my-vibe-coding) *The Aboard Podcast*, July 29, 2025. (~25 min listen or transcript.) Practitioner perspective on what changes.
- Evans, Julia. [*So You Want to Be a Wizard.*](https://wizardzines.com/zines/wizard/) Free zine. (~20 min flip-through.) The right tone for entering this work.

Optional:

- Littman, *Code to Joy*, Chapter 1: Telling Computers What to Do.

## Session Outline (120 minutes)

1. **GitHub and GitHub Pages, from scratch (~20 min).** Walk through, together: creating an account, what a *repository* is, what a *commit* is in plain language, what *main* means, and what GitHub Pages does (a free public URL pointed at the contents of your repo). Anyone who needs to sign up does it now; everyone leaves this section with a working account and one empty repository.
2. **From Artifact to Code Web (~10 min).** What persists, what changes. Why a real GitHub repository matters even for a one-page site (version history, attribution, sharing). What Claude Code Web can and cannot do compared to the desktop CLI we will tour later.
3. **Live demo: CV to ePortfolio (~25 min).** I open Code Web with a sample CV, prompt Claude to design and build a single-page site appropriate to the field, deploy to GitHub Pages, and watch the URL go live. Iterate: change the palette, add a section, fix a typo. Walk through the GitHub side: branches, pull requests, why we do not just edit `main` directly.
4. **Hands-on: your document (~50 min).** Each participant follows the same path. Roving help, pair support encouraged. The opening prompt structure is in the [exercise instructions](#core-exercise) below.
5. **Discussion: assignment design (~10 min).** Open Q&A on how AI fits into the assignments and projects you are building.
6. **Wrap (~5 min).** What broke today? What surprised you?

## Core Exercise

**CV to ePortfolio (deployed).** Adapted from `DistantCodingUMKC` Example 1 and `HumanitiesAI/weekeleven.md`.

1. **Create a fresh GitHub repository.** From your GitHub home page, click the green *New* button. Name it descriptively (`my-eportfolio`, `firstname-lastname-cv`). Set it to *Public* (Pages requires this on the free tier). Check *Add a README*. This is your first repo if you are new to GitHub — that is fine.
2. **Upload your document.** From the repo page, click *Add file → Upload files* and drag the CV / syllabus / description in. Click *Commit changes* at the bottom. (A *commit* is just a saved version — you'll make many.)
3. **Open [Claude Code Web](https://claude.ai/code).** Authorize the GitHub connection if prompted. Select the repository.
4. **Prompt:**
   > *"This repository has my [CV / syllabus / project description] in it. Read it, then build a fun-but-professional single-page website appropriate to the type of work it represents. Use the content from the document. Put the website in a subfolder called `/site`. Make it deploy-ready for GitHub Pages."*
5. **Iterate.** Ask for color changes, layout tweaks, additional sections. The conversation is the workflow.
6. **Deploy via GitHub Pages.** In the repo's *Settings → Pages*, set *Source* to *Deploy from a branch*, then choose `main` and `/site` (or `/(root)` if Claude put files at the top level). Save. Wait two minutes; refresh the Pages settings — the live URL appears at the top of that page. That URL is now yours and will stay live as long as the repo exists.
7. **Save the URL.** Bring it to Workshop 5 (we will iterate on it for accessibility and playfulness).

## Pedagogical Note

This is the workshop where some participants will feel the strongest dissonance: *I just made a website without writing any code.* The honest answer is yes — and also: you wrote prose, you made design decisions, you reviewed the output, you committed changes. That is a literacy, even if it is not the literacy you grew up calling "programming." Read Martin's *PMLA* essay before the session if you want a frame for the conversation it will provoke.

For your own teaching: this is a high-leverage assignment design, but it is also one where students can use the tool poorly. Scaffold by requiring (a) at least three iteration cycles documented in the conversation history, (b) a reflection on at least one design decision the student overrode, and (c) attribution of AI use in the README.

## Cross-references

- Source materials: `DistantCodingUMKC/index.md` (Example 1, ePortfolio); `HumanitiesAI/weekeleven.md` (GitHub Pages deploy); `DistantCoding/transcript.md` (vibe-coding framing).
