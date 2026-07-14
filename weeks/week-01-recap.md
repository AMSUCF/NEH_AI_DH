---
title: "Workshop 1 Recap: Introducing AI for DH Pedagogy"
---

**Wednesday, May 13, 2026 · CHDR · Led by Mel Stanfill**

Workshop 1 opened the NEH AI+DH series by trying to make the word "AI" concrete. Mel Stanfill walked the group from Weizenbaum's 1966 ELIZA up through large language models, the arrival of ChatGPT, and the current turn toward agentic tools — pausing along the way to try the tools directly. Participants talked to a web version of ELIZA, ran their own sentences through a tokenizer, and ran the same prompt across four different chatbots to compare how each one answered. The session closed by setting up the workshop's build-your-own-ELIZA exercise in Claude Artifacts. Throughout, the framing stayed sober rather than hyped: the point was to understand where these systems came from and what they actually do.

[← Back to Week 1](week-01.md)

## ELIZA and the ELIZA effect

Stanfill began with Joseph Weizenbaum's 1966 program and the effect named after it. The slide showed the DOCTOR script — an ELIZA program that played a Rogerian psychotherapist, reflecting a user's statements back as questions. The striking part of the history, they noted, was how readily people treated the program as a person even when they knew exactly what it was: Weizenbaum's own secretary, who had watched him write it, asked him to leave the room so she could talk to it privately. His alarm was not that the program was too clever, but that people were so ready to believe it was.

> "His worry was not, like, ELIZA is too smart — the machines are gonna take over and kill us all — but that people thought ELIZA was smart."

![Slide showing a retro terminal-style screenshot of the 1966 ELIZA DOCTOR program transcript, with a citation line below]({{ '/assets/recaps/w01/01-eliza-history.jpg' | relative_url }})

## Trying ELIZA live

The group then opened a web version of ELIZA and talked to it, watching how the responses were assembled and noticing their own instinct to anthropomorphize.

> "So try it out. Open it up. Talk to it the way you would talk to a therapist. And look at how the responses are put together. Think about whether you're anthropomorphizing as you're talking to it."

In the debrief, one participant noted in the chat that ELIZA mostly just reiterates back what you say to it; another compared the effect to the way song lyrics echo the last syllable of a line. Several attendees remarked that the simple reflection technique started to feel manipulative once you noticed the pattern, and that a few exchanges were enough to expose its small stock of Rogerian phrases. Stanfill pointed out that questions about language changing over time — a real concern for a model trained on, say, nineteenth-century literature — don't actually apply to ELIZA, because ELIZA simply repeats back the words you give it.

## AI, LLMs, and how they actually work

Next came the vocabulary: AI as a broad goal, machine learning as a subfield, deep learning as a method, and large language models as one particular use of it. Stanfill described AI as "this sort of broad, conceptual goal of creating machines that act intelligently," then drew the sharp line they wanted people to leave with — that an LLM is not a database of facts but a predictor of likely text.

> "One of the things that's really super important here is that LLMs do not know facts. They predict likely sequences of tokens."

Because the output is shaped by the training data, it can lean in odd directions. They offered a topical example.

> "The famous example that happened this week is that ChatGPT was apparently trained on a bunch of stuff that's, like, fantasy content, and so it will start mentioning goblins."

![Hand-drawn-style diagram slide showing AI, Machine Learning, Deep Learning, and LLMs as a nested stack]({{ '/assets/recaps/w01/02-how-llms-work.jpg' | relative_url }})

## Tokens and the tokenizer exercise

To make "sequences of tokens" tangible, participants ran their own sentences through a tokenizer, following Simon Willison's example.

> "So we're gonna use Willison's example. You're gonna use the AI tokenizer on your own device, and you're gonna give it a sentence that you would actually type into Claude or ChatGPT."

Attendees tested the tokenizer with subject-specific vocabulary, non-English text, and technical or philosophical phrasing, and saw that tokenization doesn't cleanly respect word or morpheme boundaries — a gap that gets wider outside English. Stanfill made the language point directly:

> "None of these tools work very well in languages other than English, period. Except DeepSeek, which is a Chinese tool. It works fairly well in Chinese."

## What "generative AI" means, and the model stack

Stanfill turned to definitions and to what sits on top of a base model. They read the MLA-CCCC Joint Task Force's working definition and then set a skeptical counterpoint beside it.

> "Generative AI systems are computer systems that can produce or generate various forms of traditionally human expression — language, images, video, and music."

> "Bender and Hanna say it's a marketing term. It actually doesn't refer to a specific thing."

They also introduced the Claude model family that the series would rely on, framing the tiers in terms of cost and speed.

> "So Opus is the most powerful, and therefore the most expensive. It will chew through your allotted use. Sonnet's in the middle, and then Haiku is fast and small."

![Bullet slide on what sits on top of the base model — reinforcement learning from human feedback, system prompts, tools, and the Claude Opus, Sonnet, and Haiku tiers]({{ '/assets/recaps/w01/03-genai-definition-model-stack.jpg' | relative_url }})

## The ChatGPT moment

With the mechanics in place, Stanfill dated the shift in public awareness — while arguing that what changed was not the underlying technology.

> "November 30th, 2022, a day that will live in infamy."

The capabilities, they pointed out, largely predated the chatbot; the interface was the wrapping around them. What arrived on that date was reach.

> "What's new in November 2022 isn't capability, it's access."

![Bullet slide headed November 30, 2022, listing ChatGPT launch facts with cited sources]({{ '/assets/recaps/w01/04-chatgpt-moment.jpg' | relative_url }})

## The current landscape and the agentic horizon

The conversation then moved from chatbots to agents — systems that don't just answer but act. Stanfill borrowed Simon Willison's compact definition.

> "An LLM agent, Simon Willison tells us, runs tools in a loop to achieve a goal."

They paired the promise with a caution, citing an image that circulates online and adding their own gloss.

> "A computer can never be held accountable, therefore a computer must never make a management decision. And I think that's just good life advice."

Applied to teaching, the worry is an assignment loop that runs end to end without a student in it at all.

> "But actually, the chat agent does all of the whole assignment loop. The student does not do anything, does not even log into the course. And this is the nightmare scenario, I think."

![Slide showing an Einstein.AI agentic-tool example with an embedded graphic panel]({{ '/assets/recaps/w01/05-agentic-landscape.jpg' | relative_url }})

## Chatbot tour: the same prompt across tools

The hands-on centerpiece was a tour of several chatbots, running one prompt through each to compare how they behave. Stanfill introduced the lineup and flagged the institutional rule attached to it.

> "The five tools are Gemini, which is the free Google chatbot that is integrated with the search and the GDocs suite."

> "This is the only one you're allowed to use for sensitive data. It's the only one that UCF is supporting and actually wants you to use, and Claude is our main one."

The instruction was to run the identical prompt through each tool and watch not just the answer but the manner of answering — its hedging, its refusals, its formatting. Four of the five tools were hands-on in the room that day; the fifth, the local DeepSeek model, came later in the session as a recorded demo run through Ollama.

> "Run the exact same prompt through all four of these … and think about how does it answer the question? What language does it use? Is it hedging? Is it refusing? What's happening with the layout? Claude really loves emojis, for example."

![Bullet slide titled the five tools, listing Gemini, DeepSeek via Ollama, ChatGPT, UCF Copilot, and Claude with short descriptions]({{ '/assets/recaps/w01/06-chatbot-tour-exercise.jpg' | relative_url }})

## Comparing the results

In the share-back, attendees reported what they had found — all anonymized here. One had run a prompt about keeping art students motivated in an age of AI across the tools and watched them converge on similar advice. Another was startled to see a tool's answer fold in notes from a conference they'd personally attended, and flagged the surveillance implication with some humor. Another compared how different tools described craft choices across award-winning short-story collections and caught every tool hallucinating at least a little, misattributing books and authors. One deliberately probed a question about African philosophy and time to test for bias and hedging; a non-native English speaker tested an academic sentence and found one tool noticeably more useful than the rest — while noting that none of them flagged a citation they had fabricated on purpose. On that last point Stanfill was blunt:

> "Things get published that have hallucinated citations and are racking up citation counts and don't exist."

## Running a model locally: the DeepSeek demo

To show what running a model on your own machine looks like — no API call, no data leaving the room — Stanfill played a recorded demo of DeepSeek running through Ollama, prompting it with a politically sensitive question and getting a flat refusal on screen: "I'm sorry, I cannot answer that question." They were candid that the local setup was a video rather than a live demo.

> "This is being run locally through Ollama, which I did not have time to set up because I found out I was doing this by myself at 7pm last night. So we did a demo video instead. But this is something where you can use these tools locally on your machine without sending data out to the servers of these companies."

![Screen-share of a recorded demo video showing an Ollama desktop chat window with the deepseek-r1 model selected and a typed prompt about Tiananmen Square]({{ '/assets/recaps/w01/07-deepseek-demo.jpg' | relative_url }})

## Why Claude / why Anthropic

Stanfill explained why the series settles on Claude — not as an endorsement of the company so much as a practical read of the current tool landscape.

> "The big thing is that the particular set of tools that Anthropic has are the broadest set of tools currently available that don't require coding knowledge."

They also gave Anthropic qualified credit on transparency relative to the wider field.

> "They have a culture of safety and interpretability, they publish about it, the publication record, they're explaining what they're doing. Bare minimum, but it's more than a lot of the people are doing."

![Bullet slide titled Why Claude / why Anthropic, listing tool surface breadth and a safety and interpretability research culture]({{ '/assets/recaps/w01/08-why-claude.jpg' | relative_url }})

## Building our own ELIZA

The session's closing exercise brought the day full circle: build an ELIZA of your own as a Claude Artifact. Stanfill set it up live, showing where the instructions were and encouraging people to make the persona their own rather than defaulting to the therapist.

> "Essentially, you're gonna use Claude Artifacts. I'm gonna open Claude, start a new chat, the instructions are here, and you're gonna pick the tone. You're gonna pick the pattern."

> "Rather than being like, be a Rogerian psychotherapist, you could do something that is more specific to you — be a Victorian orphan, be a Gen X person drowning in ennui, be the narrator of My Immortal."

![Exercise-instruction slide titled Build our own ELIZA together in Claude Artifacts, with numbered steps]({{ '/assets/recaps/w01/09-build-eliza-exercise.jpg' | relative_url }})

## Closing: what to walk away with

To wrap up, Stanfill named the takeaways they wanted everyone to keep and pointed ahead to the asynchronous Week 2.

> "The main things we want to make sure you walk away with from today: you should be able to explain what ELIZA is and how that's where we started, what an LLM is, that ChatGPT is the interface and not the technology, some basic ideas about agentic AI."

> "Week two is asynchronous, and that is posted already, so you can do that at your leisure."

![Closing slide titled with the three things to leave with, alongside reading links]({{ '/assets/recaps/w01/10-closing.jpg' | relative_url }})

## Try It Yourself

Missed the session, or want to redo the closing exercise on your own? The Week 1 page walks through it step by step: build a small ELIZA-style chatbot as a Claude Artifact, give it a style and subject of your own, and compare it to the plain pattern-matching original. See the [Core Exercise on the Week 1 page](week-01.md#core-exercise) to try it yourself.

---

*Quotes are drawn from the session transcript, lightly edited to remove filler words and false starts, and to correct obvious automatic-captioning errors (for example "Cloud" → Claude, "ELISA" → ELIZA, "Rock" → Grok) to the words the speaker actually said. Participant comments are paraphrased without attribution.*
