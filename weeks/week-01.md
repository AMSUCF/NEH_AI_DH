---
week: 1
title: "Workshop 1: Introducing AI for DH Pedagogy"
kind: workshop
theme: "LLMs, the web that fueled them, reasoning layers, the higher-ed crisis"
starts: 2026-05-11
workshop:
  title: "Workshop 1: Introducing AI for DH Pedagogy"
  date: 2026-05-13
  time: "10 AM - noon"
  location: CHDR
---

We open the series by stepping back. Before we touch a tool, we acknowledge the hard fact: generative AI has dropped into higher education in a way that feels existential — plagiarism panics, an AI-detector arms race, and faculty who feel cornered between adoption pressure and pedagogical conviction. This workshop is the field-clearing session: what is an LLM, where did it come from, and what is sitting on top of it. We trace the line from the web and digital culture — the decades of human writing, talking, and image-making that the open internet captured — to the digitized record that now fuels LLMs and multimodal models. Then we look at the **reasoning layers** and the **human feedback** training (RLHF and adjacent techniques) that sit on top of the base model and shape its efficacy, before we ever touch a tool.

By the end of the session, every participant will have a working Claude Project with one document uploaded and three useful prompts run against it.

<div class="workshop-callout" markdown="1">
**NEH Workshop 1 — Tuesday, May 13, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the broader NEH learning community.

[Open the slide deck →]({{ '/slides/web/w01/' | relative_url }}){:.btn}
</div>

## What to Bring

- A laptop with a paid [Claude Pro subscription](https://claude.ai/) already set up (or be ready to subscribe at the start of the session).
- One document to upload to your first Project — a syllabus you teach, a paper you wrote, a short reading you assign. Roughly one PDF or Word doc.
- Curiosity about what your version of UCF Copilot has been doing for you — and where it stops.

## Pre-Workshop Reading

Light prep before Tuesday so we can go deeper together:

- Berry, David M. ["The Limits of Computation: Joseph Weizenbaum and the ELIZA Chatbot."](https://ojs.weizenbaum-institut.de/index.php/wjds/article/view/106) *Weizenbaum Journal of the Digital Society* 3.3 (2023). (~25 min)
- Kirschenbaum, Matthew. ["Prepare for the Textpocalypse."](https://www.theatlantic.com/technology/archive/2023/03/ai-chatgpt-writing-language-models/673318/) *The Atlantic*, March 8, 2023. (~15 min)
- Mollick, Ethan. ["Assigning AI: Seven Ways of Using AI in Class."](https://www.oneusefulthing.org/p/assigning-ai-seven-ways-of-using) *One Useful Thing.* (~10 min)

Optional, if you want to be a step ahead:

- Bender & Hanna, *The AI Con*, Chapter 1.
- Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*, Part I.

## Session Outline (120 minutes)

1. **The existential crisis framing (~20 min).** Plagiarism, detectors, AI policy whiplash. Why the discourse feels stuck. Where humanities departments are landing — and where they are not. Reading anchor: Kirschenbaum.
2. **Where the LLM came from (~25 min).** A short history: the web, digital culture, and networked communication as the conditions that produced a digitized record of human expression at unprecedented scale. That record — text, images, code, conversation — is the training data. We name what got swept up, what was excluded, and whose labor and language is overrepresented or underrepresented. Reading anchor: Berry on ELIZA as ancestor.
3. **What an LLM actually is, and what sits on top (~25 min).** Parameters, training, inference, in plain language. Then **reasoning layers** and **human feedback** (RLHF and adjacent training) — how the base model becomes more useful, more steerable, and more aligned through layers added after pretraining. The Opus / Sonnet / Haiku family as a concrete example. Why one might pick Claude versus ChatGPT versus Gemini for different work.
4. **From chatbot to Project (~20 min).** UCF's [Microsoft Copilot](https://cdl.ucf.edu/faculty-multimedia-center-ai-tools/) is a capable single-shot chatbot — useful and fast, but it forgets you between sessions. A **Claude Project** wraps the same kind of model in persistent context and file handling. Later weeks will introduce more tightly *harnessed* tools (Artifacts, Code Web, CLI), but Projects is the gentle entry. Live demo: same prompt to UCF Copilot vs. Claude with a Project.
5. **Hands-on Projects setup (~25 min).** Everyone creates a Project, uploads the document they brought, and runs three prompts:
   1. *Summarize this document for someone in my discipline.*
   2. *What does this document assume the reader already knows?*
   3. *Suggest two ways I could revise this for an undergraduate audience.*
6. **Discussion (~20 min).** What felt different from Copilot? What pedagogical openings does this open or close? What worried you?

## Core Exercise

**Three Conversations.** This week's exercise sits at the center of the workshop and is also the asynchronous equivalent for those who cannot attend.

Take one prompt — something you would actually use in your teaching or research — and run it three ways:

1. The historical [ELIZA implementation](https://www.masswerk.at/eliza/) (yes, really). Spend at least ten minutes; notice where it breaks.
2. [UCF Copilot](https://cdl.ucf.edu/faculty-multimedia-center-ai-tools/) (or any standard chatbot you have used). Run the same prompt cold.
3. A new **Claude Project** with one document uploaded as context. Run the same prompt with that context attached.

Document what differs. Save screenshots.

## Pedagogical Note

We do not begin with awe and we do not begin with despair. We begin with sobriety. The students sitting in our courses this fall did not ask for this technology and many of them are anxious about it. The most useful thing we can do as instructors is to know where these systems came from, what an LLM actually is, what reasoning and human-feedback layers add on top, and refuse to gesture vaguely. After this session you should be able to explain to a colleague: *here is the digitized record this thing was trained on, here is what a chatbot does, here is what persistent context (a Project) adds, and here is why I am choosing one tool over another for this assignment.*

## Cross-references

- Source materials: `HumanitiesAI/weekone.md` (ELIZA exercise); `HumanitiesAI/weektwo.md` (interfaces and Kirschenbaum); `dhsi.md` (harness framing).
