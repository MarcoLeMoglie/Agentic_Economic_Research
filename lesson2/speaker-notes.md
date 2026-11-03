# Lesson 2 — Speaker notes (Italian)

36 main slides, ~80 minutes + 25-minute live demo.

Le schermate di interfaccia nel PDF sono ricostruzioni originali dimostrative, **non** screenshot verificati dell’app Obsidian.

## 01. Meet JARVIS
**Section:** The vision. **Source:** .

Aprire mostrando l’illustrazione originale ispirata ai laboratori di Iron Man. Non è un fotogramma del film: è una metafora visiva. Chiedere quanti vorrebbero un assistente che ricordi il progetto, conosca file e strumenti e sappia riprendere il lavoro. Anticipare che non stiamo riproducendo JARVIS, ma costruendo alcune sue capacità funzionali tramite memoria esterna, agenti e protocolli. Questa lezione è la seconda del corso Agentic AI for Economic Research e si concentra sull’infrastruttura di conoscenza. Tempo: 2 minuti.

## 02. Why JARVIS is not just a chatbot
**Section:** JARVIS: the vision. **Source:** Iron Man (fictional analogy); Anthropic, Building Effective Agents (2024).

Spiegare la differenza fra un chatbot che risponde e un assistente situato dentro un ambiente operativo. Le quattro funzioni sono memoria, strumenti, contesto e azione. L’azione deve essere vincolata ai permessi e idealmente osservabile. Sottolineare che la metafora cinematografica rischia di far sopravvalutare l’autonomia e l’affidabilità degli agenti: nessuna memoria esterna rende vera un’informazione errata. Tempo: 2 minuti.

## 03. Chatbot → agent → agent with a Brain
**Section:** JARVIS: the vision. **Source:** AI_course, Lesson 1 (published Oct 2026); Brain architecture current.

Riprendere il vocabolario della lezione 1: il modello produce testo e decisioni, l’harness gestisce strumenti e contesto, l’agente può eseguire un ciclo di lavoro. Il Second Brain fornisce gli stati e le decisioni che persistono. Distinguere chiaramente cartella canonica e memoria proprietaria del chatbot. Il messaggio è che si può cambiare il modello senza perdere la struttura della conoscenza. Tempo: 2 minuti.

## 04. The problem: every session starts over
**Section:** Why a Second Brain. **Source:** Long-context reliability research; Brain BOOTSTRAP / SESSION_CLOSE.

Utilizzare l’esempio di un paper con quattro coautori, diversi do-file, una revisione in corso e decisioni sull’identificazione prese due mesi fa. Un chat log può contenere tutto, ma il modello non necessariamente dispone dell’intero log e difficilmente ne estrae in modo affidabile ciò che serve. Il costo umano è ricostruire il contesto; il costo tecnico è fornire token irrilevanti. Tempo: 2 minuti.

## 05. What should the Brain remember?
**Section:** Why a Second Brain. **Source:** Brain general/agent/MEMORY_POLICY.md.

Una memoria utile separa ciò che è temporaneo da ciò che un agente futuro deve sapere. CURRENT_STATE risponde a dove siamo; DECISIONS risponde a perché abbiamo scelto una strada; SOURCES preserva evidenza; TECHNICAL_NOTES evita di ripetere lo stesso debugging. Contraddizioni e incertezze non devono essere cancellate. Evitare di conservare password e transcript integrali se non necessari. Tempo: 2 minuti.

## 06. Own your knowledge, not your model
**Section:** Why a Second Brain. **Source:** Brain general/capabilities/skills/INDEX.md; Agent Skills specification.

Il valore della portabilità è il controllo sui file, non la promessa che Claude, Codex e altri agenti facciano esattamente la stessa cosa. Mostrare il concetto di cartella Markdown unica, con piccoli adattatori per il caricamento delle istruzioni e delle skills. Ricordare che alcune integrazioni e interfacce sono specifiche di un prodotto e che i permessi devono essere riconfigurati. Tempo: 2 minuti.

## 07. New session, same project knowledge
**Section:** Why a Second Brain. **Source:** Brain BOOTSTRAP, SESSION_CLOSE; Anthropic context engineering.

Spiegare che la qualità di un contesto non coincide con la sua lunghezza. Quando una sessione è congestionata, un buon closeout permette un nuovo avvio. Il bootstrap non deve importare ogni file del vault ma deve leggere un indice e i core files del progetto. La qualità del riassunto resta essenziale: un fatto non registrato può andare perso. Tempo: 2 minuti.

## 08. Less context can mean fewer tokens
**Section:** Why a Second Brain. **Source:** Illustrative calculation; Anthropic context engineering; Meta Engineering (2026).

L’esempio numerico è illustrativo: 100.000 meno 8.000 diviso 100.000 dà 92%. Questi non sono dati misurati sul Brain dell’autore. È un confronto di input token per richiesta, non un modello totale dei costi; creare una wiki, aggiornarla e interrogare il retrieval ha un costo. Meta riferisce un risultato interno di circa 80% token per turno nel proprio sistema, che non va universalizzato. Tempo: 3 minuti.

## 09. Portable skills: instructions on demand
**Section:** Why a Second Brain. **Source:** agentskills.io/specification; AI_course Brain skills index.

Aprire la struttura di una skill: metadata YAML, corpo SKILL.md, eventuali scripts e references. Le specifiche Agent Skills utilizzano progressive disclosure: all’avvio il catalogo leggero, in seguito la skill attivata e le risorse pertinenti. La presenza di una skill nella cartella Brain non implica automaticamente discovery da qualunque AI. Mostrare la differenza tra fonte canonica e mirror nativo per l’agente. Tempo: 2 minuti.

## 10. From chatbot to research assistant
**Section:** Why a Second Brain. **Source:** AI_course; AEA Data and Code Availability Policy; Walsh and Ungson (1991).

Raccontare un ciclo di ricerca empirica reale: ipotesi, data collection, pulizia, scelta del metodo, revisione, output e replicabilità. La memoria consente a un agente successivo di sapere perché certe osservazioni sono state escluse o perché una specifica non è più usata. Il valore va valutato non solo come produttività ma come riduzione di errori ripetuti e miglior conservazione delle scelte. Tempo: 2 minuti.

## 11. A short history of external memory
**Section:** Architectures. **Source:** Bush (1945); Forte (2022); Lewis et al. (2020); Edge et al. (2024); Karpathy (2026).

Evitare una storia lineare fittizia. Bush ha posto il problema dell’associazione di documenti; Forte propone pratiche di raccolta e distillazione; RAG recupera contenuti; il grafo rappresenta relazioni; Karpathy invita a mantenere una wiki con LLM. Si tratta di livelli concettuali che possono coesistere. Tempo: 2 minuti.

## 12. Approach 1: put everything in the prompt
**Section:** Architectures. **Source:** Anthropic context engineering; Chroma context-rot evaluation (2025).

L’approccio monolitico consiste nel fornire tutti i documenti alla query. È una baseline utile per attività piccole, ma ha un costo continuo di input e spesso bassa densità informativa. Le finestre di contesto ampie non eliminano il rischio di sbagliare attenzione e priorità; quindi occorre progettare la selezione del contesto. Tempo: 2 minuti.

## 13. Approach 2: retrieval-augmented generation
**Section:** Architectures. **Source:** Lewis et al., NeurIPS 2020.

Spiegare tutti i passaggi RAG: acquisizione, parsing, chunking, indici, query, retrieval, risposta. È un sistema utile per grandi corpus, specialmente se dobbiamo citare documenti specifici. Ma se lo stesso confronto fra cinque studi viene richiesto dieci volte, il retrieval potrebbe ricostruirlo ripetutamente. Il problema non è intrinseco a ogni RAG avanzato: si può aggiungere memoria. Tempo: 3 minuti.

## 14. Knowledge bases, links and GraphRAG
**Section:** Architectures. **Source:** Edge et al. (2024); Obsidian Help (Graph View).

Distinguere i wikilink da relazioni formali. Un collegamento fra un paper e un dataset non esplicita se il dataset è usato, criticato o replicato. Un grafo tipizzato consente query più precise ma richiede disambiguazione e manutenzione. GraphRAG è un approccio specifico di recupero e sintesi su grafi, non un sinonimo di Graph View in Obsidian. Tempo: 2 minuti.

## 15. Karpathy: an LLM-maintained wiki
**Section:** Architectures. **Source:** Andrej Karpathy, LLM Wiki GitHub Gist (2026-04-04).

Presentare il gist pubblicato da Karpathy il 4 aprile 2026 come un pattern aperto, non un prodotto finito. Raw preserva le fonti, wiki conserva la conoscenza compilata, schema insegna agli agenti come aggiornare. Il punto decisivo è che un nuovo paper modifica le pagine già presenti invece di aggiungere soltanto un file isolato. Obsidian può fungere da interfaccia per vedere ciò che l’agente cambia. Tempo: 3 minuti.

## 16. LLM Wiki workflow: ingest, query, lint
**Section:** Architectures. **Source:** Karpathy (2026); Brain WIKI_WORKFLOW.md.

Illustrarne il ciclo con un paper di organizzazione industriale: ingest riassume le fonti e corregge pagine correlate; query confronta studi; lint cerca link morti e contraddizioni; promotion conserva una procedura ripetibile. Insistere sulla verifica delle fonti. Non attribuire a Karpathy una tassonomia rigida di cartelle oltre il principio che propone. Tempo: 2 minuti.

## 17. An effective hybrid: RAG + curated wiki
**Section:** Architectures. **Source:** Meta Engineering, Organizational Second Brain (2026); Brain architecture.

Mostrare la divisione delle responsabilità: wiki per conoscenza ad alta densità e uso frequente, retrieval per documenti situazionali e granulari. Meta spiega questa divisione in modo esplicito nell’articolo del settembre 2026. Per il lavoro scientifico occorre una fonte originale sempre recuperabile, perché una sintesi errata può propagarsi negli agenti futuri. Tempo: 2 minuti.

## 18. Which architecture should you choose?
**Section:** Architectures. **Source:** Lewis et al. (2020); Meta Engineering (2026); Microsoft and Glean docs.

Riassumere trade-off senza dichiarare un vincitore assoluto. In un’azienda sono centrali i permessi e la provenienza; in un gruppo accademico lo sono anche la replicabilità e la conservazione del razionale metodologico. Citare Meta come sistema più vicino alla compiled memory e Glean/Copilot come sistemi più orientati alla ricerca federata, pur esistendo molte sovrapposizioni. Tempo: 3 minuti.

## 19. Why Obsidian?
**Section:** Build it. **Source:** Obsidian Help; original course demo mock.

Precisa che la schermata è una ricostruzione grafica del vault demo, non uno screenshot di Obsidian autentico. Il punto sostanziale è che il vault è una cartella di file .md: possiamo leggerla con un editor, sincronizzarla, versionarla e darne accesso a un agente. Non occorrono necessariamente plugin complessi. Tempo: 2 minuti.

## 20. Vaults, folders and plain Markdown
**Section:** Build it. **Source:** Obsidian documentation; Brain general/INDEX.md.

Usare la gerarchia a sinistra per spiegare il ruolo del file explorer, l’indice e la differenza tra general e aree di lavoro. YAML frontmatter è opzionale e utile per metadati. Il modello di file non deve essere iperprogettato: anche quattro file ben mantenuti sono un ottimo inizio. Tempo: 2 minuti.

## 21. Links, backlinks and the Graph View
**Section:** Build it. **Source:** Obsidian Graph View documentation; original course illustration.

Il grafo didattico mostra un progetto connesso a decisioni, wiki, skill e fonti. La Graph View visualizza relazioni ipertestuali, non significa che le relazioni abbiano tipo e significato scientifico corretto. Usarla come strumento esplorativo, non sostituto degli indici e della provenance. Tempo: 2 minuti.

## 22. Canvas: think spatially
**Section:** Build it. **Source:** Obsidian Canvas documentation; original teaching reconstruction.

Canvas consente di disporre spazialmente domanda di ricerca, fonti, strategie e output, utile per un brainstorming o una mappa progettuale. Ma la decisione definitiva su una specifica o su una pipeline dovrebbe restare in un file di progetto chiaro e versionabile. Tempo: 2 minuti.

## 23. Your first Brain: four useful project files
**Section:** Build it. **Source:** Brain project template; course design recommendation.

Proporre una prima versione minimale per evitare che il pubblico percepisca il Brain come un sistema da decine di file. Un buon punto di partenza è un indice globale e quattro file per progetto. Come esercizio si può chiedere agli studenti di riprodurre il proprio lavoro accademico in questo formato. Tempo: 3 minuti.

## 24. Connect an AI agent safely
**Section:** Build it. **Source:** Brain BOOTSTRAP and MEMORY_POLICY; agent filesystem docs.

Distinguere un agente con permessi di lettura da uno con permessi di scrittura. Il bootstrap è un contratto di navigazione e comportamento. Il vault non cambia automaticamente soltanto perché un chatbot risponde: servono strumenti di filesystem e operazioni esplicite, soprattutto per le scritture. Mostrare il principio di minimo privilegio. Tempo: 2 minuti.

## 25. Let AI build the first version
**Section:** Build it. **Source:** Course-proposed workflow; Brain create_project.py conventions.

Raccontare come si può far generare all’AI una struttura iniziale completa, con template, istruzioni e script di validazione. L’agente può accelerare la parte meccanica ma l’utente deve approvare la gerarchia, la policy di memoria e soprattutto quali file possono essere modificati. Proporre una settimana di test prima di introdurre un backend di memoria semantica. Tempo: 3 minuti.

## 26. Git + GitHub: version the knowledge
**Section:** Build it. **Source:** Git docs; Obsidian Git docs; Brain Sunday review logs.

La schermata Git è illustrativa; spiega la differenza tra sincronizzazione (Dropbox), cronologia delle modifiche (Git) e hosting collaborativo (GitHub). Mostrare il significato del diff: una riga aggiunta nell’indice, una modificata nello stato e un commit verificato. Attenzione a non pushare segreti e alla possibile concorrenza fra sync cloud e modifiche di più agenti. Tempo: 3 minuti.

## 27. My Brain: three layers of one system
**Section:** My implementation. **Source:** Brain README; general/INDEX.md; brain-architecture-current.md.

Entrare nel caso vero: il Brain sul Dropbox dell’autore è un vault Markdown, organizzato in general, areas e .infra. Il Desktop è un alias e non un’altra copia. general contiene regole e routing; areas progetti; .infra supporto tecnico. Il fatto che i dati siano in Markdown è ciò che consente la loro consultazione indipendentemente dall’agente. Tempo: 2 minuti.

## 28. One Brain, many Economics projects
**Section:** My implementation. **Source:** Brain areas/Research/* project indexes and decisions.

Gli esempi sono tratti da file di progetto verificati, non da una ricostruzione ipotetica. Mafia Culture contiene vincoli sulla qualità dei dati musicali e sulle unità di analisi; Fragmented Opposition ha procedure per notizie e merge; Mafia Incendi annota lo stato dei do-file e le incertezze rimaste. La decisione scientifica non è un elemento da inferire dalla chat, ma da leggere nei file di memoria. Tempo: 2 minuti.

## 29. Anatomy of a research project
**Section:** My implementation. **Source:** Brain general/INDEX.md; MEMORY_POLICY.md.

Qui è fondamentale spiegare perché il sistema non usa un unico file MEMORY gigante. I documenti hanno ruoli: CURRENT_STATE è il presente, LOG è la cronologia, DECISIONS contiene scelte approvate, TECHNICAL_NOTES mantiene procedure. Questa separazione riduce la lettura superflua e preserva la distinzione fra ciò che sappiamo e ciò che stiamo ancora valutando. Tempo: 2 minuti.

## 30. The tool stack around the Brain
**Section:** My implementation. **Source:** Brain general/TOOLING_AND_INTEGRATIONS.md; installation requirements.

Non elencare i tool come gadget. Obsidian e Dropbox sono superficie documentale; Memanto recupero semantico locale; Mirage gestisce mount; CodeGraph e code-review-graph danno struttura al codice; Headroom comprime; Econoclast supporta critica economica; Caveman workflow. Lo status attuale di ogni tool va verificato prima di una dimostrazione che lo utilizzi. Tempo: 2 minuti.

## 31. Skills live in the Brain, not one AI
**Section:** My implementation. **Source:** Brain skill INDEX; BOOTSTRAP; Agent Skills specification.

Mostrare catalogo e corpo di una skill. Le procedure di scrittura scientifica e Overleaf sono globali, mentre il sample-construction-report per Mafia Culture è locale. Quando si dimostra che un workflow serve in più progetti, si può promuoverlo a general/capabilities/skills senza assumere che tutte le ipotesi del progetto siano generalizzabili. La struttura .agents/skills offre discovery a agenti compatibili. Tempo: 2 minuti.

## 32. My LLM Wiki: core files first
**Section:** My implementation. **Source:** Brain WIKI_WORKFLOW; LLM_WIKI_PROMPT; decision 2026-10-05.

Questa è la differenza principale rispetto alla LLM Wiki generica: il Brain dell’autore aggiorna anzitutto file core come CURRENT_STATE e DECISIONS. La cartella wiki serve per architetture o procedure lunghe e stabili. Una pagina wiki priva di indice è considerata un difetto, decisione resa esplicita il 5 ottobre 2026. La storia grezza non viene confusa con la memoria approvata. Tempo: 2 minuti.

## 33. Bootstrap → work → closeout → restart
**Section:** My implementation. **Source:** Brain BOOTSTRAP; SESSION_CLOSE; brain-management_DECISIONS.md.

La routine bootstrap carica l’indice di routing e solo il progetto richiesto; poi l’agente lavora e chiude con aggiornamento dei file core. Nell’agosto 2026 il sistema ha rimosso un dump di 184 memorie dal bootstrap e adottato un indice compatto. È un esempio molto concreto di context engineering, oltre che di organizzazione documentale. Tempo: 2 minuti.

## 34. A Brain also accumulates maintenance debt
**Section:** My implementation. **Source:** Brain MEMORY_POLICY; brain-management_DECISIONS.

La memoria degrada come il software: link rotti, informazioni obsolete, istruzioni duplicate e wiki orfane. La manutenzione può utilizzare script deterministici per la struttura e agenti AI per proporre correzioni semantiche; ma le correzioni di significato richiedono prudenza. Un file in meno non equivale sempre a una memoria migliore. Tempo: 2 minuti.

## 35. My Sunday Brain maintenance: a real audit
**Section:** My implementation. **Source:** Brain brain-management_LOG.md (2026-10-18, 2026-10-25).

Mostrare i dati documentati nei log: il 18 ottobre 1.031 file Markdown su 28 progetti; il 25 ottobre 939 file e rimozione di 19 file ridondanti dopo snapshot. La revisione domenicale è programmata ma non sempre parte se il Mac è spento; quelle due review sono state rilanciate manualmente. Il punto didattico è il flusso audit, versionamento, intervento, validazione e report. Non confondere questo ciclo con l’autostart Memanto che è una separata routine ogni tre ore. Tempo: 3 minuti.

## 36. Keep humans in control of the Brain
**Section:** My implementation. **Source:** Brain Sunday audits; AEA Data Policy; Meta Engineering (2026).

Chiudere riprendendo la domanda JARVIS: i modelli sono parte del sistema, ma il valore dipende dall’affidabilità delle informazioni, dalla continuità e dalla possibilità di controllare le azioni. Spiegare perché il valore per l’economia è un’ipotesi testabile: riduzione di costi di ricerca e coordinamento, trasferimento di competenze, meno errori ripetuti. Per un paper, la responsabilità finale resta al ricercatore. Introdurre la demo. Tempo: 2 minuti.

## Live demo — 25 minutes

0–3 min: open the synthetic vault and show the project folder, wiki and link graph.

3–7 min: a fresh agent session reads general/agent/BOOTSTRAP.md, then project state and decisions.

7–10 min: recover a dated methodological choice with source path.

10–13 min: scaffold a second synthetic project from templates.

13–16 min: discover and execute the skill in general/capabilities/skills.

16–20 min: run maintenance audit, flag orphan wiki page and broken link, propose correction.

20–23 min: inspect Git diff, run validator, commit approved changes.

23–25 min: closeout and clean restart; if AI tools fail, show the prewritten expected output.

### Demonstration safety
Use only the included synthetic vault. Never write to the real Dropbox Brain. Avoid real credentials, repository pushes and automatic schedules during class.
