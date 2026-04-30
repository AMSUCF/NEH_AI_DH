---
week: 9
title: "Workshop 5: Playful Approaches and Creative Code"
kind: workshop
theme: "Course games, planning mode, and AI policy"
starts: 2026-07-06
summary: |
  Now that we've built more confidence with Claude Code Web, we'll engage with more of its potential for playful and experimental pedagogy: in this week's workshop, we will build simple games based on concepts from your courses, and use planning mode to convey complex intention and override basic design choices. We will also think through what this type of agentic way of working means for AI policies and pedagogy.
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

## Pre-Workshop Reading

- Noble, Safiya Umoja, ["Algorithms Aren't Neutral: Safiya Noble on AI, Bias, and Building Public-Interest Technology."](https://calearninglab.org/myrobotteacher/mrt6/) *My Robot Teacher* podcast. (~30 min listen or transcript.) Required.
- Costanza-Chock, Sasha. *[Design Justice](https://design-justice.pubpub.org/),* Introduction. (~25 min) Open access.
- MLA Executive Council. ["Educational Technologies and AI Agents."](https://news.mla.hcommons.org/2026/01/30/educational-technologies-and-ai-agents/) *MLA News*, January 30, 2026. (~10 min) The most direct disciplinary statement on AI policy in humanities classrooms.

Optional:

- Sample, Mark. ["Procedural Rhetoric."](https://www.electronicbookreview.com/essay/procedural-rhetoric/) On games as arguments — useful frame for the build half of the session.
- Noble, *Algorithms of Oppression*, Chapter 1. ([UCF library ebook](https://go.openathens.net/redirector/ucf.edu?url=https%3A%2F%2Fdoi.org%2F10.2307%2Fj.ctt1pwt9w5))

## Session Outline (120 minutes)

1. **Why playful, why games.** Refik Anadol does it. Mark Sample does it. Allison Parrish does it. Play makes the labor of iteration visible and survivable. Games are arguments — and humanities-scale games (Twine, Bitsy, single-page browser games) are inside reach for a non-coder with Claude Code Web.
2. **Planning mode, the workshop's central technical move.** We don't just prompt and watch. Before Claude builds anything, we ask it to *plan*: "Enter plan mode. Do not exit plan mode until I confirm the plan is ready. Ask clarifying questions until you understand what I want." This single move is the difference between a fast wrong build and a slower right one. We practice it together.
3. **Live build: a course-concept game.** I take a single concept from a course I teach, and we build a small browser game around it together — using planning mode to surface the design questions before any code is written. Could be a Bitsy-style room-based piece, a single-page choice game, a quiz with explanatory feedback, or a memorization tool with a twist.
4. **Hands-on: build your tool.** Each participant builds a small interactive tool with planning mode on the topic they brought:
   - A clickable timeline for a course unit
   - A recommender that takes inputs and returns a curated suggestion
   - A quiz or knowledge-check tool with results that *explain* rather than grade
   - A single-page choice-driven game (a Twine-style structure rendered in HTML/CSS/JS)
   - A generator (a Markov-chain mash-up of public-domain text, a centosizer for poetry, a found-poetry tool)
5. **AI policy, after agentic.** Pivot to the syllabus question. Now that you've spent two workshops *being* the agent, what does that mean for the AI policy in your course? Working in pairs, draft (or revise) a one-page course AI policy that addresses:
   - **Copyright and attribution.** What gets cited, what gets attributed, what gets refused.
   - **Accessibility.** AI as a tool *for* accessibility — alt-text, captioning, plain-language translation — not just a problem.
   - **Equity of access.** Who pays for Pro? Are alternatives provided?
   - **Labor.** Whose labor is being replaced or extended?
   - **UDL.** Multiple means of engagement, representation, action/expression.
   - **Agentic specifically.** What changes in the policy when "use AI" can mean "let an agent do the work"? *This is the new question this week.*
6. **Discussion.** Read each other's policies. What surprised you? What would your colleagues push back on?

## Core Exercise

Two halves, both required:

**Part A — Build a small game or playful tool with planning mode.** Use Claude Code Web. Deploy via GitHub Pages. Prioritize delight, weirdness, and clarity over scale — small is good. The opening prompt structure:

> *"Enter plan mode. Do not exit plan mode until I confirm the plan is ready. I want to build [describe the tool: a quiz / a Bitsy-style room game / a recommender / a generator] about [the course concept you brought]. The audience is [students in this course / a public-facing audience / a colleague]. The constraint is HTML / CSS / JS only, deployed on GitHub Pages, no build step. Ask me clarifying questions until you understand what I want."*

Iterate the plan with Claude before letting it build. Notice what questions it asks; notice what it gets wrong about your discipline that you have to override.

**Part B — Draft a course AI policy.** Write a one-page AI policy for a course you teach (or plan to teach). Address copyright, attribution, accessibility, equity of access, labor, UDL, and the new agentic question. Frame the policy as an invitation, not a prohibition — what does ethical use *enable*, not just what does it forbid?

## Pedagogical Note

The most common mistake in AI policies is treating them as a fence. The students who most need clear AI guidance are the ones least likely to ask — the ones who already feel anxious about what counts as cheating. A policy framed as *invitation* (here is when AI use is welcome, here is how to attribute it, here is what to do if you are unsure) reaches those students. A policy framed as *prohibition* drives them underground.

The agentic shift specifically: a student saying "Claude wrote this paper" is one kind of question. A student saying "I told Claude what I wanted, planned it together, reviewed three drafts, overrode two design decisions, and committed each version" is a different kind of work — closer to what we're asking them to do anyway. The policy has to be able to tell those apart.

## Cross-references

- Source materials: [HumanitiesAI/weeknine](https://anastasiasalter.net/HumanitiesAI/weeknine.html) (recommender stages), [HumanitiesAI/weektwelve](https://anastasiasalter.net/HumanitiesAI/weektwelve.html) (planning mode + agentic Code Web), [CriticalMaking2026/exercises/six_game](https://anastasiasalter.net/CriticalMaking2026/exercises/six_game.html) (Bitsy game design), [CriticalMaking2026/exercises/nine_generation](https://anastasiasalter.net/CriticalMaking2026/exercises/nine_generation.html), [CriticalMaking2026/exercises/eleven_narrative](https://anastasiasalter.net/CriticalMaking2026/exercises/eleven_narrative.html).
