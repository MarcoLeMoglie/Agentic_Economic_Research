# Lesson 2 speaker notes

Spoken notes for the 36 content slides. Minutes are a guide for a two-hour class, with about 25 minutes held for the live demo. Do not read the slide aloud. The transition line is the bridge to the next slide.

## Slide 1. Meet JARVIS (1.5 min)

JARVIS is the name the films give to Stark's assistant: Just A Rather Very Intelligent System. In the workshop he already knows which suit was built last week, he can reach the tools, and he acts on the armour rather than stopping at an answer. Use him as a direction, not as a product.

No current system holds a whole research life in its head and also moves the files. The question on the slide is the one the rest of the lesson answers. Say that the frame is a stand-in: there is no film still in the deck, because a still from Iron Man (2008) would need a redistribution licence before it goes into a repository. The metaphor stays. What we want is an assistant that returns to the same project and finds the work where the last session left it.

Transition: What exactly would we need?

## Slide 2. What makes JARVIS different from a chatbot? (2 min)

Walk the four boxes and tie each one to a word from Lesson 1. Remembers is files plus a context window, not a model that learned the student. Reaches tools is the tool list and MCP. Knows the setting is the rules file and the project folder you opened.

Acts is a permission to write, followed by a report of what changed. A chatbot can do a piece of each of these inside one tab. It does not keep the project. When the tab closes, the workshop is empty again. The takeaway is the line to leave on screen for a moment: a chatbot answers a message; this kind of assistant keeps working on the same project.

Transition: Three of the four exist today.

## Slide 3. Can we build it today? (2.5 min)

The left box is Lesson 1's chatbot: a model and a window. The middle box is Lesson 1's agent: a harness and tools, so it can edit files, and then the session ends and the memory ends with it. The right box is this lesson. The agent reads a small set of files at the start, so the new session begins where the last one stopped.

The feasible column is what students can set up this term: read and write project files, call tools, reload rules, load a procedure only when the task needs it. The missing column is the part people skip. Nothing is stored unless someone writes it. The agent does not know which sentence is worth keeping. A wrong note is read again next week with the same confidence. Point at Anthropic's context-engineering note for the idea that the window is assembled, not remembered.

Transition: What goes wrong without it.

## Slide 4. The problem with ordinary chatbots (2 min)

The left column is an illustration, and the slide says so. It is a six-month paper told as five failures, not as someone's log. Week 2, the sample is explained again. Week 5, the agent clusters by province after the decision was municipality.

Week 9, a new chat, and the reason 2020 was dropped is gone. Week 14, two chats, two outlier rules. Week 20, the coauthor's instructions are in a thread that cannot be found. The right column is the bill for each failure: tokens, a decision made twice, a slow restart, contradictory outputs, and no place to check.

The line to land is that a chat log records what was said. It is a poor record of what was decided. Decisions are short. Logs are long.

Transition: So what should be kept?

## Slide 5. Persistent memory (2 min)

Read the table as a filing rule, not as a software feature. State is where the project stands today. Decisions are the choice, the date, and the reason. Constraints are what must not change.

Sources are where a number came from. Solved errors are the bug and the fix that worked, so the next session does not rediscover it. Next actions are the first thing to do, not a wish list. Procedures are steps you repeat, written once.

Then separate three things students mix up. Chat history is everything said, in order, mostly noise. A document archive is the evidence: papers, data, drafts. Persistent memory is the short file you would hand a coauthor who joins tomorrow. If a sentence would not help that coauthor, it does not belong in the memory file.

Transition: And that file should not live inside one vendor's app.

## Slide 6. Own your knowledge, not your model (2 min)

The diagram is the portability claim. One Markdown folder, five harnesses, including one that does not exist yet. Plain text is the part that moves.

An agent that can open a folder can read an index, a state file, a decision, and a skill. Changing provider does not move that memory, because the memory was not stored inside the provider. The less portable list is the setup you repeat: the rules file has a different name in each harness, AGENTS.md or CLAUDE.md or a Cursor rule, and MCP servers are configured again. Memory that lives only inside a vendor's app stays with the vendor. Say that the course vault uses AGENTS.md because more than one harness reads it.

Transition: Which is why a new session can be cheap.

## Slide 7. New session, same knowledge (2.5 min)

This is a reminder of Lesson 1, not a new lecture. The left panel is one long chat. Early decisions sit far back. A compaction summary replaces old turns and drops detail.

As the window fills, the model attends less well to the middle. Chroma's 2025 note on context rot is the citation for that decay, and it is the same source Lesson 1 used. The right panel is a fresh session that loads four small blocks: the rules file, the index, the state, and the next actions. Most of the window stays free for the task.

A fresh session helps when the chat has wandered. It helps only if the closeout wrote the decision down. Anything the closeout skipped is gone. The cost of a new session is low when the files are current, and high when they are not.

Transition: Loading less also changes the bill.

## Slide 8. Fewer tokens, better context (2.5 min)

The bars are an illustration. One hundred thousand tokens against eight thousand is a 92 percent cut for that one request. Say the label out loud: these are not a measured benchmark. They show the shape of the saving when the agent loads the files the task needs and leaves the rest on disk.

The table is five ways that happens. Progressive disclosure shows a name and a description first, and the full text only if the task matches. Selective loading opens one project. Retrieval fetches a few passages.

Prompt caching discounts a prefix that repeats. Compaction replaces old turns with a summary. Then the warning under the table: a cheaper request is not a cheaper project. Writing the notes, building an index, and keeping both current also spend tokens and time. The saving is in the requests you will make again.

Transition: Skills are the same idea, applied to procedures.

## Slide 9. Portable skills (2 min)

Open the file box. It is the real front matter of the lecture skill that checks the synthetic panel, not a mock. At the start of a session the agent sees the name and the description, a few dozen tokens, for every skill in the folder. When a request matches, it reads the full SKILL.md.

Scripts and templates load only if a step calls them. The same folder works in any harness that follows the Agent Skills format, which is why the lecture vault keeps a copy under the project and a discovery copy where the harness looks. The muted line is the part students miss. Pasting a folder of procedures into every prompt saves nothing. The saving is the staging: most skills stay as a name until one of them is needed.

Transition: Put the pieces on one research project.

## Slide 10. From chatbot to research assistant (2 min)

This chain is the synthetic project the demo will open. Read it as a file map. The hypothesis, the estimator, the panel, the script, the labelled result, and the clustering decision each live in a file the agent can open. Callaway and Sant'Anna is the estimator named in the design note.

The 0.031 figure is a lecture line. It is not estimated from the CSV, and the slide says so. The coauthor rules are constraints: do not edit raw data, and build tables only through the script that owns them.

The real case on the right is from the mafia-culture state file, 18 October 2026. It records that 1,949 rows are the old artist universe, not 1,949 verified narcocorrido artists. An agent that reads the file does not report the wrong count. That is cumulative knowledge: each session starts from the last verified state and is supposed to leave a new one.

Transition: How people have tried to store that knowledge.

## Slide 11. A short history of external memory (2.5 min)

Do not narrate every node. The point is that external memory is old, and the 2026 design stacks older ideas. Bush's 1945 Memex is a desk that stores one person's records and links them. Personal knowledge management, through the 1990s and 2000s, is notes, folders, and tags.

Forte's 2022 book names two schemes students may already use: CODE for the flow of a note, and PARA for the folders. Wikis and knowledge bases are curated pages. Vector search finds by meaning. Lewis and coauthors, 2020, retrieve passages and then generate.

Edge and coauthors, 2024, build a graph of entities and summarise by community. Karpathy's 2026 gist has the model write the wiki and keep it. These layers coexist. A system this year often uses three of them at once. Say that the next slides take the designs one at a time, including the one that is only a long prompt.

Transition: Start with the design that has no machinery.

## Slide 12. Everything in the prompt (2 min)

This is the design with no index. You put the files in the prompt. The model reads the author's words, and there is nothing to maintain. It works while the material fits comfortably in the window, which for one paper it often does.

The limits are the reason it does not scale to a research agenda. The window caps the corpus. Every request pays for every token, including the pages that were irrelevant. Those pages also dilute attention.

And every update means sending the whole pile again, because nothing was stored between calls. The takeaway is the scope. Fine for one paper. Not for a stack of projects, a year of decisions, and the procedures that repeat. The later designs exist because this one stops being cheap and stops being accurate as the folder grows.

Transition: The usual next step is to retrieve a few passages.

## Slide 13. Retrieval-augmented generation (3 min)

Walk the six boxes left to right, slowly. Documents are split into chunks, the chunks are indexed by keywords or by embeddings, a question retrieves the top k, and the model reads the question together with those passages and writes an answer that is supposed to cite them. Then the three retrieval styles. Lexical search, BM25 in Robertson and Zaragoza's 2009 survey, matches words.

It is the right tool for a variable name, a statute number, a municipality code. Semantic search matches a paraphrase, and it misses the exact string. Hybrid runs both and merges the ranks. The failure table is what to say when a student trusts the answer because it has a citation. The chunk boundary cut the sentence.

The right paper did not enter the top k. The answer needed ten passages and k was five. Or the model wrote past what the passages say. Retrieval reduces the pile. The synthesis still has to be checked.

Transition: A wiki tries to do the synthesis once.

## Slide 14. Knowledge bases, wikis and GraphRAG (2.5 min)

The chain at the top is a typed relation, which is the new object. A paper uses a method, the method was estimated on a dataset, the dataset is implemented in code, the code produces a table, the table reports a result. A folder of files does not say that. A link says two notes are related.

A typed edge says how. The table then separates words students use as synonyms. A repository is files. A wiki is pages written for a reader and linked by hand. A knowledge base is those pages after review.

A link graph is which page points at which. A knowledge graph adds the types. GraphRAG, Edge and coauthors 2024, extracts such a graph from text and retrieves over communities of nodes, which helps questions that no single passage answers. The question to leave up: which results depend on this dataset? A folder cannot answer it without a person rereading.

Transition: Karpathy's version asks the model to keep that wiki current.

## Slide 15. Andrej Karpathy's LLM Wiki (2.5 min)

The figure is a reading of the gist dated 4 April 2026, not a film of the page. The gist itself is the source, and the URL is in the references. Karpathy separates three layers, and the slide uses his names. Raw sources are the papers and notes.

The model reads them and does not edit them. The wiki is Markdown the model writes and updates: summaries, entities, concepts, links. The schema is a rules file, CLAUDE.md or AGENTS.md, that says how the wiki is organised and what to do when a source arrives.

The human picks the sources and asks the questions. The model does the bookkeeping that usually makes a person abandon a wiki: the cross-reference, the updated summary, the note that a new paper conflicts with an old one. Say that this is a pattern, not a product. The gist tells you to hand it to your own agent and work out the folders together.

Transition: He also names the three operations.

## Slide 16. Ingest, query, lint (2.5 min)

Three operations, and one extra that matters for research. Ingest reads one new source, writes its summary, updates every page the source touches, and logs the change. Query asks the wiki rather than the raw pile, and a good answer can be filed back as a page so the exploration is not lost in a chat.

Lint looks for contradictions, stale claims, orphan pages, missing links, and concepts that are mentioned but have no page. The orange band is promotion. A result that was checked in a session should leave the chat and become a page, a decision, or a skill. The five edits on the right are one paper arriving: a new summary, an estimator added to the staggered DiD page, an estimate on an entity page, a conflict flagged under open questions, and two new rows on the index. That is the maintenance a person skips and then blames the wiki for being stale.

Transition: You will want both the wiki and the original passage.

## Slide 17. Hybrid RAG + LLM Wiki (2 min)

Draw the split with a hand if you are standing near the screen. Raw sources feed two stores. Retrieval holds exact passages, quotes, and numbers. The wiki holds the synthesis, the decisions, and the links.

The agent uses both, then a validation step checks the claim against the source or reruns the code, and only then does a memory update write back to the wiki. The arrow returns because the wiki is an output, not only an input. The sentence to say twice: the wiki answers what we know and what we decided. Retrieval answers where the source says it.

The takeaway is a publishing rule. Orient with the wiki. Go back to the source for any number that will appear in a paper. A wiki page is not a citation.

Transition: Put the designs in one table, then look at firms.

## Slide 18. Comparing architectures, and firms (2 min)

The table is qualitative, and the muted line says the author made it. Do not let a student read a cell as a benchmark. Full prompt has no setup and no reuse. RAG needs an index and is only as good as the chunks.

A knowledge base is slow to build and strong on the topics someone reviewed. GraphRAG spends many tokens on extraction and helps global questions, with provenance that is one step removed from the page. An LLM wiki is a folder plus a schema, maintained at each ingest, and it reuses well if the links back to raw sources stay honest. Hybrid costs the most to maintain and, if it is maintained, covers both the synthesis and the passage.

Then the firms, briefly. Glean and Microsoft 365 Copilot index company documents and answer inside the permissions the user already has. Meta has described an internal organisational second brain. The hard part in a firm is the same as in a lab: who may see what, a stale page that looks official, and a memory that outlives the reason it was written.

Transition: We are going to build the small version, on a laptop.

## Slide 19. Why Obsidian? (2 min)

Obsidian is a reader for a folder. The figure is that folder, drawn from the lecture vault on disk, because the app on this machine stayed on its plugin-loading screen when the slides were built. Say that plainly if a student asks why the picture is not the app chrome. The files are the same files the app would open.

The table is the reason to use it rather than a notes product. The vault is a folder. Markdown is plain text, so the notes survive the app. Files stay on the machine unless you sync them.

A plugin is code you chose to run, with access to those files. Any agent that can open the folder reads the same notes the human reads. That last row is the point of the lesson. The second brain is not the app. The app is one way to look at the folder.

Transition: What the folder should contain.

## Slide 20. Vaults, folders and Markdown (2 min)

One folder per project, and the same file names in every project, so an agent does not have to guess whether today's state is called status, notes, or current. An index at each level says what is here and what to read first. The front matter on the slide is the real header of the transit-jobs state file: type, project, updated, status. A program can read those fields without understanding the prose.

Obsidian shows the same fields as Properties. That is the whole trick of plain text. The human edits a note.

A script checks a date. An agent reads both. If the class is in Obsidian, toggle Properties on this file and show that the YAML and the panel are one thing. If the app is not open, the file box is enough.

Transition: How notes point at each other.

## Slide 21. Links, backlinks and graph view (2.5 min)

The picture is the real graph view of my vault in July 2026, with node labels off. Colours are folders. It is there to show density, not to be read. A wikilink is typed as a double bracket around a note name.

A backlink is the list, on each note, of the notes that point at it. Both are useful, and both are weaker than they look. A link says the notes are related. It does not say whether one uses the other, was estimated on the other, or contradicts the other.

That is the distinction from the GraphRAG slide, brought back as a limit. The graph view is a map for the human. The agent still needs the sentence in the note. Do not let the picture become the argument. The argument is the link type you did not write down.

Transition: A board, for the argument that is not a list.

## Slide 22. Obsidian Canvas and plugins (2 min)

The figure is the real canvas file in the lecture vault, paper-map.canvas, drawn from the JSON. Five cards: the question, the data, the design, the simulated result, and the open issue about the 2008 placebo. Canvas saves a board of cards and arrows as a file in the vault, so it is not trapped in the app. Cards can be notes, text, or images.

The JSON Canvas spec is the format. Then three core plugins worth turning on, and no others at the start. Templates give the same skeleton to each new note. Properties make front matter editable.

Backlinks show who points here. The muted line is the warning. A community plugin is third-party code with access to the vault. Install one when you need it, and know what it can read.

Transition: The smallest vault that is already useful.

## Slide 23. Build your first brain (2.5 min)

Six files, and then stop. A README says what the vault is, for the human and for the agent. general/INDEX.md is the map and the first file to read. PROJECT_BRIEF changes rarely: the question, the scope, the people.

CURRENT_STATE is where things stand today, and it is allowed to be rewritten often. NEXT_ACTIONS is the next three things, not a backlog. DECISIONS is the date, the decision, and the reason. The tree on the slide is the shape, not a requirement to create every folder tonight.

The takeaway is a discipline. Six files are enough for the first month. Add a file when one of these gets too long to read at the start of a session. A vault that begins with thirty templates is a vault nobody updates.

Transition: Then let an agent see the folder.

## Slide 24. Connect an AI agent (3 min)

Six links between the agent and the vault, and each one is a rule you can check. Folder access means the vault is the workspace, or an extra folder the harness is allowed to read. Permissions: read freely, ask before writing, and do not touch paths outside the vault. The instructions file at the root points at the bootstrap, so every harness that reads AGENTS.md gets the same opening.

Bootstrap means read the index, then only the project the human named. Canonical memory is the Markdown. A chat memory, a vector index, a plugin cache: if they disagree with the file, the file wins.

Controlled writes mean the agent proposes an edit and Git shows the diff before it becomes the record. The definition on the slide is the sentence to repeat. Reading is not remembering. The agent remembers only what someone wrote back into the files.

Transition: You can also ask the agent to create the folder.

## Slide 25. Let AI build your brain (2.5 min)

The flow is a sequence with a stop in it. You state the requirements. The agent proposes a design. It creates the vault only after you accept the tree.

You read what it wrote. You iterate. The file box is the prompt, and it is written to be copied. A PhD student in economics, a vault under Documents, one folder per project, four files inside each, an index, an AGENTS.md, a bootstrap, a session close. The last sentences are the control: do not invent content, leave placeholders, show the tree, and wait before writing any file.

Students will drop that last sentence and then spend an hour undoing plausible paragraphs. The takeaway is the order. Ask for the tree first. Then read what it wrote. A design you did not read is a design you will not maintain.

Transition: Once the files exist, they need a history.

## Slide 26. Git, GitHub and Obsidian (2.5 min)

The two panels are the terminal, not the Obsidian Git plugin. The left is git log of the lecture vault, including the audit commit on the branch final-verified. The right is the diff of the decisions file after that audit. Dropbox syncs a file across machines and keeps versions, without a message that says why the file changed.

Git records the change, the message, the diff, and a way back. GitHub hosts the repository. Notes about people and projects should be in a private repository. Obsidian Git is a plugin that commits and pushes from inside the app, if you want that later.

The muted line covers two practical failures. A gitignore keeps secrets, caches, and large data out of the history. Two machines editing the same note produce a conflict a person has to resolve. Git does not remove that conflict. It shows it.

Transition: This is the shape I actually use.

## Slide 27. My brain architecture (2 min)

The tree was checked against the live folder on 1 November 2026, and it leaves out credential files and private project names that do not help the class. Markdown under general and areas is the source of truth. Tools, the graph, and the local memory server are support. When they disagree, the file wins.

The vault has lived on Dropbox since 3 October 2026. New projects come from one script, create_project.py, so the file names match. general holds the rules, the routing table, the skills, and the templates.

areas holds the work, split into Research, Grant, Teaching, Tesi, and Other. The hidden infra folder holds scripts and the prose tools. An agent is told to read general and areas. It is not told to browse infra for the content of a project.

Transition: How many projects that is.

## Slide 28. One brain, many projects (2 min)

The counts were taken from general/MEMORY.md on 1 November 2026. Research 15, Other 11, Teaching 2, Grant 2, Tesi 1. The accent line names a few so the boxes are not anonymous: mafia-culture, mafia-incendi, and fragmented-opposition under Research, brain-management under Other, AI_course under Teaching. The file box is three real rows of the routing table, with the links shortened so the slide can be read.

Each row points at the index, the state, the agent memory, and the decisions for that project. The agent opens one row. It does not open thirty projects and hope the relevant paragraph is in the window. That is selective loading from the earlier slide, applied to a real vault. If a project is missing from the table, the bootstrap will not find it, which is why a new project has to add its row.

Transition: What is inside one of those rows.

## Slide 29. Anatomy of a project (2 min)

Four files at every start: the index, the state, the next actions, and the agent memory. The agent memory is the short note for the next agent, including the mistakes not to repeat. The second group is read when the task needs it. The brief is the question and the scope.

Decisions carry the date, the context, the choice, and the reason. Technical notes hold commands, bugs, and fixes. Sources say where a fact came from. The third group is history. The log is what happened, by date.

Session summaries are one paragraph. Prompts worth reusing have a place, so a good prompt is not trapped in a chat. The file box is a real decision from fragmented opposition, 5 June 2026: a recovery procedure left the chat and became a global skill. Separate files, separate jobs. The agent reads four short files instead of one long one.

Transition: The tools around those files.

## Slide 30. My tool stack (2 min)

Read the status column, because it is the honest part. Obsidian and Markdown are in daily use. The local memory server, Memanto, was online on this machine on 1 November 2026. Caveman is active in this course workspace.

The writing tools on the next rows are in use, including the checks that were run on these notes. The Sunday review ran on 11, 18, and 25 October. The other rows are documented in the vault and were not started for this slide. Do not promote a documented tool into a tool you claim to have run. Mirage, the code graphs, Headroom, and Econoclast are in the table because they are part of the stack as written down, and the status cell says documented. A student who copies the table should copy the status cell too.

Transition: Where a repeated procedure went.

## Slide 31. Portable skills in my brain (2 min)

A skill that starts inside one project and turns out to be useful elsewhere is promoted. The Spotify pipeline is the example. It lives in the mafia-culture project, and a copy lives under general/capabilities/skills, so another project can find it without opening the music notes. Promotion is a copy plus an index row, not a move that breaks the project that still needs the original.

The lecture vault does the same thing at a smaller scale with the panel check. Discovery is a separate copy, because Codex and OpenCode look in a folder the project tree does not use. Say that two copies can drift. The maintenance job includes noticing when they do. A skill that only one project will ever need should stay in that project. Promotion is for the procedure you would explain to a different project.

Transition: How the wiki layer sits on top of this.

## Slide 32. My adaptation of the LLM Wiki (2.5 min)

Karpathy's pattern, with two local rules. The model patches the core files first: state, decisions, index, log. A wiki page is for a long document, not for a sentence that belongs in the decision file. Every wiki page has to appear in the index, under a Wiki heading, or it is invisible to the next session.

That rule is one of the defects the demo will find. The lecture vault has a wiki page that the index does not list. In the real vault the same rule is what the Sunday check looks for. Raw sources stay raw.

The model does not rewrite a paper in order to remember it. It writes a page that points back. If the page and the paper disagree, the paper wins and the page is fixed. The schema is the workflow file the bootstrap already told the agent to read.

Transition: What happens at the start and at the end of a session.

## Slide 33. Bootstrap and session close (2.5 min)

The bootstrap reports four things, and the file box is that instruction from the real file. What the project is, where it stands, what is blocked, and what to do next. It reads the index and then one project. It does not tour the vault.

The close is the other half, and it is the half people skip when they are tired. Update the state. If a decision was made, append it with the date and the reason. Append the log.

Set the next actions to what is actually next. A session that ends in the chat and not in the files did not happen, as far as the next agent is concerned. The four-thing report is also a check on the human. If the agent cannot say where the project stands, the state file is empty or wrong, and that is the thing to fix before the research question.

Transition: Files that are not maintained become a confident kind of wrong.

## Slide 34. A brain needs maintenance (2 min)

Five defects, all planted in the lecture vault, all ordinary. A wiki page is missing from the index. A wikilink points at a filename that does not exist. Two decisions contradict each other and the older one is not marked as superseded.

Two wiki pages overlap enough that a reader cannot tell which is current. A fact from a coauthor call sits in raw and did not reach the state file. These are ordinary failures.

They are what happens when the closeout is skipped. The next session can repeat them, because the file looks like a decision. Maintenance is the lint operation from Karpathy's gist, run on your own notes. The demo will ask an agent to list certain problems and possible problems separately, and to wait before editing.

Transition: What that looks like once a week.

## Slide 35. My Sunday maintenance (2.5 min)

The flow is the checklist, and the dates are three real runs, not a schedule drawn for the slide. On 11 October the 9:02 run failed because the Mac was offline. It was rerun later. On 18 October the vault had 1,031 Markdown files, 28 projects, 144 wiki pages, and 481 raw files.

The snapshot was 3b61096. Twenty-two files were deleted, each deletion listed. On 25 October the 8:57 run failed and the rerun was about 10:55. The vault had 939 Markdown files. The snapshot was 939fc3c.

Twenty-three Desktop paths were rewritten, and 19 files were deleted. The slide does not name the scheduler. It was a scheduled agent run. A failed run is part of the record. Say that a checklist which hides the failures is not a checklist. Two of the three runs needed a human to notice that the machine had been asleep.

Transition: What to copy, at a size that fits a term.

## Slide 36. Keeping your brain healthy (2 min)

Five habits, then stop. Write the decision on the day, with the reason. One project per session, so the bootstrap stays short. Promote a repeated procedure into a skill instead of pasting it into the next prompt. Run a lint on a schedule you will keep, and record the run that failed. Read the diff before you commit.

Hayek in 1945 argued that the knowledge that matters is local. Walsh and Ungson treat organisational memory as a store that can be wrong and still be used. Cohen and Levinthal's absorptive capacity is recognising which result is worth keeping. Garicano's hierarchy pushes the routine down and the exception up: the skill is the routine, the decision file is the exception.

Brynjolfsson, Li, and Raymond, Quarterly Journal of Economics 2025, find about a 15 percent gain for customer-support agents using a generative assistant, larger among the less experienced. The working-paper figure of 14 percent is the earlier number. The AEA data and code policy asks for a result someone else can rerun. A second brain that cannot show where a number came from fails that test. The demo is next. If it fails, the branch final-verified is the ending already prepared.

Transition: Open the lecture vault.

