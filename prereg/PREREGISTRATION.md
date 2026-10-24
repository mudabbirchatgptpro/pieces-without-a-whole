# Pre-registration: Pieces Without a Whole

**Study:** Modularity, verifiability and the "learning operating system" in education technology
**Author:** Mudaber Jamshaid (independent researcher; Ed.M., Harvard Graduate School of Education)
**Registered:** 24 October 2026, before any product in the sample was coded.
**Status of data at registration:** stated in full in section 6. Nothing is hidden.

---

## 1. Research questions

- **RQ1.** Across the layers of the education technology stack, does adoption of open interface standards follow how verifiable each layer's information is, as Christensen's modularity theory predicts?
- **RQ2.** Does any product marketed as an operating system for learning or for schools perform the five functions of an operating system, including a learner model that independent tools write to?
- **RQ3.** When the major AI products connect to schools, where do they write evidence of learning: nowhere, into one platform's own store, or into a record that other vendors' tools can read?

## 2. Theory being tested

Christensen's modularity theory holds that an interface becomes modular, so that independent firms can build on either side of it, only when it is "specifiable, verifiable, and predictable." Where those conditions fail, firms integrate across the interface.

This study adds one refinement, stated here before testing. "Verifiable" can mean three different things, and only the third is hard in education:

| Level | What the receiving system can check | Example |
|---|---|---|
| V1 Syntactic | The message has the right format and fields | A grade arrives as a number between 0 and 1 |
| V2 Provenance | Who issued the message, and that it was not altered | A signed credential from a named school |
| V3 Referent | That the thing the message describes is true, by checking against an independent source of truth the receiver can reach | A roster says a student is enrolled; the district student information system confirms it |

**Hypothesis H-V.** Standards whose referent is checkable (V3) reach broad certification. Standards whose referent is a claim about what a learner knows or did while learning cannot reach V3 without reassessment, and stay thinly adopted even when V1 and V2 are solved. Cryptographic signing (V2) does not substitute for V3.

## 3. Pre-registered predictions

Each prediction names its resolution date and the observation that refutes it.

**P1 (forward, registry).** On the public 1EdTech certification directory read on or after 30 June 2027, the number of distinct organizations certified for Comprehensive Learner Record (CLR, any version) will be less than 25 percent of the number certified for OneRoster (any version). At registration the ratio is 9 to 95, about 9.5 percent.
*Refuted if* CLR organizations are 25 percent or more of OneRoster organizations on that date.

**P2 (this study, classification).** No product in the sampling frame (section 5) meets all five functions in the codebook (section 4) together with the sufficiency rule.
*Refuted if* both coders, or the adjudicated code, classify at least one product as a learning operating system.

**P3 (this study and forward, AI audit).** None of the audited AI products (section 5.3) documents writing learner evidence (mastery, competency or learning-activity data, not only a numeric grade) into a record that other vendors' tools can read through an open standard (CLR, Caliper, xAPI, Open Badges, CASE-aligned assertions, or Ed-Fi). The same holds on 30 June 2027.
*Refuted if* public documentation from the vendor shows any audited product doing so, on either date.

**P4 (this study, standards audit).** Coding each 1EdTech standard by the highest verifiability level its information can reach (V1 to V3, section 2) will rank the standards in the same order as their certification counts, with Spearman's rho of at least 0.6.
*Refuted if* rho is below 0.6. This prediction is exploratory, not confirmatory, because the certification counts were seen before it was written (section 6).

## 4. Codebook: the five-function test

Sources for the functions: Silberschatz, Galvin and Gagne (2018); Tanenbaum and Bos (2014); US v. Microsoft, Findings of Fact (1999), para. 2; Gawer and Cusumano (2014); Kay (2008).

Each function is coded **0, 1 or 2** from public documentation only (vendor documentation, developer pages, help centers, standards listings, and the 1EdTech directory). Marketing copy alone can earn at most 1.

| Code | F1 Cross-tool scheduling | F2 Open interfaces | F3 Persistent learner model | F4 Per-tool data protection | F5 Third-party platform |
|---|---|---|---|---|---|
| Meaning | Decides or sequences what a learner does next across activities | Published interfaces outside developers use to read or write roster, launch, results or learner information | A model of what the learner knows (mastery or knowledge state, not only grades or completions) that persists | Controls each tool's access to a child's data | Runs tools made by independent developers |
| **2** | Documented sequencing of activities delivered by **two or more independent vendors' tools** | Public developer documentation or 1EdTech certification for an open standard, with outside developers shown using it | Documented learner model that **two or more independent vendors' tools write to** | Documented per-tool or per-app permissions or scopes over student data | At least two independent third-party tools documented as running inside or on it |
| **1** | Sequencing only across the vendor's own tools, or claimed without documentation | Proprietary API with no public docs, or a standard claimed but not certified | A learner model that only the vendor's own tools write to, or a cross-tool record of grades or completions only | A privacy policy or district-level setting with no per-tool control | Integrations listed but not running inside it (for example, links out or data sync only) |
| **0** | No sequencing, or sequencing within a single activity only | No documented interface | No persistent learner model | No documented control | No third-party tools |

**Sufficiency rule.** A product is a **learning operating system** only if it scores 2 on all five functions **and** the documentation shows that at least two independent vendors' tools write to the F3 learner model that the F1 scheduler acts on.

**Derived class** (assigned mechanically from the codes, in this order):
1. **Learning operating system:** sufficiency rule met.
2. **External platform:** F2 = 2 and F5 = 2, but F1 or F3 below 2 (for example, a learning management system or a rostering layer).
3. **Internal platform (suite):** F1 or F3 at least 1 across the vendor's own tools, F5 below 2.
4. **Single application:** none of the above.

**Coding procedure.**
- Evidence collection and coding are separated. Evidence agents build a dossier for each product (URLs, dated quotations) and do not code.
- Two coders work independently and blind to each other's codes, from the same dossiers. Coder A and Coder B are separate AI model instances given only this codebook and the dossiers. They may open the cited URLs, but they may not search for new evidence. This keeps the evidence base identical.
- A human coder (the author) independently codes a random sample of at least 15 products, drawn with a fixed seed (20261024) after the AI coding is complete and before the author sees the AI codes for those products.
- Agreement is reported before any disagreement is resolved: Cohen's kappa (unweighted and linearly weighted) per function and for the derived class, for A vs B and for human vs each AI coder.
- Disagreements are resolved by the author, against the dossier, with the reason recorded.
- All dossiers, codes, disagreements and resolutions are released.

## 5. Sampling frame

The frame is fixed by rule, not by choosing products.

**5.1 Self-described operating systems.** Every product whose own website describes it as an "operating system" (or "OS") for learning, for schools or for education, found by these exact searches run between 24 and 26 October 2026: "operating system for schools"; "learning operating system"; "AI operating system" plus "schools"; "education operating system"; "school OS"; "OS for learning". Products for corporate training only are excluded.

**5.2 Platforms and layers.** The six most widely used learning management systems in US K-12 and higher education (Canvas, Schoology, Google Classroom, Brightspace, Blackboard, Moodle); the main rostering, identity and data layers (Clever, ClassLink, Ed-Fi, Edlink); and integrated AI school models with public documentation (Timeback from Alpha School, Khanmigo).

**5.3 AI audit (RQ3).** Claude for Education (Anthropic), ChatGPT Edu (OpenAI), Gemini for Education and Gemini in Google Classroom (Google), IgniteAI (Instructure), Khanmigo (Khan Academy), MagicSchool, SchoolAI, Brisk Teaching.

**5.4 Most-used instructional tools.** The instructional products (not general productivity, video or communication tools) in the most recent Instructure EdTech Top 40 list available on 24 October 2026.

Target size: 40 to 60 products. If 5.1 to 5.4 together give more than 60, all of 5.1, 5.2 and 5.3 are kept and 5.4 is trimmed from the bottom of its ranking.

## 6. What existed before registration (full disclosure)

- **Registry counts were already seen.** Organizations certified per standard on the public 1EdTech directory, read 14 and 19 October 2026: LTI 199; OneRoster 95; Open Badges 48; CASE 16; CLR 9; Caliper 6 (19 October figures where both exist). This is why P4 is labeled exploratory.
- **A pilot classification exists.** In a 14 October 2026 planning document, a single coder classified 13 products against an earlier draft of this test and found none meeting all five functions. It is a pilot, not data. Neither coder in this study is given it.
- **The thesis was stated in a proposal** sent to the Clayton Christensen Institute on 19 October 2026.
- **AI use.** The author used AI tools (Anthropic's Claude) for literature search, evidence collection, coding as two of the three coders, analysis and drafting. The author designed the study, adjudicates every disagreement, codes the human sample, and is responsible for all claims. This is disclosed in every output.

## 7. Analysis plan

- RQ1 and P4: Spearman's rho between the V-level rank and the certification-count rank across 1EdTech standards with at least one certified organization. Data Privacy (a TrustEd Apps seal, not an interface standard) is excluded.
- RQ2 and P2: frequency table of derived classes; the function most often missing among self-described operating systems.
- RQ3 and P3: for each AI product, the most distant place it writes learner evidence: none; own store; one platform's store (for example, an LMS gradebook); cross-vendor open record.
- No statistical significance testing is planned for RQ2 and RQ3; they are census-style descriptive tests of universal claims, where a single counter-example refutes.
