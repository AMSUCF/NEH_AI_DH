---
layout: default
title: NEH DH+AI Workshop Series
---

- **Project:** *Building a Digital Humanities Generative AI Learning Community*
- **Funder:** National Endowment for the Humanities
- **Host:** Center for Humanities and Digital Research (CHDR), University of Central Florida
- **Leads:** Dr. Anastasia Salter (anastasia at ucf.edu) and Dr. Mel Stanfill
- **Term:** Summer C 2026 (May 12 – August 1)
- **Workshops:** Six biweekly Tuesdays, 10 AM – noon at CHDR (streamed and recorded)

## Contents

- [Who This Is For](#who-this-is-for)
- [What We Are Building](#what-we-are-building)
- [Tool Stages](#tool-stages)
- [Schedule](#schedule)
- [How the Asynchronous Weeks Work](#how-the-asynchronous-weeks-work)
- [Recommended Setup](#recommended-setup)
- [Weekly Modules](#weekly-modules)
- [Acknowledgements](#acknowledgements)

## Who This Is For

This workshop series is being offered at UCF to a cohort of **Digital Humanities AI Fellows**, and is being made openly available to **faculty and graduate students across humanities disciplines** who are interested in thinking both pragmatically and critically about generative and agentic AI in their teaching and research. We assume:

- No coding background. We will read code, but you will not be asked to write it from scratch — that is the point of the tools we are using.
- Mixed technical comfort. Some participants have never used Claude. Others have written about it. Both are welcome.
- A working interest in pedagogy. The series is anchored in higher-ed practice: how AI changes (or fails to change) what we ask students to do, how we read with them, and what counts as scholarly work.

## What We Are Building

The series unfolds across three arcs:

1. **Stage 1 — Text** *(Weeks 1–4)*. We start with what an LLM actually is — tracing its history through the way the web, digital culture, and networked communication built up the digitized record of human expression that now fuels LLMs and multimodal models. We look at how **reasoning layers** and human feedback (RLHF and related training) sit on top of the base model to shape its efficacy, and what that means for the higher-ed conversation about plagiarism, expertise, and reading. We use **Claude Projects** to upload a small corpus and explore it.
2. **Stage 2 — Visual** *(Weeks 5–6)*. We move to **Claude Artifacts** for image-to-text translation, alt-text generation, archival metadata, and critical reflection on AI-generated imagery already circulating in our communities. This stage foregrounds **bias** in vision models and training data, and the unresolved **copyright** questions around image generation and reuse.
3. **Stage 3 — Code** *(Weeks 7–10)*. We use **Claude Code Web** to build small interactive tools — an ePortfolio, a recommender, a humanities-centered teaching site. Because most participants will not have used them before, we introduce **GitHub** and **GitHub Pages** from scratch, and deploy our projects there. We address accessibility, Universal Design for Learning, AI policy, and copyright.
4. **Stage 4 — Agentic Futures** *(Weeks 11–12)*. The final session offers a brief tour of **Cowork** and the **Claude CLI**, with attention to the emerging agentic landscape and the sustainability of what we have built. The closing async week is reserved for sharing, reflection, and planning what to carry into your fall classroom.

## Tool Stages

| Stage | Weeks | Tool | What it changes |
|-------|-------|------|-----------------|
| 1 | W1–W4 | Claude Projects | Persistent context, file uploads, text analysis |
| 2 | W5–W6 | Claude Artifacts | Visual analysis, shareable interactive outputs |
| 3 | W7–W10 | Claude Code Web | Multi-file projects, GitHub Pages deployment |
| 4 | W11–W12 | Cowork + Claude CLI (tour only) | Agentic workflows, terminal-native AI |

## Schedule

All workshops are at CHDR, 10 AM – noon, on Tuesdays. They are streamed and recorded; attendance is optional.

{% include weeks-grid.html %}

## How the Asynchronous Weeks Work

The off-weeks (2, 4, 6, 8, 10, 12) are designed to **reinforce** what the workshop introduced, not to add new pressure. Each async page presents a **deep-dive menu**:

- **Reading menu** — three to five curated readings tagged <span class="tag tag-light">Light</span> (a single short piece, ~20 minutes), <span class="tag tag-standard">Standard</span> (a chapter or longer essay, ~60 minutes), or <span class="tag tag-deep">Deep</span> (a book section or multi-piece arc, ~3 hours). Pick what fits your schedule. Nobody is "behind."
- **Exercise menu** — two to three optional exercises at varying time commitments (~30 min, ~90 min, ~3 hours).

The full curated list is available on the [Readings](readings.md) page; the full exercise menu is available on the [Exercises](exercises.md) page.

## Recommended Setup

**For Stages 1 and 2** (Workshops 1–3, weeks 1–6):

- A paid [Claude Pro subscription](https://claude.ai/) — required for Projects, Artifacts, and most exercises
- A laptop you can bring to CHDR
- A small collection of texts or images relevant to your discipline (a syllabus, a paper, a teaching corpus, a digitized image set) to upload to your first Project

**For Stage 3** (Workshops 4–5, weeks 7–10):

- A free [GitHub account](https://github.com/) (use your `.edu` email for [GitHub Education](https://education.github.com/) benefits)
- Claude Code Web access (included with Pro subscription)

**For Stage 4** (Workshop 6, weeks 11–12):

- Optional: install [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) and [Ollama](https://ollama.com/) before the session if you want to follow along on your own machine. The session itself is demo-driven.

## Weekly Modules

The grid above links to each module. Workshop weeks are colored; async weeks are bone.

## Acknowledgements

This material is based upon work supported by the **National Endowment for the Humanities**. Any views, findings, conclusions, or recommendations expressed in this material do not necessarily reflect those of the NEH.

The series synthesizes materials from prior work by Dr. Salter and collaborators, including ENG 6806 *Humanities in the Age of AI*, ENG 6819 *Critical Making in Digital Humanities*, the *Distant Coding for the Digital Humanities* MLA workshop (with Lai-Tze Fan), the UMKC *Distant Coding* intensive, and *DHSI 2025: DH Programming Pedagogy in the Age of AI* (with John Murray). Companion text: Emily K. Johnson and Anastasia Salter, [*Critical Making in the Age of AI*](https://github.com/amsucf/CritMakingAgeOfAI) (open access).
