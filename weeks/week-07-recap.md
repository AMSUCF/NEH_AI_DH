---
title: "Workshop 4 Recap: Web and Interactive Applications"
---

**Wednesday, June 24, 2026 · CHDR · Led by Anastasia Salter, with guests from the ELC 5 editorial collective**

Workshop 4 crossed the halfway point of the series and turned to the literacy underneath everything so far: code. After a genuinely cursed technical start (Zoom hard-crashed the presenting machine minutes in, forcing a live reboot), Anastasia Salter framed agentic AI as the biggest current shift in computational literacy, walked the group through GitHub and GitHub Pages from scratch, and ran two full builds in Claude Code Web: a P5.js animation of elephants dancing in the rain, and their own CV converted into a Lisa Frank portfolio site, both deployed live to free public URLs. Along the way came a pointed reading of UCF's policy banning agentic tools, a workaround for a freshly broken GitHub connector, and a preview of Claude Code Desktop. The session closed with guests Eli Ortega, Dan Cox, and Zach Whalen of the *Electronic Literature Collection* Volume 5 editorial collective, trailering an afternoon session on creativity and AI.

[← Back to Week 7](week-07.md)

## Code literacy after agents

Salter opened by naming the through-line: the last several workshops have all quietly involved code, and code is where AI is transforming industry fastest. Borrowing Annette Vee's term "code literacy," they located the change in both how people understand computational systems and how they build them. For digital humanities specifically, the pragmatic value lands on a sore spot, the project-by-project funding model that builds archives and then abandons them.

> "It's often for assisting with the labor that no one funds or supports."

The stakes are also professional and institutional. DH has long justified itself by giving students marketable technical skills, an argument Salter has made to administrators themselves, and the workshop series itself exists partly so the university can tell an AI story across its units.

> "If you apply to this cohort in part as a survival strategy for yourself, that is wise."

Each workshop has put the model in a more capable wrapper, "the race car that we put AI in has gotten more complicated with each round," and this session reached the most powerful tier. That power cuts both ways: "agentic tools right now are built for people who already understand software," which is exactly why the baseline literacies matter. Students who build them can navigate these tools and understand their impacts, Salter argued, "even if they choose not to use it themselves."

## GitHub, the training ground

Before touching Claude, the group toured what Salter cheerfully called a weird thing: "GitHub has played a major role in making AI what it is." As the web's biggest pile of open source projects, abandoned experiments, and well-maintained codebases, it is a large part of what the models trained on, with a practical corollary:

> "A good rule of thumb is that the more popular a language is on places like GitHub, the better AI is going to be at producing its code."

The vocabulary lesson was deliberately plain. A repository is "just a folder, it's like working in Google Drive, but with a complete history, but the history has save points called commits." As a live example, Salter pulled up this workshop series' own repository, at that point 77 commits deep.

> "Claude has authored most of the commits on this repository."

![GitHub commit history for the workshop repository, showing a series of commits co-authored by AMSUCF and claude with verified badges and commit hashes]({{ '/assets/recaps/w07/01-commit-history.jpg' | relative_url }})

That authorship shift is everywhere, they noted: open source maintainers are being overwhelmed by AI-authored pull requests of uncertain quality, a code version of the textpocalypse from Workshop 2, and it is happening faster in code than anywhere else.

## The policy problem

Why start with Claude Code Web, which Salter called, flatly, "the worst. It's just the worst"? Because it is the only one of the three Claude Code interfaces that requires no installation, and UCF policy currently prohibits installing the others on university machines. Salter put the policy itself on screen and read out its bottom line, that there are "no safe examples or applications of agentic browsers or agentic desktop apps."

![UCF Artificial Intelligence for All policy page on agents, with the bottom line highlighted: there are no safe examples or applications of agentic browsers or desktop apps, and UCF students, faculty, and staff are urged to avoid installing or using agents]({{ '/assets/recaps/w07/02-ucf-agents-policy.jpg' | relative_url }})

Their assessment was not gentle, and it came with a labor-market warning.

> "I have talked to multiple employers who've said they would not even remotely consider the application of someone who doesn't know how to use, at the very least, Claude Code from the command line."

A participant asked how there can be an overarching institutional push for AI and handcuffs on using it at the same time; the room's answer, risk mitigation, led Salter to Ethan Mollick's essay "The IT Department Where AI Goes to Die," on what happens when technology decisions belong to people whose job is avoiding risk. The famous agent horror stories got a deflationary read.

> "A person who sets an agent loose on a database with no guardrails was very likely to just delete it themselves."

> "Problem exists between keyboard and chair."

Another participant pushed the humanities angle: this is precisely where a humanities voice belongs, since these are situations that demand judgment. Salter agreed, adding that the weird, experimental uses being locked out by policy are exactly the work humanities, arts, and theater programs should be doing. The rest of the session, they promised, would be "weird, useful, strange things with code."

## Three interfaces, one tool

A quick genealogy set up the demos. The command line tool came first, made by software developers for software developers. Claude Code Desktop followed as a friendlier face, and Cowork after that, renamed and restricted for people put off by the word code: "when you're working with Cowork, you're working with defanged Claude Code." The frustration of these interfaces is not new to DH.

> "Most of the suffering in digital humanities has always been about software interfaces, and the fact that software interfaces were designed for developers, by developers, without other users in mind. That has always been true."

## The token ordeal

Connecting Claude Code Web to GitHub should be one click. The week of the workshop, it was not: the OAuth connector had broken (only for new authorizations), so the session detoured through GitHub's developer settings to generate a personal access token, the workaround Salter and collaborators had debugged that morning. The guidance: scope the token to repositories only, never grant deletion, and "we love repo-only access." Salter declined to generate one on screen, "because I was raised by two security professionals." Live chat triage got one online participant through an interface that kept redirecting away from the web version entirely, a bug hunt conducted in parallel with the lecture. The verdict on the whole affair: "Software developers, man."

## Elephants in top hats, deployed

With a connection working, the first build began with a naming lesson. The new repository (christened Improved Octo Pancake, from GitHub's suggested names) is a folder on the web, not on your computer, and its name has to live in a URL: "No spaces. No weird characters. Whatever you put in is something you're gonna have to type later." The prompt was deliberately silly: build a P5.js animation of elephants with top hats dancing in the rain.

![Claude Code Web session titled Elephants dancing in rain, showing the build prompt and the initialization steps: set up a cloud container, cloned repository, started Claude Code]({{ '/assets/recaps/w07/03-codeweb-elephants-build.jpg' | relative_url }})

The cloud container, Salter explained, is the pedagogical selling point. Everything runs on Anthropic's servers, so "the risk to you when you're working with Claude Code Web is pretty much zero," and no student can email at midnight to say the agent deleted their hard drive. From there the session walked the deploy path that would repeat all morning: find the branch Claude created, read the diff (413 lines added), turn on GitHub Pages in the repository settings, and wait for the brown dot to become a green checkmark. Then the URL went live.

> "It gave me features I didn't ask for. Click to add an elephant. Folks, this just got so much better."

> "Press R to make it rain harder."

![Deployed GitHub Pages site showing three cartoon elephants in red-banded top hats dancing in falling rain, with instructions to click to add an elephant and press R to make it rain harder]({{ '/assets/recaps/w07/04-elephants-live.jpg' | relative_url }})

Salter reminded the room that Claude is not an image generator, so the elephants are pure vector graphics and animation code, and noted the model doing the work was not even the top of the line: "Sadly, we lost access to Fable before we could really try it out. Thank you, U.S. government." For many projects, they argued, this workflow now "replaces Squarespace, WordPress, and Wix."

## Iteration and the cost slider

Round two asked for thunder synced to the visuals, pinker elephants, and a full psychedelic treatment ("Claude knows what I mean. It's been on Reddit."). While it built, Salter covered the settings that actually change outcomes: for code, stay on Opus 4.8 at high reasoning, and remember that the faster-to-smarter slider "is also the cost sliding scale." The system is non-deterministic, so participants' elephants arrived with umbrellas and thunder nobody requested, and the fix for unwanted surprises is specificity: name the technology you want or accept "a roll of the dice, what Claude decided to do."

![Claude Code Web session showing Claude planning the psychedelic rebuild: a web audio synth engine, synthesized thunder tied to lightning, pinker elephants, and hue-cycling trails, with a diff of 413 added lines pending]({{ '/assets/recaps/w07/05-acid-trip-iteration.jpg' | relative_url }})

## The CV becomes a Lisa Frank portfolio

The second full build modeled the week's core exercise: a fresh repository, a raw unprepared .docx CV uploaded through the browser ("exactly how our students would work"), and a mode switch. Alongside accept-edits and the YOLO auto mode, Claude Code offers plan mode, which Salter called "the more academic setting," where the model proposes before it builds. The prompt: review the CV in this folder and convert it to a Markdown portfolio site using Lisa Frank aesthetics and too much animation.

![Claude Code Web new session connected to the another-portfolio-demo repository on the main branch, with a typed prompt asking Claude to review the CV in the folder and convert it to a Markdown portfolio site using Lisa Frank aesthetics and too much animation]({{ '/assets/recaps/w07/06-plan-mode-lisafrank.jpg' | relative_url }})

Claude tore into the Word file ("Let me extract the readable text from the document XML! Because Word is evil!") and processed the whole CV, prompting Salter's translation of its tone: "I now have the complete CV! Allow me to fill these comments with way too much praise!" On the aesthetic: "Lisa Frank, it's problematic, but the aesthetics live on."

The build surfaced the one genuinely painful part of the browser workflow: branches and merges. Claude works on its own auto-named branch (this one drew "claude-vigilant-johnson") and never touches yours uninvited, "Claude respects the main branch," so publishing changes means a parade of pull request confirmations.

> "There's an amazing number of steps here, but they all involve clicking the green button."

> "You weren't sincere enough. Gotta click it again."

![GitHub compare view for the portfolio repository showing Claude's auto-named branch able to merge, with a pull request titled Add Lisa Frank-inspired portfolio site and a green View pull request button]({{ '/assets/recaps/w07/07-pull-request.jpg' | relative_url }})

Salter's classroom practice is repetition: have students run the full cycle at least three times, "because it's all interface literacy," and without it students "get defeated by interfaces that are not designed with any of us in mind." The result of this run, meanwhile, went live in all its glory: a hot-pink-and-mint portfolio with a dancing unicorn landing page, emoji cursor trails, and a marquee of research areas.

> "Little emoji heavy there, Claude, but okay."

![Deployed Lisa Frank-style portfolio site on a mint green background, with the name in rainbow bubble script, a unicorn emoji, sparkle decorations, and job titles rendered in glittery purple type]({{ '/assets/recaps/w07/08-portfolio-live.jpg' | relative_url }})

It was, Salter admitted, too much even for them: "I best delete this one. I can't count it as this being on the web, this is not okay."

## Web design is dead, platforms are worse

Stepping back from the demo, Salter delivered the eulogy: "I want to speak for a moment to the field of web design. So that's dead." What the morning produced was not far from what capstone web design students once built over a semester. The sharper point was aimed at the paid alternatives: Squarespace, Wix, and their WYSIWYG kin are inaccessible, unexportable by design, and no longer worth money or content, because "they deliberately want you locked into their ecosystem." GitHub Pages, by contrast, is free, and "your students will be able to carry it with them when they leave campus."

Their own practice made the case concretely. Salter no longer pays for any web hosting and updates their site by talking to Claude Code, often from a phone: "Someone will point out, hey, you just taught this workshop, is this link anywhere? And I'll be like, yes. Yes, it is. It's on my website. Give it 2 minutes." A participant question about escaping Squarespace turned into the deeper use case, liberation of content from proprietary platforms, whether a Wix site, a Canvas export, or an old Flash project: "I have something that was built in a proprietary software tool, and I want to free it." (Guest Dan Cox, it emerged, has built a tool for exactly the Canvas-export version of this problem.)

## Guests: the Electronic Literature Collection, Volume 5

The session's coda introduced the editorial collective of the *Electronic Literature Collection* Volume 5, in town for an editorial retreat: Eli Ortega, Dan Cox, and Zach Whalen, with fourth editor Danny Spinoza unable to attend. The ELC anthologizes electronic literature roughly every five years, and the team previewed an afternoon session on creativity and AI, including statistics from the current call for submissions and the range of responses it drew, some more antagonistic than others. Asked whether they were the first ELC editors to deal with AI, the answer was a firm no: Salter, who served on the ELC3 team a decade earlier, pointed out that the collection has gathered chatbots and Twitter bots for over fifteen years. The e-lit community, they noted, holds the full range of positions at once: "We have folks who will not touch AI for their code, and folks who will not touch code again."

## Desktop, local AI, and the unequal landscape

The homework pointer came with a preview of Claude Code Desktop, where sessions can run in the cloud or locally, and locally is where the real power and the real risk begin: "when it asks you to install a Python library, it's installing it on your computer." Salter's advice for going local: pair it with GitHub Desktop, work inside a repository so version control can absorb mistakes, and (with a wink) not on a UCF machine.

![Claude Code Desktop app showing usage statistics and an activity heatmap, a session picker offering Local, Cloud, Remote Control, and SSH options, and a banner reading Claude Fable 5 is currently unavailable]({{ '/assets/recaps/w07/09-desktop-local-cloud.jpg' | relative_url }})

A publisher's newly released AI policy, restricting authors to "private AI systems" owned by their institutions, surfaced in discussion and drew a structural critique: institutions with Anthropic enterprise deals get real tools while everyone else gets locked out, "an incredibly unequal landscape among academic researchers," a digital divide turned into policy. The same holds for students who follow campus rules and graduate less prepared than peers elsewhere. Salter's recurring answer to the privacy, copyright, and environmental anxieties alike was local models, with new hardware in the building to support exactly that research.

> "The answer to all of this really is local AI. It's the answer to the environmental anxiety, to privacy questions, to just about everything."

The closing pitch pointed at the next two in-person sessions and the command line: "bring a non-UCF-managed system to our next workshops. We will be going towards the power tool." And, on returning to a terminal-first world: "We're going back to the days of MS-DOS. They were fun!"

![Closing slide titled Your URL is yours, noting the URL stays live as long as the repo exists and you own the work, version history, and attribution, with links to the Workshop 4 page, the Week 8 async exercise, and the Martin and Evans readings]({{ '/assets/recaps/w07/10-closing-slide.jpg' | relative_url }})

## Try It Yourself

Missed the session, or want your own live URL? The Week 7 page walks through both paths: create a public GitHub repository, upload your CV (or a 5 to 15 image set), connect it in Claude Code Web, plan before you build, iterate, and deploy via GitHub Pages. Your site should be live within the session, and the URL is yours to keep. See the [Core Exercise on the Week 7 page](week-07.md#core-exercise) to try it yourself.

---

*Quotes are drawn from the session transcript, lightly edited to remove filler words and false starts, and to correct obvious automatic-captioning errors (for example "Annette V" → Annette Vee, "Ethan Moloch" → Ethan Mollick, "keyboard and share" → keyboard and chair, "defanged, clawed code" → defanged Claude Code, "Quad Code," "Cloud Code," "Clyde code," and "CLUD code" → Claude Code, "Claw" and "clot" → Claude, "Poll Request" → pull request, and "Maine" → main) to the words the speaker actually said. Participant comments are paraphrased without attribution.*
