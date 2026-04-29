---
week: 11
title: "Workshop 6: Agentic Futures, Curricular Sustainability"
kind: workshop
theme: "Local agentic powertools (demo-only) and disciplinary consequences"
starts: 2026-07-20
summary: |
  While Claude Code Web is one of the most powerful agentic tools available through the web, the real agentic powertools are usually run on your own machine. In this session, we'll demo what these types of tools are capable of, and discuss the consequences of these ways of working for our disciplines and our students future careers. Currently, UCF does not allow faculty to install local agentic tools on university computers without considerable permissions considerations, so this week's workshop will primarily demo ways of working you mmight want to explore further on your own machine.
workshop:
  title: "Workshop 6: Agentic Futures, Curricular Sustainability"
  date: 2026-07-22
  time: "10 AM - noon"
  location: CHDR
---

The hands-on portion is a writing exercise, not an installation: drafting a `CLAUDE.md` for your own work.

<div class="workshop-callout" markdown="1">
**NEH Workshop 6 — Tuesday, July 22, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community. This is the last in-person session of the series, so we will reserve time for closing Q&A.

[Open the slide deck →]({{ '/slides/web/w11/' | relative_url }}){:.btn}
</div>

## A Note on Installation This Week

This is a demo-driven session because, for most of you, *installation isn't the move right now*. Specifically:

- **UCF policy.** UCF does not currently allow faculty to install local agentic tools (Claude CLI, Ollama, MCP servers connected to local data) on university-owned computers without significant permissions review. The university's central IT and the College of Arts & Humanities are working through what an institutional path looks like; for now, the safer assumption is that local installation lives on your *personal* machine, on your own time.
- **Your students likely will install these.** Especially anyone going into industry roles, library/archive work, or research-adjacent careers. Knowing what these tools *do* — even without running them — is part of what they need from us.
- **The pedagogical question is therefore: what do you teach people to recognize, even if you don't teach them to install?**

The answer this session offers: the *vocabulary* (agentic, MCP, skills, subagents, planning mode), the *workflow* (Brainstorm → Spec → Plan → Implementation → Review), and the *artifact you can write today without installing anything*: a `CLAUDE.md` for your own work.

## What to Bring

- A laptop. Admin access if you want to follow the optional install demos in real time on a personal machine; not required.
- The artifacts you have built across the series: your W7 ePortfolio URL, your W9 playful tool URL, your draft AI policy, your Skill from W4 if you built one. The Cowork demo will use them.
- A notebook (paper or digital) for the `CLAUDE.md` writing exercise.

## Pre-Workshop Reading

- Underwood, Ted. ["The Marionette Theater of AI."](https://tedunderwood.com/2026/02/08/the-marionette-theater-of-ai/) *The Stone and the Shell*, February 8, 2026. (~20 min) The most lucid recent essay on what agentic systems are doing to scholarly work.
- Cohen, Dan. ["AI and Libraries, Archives, and Museums, Loosely Coupled."](https://newsletter.dancohen.org) *Humane Ingenuity.* (~15 min) The DH-specific framing for MCP and connected tools.
- Anthropic. ["Introduction to Model Context Protocol."](https://docs.anthropic.com/en/docs/build-with-claude/mcp) (~10 min) Skim — you do not need to install anything.

Optional, for those who want the deeper picture:

- Vincent, Jesse. ["Superpowers: How I'm Using Coding Agents in October 2025."](https://blog.fsck.com/2025/10/09/superpowers/)
- Willison, Simon. *[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)* (introduction and "Subagents").

## Session Outline (120 minutes)

1. **The vocabulary, restated.** Agentic, tool use, planning, subagents, MCP, skills. Why "agent" is doing a lot of work in the discourse and what it actually means inside Claude.
2. **Cowork tour.** Live walkthrough of a Cowork session — Claude working alongside me in real time on a shared problem. We use one of *your* W7 or W9 artifacts as the working surface. The point is *what changes when the conversation is collaborative rather than turn-taking.*
3. **Claude CLI tour.** Claude in the terminal on my personal machine. Slash commands, `/init`, `/plan`, `CLAUDE.md` for context engineering, the Superpowers workflow (Brainstorm → Spec → Plan → Implementation → Review). I demo on a small humanities project; you watch.
4. **MCP, briefly.** What MCP is — "USB-C for AI" — and one example: connecting Claude to a Zotero library so research and writing share a context. Hugging Face MCP for archival audio (Whisper transcription) is another humanities-relevant example. Why this matters for the next academic year.
5. **The disciplinary and career conversation.** What happens to research, writing, and teaching workflows when *some* people in your department are using these tools at the CLI level and others aren't? What does this mean for graduate students entering academic and adjacent job markets in 2027–2030? Where is the institutional policy conversation right now? This is the part of the session that's pure discussion — bring the questions you've been collecting.
6. **Writing exercise: your `CLAUDE.md`.** Draft a `CLAUDE.md` document — a context file an agent could read to understand your research domain, your typical workflows, your preferences, and your boundaries. No installation required; we just write the markdown. Templates and examples on screen.
7. **Open Q&A and closing.** Last in-person session of the series. Bring whatever questions about agentic tools, your `CLAUDE.md`, or what to carry into the fall you have not had a chance to ask yet.

## Core Exercise

**Write a `CLAUDE.md` for your work.** This is a low-tech exercise with high pedagogical leverage. The document is a piece of *meta-pedagogy*: thinking about how an AI agent should be onboarded to your work clarifies what your work actually is.

Cover at minimum:

1. **Who you are and what you do.** One paragraph.
2. **Your domain.** Disciplines, methods, topics, key conversations.
3. **Your typical workflows.** What you tend to ask AI to help with; what you do *not* want it to do.
4. **Your preferences.** Citation style, voice, audience defaults.
5. **Your boundaries.** What you will not delegate. What requires your hand.

Save the file. Whether or not you ever install the CLI, the document is a deliverable in its own right — useful as a teaching artifact, a research statement, and a self-clarifying exercise. If you do later install the CLI on a personal machine, this file goes at the root of your project directory and Claude reads it on every session.

*Source: [DHSI 2026 — dhsi-2026-course-packet](https://anastasiasalter.net/DHSI_DH_AI_2026/dhsi-2026-course-packet.html) (context engineering); [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (skills + agentic workflows).*

## Pedagogical Note

The agentic horizon is real but it is also still half-hype. Take what is useful — the discipline of writing context, the visibility of structured workflows like Superpowers, the genuine power of MCP for research integration — and stay skeptical of the rest. The most important sentence in any conversation about agentic AI is *what would I have to give up to use this?* The answer is rarely zero.

For our students entering the workforce: the question isn't whether they'll encounter these tools — they will. The question is whether they'll have any framework for thinking critically about which ones to use, when, and what to refuse. That framework comes from the humanities. *Especially* the humanities.

## Cross-references

- Source materials: [DHSI 2026 — dhsi-2026-course-packet](https://anastasiasalter.net/DHSI_DH_AI_2026/dhsi-2026-course-packet.html) (Sessions 3–6: CLI, Ollama, MCP, Superpowers); [HumanitiesAI/weekthirteen](https://anastasiasalter.net/HumanitiesAI/weekthirteen.html) (local models), [HumanitiesAI/weekfifteen](https://anastasiasalter.net/HumanitiesAI/weekfifteen.html) (skills, subagents); [CriticalMaking2026/exercises/thirteen_tools](https://anastasiasalter.net/CriticalMaking2026/exercises/thirteen_tools.html) (Claude Code for tool-building).
