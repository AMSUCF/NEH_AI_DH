---
week: 6
title: "Cowork and Multimodal AI (Asynchronous)"
kind: async
theme: "Scheduled Cowork tasks, local models via Hugging Face, caption correction, and the image-to-image loop"
starts: 2026-06-15
summary: |
  This week extends Workshop 3's visual-analysis work into automated, local, and accessibility-focused territory. Try scheduling an agentic task in Claude Cowork, set up the Hugging Face connector and run a local model for alt-text, correct auto-captions on a recorded talk, close the loop from image *analysis* to image *generation* across several tools, draft a slide deck with Claude Design, or build a voice interface as an AI Artifact.
---

There is no in-person meeting.

<div class="async-callout" markdown="1">
**Asynchronous expectations.** Read the **Required** items in the menu below and complete **at least one** of the six exercises. **Post the result of that exercise back in the cohort Discord** — a screenshot, a spreadsheet, a folder of alt-text, a corrected caption file, a set of generated images, or a short reflection on what surprised you. The Discord post is the deliverable. Also do the small **Workshop 4 setup** at the bottom (GitHub account), because the next session depends on it.
</div>

## Where This Week Fits

Workshop 3 framed image *generation* and image *analysis* as two sides of the same coin, and ended on two threads we set aside for later: **Claude Cowork** (Claude working in a local folder with read/write access) and **local models** (running the model on your own machine instead of sending images to someone else's server). This week picks both of them up. Several of the exercises live in **Cowork**; one closes the loop back to image generation and asks the W5 question again — *every generated image is a picture of its training data* — but now with your own analyzed set as the input; and two stay in Claude proper, drafting a slide deck and building a working voice tool.

A reminder that carries over from Workshop 3: **always point Cowork at a new, empty folder** with only the materials you want it to touch — never a broad personal directory.

## Reading Menu

- <span class="tag tag-required">Required</span> <span class="tag tag-standard">Standard</span> Crawford, Kate, and Trevor Paglen. ["Excavating AI."](https://excavating.ai/) If you skipped it for W5, this is the week — it is the structural critique behind Exercise D's "what does the result tell you about the dataset" question.
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> *Washington Post.* ["This is how AI image generators see the world."](https://www.washingtonpost.com/technology/interactive/2023/ai-generated-images-bias-racism-sexism-stereotypes/) The interactive we looked at in Workshop 3 ("toys in Iraq," "a house" by country). Keep it open while you do Exercise D.
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Willison, Simon. ["Build and share AI-powered apps with Claude."](https://simonwillison.net/2025/Jun/25/ai-powered-apps-with-claude/) (~15 min) A practitioner walkthrough of Artifacts that can call Claude — the exact capability behind Exercise F.
- <span class="tag tag-required">Required</span> <span class="tag tag-light">Light</span> Willison, Simon. *[How Coding Agents Work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)*, the section **"What is an agent?"** (~10 min) A preview of the agentic vocabulary we'll formalize in Workshop 4 — and the right frame for the scheduled task in Exercise A.

Optional:

- <span class="tag tag-standard">Standard</span> Bender & Hanna, *The AI Con*, Chapter 5: Artifice or Intelligence? AI Hype in Art, Journalism, and Science. The hype-versus-substance frame for everything multimodal — recommended if you want the critical anchor.
- <span class="tag tag-light">Light</span> WebAIM. ["Captions, Transcripts, and Audio Descriptions."](https://webaim.org/techniques/captions/) (~15 min) Why caption accuracy matters and what "good enough" actually means — background for Exercise C.
- <span class="tag tag-light">Light</span> Halperin, Brett. ["Hollywood Film Workers Strike Against AI."](https://stars.library.ucf.edu/elo2024/algorithmsandimaginaries/schedule/3/) ELO 2024. The labor side of multimodal AI in commercial use.
- <span class="tag tag-light">Light</span> [Anne Marie Oliver on AI embroidery](https://lolliandgrace.com/blogs/blog/artificial-intelligence-in-the-embroidery-space) — a craft-community practitioner perspective, surprisingly transferable to discipline-specific multimodal questions.

## Exercise Menu — Pick One, Post to Discord

### A. Schedule an agentic task in Claude Cowork (~60–90 min setup, then it runs itself)

This is the agentic move we'll name formally in Workshop 4: instead of asking Claude to do one thing once, you give it a standing instruction and a schedule, and it runs on its own. **Cowork** can hold a scheduled task against a local folder.

1. **Make a dedicated folder.** Create a new, empty folder (e.g. `~/cowork-agentic-watch/`). This is the only place the task will read from and write to.
2. **Open Cowork and point it at that folder.**
3. **Write a detailed instruction — detail is the whole exercise.** A vague task ("keep me updated on AI") produces noise. Build out the *what, where, format, and when*. A worked example:

   > *"Every morning at 8 AM, search the web for new articles, papers, and tool announcements about **agentic AI applications in [your field — e.g. archival description, language pedagogy, museum interpretation]**, published in roughly the last 24 hours. For each item, capture: title, source, URL, publication date, a 2–3 sentence summary, and a relevance note tied to my work. Append new rows to `agentic-watch.xlsx` in this folder — do not overwrite existing rows, and skip anything already listed. Highlight in yellow any item that looks directly usable in my teaching. At the end of each run, write a one-line digest at the top of a `digest.md` file."*

   Notice what makes this useful: a **named output file**, an **append-don't-overwrite** rule, a **dedup** rule, an explicit **schema** for each entry, and a **relevance filter** in your voice.
4. **A more ambitious variant.** Ask Cowork to store the same data in a **web-friendly form** — `articles.json` with one object per item — and then to **build a small front-end** (a single `index.html`) to browse, filter, and search it. Heads up: **Cowork will likely suggest you use Claude Code instead** for the front-end. That suggestion is itself the lesson — note when the chat/Cowork interface hands off to a code-first tool, because that's exactly the boundary Workshop 4 is about.
5. **Let it run at least once (or trigger it manually), then read the output critically.** Did it follow the schema? Did it dedup? Are the "relevant" items actually relevant, or did it pad the list? Tighten the instruction and run again.

*Post to Discord:* a screenshot of the spreadsheet (or the front-end), plus one or two sentences on what you had to add to the instruction to make the output trustworthy.

### B. Run a local model for alt-text via the Hugging Face connector (~45–60 min)

Workshop 3 ended on the local-models question: web tools like Claude send your images to someone else's server; a **local model** keeps them on your machine. This exercise wires Claude up to **Hugging Face** so it can find and reason about an open model for the job.

1. **Add the connector.** Go to [claude.ai/settings/connectors](https://claude.ai/settings/connectors) and add **"Hugging Face"** from the gallery. (For higher rate limits, set an `HF_TOKEN` — see [hf.co/settings/mcp](https://hf.co/settings/mcp/) — or [create a free account](https://hf.co/join).)
2. **Make a new folder and select it in Cowork.** Move a handful of **test images** into it (reuse your Workshop 3 set if you like).
3. **Confirm the Hugging Face connector is turned on** for this conversation.
4. **Prompt Claude to find a local model for the task:** *"Search Hugging Face for a local (open-weights) model suited to writing alt-text / image captions for these images. Compare two or three candidates — size, license, what they're trained on — and recommend one I could run on my own machine. Then draft alt-text for each image in this folder."*
5. **Read the recommendation as a research result, not just an answer.** What did it suggest, and *why*? What's the license? How does its alt-text compare to what Claude itself produced in Workshop 3 — does the smaller, open model flatten more, hallucinate more, or handle your domain's specifics worse? This comparison *is* the local-vs-cloud trade-off made concrete.

**Set expectations:** a local, open model writing alt-text through Cowork **won't give you much detail.** Expect short, generic descriptions — "a black and white photograph of a building" rather than the situated, context-aware reading Claude produces in the chat window. That gap is the point: it shows you concretely what you trade away when you keep the images on your own machine.

*Post to Discord:* the model it recommended (with one line on the license/trade-off it surfaced) and a side-by-side of one image's alt-text from the local model vs. from Claude.

### C. Correct auto-captions with Claude (~45–60 min)

Auto-captions on recorded talks are reliably wrong in the exact places that matter: names, jargon, your discipline's terms-of-art. Claude can clean them up — with an important limitation to understand.

1. **Gather a video and its captions.** A Zoom recording of one of your lectures plus its auto-generated `.vtt`/`.srt` caption file is ideal. Put **both** in a new project/Cowork folder.
2. **Prompt with context and a clear instruction:** *"This is a recording of [course / topic / who's speaking]. The caption file was auto-generated and has errors, especially in names and specialized terms. Use the video to make determinations about likely errors in the captions, fix them, and return a corrected caption file with the original timing preserved. Flag anything you're unsure about rather than guessing. Key terms to watch for: [list names, jargon, titles]."*
3. **Know what's actually happening.** Claude **won't review the audio.** What it can do is **look at screenshots of the slides at given timestamps** — so it corrects captions by reading on-screen text and context, not by listening. That's powerful for slide-heavy talks and weak for discussion-heavy ones.
4. **For long or audio-only recordings**, this chat-based approach gets unwieldy. The better path — which you'll be equipped for after Workshop 4 — is **Claude Code**, using a model directly for **transcription** from the audio. Note where the chat tool's ceiling is.

*Post to Discord:* a before/after snippet of a few corrected lines (especially a fixed name or term), and a note on where the "reads slides, not audio" limitation showed.

### D. Close the loop: image analysis → generation → reading the dataset (~60–90 min)

This is the exercise that completes the Workshop 3 argument. You analyzed a set; now you'll ask the model to *generate into* that set, and read the generated image as a picture of the training data behind it.

1. **Start from a related image set** in a Claude Project — your own photos, public-domain art by one artist, a run of similar historical documents, a set of comic covers, whatever shares a connection. (Your W5/Workshop 3 set works.)
2. **Run an analysis** across the set: shared visual features, period markers, composition, what they have in common.
3. **Ask for a generation prompt:** *"Based on this set, write me a text-to-image prompt that would generate a new image fitting naturally into this collection."*
4. **Run that one prompt through several generators** — **Microsoft Copilot**, **Google Gemini**, and **ChatGPT Images** (use whatever you have access to; two is enough). Don't tweak the prompt between tools — the point is to hold it constant.
5. **Read the results against the set and against each other.** Where each generator "fills in" beyond your prompt — the faces, the bodies, the settings, the defaults it reaches for — tells you what its training data assumes. Connect it back to the *Washington Post* interactive and "Excavating AI": **what does the divergence tell you about the dataset itself**, both yours and theirs?

*Post to Discord:* the prompt, the images from each generator side by side, and your read on what the differences reveal.

### E. Make a slide deck with Claude Design (~60–90 min)

Claude Design generates editable, PowerPoint-style decks from a prompt — a fast way to draft a talk and a good test of how far you can push past the default template.

1. **Open Claude Design and select "New Slide Deck."**
2. **Feed it real content** — notes from a lecture, a paper abstract, or a workshop you've given.
3. **Prompt:** *"Build a slide deck for a 15-minute talk based on this content. Make it visually distinctive — not the default corporate template — and match it to [my discipline / the tone of the talk]."*
4. **Iterate at least three rounds** — color, layout, typography, visual hierarchy. Notice what's faster than building it by hand, and what's worse.

*Post to Discord:* a couple of slides (or the exported deck) and one line on what Design got right and what you had to fight it on.

### F. Build a voice interface as an AI Artifact (~2–3 hr, advanced)

You can prompt Claude to build a working voice interface — input *and* output — entirely inside an Artifact, no code on your part. This is a direct bridge to the tool-building in Workshop 4.

1. **Turn on AI Artifacts in Settings first** (the Artifacts capability that lets an Artifact call Claude). Without it, the prompt below won't produce a working interface.
2. **Open a new conversation and prompt:** *"Make me an AI artifact that uses a voice interface for [your goal — e.g. asking questions about a primary source in my course, quizzing me on key terms, talking through an idea from my research]. Use the Web Speech API for voice input and output, and show a clear visual indication of when it's listening versus responding."*
3. **Iterate and talk to it.** Tighten the goal, the prompts it asks back, the personality. Compare it to Claude's built-in voice mode — what does building your own give you that the default doesn't?

*Post to Discord:* a screenshot or short screen recording of your voice artifact, plus a note on what you'd change before putting it in front of students.

## What to Carry Into Workshop 4

Workshop 4 (June 24) is the first session in **Stage 3** — Claude Code Web. To prepare:

- **Set up a [GitHub account](https://github.com/)** if you don't have one. Use your `.edu` email and apply for [GitHub Education](https://education.github.com/) benefits — approval takes a few days, so do it now.
- **Bring a CV, syllabus, dataset, or short project description** in `.docx`, `.pdf`, plain text, or `.csv`. We'll turn it into a deployed website during the session.

If you did Exercise A or C and felt Cowork hand you off toward Claude Code, hold onto that feeling — Workshop 4 is where we cross that line on purpose.

## Cross-references

- Source materials: [HumanitiesAI/weekseven](https://anastasiasalter.net/HumanitiesAI/weekseven.html) (multimodal generation comparison), [HumanitiesAI/weekfive](https://anastasiasalter.net/HumanitiesAI/weekfive.html) (image generation iteration), [HumanitiesAI/weekeight](https://anastasiasalter.net/HumanitiesAI/weekeight.html) (image detection in the wild).
