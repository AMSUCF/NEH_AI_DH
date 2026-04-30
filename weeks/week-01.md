---
week: 1
title: "Workshop 1: Introducing AI for DH Pedagogy"
kind: workshop
theme: "ELIZA, LLMs, the ChatGPT moment, the agentic horizon"
starts: 2026-05-11
summary: |
  In this introduction, we will try to pin down the nebulous term "AI" by looking at historical precedents and the component parts, including Large-Language Models. We will survey the space of current commercial AI, with what are often referred to as "frontier" or "foundation" models, and begin our work with Claude by exploring the interface and settings and completing some introductory exercises.
workshop:
  title: "Workshop 1: Introducing AI for DH Pedagogy"
  date: 2026-05-13
  time: "10 AM - noon"
  location: CHDR
---

By the end of the session, every participant will have a working Claude account configured to their preferences and have built a small ELIZA-style chatbot together as a Claude Artifact.

<div class="workshop-callout" markdown="1">
**NEH Workshop 1 — Tuesday, May 13, 10 AM – noon, CHDR**

Streamed and recorded. Open to UCF faculty, graduate students, and the larger arts and humanities community.

[Open the slide deck →]({{ '/slides/web/w01/' | relative_url }}){:.btn}
</div>

## What to Bring

- A laptop with a paid [Claude Pro subscription](https://claude.ai/) already set up (or be ready to subscribe at the start of the session — about $20/month, $60 for the three-month series).
- A document, conversation, or short piece of writing you'd be willing to use as a first prompt — your CV, a syllabus, a paper draft, a teaching reflection.
- Curiosity about what the chatbot you've already used (UCF Copilot, ChatGPT, Gemini) has been doing for you — and where it stops.

## Pre-Workshop Reading

Light prep before Tuesday so we can go deeper together:

- Berry, David M. ["The Limits of Computation: Joseph Weizenbaum and the ELIZA Chatbot."](https://ojs.weizenbaum-institut.de/index.php/wjds/article/view/106) *Weizenbaum Journal of the Digital Society* 3.3 (2023). (~25 min) The history piece we open the session with.
- Mollick, Ethan. ["A Guide to Which AI to Use in the Agentic Era."](https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the) *One Useful Thing*, February 18, 2026. (~15 min) The argument that choosing AI tools now means thinking in three layers — model, app, and harness — rather than just "which model is best."
- Mollick, Ethan. ["Assigning AI: Seven Ways of Using AI in Class."](https://www.oneusefulthing.org/p/assigning-ai-seven-ways-of-using) *One Useful Thing.* (~10 min) The most useful 10-minute read in the series for new adopters.

Optional, if you want to be a step ahead:

- Bender & Hanna, *The AI Con*, Chapter 1.
- Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*, Part I.

## Session Outline (120 minutes)

The workshop is built in four acts. Slide deck linked above; this outline maps the flow.

1. **ELIZA and the ELIZA effect.** Weizenbaum's 1966 chatbot, the secretary who asked him to leave the room, the two roads from MIT (Weizenbaum's lifelong critique vs. Minsky's AI Lab and Pentagon funding). We try the [masswerk.at web ELIZA](https://www.masswerk.at/eliza/) live and notice what our brains do.
2. **AI, LLMs, and how they actually work.** AI as a field, ML as a subfield, deep learning as a method, LLMs as a particular use of deep-learning transformers. Tokens (try [the OpenAI Tokenizer](https://platform.openai.com/tokenizer)), pretraining vs. inference, RLHF and reasoning layers, the Opus / Sonnet / Haiku family.
3. **The ChatGPT moment.** What already existed before November 30, 2022 — the GPT-3 API (June 2020), GitHub Copilot (June 2021). What the chatbot interface added: access. Why "the chatbot was the wrapping" is the most useful sentence to have in your back pocket.
4. **The current landscape and the agentic horizon.** A short survey of what people mean by "frontier" and "foundation" models — Claude (Anthropic), GPT-5 (OpenAI), Gemini (Google), Llama (Meta open weights). Where the conversation is shifting now: from *did the chatbot write this?* to *did the agent do the work?* Reading anchor: the Chronicle on agentic AI in higher ed.

The hands-on portion runs through the second half:

5. **Chatbot tour: five conversations.** Same prompt, five tools, in this order:
   1. **[Google Gemini](https://gemini.google.com/)** — free, fast, integrated with Google's ecosystem; the model many of our students already use.
   2. **[DeepSeek](https://chat.deepseek.com/)** running locally through **[Ollama](https://ollama.com/)** — an open-weights model on a personal machine, no API call, no data leaving the room. The "what does *local* feel like" demo.
   3. **[ChatGPT](https://chat.openai.com/)** — the chatbot that defined the genre, OpenAI's flagship.
   4. **[UCF Copilot](https://cdl.ucf.edu/faculty-multimedia-center-ai-tools/)** — the institutional option most of you already have. Microsoft's wrapper around an OpenAI model, with UCF's data-privacy framing on top. **This is the only tool UCF currently supports or allows for use with restricted data.**
   5. **[Claude](https://claude.ai/)** — Anthropic's flagship; the tool we use for the rest of the series.
   We will be moving back and forth between these throughout the workshop while prioritizing Claude, to build an understanding of the different tools available.
6. **Why Claude / why Anthropic.**
   - **Tool surface.** Projects + Artifacts + Code Web + CLI is currently the broadest set of *non-coder-accessible* tools across any provider. The conceptual framework transfers, but right now the build path is best on Claude.
   - **Safety + interpretability research culture.** Anthropic publishes more on alignment and model behavior than its peers; for a humanities audience, that publication record is part of what we're choosing.
   - The series is designed so the framework transfers if you choose a different tool — and I'll point at where it would.
7. **Setting up Claude.** Subscription confirmation. Settings tour (model selection, conversation history, custom instructions, voice mode if available, Artifacts toggle). Style preferences. Why these choices matter for the rest of the series.
8. **Build our own ELIZA in a Claude Artifact (group exercise).** Prompt Claude together to construct a Rogerian-style chatbot Artifact in the spirit of Weizenbaum's 1966 original — but with stylistic latitude. Try it. Compare to the masswerk ELIZA. Observe where the ELIZA effect kicks in, sixty years on.

## Core Exercise

**Build our own ELIZA — together, in Claude Artifacts.** This is the workshop's closing exercise and the asynchronous equivalent for those who cannot attend.

1. Open [Claude](https://claude.ai/) and start a new chat.
2. Prompt: *"Build a Claude Artifact: a chatbot **in the spirit of** Weizenbaum's 1966 ELIZA — pattern-match the user's input and reflect it back as questions. Style and tone are yours: a snarky librarian, a doom-prophet, a noir detective, a Rogerian therapist. Don't pretend to know more than the pattern."*
3. Open the Artifact in the side panel. Talk to it the way you talked to the masswerk ELIZA.
4. **Compare.** What does Claude do that pattern-matching can't? What does it do that pattern-matching *also* did? Where does the ELIZA effect kick in this time?
5. Save the Artifact URL — bring it to the W2 async discussion.

## A Frontier-Model Quick Reference

A pocket survey of the major commercial "frontier" or "foundation" models as of Spring 2026. The names move fast; the players are roughly stable.

| Maker | Family | Used in this series |
|---|---|---|
| Anthropic | Claude (Opus, Sonnet, Haiku) | All workshops |
| OpenAI | GPT (5, 4o), Images | **W1 chatbot tour** (ChatGPT); W6 multimodal (OpenAI Images) |
| Google | Gemini (Pro, Flash, Nano Banana) | **W1 chatbot tour** (Gemini); W6 multimodal (Nano Banana) |
| DeepSeek (open weights) | DeepSeek V3 / R1 | **W1 chatbot tour** (local via Ollama); W11 local-models discussion |
| Microsoft | Copilot (wraps OpenAI) | **W1 chatbot tour** (UCF Copilot) |
| Meta | Llama (open weights) | W11 local-models discussion |
| xAI / Mistral / others | Grok, Mistral | Referenced |

We use Claude across the series for one practical reason: it is the model whose Projects, Artifacts, and Code Web tools currently make it easiest for non-coders to build something they can share. The conceptual framework transfers across providers — and W1's chatbot tour is the moment we make that transfer-ability literal.

## Pedagogical Note

We do not begin with awe and we do not begin with despair. We begin with sobriety. The students sitting in our courses this fall did not ask for this technology and many of them are anxious about it. The most useful thing we can do as instructors is to know where these systems came from, what an LLM actually is, what reasoning and human-feedback layers add on top, and refuse to gesture vaguely. After this session you should be able to explain to a colleague: *here is the ELIZA effect, here is what an LLM does, here is what changed on November 30, 2022, and here is what "agentic" means now.*

## Cross-references

- Source materials: [HumanitiesAI/weekone](https://anastasiasalter.net/HumanitiesAI/weekone.html) (ELIZA exercise + Three Conversations), [HumanitiesAI/weektwo](https://anastasiasalter.net/HumanitiesAI/weektwo.html) (interfaces + Chamberlain).
- Companion text: Johnson & Salter, *[Critical Making in the Age of AI](https://www.fulcrum.org/concern/monographs/zc77ss95p)* (open access).
