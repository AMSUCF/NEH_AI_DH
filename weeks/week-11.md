---
week: 11
title: "Workshop 6: Agentic Futures, Curricular Sustainability"
kind: workshop
theme: "Local agentic powertools (demos you can follow along with) and disciplinary consequences"
starts: 2026-07-20
summary: |
  While Claude Code Web is one of the most powerful agentic tools available through the web, the real agentic powertools are usually run on your own machine. In this session, we'll demo what these types of tools are capable of, and discuss the consequences of these ways of working for our disciplines and our students future careers. Currently, UCF does not allow faculty to install local agentic tools on university computers without considerable permissions considerations, so this week's workshop will primarily demo ways of working you might want to explore further on your own machine — or try later on our new CHDR Spark.
workshop:
  title: "Workshop 6: Agentic Futures, Curricular Sustainability"
  date: 2026-07-22
  time: "10 AM - noon"
  location: CHDR
---

We're going to take a tour through the Claude CLI, MCP, Hugging Face, and Ollama. Feel free to follow along if you have your own device — and remember you can also try some of these tools later on our new CHDR Spark.

<div class="workshop-callout" markdown="1">
**NEH Workshop 6 — Wednesday, July 22, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community. This is the last in-person session of the series, so we will reserve time for closing Q&A.

[Open the slide deck →]({{ '/slides/web/w11/' | relative_url }}){:.btn}
</div>

## A Note on Installation This Week

This is a demo-driven session because, for most of you, *installation isn't the move right now*. Specifically:

- **UCF policy.** UCF does not currently allow faculty to install local agentic tools (Claude CLI, Ollama, MCP servers connected to local data) on university-owned computers without significant permissions review. The university's central IT and the College of Arts & Humanities are working through what an institutional path looks like; for now, the safer assumption is that local installation lives on your *personal* machine, on your own time. The current institutional landscape is at [UCF AI Resources](https://aiforall.ucf.edu/resources/).
- **Your students likely will install these.** Especially anyone going into industry roles, library/archive work, or research-adjacent careers. Knowing what these tools *do* — even without running them — is part of what they need from us.
- **The pedagogical question is therefore: what do you teach people to recognize, even if you don't teach them to install?**

The answer this session offers: the *vocabulary* (agentic, MCP, skills, subagents, planning mode), the *demos* (Claude CLI, MCP servers, local models, Ollama), and a *place to try it all without installing anything on your own machine*: the new CHDR Spark.

## What to Bring

- A laptop. If it is a personal machine and you want to follow along, install the [Claude Code CLI](https://code.claude.com/docs/en/quickstart) — or at least Claude Code Desktop — and [Ollama](https://ollama.com/download) beforehand, and make a [Hugging Face account](https://huggingface.co/join) if you want to try fine-tuning or playing with models. None of this is required.
- [GitHub Desktop](https://desktop.github.com/), if you want the easiest on-ramp to the CLI: select **Repository → Open in Command Prompt** (or Terminal) and type `claude`.

## Pre-Workshop Reading

- Mollick, Ethan. ["The Twilight of the Chatbots."](https://www.oneusefulthing.org/p/the-twilight-of-the-chatbots) *One Useful Thing.* (~15 min) Why the chat window is giving way to agents — the framing we open with.
- Underwood, Ted. ["The Marionette Theater of AI."](https://tedunderwood.com/2026/02/08/the-marionette-theater-of-ai/) *The Stone and the Shell*, February 8, 2026. (~20 min) A lucid recent essay on what agentic systems are doing to scholarly work.
- Cohen, Dan. ["AI and Libraries, Archives, and Museums, Loosely Coupled."](https://newsletter.dancohen.org) *Humane Ingenuity.* (~15 min) The DH-specific framing for MCP and connected tools.
- Anthropic. ["Introduction to Model Context Protocol."](https://docs.anthropic.com/en/docs/build-with-claude/mcp) (~10 min) Skim — you do not need to install anything.

Optional, for those who want the deeper picture:

- Vincent, Jesse. ["Superpowers: How I'm Using Coding Agents in October 2025."](https://blog.fsck.com/2025/10/09/superpowers/)
- Willison, Simon. *[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)* (introduction and "Subagents").

## Session Outline (120 minutes)

1. **Framing: demoing the power tools.** A tour through the Claude CLI, MCP, Hugging Face, and Ollama. Follow along if you have your own device — or try these tools later on our new CHDR Spark.
2. **The twilight of the chatbots.** Mollick's argument that the chat window is giving way to agents — and the labor reality check that comes with it: Altman's ["jobs that aren't real work"](https://www.tomshardware.com/tech-industry/sam-altman-says-ai-could-eliminate-jobs-that-arent-real-work) and Graeber's bullshit jobs.
3. **Demo: Claude CLI.** [Installation directions](https://code.claude.com/docs/en/quickstart); the easiest way in is to select **Repository → Open in Command Prompt** (or Terminal) from GitHub Desktop and type `claude`. Overview of the commands: slash commands, the Shift+Tab modes, plugins, and skills.
4. **Installing an MCP server.** Example one: the [Hugging Face plugin](https://huggingface.co/mcp). Example two: the [Zotero MCP](https://github.com/54yyyu/zotero-mcp), so research and writing share a context.
5. **Live demo: Claude CLI running local models.** Using Superpowers, we'll describe the project, have Claude select the best local model for audio transcription, and build an interface for our transcription tool.
6. **Live demo: Ollama.** [Installation](https://ollama.com/download); then the Claude Code CLI with Ollama — a local model driving the same power tool (a less competent agent).
7. **Closing: where will this take you?** All of these tools seem to be on a trajectory of growing more powerful (and potentially more expensive) — but local models are also rising in capability. Open Q&A: this is the last in-person session of the series, so bring the questions you've been collecting.

## Take-Home Exercise

**Write a `CLAUDE.md` for your work.** The in-session time goes to the demos, but this is the artifact to draft afterward — a low-tech exercise with high pedagogical leverage. The document is a piece of *meta-pedagogy*: thinking about how an AI agent should be onboarded to your work clarifies what your work actually is.

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
