---
title: "Workshop 6 Recap: Agentic Futures, Curricular Sustainability"
---

**Wednesday, July 22, 2026 · CHDR · Led by Anastasia Salter, with Mel Stanfill**

The final in-person session of the series was a tour through the power tools: the Claude Code command line interface, MCP servers, Hugging Face, and Ollama. Anastasia Salter framed the two hours as literacy-building rather than hands-on requirement, since UCF policy keeps most of these tools off university machines, and demoed a workflow most attendees had never seen end to end: an accessible, fully voiced rebuild of a 1984 Infocom game assembled from historical source code and local models, steered from a terminal and, at one point, from a phone. Mel Stanfill kept the questions flowing from the chat, and the session closed where the whole series has been pointing: what agentic AI means for curriculum, for students entering a reshaped workforce, and for who keeps control of these capacities as the frontier companies and the open-weights world race each other.

[← Back to Week 11](week-11.md)

## The twilight of the chatbots

The framing picked up the series' opening thread, from ELIZA in week one to the interface most people still equate with AI, and declared it on its way out. "The chatbot as the way you work with AI was always a tech demo, not actually how AI is useful," Salter argued, and while the chat window will persist for entertainment and quick questions, "the things I'm going to show you today are how the people who are working with AI towards professional purposes work with it now."

The labor stakes came first, through Altman's claim that AI will only eliminate "jobs that aren't real work" and David Graeber's bullshit jobs theory. The room's shared experience of filling out the same travel information four times across UCF systems stood in for the whole category of work worth automating. The real challenge, Salter suggested, is that institutions rolling out chatbots for productivity are not distinguishing the meaningful work from the meaningless, and people keep offloading the wrong parts.

> "Figuring out which part of your job is bullshit is something that these tools allow you to do."

![Workshop slide showing the cover of David Graeber's Bullshit Jobs beside a quotation arguing that AI is being marketed as the cure for meaningless work]({{ '/assets/recaps/w11/01-graeber-slide.jpg' | relative_url }})

## Installing the power tool, safely

The Claude CLI got the full plain-language treatment: what a terminal is, why installing a command differs from installing an app, and why Git for Windows matters ("we're installing the verb Claude on our machine, so we can call on it whenever we want"). The most emphatic advice of the day was about where not to run it.

> "When you hear horror stories of someone deleted all of their family photos, or all the versions of their dissertation... this is what they did. They went into their root directory, and they told Claude, have at it."

The recommended on-ramp remains GitHub Desktop: create or open a repository, choose Open in Command Prompt (or Terminal), and type `claude`, so the agent only ever sees the folder you mean it to change. "Only run Claude in the folder that you want it to make changes in." Anything beyond that box requires permission, and the security calculus is personal: "It's all about your tolerance for risk versus your tolerance for hassle. My tolerance for risk is higher than my tolerance for hassle." Auto mode got the same warning label it earned in earlier sessions, with an extra edge on the command line: "YOLO mode on your command line is more dangerous than YOLO mode over on any of the other tools we've looked at... We told you to use the safety glasses with the power tool."

## A tour of the cockpit

From there the session walked the interface: slash commands as shortcuts around natural language, `/model` (with a stop at Fable, "you don't always need to throw Fable at a problem. Fable is a lot"), `/help`, `/init` for documenting an existing codebase, and Shift+Tab to cycle between manual, accept-edits, plan, and auto modes. Plan mode kept its series-long billing as where every project should start.

The plugin marketplace drew particular attention for teaching-adjacent gems: a skill creator (Salter's example: a skill that applies UCF accessibility guidelines to any HTML it builds), Code Simplifier for a cleanup pass at the end of a project, Playwright so the agent can read its own browser errors, and CLAUDE.md management for the context file that this week's take-home exercise asks everyone to write. Superpowers, installed here via `/plugin`, remains the workflow backbone: "I use superpowers constantly, because it organizes the workflow structure in ways I don't like to have to think about myself." The Telegram and Slack bridges got a knowing nod as the shape of things: dev teams already delegate tasks to Claude in the same channels where they delegate to each other. And the standing caveat applied to all of it:

> "Think about where you're getting it from and the extent to which you trust them before you get some random person's Claude skill on your computer."

![Claude Code plugin marketplace in the terminal listing skill-creator, code-simplifier, github, playwright, and claude-md-management plugins with install counts]({{ '/assets/recaps/w11/02-cli-plugins.jpg' | relative_url }})

## MCP: an agent-forward way of accessing something else

MCP servers got the week's simplest definition, "an agent-forward way of accessing something else," and the most DH-relevant examples: a Zotero server that lets Claude run semantic searches over your research library, or a custom server for your own archive project that pulls records, updates descriptions, and checks for errors. The hands-on example was the Hugging Face connector, with a walk through the permission controls that let you require approval for anything that touches data or spends money, or block a capability outright.

The pitch for Hugging Face itself was Claude-as-interpreter. Model cards are written for engineers, and choosing among a dozen OCR models is nobody's idea of humanities research. The workflow demonstrated: point Claude at the documentation and a sample file and let it recommend, as with the undergraduate journal digitization project where Claude picked the OCR model but the conversion ran locally, cheaply, without sending student writing anywhere.

> "Claude then becomes the tool by which you navigate this nonsense, which was not written for you... My eyes glaze over when I have to read about someone's PDF to Images function."

![Claude connector settings for Hugging Face showing read-only tools and write tools each set to needs-approval]({{ '/assets/recaps/w11/03-hf-connector.jpg' | relative_url }})

## Audio Hiker: making a 1984 game speak

The centerpiece demo tackled the historical source code of Infocom's *Hitchhiker's Guide to the Galaxy*, released as an archival snapshot and never made accessible. The project goal: a version playable entirely by ear, with local text-to-speech models voicing every character, eventually driven by voice input. For Salter this is the two things AI currently does best for their side of the field: "taking old source code that hasn't been maintained... and bringing it up to usability. And then adding accessibility features it never had."

A question from Mel Stanfill about a twenty-year-old Flash project, too large for GitHub and not something to hand to UCF servers, set up the workflow's key point: none of this requires publishing anything. A repository in GitHub Desktop can stay entirely local, keeping version control while the media files never leave your machine, with backups on a private repo, an external drive, or Hugging Face (where datasets, once cleaned, are best shared for other researchers). The demo then ran `/init` over the ZIL source, where Claude correctly flagged the code as historical and unlicensed, "an artifact for study rather than something to refactor," and moved into plan mode for the accessible wrapper.

![Claude Code in plan mode after writing a CLAUDE.md for the Hitchhiker's Guide source, with a prompt describing an audio-driven accessible version built on local models]({{ '/assets/recaps/w11/04-audiohiker-planmode.jpg' | relative_url }})

The already-built version showed what Superpowers leaves behind: a folder of numbered task briefs and reports, twelve for the first-stage prototype alone, plus plans and specs documents where the real authorial work happens. "This is the part of the process where you should be spending the most time on any project."

![File explorer view of the audiohiker superpowers folder showing review diffs and twelve numbered task briefs and reports]({{ '/assets/recaps/w11/05-superpowers-tasks.jpg' | relative_url }})

The voice casting turned out to be a data file: a `voices.json` where every character gets a prose description, the narrator "a middle-aged British man narrates in a warm, dry, faintly amused tone," the Vogon captain booming "in a slow, sneering, self-important voice." Claude pulled the Piper text-to-speech model from Hugging Face through the MCP connector, and those descriptions keep the audio consistent across hundreds of generated fragments. The ethics of voice synthesis got direct treatment, from deepfake fraud to the professor who lost his voice to throat cancer and now narrates his courses through a model trained on his old recordings. The first prototype read every score line and room title aloud, exactly like a screen reader, which became the point:

> "The screen reader interfaces do the same thing... but the difference is here, I can get it to stop that nonsense. You can't get a screen reader to stop it."

![VS Code showing the audiohiker voices.json file with prose voice descriptions for the narrator, Ford, Prosser, the barman, the Vogon captain, and the Guide]({{ '/assets/recaps/w11/06-voices-json.jpg' | relative_url }})

## Pushing fixes from the dog walk

A crowd-pleasing aside: `/remote-control` hands the running session to the Claude app on your phone. Salter sent "remove the part where the score is repeated every turn" from their phone and watched it arrive on the demo machine, `/rc active` glowing at the bottom of the terminal.

> "When you hear about people who are working at big companies who are pushing fixes from their morning commute, that is what they are doing. They're running Claude on a more powerful system and talking to it from their cell phones."

![Claude Code terminal with remote control active, showing a fix request sent from a phone to remove the repeated score line from the game's narration]({{ '/assets/recaps/w11/07-phone-remote.jpg' | relative_url }})

## Ollama, or the answer to the bubble question

Local models got introduced as the answer to nearly every objection the series has fielded: privacy, the environment, distrust of Silicon Valley, and the colleague who confidently predicts the AI bubble will burst and take the tools with it. Ollama is the friendly wrapper, and it is how the new CHDR Spark will serve local models this fall. The demo revisited the DeepSeek censorship experiments from week one, reframed for research: running a model locally is "a very safe way to test models that are questionable in their origin," and for anyone studying AI globally, the ability to pull a Chinese open-weights model onto your own machine, away from its company's servers, is a method.

The UCF policy nuance got careful handling. Installing Ollama and running models entirely locally sends no data anywhere, which Salter distinguished from using Ollama's cloud models on a university machine, while being honest that agentic tools of any kind live in institutional gray space. The soapbox moment was brief and self-aware: "We already can't post the video recordings, so we're posting nice summaries written by Claude. But that has to change. It's absurd."

The reveal was `ollama launch claude`: the same Claude Code interface, wrapped so that a locally installed model does all the thinking. "You're still using Claude Code as the race car, but you're changing out your driver to be a local model." Gemma 4 is the current favorite driver; Qwen's coding models and DeepSeek are alternatives; the smallest Gemma editions run on a phone, and that phone-sized model already outperforms the GPT that started the whole panic in 2022.

> "Learning Claude Code, as I tell students regularly, is not just about learning to use Anthropic services and servers. You're just using currently the best command line tool that everyone else is imitating, and you can run it without paying Anthropic a dime in the future."

![Ollama's Launch screen listing terminal agents it can wrap, with Claude Code at the top and the command ollama launch claude]({{ '/assets/recaps/w11/08-ollama-launch.jpg' | relative_url }})

## Harbor towns: measuring the trajectory

To make the capability curve visible, Salter pulled up Ethan Mollick's long-running benchmark prompt: a procedurally generated 3D simulation of a harbor town evolving from 3000 BCE to 3000 CE. Kimi K3, an open-weights model released the week before and runnable on the Spark, produced a polished simulation with light rendering, era transitions, and ships that stay in the water, a result that would have embarrassed frontier models a year earlier. GPT-4's 2023 attempt looked prehistoric by comparison; Fable's version added museum-scale aesthetics and a sun slider.

> "Open weights models are as capable as some of our frontier models were a year and a half ago. And much more capable than frontier models were two or three years ago."

![Kimi K3's harbor town simulation named Portus in its medieval era, showing a walled 3D town with a cathedral, docks, and sailing ships]({{ '/assets/recaps/w11/09-harbortown-kimi.jpg' | relative_url }})

![Fable's harbor town simulation in a pale museum-like style, showing a Neolithic settlement labeled 2715 BCE with a sun slider and timeline controls]({{ '/assets/recaps/w11/10-harbortown-fable.jpg' | relative_url }})

The closing read of the landscape inverted the usual worry. The questions that dominate campus conversation are prohibition and refusal; the ones that should concern us are access and control, whether regulation and hardware prices will lock these capacities back inside the frontier companies just as local alternatives mature. "Enjoy the prices of the next generation of cell phones."

> "The questions around AI tend to be talked about in terms of prohibition and refusal by a lot of people right now, but the ones that concern me much more are questions of access and control."

## What happens in September

The last stretch turned practical: the cohort's funded participants owe course revisions and new courses, and UCF's compressed curriculum calendar means proposals need to be ready for committees by September. The Q&A became a strategy clinic. When a full Kuali proposal is needed versus an informal refresh, why teaching a special topics course while its formal proposal is in the pipeline builds the enrollment case, and the rhetorical politics of naming, where "AI" in a title attracts some students, repels others, and invites turf battles ("our AI course used to be the database course... I argued that AI is the next big database. They bought it").

A participant question from the chat, about whether agentic AI is simply becoming how the work gets done, brought the series' hardest line. Bluesky and Spotify ship agent-written code; scrapers without AI-generated code functionally no longer exist; "those who are trying to pass the purity test as far as AI usage are going to find it exceedingly hard to do computational labor of any kind." Salter reserved their sharpest worry for what we teach students to want:

> "They are living in a world that is being rebuilt by AI agents, and being rebuilt for AI agents. And so their decision not to engage won't change the fact that the world is changing around them."

The alternative-assignment compromise, comforting students with the assurance that they don't need to know this, "won't serve them well in the end." Preparing students on the real power tools, including local AI, "is preparing them much more to make subversive moves and be in control than if you follow the UCF script and hand them a Copilot chatbot to write an essay for them." And the self-implicating punchline about curricular lag: "UCF still has a web design degree. That is hilarious to me... I say as the former director of the web design program."

The series ended with thanks, a promise of fall workshops in CHDR on getting started with the Spark, and a benediction for the return to campus: go be the people in your departments who can speak knowledgeably to both the pitfalls and the opportunities.

## Try It Yourself

The take-home exercise needs no installation at all: write a `CLAUDE.md` for your work, the context document that tells an agent who you are, what you do, how you work, and what you refuse to delegate. It is meta-pedagogy in a markdown file, and useful whether or not you ever open a terminal. See the [Take-Home Exercise on the Week 11 page](week-11.md#take-home-exercise) for the full prompt.

---

*Quotes are drawn from the session transcript, lightly edited to remove filler words and false starts, and to correct obvious automatic-captioning errors (for example "Cloud Code," "Quad Code," "CloudCo," and "BUD CLI" → Claude Code, "Olama" and "a llama" → Ollama, "Hugging Place," "Huggy Face," and "Talking Face" → Hugging Face, "quad skill" → Claude skill, "my tolerance for hack" → hassle, "written by the squad" → written by Claude, "Bullock" → Mollick, and "Jim before" and "GEMA4" → Gemma 4) to the words the speaker actually said. Participant comments are paraphrased without attribution.*
