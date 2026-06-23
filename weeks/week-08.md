---
week: 8
title: "Build Something Real (Asynchronous)"
kind: async
theme: "Confidence-building across Claude Code Web and Claude Code Desktop (with Hugging Face plugins)"
starts: 2026-06-29
summary: |
  Workshop 4 introduced two interfaces side by side — Claude Code Web in the browser and Claude Code Desktop on your own machine. This week you pick one of four projects and carry it to a finished thing. Two run in Claude Code Web (rebuild an old site you'd given up on; build an interactive educational resource for a course). Two run in Claude Code Desktop and reach for open models on Hugging Face through plugins (a tool for a project; a local audio/captioning tool for your own class). Required reading: Willison's "Beyond Vibe Coding" and Farrell's "After Software Eats the World."
---

There is no in-person meeting.

<div class="async-callout" markdown="1">
**Asynchronous expectations.** Read the **Required** items in the menu below and complete **at least one** of the four projects. **Post the result back in the cohort Discord** — a live URL, a screenshot, a short screen recording of your tool running, or a paragraph on what surprised you. The Discord post is the deliverable. The two Claude Code Web projects (A, B) are the natural next step after Workshop 4; the two Claude Code Desktop projects (C, D) are the deeper, optional path for anyone ready to work locally.
</div>

## Two Tracks, One Habit

Workshop 4 ran one demo in **Claude Code Web** (the browser, at [claude.ai/code](https://claude.ai/code)) and one in **Claude Code Desktop** (the local app). This week is where that comparison becomes muscle memory. Pick a project from either track; the underlying habit — *describe the goal, let the agent plan, iterate, judge the output* — is the same on both.

**Track 1 — Claude Code Web (projects A, B).** Browser-only, nothing to install. The same loop from Workshop 4:

```
1. Initialize a fresh GitHub repo (Public, with a README).
2. Upload any source files (old site files, handouts, JSON, images).
3. Open Claude Code Web; select the repo.
4. Enter plan mode; describe the goal, the audience, the constraints.
5. Confirm the plan, then build. Push. Check the live URL. Iterate.
```

**Track 2 — Claude Code Desktop (projects C, D).** The local app — the one we demoed alongside Code Web and tour fully in **Workshop 6 (W11)**. The files live on your machine, you run code locally, and you can give Claude new powers through **plugins** (including a Hugging Face plugin that lets it reach open models like Whisper):

```
1. Install Claude Code Desktop on a machine you control.
2. Open a local project folder; drop your source files in.
3. (Project D) Add the Hugging Face plugin so Claude can call open models.
4. Enter plan mode; describe the tool you want.
5. Confirm, build, run it locally, iterate. Commit through GitHub Desktop.
```

> **A note on where Desktop runs.** UCF currently does not allow faculty to install local agentic tools on university computers without going through a permissions process — so treat the Desktop projects (C, D) as work for a **personal machine**. This is the same constraint we discuss in Workshop 6; W8 is just an early on-ramp for anyone who wants to start now. If a local install isn't an option for you, stay in Track 1 — you can do everything required this week in the browser.

If anything breaks on either track — a build error, a deploy failure, a plugin that won't connect — paste the error or a screenshot back to Claude and ask. **Most issues resolve in one or two prompts.** Debugging *with* Claude rather than around it is the literacy worth building this week.

## Reading Menu

- <span class="tag tag-required">Required</span> <span class="tag tag-standard">Standard</span> Willison, Simon. ["Beyond Vibe Coding."](https://simonwillison.net/2025/Sep/4/beyond-vibe-coding/) September 4, 2025. (~30 min) When the chat-driven model breaks down, and what to do instead — the frame for moving from "vibe" to a real, repeatable build process, which is exactly the jump these four projects ask for.
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Farrell, Henry. ["After Software Eats the World, What Comes Out the Other End?"](https://www.programmablemutter.com/p/after-software-eats-the-world-what) October 3, 2024. (~25 min) Helpful framing for what you just did in W7 and are extending now: what changes when building software gets this cheap.
- <span class="tag tag-light">Light</span> Cohen, Dan. ["The Index and the Vector."](https://newsletter.dancohen.org) *Humane Ingenuity.* (~15 min) The DH-specific framing of what these tools change for archives and reference work.
- <span class="tag tag-standard">Standard</span> Littman, *Code to Joy*, Chapters 2–3 (The What of Programming; Sequencing Commands). (~90 min) An accessible introduction to programming concepts; a useful counterpoint to vibe-coding hype, and good ground before the Desktop projects.

## Project Menu — Pick One

Each ends in something you can show: a live URL or a working local tool. Pick the one that fits a real need you have.

### A. Rebuild an old web project — Claude Code Web (~2 hr)

Pick a website you made and then let lapse — a Flash-era project now unplayable, a long-dead WordPress or Omeka exhibit, a course site stuck in a template you've outgrown, a static page that looks like the year you made it. **Make a copy of it in a fresh repo and set Claude on the rebuild.**

1. **Create a fresh GitHub repo** (Public, *Add a README*). Get the old site's files in: download the existing HTML/CSS/assets and drag them in via *Add file → Upload files*, or, if the original is gone, gather screenshots and any surviving text.
2. **Open [Claude Code Web](https://claude.ai/code)** and connect the repo.
3. **Plan first:** *"Enter plan mode. This repo holds an old website of mine. Read what's here, then propose a plan to rebuild it as a modern, accessible, responsive single site that preserves the original content and intent. Don't build until I confirm."*
4. **Confirm, then build and iterate.** Decide deliberately what to preserve (the content, the voice) versus modernize (layout, accessibility, mobile).
5. **Deploy via GitHub Pages** and save the URL.

The point is recovery and stewardship: agentic tools make it realistic to bring abandoned scholarship back online. *Related DHSI demo: [Deploying to GitHub Pages with Claude Code for Web](https://anastasiasalter.net/DHSI_DH_AI_2026/).*

### B. Build an interactive educational resource — Claude Code Web (~2 hr)

Make a web resource for one of your courses that has a real **interactive component** — not a static handout, but something a student *does*. A clickable timeline, a filterable glossary or dataset explorer, a self-check quiz, a concept simulation, an annotated map, a step-through of a primary source.

1. **Create a fresh GitHub repo** (Public, *Add a README*). Upload your source material — the glossary, the dataset, the readings list, the images.
2. **Open [Claude Code Web](https://claude.ai/code)** and connect the repo.
3. **Plan first:** *"Enter plan mode. Build a single-page interactive learning resource for [course/topic] from these materials. It should let a student [filter / quiz themselves / step through / explore]. HTML/CSS/JS only, no build step, deploy-ready for GitHub Pages. Don't build until I confirm."*
4. **Confirm, build, iterate.** Read it as a teacher: is the interaction doing pedagogical work, or just decoration?
5. **Deploy via GitHub Pages** and save the URL — you can reuse this pattern when we build course games in **Workshop 5 (W9)**.

*Source patterns: [HumanitiesAI/weekeleven](https://anastasiasalter.net/HumanitiesAI/weekeleven.html), [HumanitiesAI/weeknine](https://anastasiasalter.net/HumanitiesAI/weeknine.html).*

### C. Build a project tool — Claude Code Desktop (~2–3 hr)

Use **Claude Code Desktop** (local, personal machine) to build a small tool that you or your students would actually use in a project — something that takes files on your disk and does work on them. A spreadsheet-to-clean-dataset converter, a citation reformatter, a batch file-renamer for an archive, a metadata extractor, a corpus-cleaning script with a tiny interface.

1. **Install Claude Code Desktop** and open a fresh local folder. Drop in a few real sample files.
2. **Plan first:** *"Enter plan mode. I want a tool that takes [these files] and produces [this output]. I'll run it on my own machine. Propose the simplest design and tell me what I'll need installed. Don't build until I confirm."*
3. **Confirm, build, run it locally, iterate.** Watch how this differs from Code Web: the files stay on your machine, you run the tool yourself, and the conversation can touch your real working directory.
4. **Commit through GitHub Desktop** if you want to keep or share it.

This is the on-ramp to the local-powertools workflow we tour in **Workshop 6 (W11)**. *Related DHSI demo: [Distant Coding with Claude Code](https://anastasiasalter.net/DHSI_DH_AI_2026/) and the student "Archive Prep Tools" project.*

### D. Build a local audio / captioning tool with Hugging Face plugins — Claude Code Desktop (~3 hr)

The most ambitious option, and a direct extension of the **Hugging Face connector** work from W6. Use **Claude Code Desktop** plus a **Hugging Face plugin** to build a tool for your own class that runs an open model locally — for example, a **caption-correction system** (transcribe a recorded lecture with Whisper, then fix and format the captions) or a **local audio tool** (clip, transcribe, or summarize oral-history or fieldwork recordings) — without uploading sensitive recordings to the cloud.

1. **Install Claude Code Desktop** and open a fresh local folder. Add a sample audio or video file you have rights to.
2. **Add the Hugging Face plugin** so Claude Code can reach open models on the [Hugging Face Hub](https://huggingface.co/) (Whisper for transcription, and others). If it asks you to authenticate, set your `HF_TOKEN` from your [Hugging Face settings](https://huggingface.co/settings/tokens).
3. **Plan first:** *"Enter plan mode. Using the Hugging Face plugin and a Whisper model running locally, build me a tool that transcribes this audio and lets me correct the captions, then exports clean `.srt` (or `.vtt`). Everything stays on my machine. Tell me what to install. Don't build until I confirm."*
4. **Confirm, build, run it locally, iterate.** Read the captions critically — accuracy on names, jargon, and overlapping speech is exactly the judgment that keeps you in the loop (see WebAIM on why caption accuracy matters, from W6).
5. **Commit through GitHub Desktop** if you want to reuse it next term.

*Related DHSI demos: the Hugging Face MCP and Whisper-for-archival-audio demonstrations, and the student "Archive Prep Tools" project — [DHSI 2026](https://anastasiasalter.net/DHSI_DH_AI_2026/).*

## What to Carry Into Workshop 5

Bring a **dataset or course concept** you'd turn into a small interactive thing — a concept you'd make a game of, a corpus you'd make a quiz from, a collection you'd make a generator for. (Project B is a good way to surface one.) And bring **a paragraph of AI policy from your current syllabus** — even one paragraph; if you don't have one, bring a syllabus and a willingness to draft.

## Cross-references

- Builds on: [Week 6](week-06.md) (Hugging Face connector, caption correction) and [Week 7](week-07.md) (Code Web vs. Code Desktop, GitHub Pages).
- Looks ahead to: [Workshop 5 (W9)](week-09.md) (course games, planning mode) and [Workshop 6 (W11)](week-11.md) (local agentic powertools, toured fully).
- Source materials: [DHSI 2026](https://anastasiasalter.net/DHSI_DH_AI_2026/) (Image Metadata, GitHub Pages deploy, Hugging Face MCP, Whisper audio), [HumanitiesAI/weekeleven](https://anastasiasalter.net/HumanitiesAI/weekeleven.html), [HumanitiesAI/weeknine](https://anastasiasalter.net/HumanitiesAI/weeknine.html).
