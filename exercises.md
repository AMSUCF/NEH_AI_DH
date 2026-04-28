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

### Workshop 1 (May 13) — Three Conversations

<span class="tag tag-light">Light</span> **Compare a chatbot to a harnessed Claude.** Take one prompt from your own teaching or research and run it three ways: (1) the historical [ELIZA](https://www.masswerk.at/eliza/) implementation; (2) [UCF's Copilot](https://cdl.ucf.edu/faculty-multimedia-center-ai-tools/) (a standard chatbot); (3) Claude Sonnet inside a fresh **Claude Project** with one PDF or DOCX uploaded. Note where context, persistence, and tool use change the answer.

*Source: adapted from `HumanitiesAI/weekone.md` (ELIZA exercise).*

### Week 2 (async) — LLM fundamentals deep-dive

- <span class="tag tag-light">Light</span> **Iterate a poem in Claude.** Pick a form (haiku, sonnet, ghazal). Iterate ten times in Claude Sonnet, publish the final as a Claude Artifact. Reflect on how the interface shapes the writing. *Source: `HumanitiesAI/weektwo.md`.*
- <span class="tag tag-standard">Standard</span> **Project for a syllabus review.** Upload your current course's syllabus to a Project. Ask Claude to identify outdated sources, flag accessibility issues, and suggest two AI-aware revisions. Save the resulting recommendations as a markdown doc.
- <span class="tag tag-deep">Deep</span> **Three-models comparison.** Run the same teaching question through Claude Opus, Claude Sonnet, and Claude Haiku within one Project. Document what shifts: depth, hedging, hallucination rate, time. Write a one-page "model selection" memo for yourself.

### Workshop 2 (May 27) — Distant Reading with Projects + Artifacts

<span class="tag tag-standard">Standard</span> **Build a small corpus, read it across.** Bring three to five short texts in your discipline (chapters, articles, primary sources). Upload them to a Project, and prompt Claude through a sequence of distant-reading moves: stopword filter → bag-of-words → key phrases → character or theme network → comparative read. End with an Artifact that summarizes the patterns visually.

*Source: `HumanitiesAI/weekfour.md` and `DistantCodingUMKC` Example 2.*

### Week 4 (async) — Distant reading menu

- <span class="tag tag-light">Light</span> **One Project Gutenberg book.** Pick a single text, run the basic distant-reading prompts in a Project, generate a word cloud and character network. *Source: `HumanitiesAI/weekfour.md`.*
- <span class="tag tag-standard">Standard</span> **Compare Voyant to Projects.** Upload the same text to [Voyant Tools](https://voyant-tools.org/) and to a Claude Project. Run equivalent analyses and document what each surfaces, misses, and misreports.
- <span class="tag tag-deep">Deep</span> **Preview Code Web for distant reading.** Connect Claude Code Web to a small GitHub repo of texts. Ask it to write a Python preprocessing script and a JSON output. Don't worry about understanding the code — focus on what the workflow makes visible. *Source: `HumanitiesAI/weekfourteen.md`.*

---

## Stage 2 — Visual (Weeks 5–6)

### Workshop 3 (June 10) — Visual analysis with Artifacts

<span class="tag tag-standard">Standard</span> **Image-to-text translation set.** Bring five to ten images (archival, public-domain, your own teaching set, or a personal corpus). Upload to Claude. Generate alt-text for each, build a metadata table, and produce a comparative description. Publish the metadata table as an Artifact you can share with students.

*Source: `HumanitiesAI/weeksix.md` and `DistantCodingUMKC` Example 3.*

### Week 6 (async) — Visual AI in the wild

- <span class="tag tag-light">Light</span> **AI-detection scavenger hunt.** Pick a community you spend time in (a hobby forum, a subject area on Pinterest, an Instagram subculture). Find three images you suspect are AI-generated. Run them through Claude Sonnet for analysis. Reflect on what cues helped you spot (or miss) them. *Source: `HumanitiesAI/weekeight.md`.*
- <span class="tag tag-standard">Standard</span> **Generate, then critique.** Use Claude (or Adobe Firefly, Midjourney, Gemini) to generate three images in your domain. Document the iteration. Critique the results through one of this stage's readings — Demsky, Jebb, or Crawford & Paglen. *Source: `HumanitiesAI/weekfive.md`.*
- <span class="tag tag-deep">Deep</span> **Build a small visual archive Artifact.** Take a public-domain collection (Library of Congress, Internet Archive). Upload 15+ images to a Project. Generate accessible alt-text, build a thematic visualization, publish as an Artifact gallery.

---

## Stage 3 — Code Web (Weeks 7–10)

### Workshop 4 (June 24) — From CV to ePortfolio

<span class="tag tag-standard">Standard</span> **Build and deploy a one-page site.** Bring a CV, a syllabus, or a project description in `.docx` or `.pdf`. Open Claude Code Web, connect a fresh GitHub repo, prompt Claude to design and build a site appropriate to your field. Deploy to GitHub Pages.

*Source: `DistantCodingUMKC` Example 1, augmented by `HumanitiesAI/weekeleven.md`.*

### Week 8 (async) — Rebuild a handout

- <span class="tag tag-light">Light</span> **Improve last week's site.** Iterate twice on the W7 ePortfolio: one accessibility pass (alt-text, contrast, heading structure), one content pass.
- <span class="tag tag-standard">Standard</span> **Static handout → interactive page.** Take a paper handout you currently give students. Use Claude Code Web to convert it into a one-page interactive site (a clickable timeline, a quiz, a structured glossary).
- <span class="tag tag-deep">Deep</span> **Recommender or Buzzfeed-style tool.** Build a JSON dataset relevant to your discipline (100 books, 50 films, 30 archives) plus a minimal interactive front end. *Source: `HumanitiesAI/weeknine.md`.*

### Workshop 5 (July 8) — Playful, Accessible, Creative Code + AI Policy

<span class="tag tag-standard">Standard</span> **Build a playful teaching tool *and* draft a course AI policy.** Two halves:
- *Build* — a small interactive tool: a timeline, a recommender, a quiz, a generator, a memorial. Prioritize delight over scale.
- *Draft* — a one-page course AI policy that addresses copyright, attribution, accessibility, and labor. Frame it through Universal Design for Learning.

*Source: `HumanitiesAI/weeknine.md` + `HumanitiesAI/weektwelve.md` + ENG 6813 [Week 9](../InterdisciplinaryTeaching-main/InterdisciplinaryTeaching-main/weeks/week-09.md) prompt.*

### Week 10 (async) — UDL and AI policy

- <span class="tag tag-light">Light</span> **Policy A/B.** Take an existing AI policy from a colleague's syllabus. Use Claude in a Project to identify three UDL-aligned revisions. Document them.
- <span class="tag tag-standard">Standard</span> **Accessibility audit.** Run the W7 site (or any class artifact) through an accessibility checker. Use Claude Code Web to fix the top three issues.
- <span class="tag tag-deep">Deep</span> **Full syllabus integration.** Revise one full syllabus to integrate AI policy, signature assignment, and at least one AI-aware exercise. (ENG 6813 students: this maps to your Course Syllabus deliverable due July 19.)

---

## Stage 4 — Agentic Futures (Weeks 11–12)

### Workshop 6 (July 22) — Cowork + Claude CLI tour

<span class="tag tag-light">Light</span> **Watch the demo, write a CLAUDE.md.** This session is mostly demo. Your hands-on portion: in a text editor, draft a `CLAUDE.md` that describes your research domain, your typical workflows, and your preferences. Don't install anything yet — just write the document.

*Source: `DistantCodingUMKC` Day 2 + `dhsi.md` context-engineering framing.*

### Week 12 (async) — Sustaining and sharing

- <span class="tag tag-light">Light</span> **Final reflection (500 words).** What did you build, what surprised you, what will you carry into your fall classroom? *Source pattern: `HumanitiesAI/finalreflection.md`.*
- <span class="tag tag-standard">Standard</span> **Share-back to Humanities Commons or a public repo.** Take one artifact from the series — a syllabus revision, a teaching tool, a corpus, a policy — and post it to [Humanities Commons](https://hcommons.org/) or a public GitHub repo with a README that another teacher could pick up.
- <span class="tag tag-deep">Deep</span> **Try one CLI or Cowork session on your own.** Install [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) and run one full Brainstorm → Spec → Plan → Implementation cycle on a small DH project. Document the experience.

---

## Bring-along checklist

For each in-person workshop, bring:

| Workshop | What to bring |
|----------|----------------|
| W1 (May 13) | A laptop. A syllabus or one paper to upload. |
| W2 (May 27) | A small corpus (3–5 texts) in your discipline. |
| W3 (June 10) | An image set (5–10 images you have rights to). |
| W4 (June 24) | A CV or syllabus in `.docx`. A free GitHub account, ready. |
| W5 (July 8) | A draft AI policy (even one paragraph). The W4 site URL. |
| W6 (July 22) | A working laptop with admin access if you want to follow the optional CLI install. |
