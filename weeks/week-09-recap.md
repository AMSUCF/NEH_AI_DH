---
title: "Workshop 5 Recap: Playful Approaches and Creative Code"
---

**Wednesday, July 8, 2026 · CHDR · Led by Anastasia Salter, with Sarah Norris and Mel Stanfill**

Workshop 5 landed two days before UCF's syllabus deadline, and the room felt it. The session ran in three movements. Sarah Norris opened with a librarian's tour of where to find data for AI-assisted projects, from library databases and special collections to government sources. Mel Stanfill followed with a walkthrough of their research scrapers, small AI-built tools for studying tagging on the Archive of Our Own, presented as a model of iteration as method. Anastasia Salter then took the room into Claude Code Desktop with the Superpowers plugin, building a cozy Linux-terminal teaching game live with the room's input, and screened a pre-recorded demo of the session's most audacious workflow: rebuilding an entire Canvas course, Simple Syllabus and all, without ever touching the Canvas interface. The closing turn to AI policy, run against UCF's own preset syllabus statements, gave the whole session its theme: the gap between what agentic AI makes possible for humanities students and all the ways institutions discourage anyone from learning it.

[← Back to Week 9](week-09.md)

## Sarah Norris: what counts as data

Norris opened with a disclaimer that doubled as a thesis about library expertise: "I am not a data expert, but I am a librarian." Her core invitation was to think expansively about sources.

> "Lots of things can be the data points that you need for the research that you're doing."

Archival documents, photographs, secondary sources, even the metadata and abstracts inside library database records can feed an AI-assisted project, and the library's databases go well beyond journal articles. The rapid tour hit Sage Research Methods for openly licensed datasets, SimplyAnalytics for demographic mapping (demonstrated on Orlando), the digital collections of the Library of Congress, DPLA, National Archives, and Smithsonian, UCF's own special collections and the STARS institutional repository, open data repositories (Dryad, Figshare, Zenodo, Harvard Dataverse, and Re3data as "a data repository of other data repositories"), and government data, which she praised with a wry caveat about the present: it's free, largely public domain, longitudinal, and valuable across disciplines, "if the sites exist and work correctly."

![SimplyAnalytics mapping interface showing demographic data categories and a color-coded map of educational attainment by zip code around Orlando]({{ '/assets/recaps/w09/01-simplyanalytics.jpg' | relative_url }})

Her sample scenario stitched it together: 1950s Florida tourism research combining digitized special collections, open Library of Congress photographs, and historical newspapers, with Claude identifying recurring themes and drafting metadata. Along the way she pointed the cohort to the library's subject specialists, including government information librarian Rich Gause, and closed with the standing offer:

> "Don't just use it for articles. We have lots of other things we can help with, too."

## Mel Stanfill: iteration is the method

Stanfill's section marked the week's shift: "we're starting to move into building things that run." Their examples were the scrapers behind their current research on the Archive of Our Own, built in conversation with Claude for a book chapter on tagging. The framing mattered as much as the tools: "these are small tools for myself, for my own research," published openly on GitHub but never intended as general-purpose software.

The workflow starts from what already exists. Since open source code is open, an existing scraper can become the model.

> "If I know there's already a scraper out there that in some way extracts data from the platform, I can point Claude to it as an example."

Their tag crawler descends from their own earlier metadata scraper, which in turn built on an open-source AO3 scraper from a Berkeley research group, revised because anti-AI-scraping architecture now demands a gentler touch: "It needed to act more human," slower and more polite to the servers. The result took 31 hours to collect metadata for 20,000 stories, a hundred for each of the 200 most-used tags. Analysis followed the same conversational pattern: Claude's own network visualizations proved "really, deeply ugly" (Gephi-ready exports fixed that), but co-occurrence heatmaps across ratings, fandoms, and warnings delivered. The key epistemological point drew a clean line around trust:

> "It didn't generate the things. It wrote the scripts. So I don't have to trust it to be right in how it does the analysis. I just have to trust that it wrote software well. That's a different thing to check."

![Slide titled Heatmaps: tags by ratings and tags by tags, showing two co-occurrence heatmap visualizations from the AO3 tag crawler beside the prompts that requested them]({{ '/assets/recaps/w09/02-ao3-heatmaps.jpg' | relative_url }})

Stanfill was frank about the labor economics underneath: "when there used to be grant money, and I used to be able to hire students, I would have hired them to write these scrapers." In its absence, an assistant that tolerates endless revision has its virtues: you can go back and forth "in a way that a human collaborator might want to strangle you. Claude doesn't care." The project folder told the story, five versions of the scraper, nine of the visualizer, error logs and CSVs piling up alongside Jupyter notebooks (their preferred interface: "I am not comfortable in the command line. I have never been comfortable in the command line").

> "Nothing was right the first time. And that's not failure. That's the workflow."

![Slide titled Iteration is the method, listing dozens of versioned scraper, visualizer, and analysis files in the tag crawler project folder]({{ '/assets/recaps/w09/03-iteration-method.jpg' | relative_url }})

## The refusal question

A question about students who refuse AI entirely, in a discipline where colleagues might back them, opened the session's liveliest exchange. The short answer from the front of the room: good luck finding software that wasn't made with AI, from Bluesky to Facebook to Google. Salter pushed the point into the territory of environmental ethics, comparing AI refusal to selective consumption politics: the student objecting on environmental grounds is rarely also a vegan who doesn't drive, streaming and gaming have data-center costs too, and the almond milk in the vegan's fridge has a staggering water footprint.

> "Because AI is so easy to object to, it's very easy for people to create this ethical sense and this sense of the performance of virtue by avoiding it specifically. And making people more aware of how performative that is is, I think, part of our job."

Their own syllabus takes the direct route: AI use is required, and one of UCF's own preset policy options now backs that up. For faculty being told by leadership to offer alternative assignments while also teaching AI, they had sympathy and no illusions: "that tension is not tenable... It sets up individual faculty to be the scapegoat." A participant question about keeping up with the pace of change drew the digital humanities answer: this has always been the field's condition, courses built on Twitter scrapers died with Twitter, and the trick is finding your discipline's people ("if you're in history, just following Dan Cohen's discussions of what he's up to in AI will keep you well in the loop"). On whether AI literacy is extra uncompensated labor:

> "It's no more that than knowing how to use Webcourses or Zoom is... Every single person who teaches at this university has to do all of the things that used to just be the digital humanities weirdos."

## Building Shelf Life, live

The build half moved to Claude Code Desktop paired with GitHub Desktop, "a back and forth walkie-talkie" between the folder on your computer and the web. After creating a local repository (LinuxGame, named by the room), Salter toured the Customize panel, skills, connectors, and the plugin that anchors this stage of the series: Superpowers, "an additional core library that Anthropic has endorsed for dealing with complex projects" that bakes brainstorming, planning, and design documents into the workflow. (Several participants' installs refused to cooperate, an inconsistency Salter diagnosed cheerfully as life with a GUI the developers barely prioritize: the command line remains "the answer to fixing it.")

![Claude Code Desktop plugins panel showing the Superpowers plugin alongside Anthropic plugins for productivity, commit commands, and code review]({{ '/assets/recaps/w09/04-superpowers-plugins.jpg' | relative_url }})

The modes got plain-language definitions: manual permissions is "the exhausting I-would-like-to-watch-everything-you-do-over-your-shoulder mode," plan mode is where every project should start, and auto mode is "a slightly safer version of YOLO." The prompt was assembled from the room's shouted specifications: a cozy game teaching the Linux terminal to total beginners, managing the inventory and customers of a magical bookstore, MIDI-style music, browser-playable for GitHub Pages deployment. Superpowers took over immediately, and the clarifying questions began: how many terminal skills (core navigation, plus searching, plus power tools), story days versus free play, how the bookstore fiction wraps the terminal.

![Claude Code Desktop in plan mode asking which Linux terminal skills the game should teach, with options ranging from core navigation to power tools]({{ '/assets/recaps/w09/05-planmode-questions.jpg' | relative_url }})

One thing the planner will never do is push back on the premise, which became a teaching point about workshopping ideas with peers before bringing them to the machine.

> "It will not tell you ever that your idea for a game is terrible... Claude will just think whatever you've decided is the bestest thing. And that's the sycophantic problem of AI."

The pedagogical frame: even for classes where students won't or can't use AI hands-on, an instructor can run exactly this exercise live, with the whole class answering the clarifying questions and critiquing the playable result. It is also a window into personal software, custom tools for purposes no product serves, from board-game collection organizers to whatever your course needs next. The room voted on names (Shelf Life beat Tome Keeper, Paw and Prompt, and Grip and Grimoire), the plan came back with a virtual file system and curriculum sketch, and Salter accepted it in auto mode with a single word: "YOLO."

![Claude Code Desktop building the game, with a local browser preview showing the Shellf Life terminal sandbox: a simulated bookshelf file system where cat and grep commands read cozy book files]({{ '/assets/recaps/w09/06-shellflife-localhost.jpg' | relative_url }})

## The power tool: a Canvas course without Canvas

While the game built in the background, Salter screened the pre-recorded centerpiece: how they handled the July 10 syllabus deadline. The demo started from an empty Webcourses shell the Friday before and a personal rule about where AI belongs in academic labor.

> "I won't use AI for grading at all. I don't use it for student feedback. I don't put student work in AI. But if I see a task that involves my work and content that I can make easier in any possible way, I will use AI to do that."

The workflow ran through Claude Code on the command line, with an on-ramp anyone can use: open the repository in GitHub Desktop, choose Open in Command Prompt, and "the only terminal command you ever have to use is claude." The prompt asked for a Fall 2026 rebuild of their AI course: a Ghost in the Shell aesthetic refresh, the recalibrated Thanksgiving week, a full review of the 2025 materials for broken links and outdated references (it duly flagged the unit built around the now-shuttered Sora), and deployment both to GitHub and to Canvas. Superpowers picked the project up, did its own web research on the UCF academic calendar, and asked fourteen clarifying questions.

> "I do all the thinking in my course planning. All of those exercises are already written... I don't need to check that every single link still works. I can let an agent do that."

![UCF Webcourses Canvas view of the rebuilt course, with weekly Ghost-themed modules, discussions, video lecture pages, and scheduled unlock dates all generated by the agent]({{ '/assets/recaps/w09/07-canvas-course.jpg' | relative_url }})

The Canvas half rode the API ("the way developers actually work with it... happens through code"), authorized by an access token that Salter set to expire the next day. The showstopper was Simple Syllabus, which the API cannot reach: Claude confirmed the limitation, then proposed and executed a workaround, generating the required content and filling in the entire form itself through the Claude for Chrome browser extension, in a browser window Salter had logged in personally.

> "And it did. This is just the sort of thing that brings me sheer joy. And when people say they completely hate AI, I'm like, but have you ever had Claude do your Simple Syllabus? It's a high."

![Simple Syllabus editor in Webcourses showing course policy fields fully filled in with formatted text, as completed by the browser extension]({{ '/assets/recaps/w09/08-simple-syllabus-filled.jpg' | relative_url }})

The result: slides embedded in every module ("without ever using PowerPoint again, which is a life goal of mine that I'm finally achieving"), accessibility handled by a skill loaded with UCF's guidelines, and a standing pipeline where edits to the markdown propagate to both the public site and Canvas. "I have not edited this course myself at all. I have not touched this Canvas interface. I will use it for grading and literally nothing else. Probably."

## The policy problem, again

The syllabus deadline made the AI policy segment unavoidable, and Salter ran it against UCF's own preset options in Simple Syllabus. The assignment-by-assignment and required options both lean on citation formats built for a chatbot age, complete with dated Copilot examples, which drew the session's sharpest methodological objection, credited to a comparison Ted Underwood has made to the era when people imagined citing every Google search: a non-deterministic system cannot be re-queried for the same output.

> "If the point of a citation is to have a reproducible sense of where something came from, that ain't it."

The prohibition option fared worse, since generative AI is already inside the library databases, the search engines, and the word processors: a policy "that cannot be followed or enforced" offered as a model. Salter's own policy, typed into the Other box (missing S and all), runs two sentences.

> "This course engages with AI as both an object of study and as a method of study in the humanities. Every assignment will engage with AI through different modalities and lenses, with instructions on how to document or reflect that engagement."

![Simple Syllabus AI policy options, showing UCF's preset statements for required, permitted-with-disclosure, and prohibited AI use, with a custom two-sentence policy typed into the final option and selected]({{ '/assets/recaps/w09/09-ai-policy-presets.jpg' | relative_url }})

The discussion ranged into the hard parts a syllabus paragraph cannot fix. Accessibility: Salter spoke from personal experience about voice-to-text now doing much of their writing because typing is painful, and a participant added that telling students they cannot use AI-based accessibility tools can run into the ADA. Equity: "the kid paying for a Max subscription and using Fable is going to make a better game than the student who doesn't... but may not necessarily have a better game idea." Labor: some assignments now require agentic tools simply to be buildable at the scale and timeline asked. For the participant facing four syllabi in 48 hours, the advice was triage: teach three courses the same as ever, "but on course number four, I'm going to take a step towards thinking about, okay, what can my students do to start to create meaning in conversation with this type of tool." And framing throughout: invitation over prohibition, "which has literally never worked."

## Shellf Life, deployed

The game finished during the policy discussion, interrupting it with delight ("oh my god, it's gotten so much cuter! There's a cookbook shelf!"). Published through GitHub Desktop's big blue button and deployed to Pages, *Shellf Life* turned out to be a fully realized cozy bookshop: story days, a hedgehog customer named Bramble, a music toggle, and a feline guide named Marginalia who teaches ls, cd, cat, and grep as spells for finding books, complete with gentle corrections for typos.

![The deployed Shellf Life game in a browser: an illustrated cozy bookshop with fantasy, mystery, and cookbook shelves, a cat sleeping on the counter, and a terminal pane where Marginalia the cat guides the player through cd commands]({{ '/assets/recaps/w09/10-shellflife-live.jpg' | relative_url }})

Salter's play-testing method doubles as the whole session's workflow in miniature: open a notepad, dictate observations while playing, paste the notes to Claude Code, iterate. The closing pitch connected the play to the stakes.

> "You can make games for every week of your course if you were so ambitious."

> "The goal was to highlight this tension between all the things that agentic AI makes more possible for humanities and arts students, and all of the ways we're discouraging them from learning it."

And, in the spirit of a session that opened with a syllabus deadline and closed with a hedgehog: "I love to end these sessions with things I have no fixes for."

## Try It Yourself

Missed the session, or ready to build? The Week 9 page has both halves of the core exercise: install the Superpowers plugin in Claude Code Desktop, create a local repository in GitHub Desktop, and use plan mode to build a small game or playful tool from a concept in your course, deployed to GitHub Pages; then draft a one-page course AI policy framed as an invitation rather than a fence. See the [Core Exercise on the Week 9 page](week-09.md#core-exercise) to try it yourself.

---

*Quotes are drawn from the session transcript, lightly edited to remove filler words and false starts, and to correct obvious automatic-captioning errors (for example "Marshallia," "Martinelli," and "Marcelia" → Marginalia, "clot" → claude, "a Mac subscription" → a Max subscription, "web courses" → Webcourses, and "Cloud Code" and "Quad Code" → Claude Code) to the words the speaker actually said. Participant comments are paraphrased without attribution.*
