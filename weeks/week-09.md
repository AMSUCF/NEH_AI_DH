---
week: 9
title: "Workshop 5: Playful Approaches and Creative Code"
kind: workshop
theme: "Course games, planning mode, and AI policy"
starts: 2026-07-06
summary: |
  Now that we've built more confidence with Claude Code, we'll move to Claude Code Desktop with the Superpowers plugin and engage with more of its potential for playful and experimental pedagogy. We'll open with demos of tools for research and pedagogy — Sarah Norris on finding data, and Mel Stanfill on building research scrapers with AI assistance. Then, in the build half of the workshop, we will make simple games and tools based on concepts from your courses, and use planning mode to convey complex intention and override basic design choices. We'll manage our projects with GitHub Desktop and deploy to Pages. We will also think through what this type of agentic way of working means for AI policies and pedagogy.
workshop:
  title: "Workshop 5: Playful Approaches and Creative Code"
  date: 2026-07-08
  time: "10 AM - noon"
  location: CHDR
---

<div class="workshop-callout" markdown="1">
**NEH Workshop 5 — Wednesday, July 8, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community.

[Open the slide deck →]({{ '/slides/web/w09/' | relative_url }}){:.btn}
</div>

## What to Bring

- Your laptop and Claude Pro subscription.
- The W7 site URL (we may iterate on it, or branch off it).
- A draft AI policy from your current syllabus, even one paragraph. If you do not have one, bring a syllabus with no AI policy and a willingness to draft.
- **A concept from your course you'd be willing to turn into a game** — a key term to learn, a decision tree to internalize, a periodization to memorize, a set of texts to compare. Anything where "play it" might teach better than "study it."
- **Ideas for more complicated tools or problems you'd love to solve** — the harder, messier things you wish you could build for your research or teaching, whether or not you think Claude Code can help. We'll use these to map where these tools genuinely reach and where they don't (yet).

## Pre-Workshop Reading

- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Noble, Safiya Umoja, ["Algorithms Aren't Neutral: Safiya Noble on AI, Bias, and Building Public-Interest Technology."](https://calearninglab.org/myrobotteacher/mrt6/) *My Robot Teacher* podcast. (~30 min listen or transcript.)
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> University of Central Florida. ["Use of Artificial Intelligence (AI) Tools"](https://infosec.ucf.edu/document/ai-guidance/) (UCF IT) and ["Agents"](https://aiforall.ucf.edu/agents/) (AI for All). (~10 min skim) UCF's institutional position on agentic AI — the frame your course policy sits inside.
- <span class="tag tag-light">Light</span> Costanza-Chock, Sasha. *[Design Justice](https://design-justice.pubpub.org/),* Introduction. (~25 min) Open access.
- <span class="tag tag-light">Light</span> MLA Executive Council. ["Educational Technologies and AI Agents."](https://news.mla.hcommons.org/2026/01/30/educational-technologies-and-ai-agents/) *MLA News*, January 30, 2026. (~10 min) A direct disciplinary statement on AI policy in humanities classrooms.

Optional:

- <span class="tag tag-standard">Standard</span> Sample, Mark. ["Procedural Rhetoric."](https://www.electronicbookreview.com/essay/procedural-rhetoric/) On games as arguments — useful frame for the build half of the session.
- <span class="tag tag-standard">Standard</span> Noble, *Algorithms of Oppression*, Chapter 1. ([UCF library ebook](https://go.openathens.net/redirector/ucf.edu?url=https%3A%2F%2Fdoi.org%2F10.2307%2Fj.ctt1pwt9w5))

## The Session

The workshop runs in three movements. **First, building tools for research and pedagogy.** Sarah Norris opens with a demo on finding data, and Mel Stanfill walks through her research scrapers — an AO3 tag crawler built iteratively with an AI coding assistant, from the first scraping prompt through debugging, co-occurrence networks, and heatmaps, with the versioned file tree as a record of the process. These are the model for what we build next: small, open, single-purpose tools.

**Then we build games and course resources.** Using Claude Code Desktop with the Superpowers plugin and planning mode, each of us makes a small, strange, course-specific artifact — a clickable timeline, a game, a tool your students would actually use, or a generator — and deploys it to GitHub Pages. We work in planning mode throughout: describing what we want, watching Claude ask clarifying questions, and overriding what it gets wrong about our disciplines before any code is written.

**Then we turn to the syllabus.** Having spent two workshops *being* the agent, we pivot to the policy question that follows from it. Working in pairs, we draft (or revise) a one-page course AI policy and read each other's, framing the policy as an invitation rather than a fence — and reckoning with what changes when "use AI" can mean "let an agent do the work." UCF's own [guidance](https://infosec.ucf.edu/document/ai-guidance/) already restricts agentic tools and treats an agent doing the coursework as misconduct; see the Pedagogical Note below.

## Core Exercise

Two halves, both required:

**Part A — Build a small game or playful tool with planning mode.** Use Claude Code Desktop with the Superpowers plugin (install it and add your customization first). Manage the project as a local repository in GitHub Desktop and deploy via GitHub Pages. Prioritize delight, weirdness, and clarity over scale — small is good. The opening prompt structure:

> *"Enter plan mode. Do not exit plan mode until I confirm the plan is ready. I want to build [describe it: a Bitsy-style room game / a playable artifact from a sample text / a tool that helps my students with a task / a generator] about [the course concept you brought]. The audience is [students in this course / a public-facing audience / a colleague]. The constraint is HTML / CSS / JS only, deployed on GitHub Pages, no build step. Ask me clarifying questions until you understand what I want."*

Iterate the plan with Claude before letting it build. Notice what questions it asks; notice what it gets wrong about your discipline that you have to override.

**Part B — Draft a course AI policy.** Write a one-page AI policy for a course you teach (or plan to teach). Address copyright, attribution, accessibility, equity of access, labor, UDL, and the new agentic question. Frame the policy as an invitation, not a prohibition — what does ethical use *enable*, not just what does it forbid?

## Pedagogical Note

The most common mistake in AI policies is treating them as a fence. The students who most need clear AI guidance are the ones least likely to ask — the ones who already feel anxious about what counts as cheating. A policy framed as *invitation* (here is when AI use is welcome, here is how to attribute it, here is what to do if you are unsure) reaches those students. A policy framed as *prohibition* drives them underground.

This is not only ours to decide. UCF IT's [AI guidance](https://infosec.ucf.edu/document/ai-guidance/) names *agentic* AI explicitly and approves agentic coding tools like Claude Code only for *unrestricted* data, prohibiting them for anything classified as restricted or highly restricted. The AI for All [guidance on agents](https://aiforall.ucf.edu/agents/) goes further, urging students, faculty, and staff to "avoid installing or using agents on UCF devices or any device that connects to UCF data." Read alongside UCF's [definition of academic misconduct](https://guides.ucf.edu/ai/academic-integrity), letting an agent *do* the coursework is squarely an honor-code problem, not a gray area. These are questions that remain unresolved, and the answers will vary by discipline and by context.

## Cross-references

- Source materials: [HumanitiesAI/weeknine](https://anastasiasalter.net/HumanitiesAI/weeknine.html) (recommender stages), [HumanitiesAI/weektwelve](https://anastasiasalter.net/HumanitiesAI/weektwelve.html) (planning mode + agentic Code Web), [CriticalMaking2026/exercises/six_game](https://anastasiasalter.net/CriticalMaking2026/exercises/six_game.html) (Bitsy game design), [CriticalMaking2026/exercises/nine_generation](https://anastasiasalter.net/CriticalMaking2026/exercises/nine_generation.html), [CriticalMaking2026/exercises/eleven_narrative](https://anastasiasalter.net/CriticalMaking2026/exercises/eleven_narrative.html).
