# Dossier: SchoolWare (Happy Digital, schoolware.io)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentD

## Identity
- Footer self-description: "SchoolWare is the operating system for modern schools" (https://schoolware.io/, accessed 2026-10-24)
- FAQ: "SchoolWare is an all-in-one operating system for schools. It brings admissions, student records, attendance, fees, academics, timetables, communication, and parent/teacher/student portals into a single secure platform." (https://schoolware.io/faq/, accessed 2026-10-24)
- Self-description as OS, homepage hero (reproduced): "The school operating system Run the whole school from one place." (https://schoolware.io/, accessed 2026-10-24)
- Vendor entity: "© 2026 Happy Digital. All rights reserved." (https://schoolware.io/, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
None found. The nearest items are administrative scheduling and roadmap AI features:
- "Timetable Build class and teacher timetables that stay in sync with attendance, rooms, and the parent portal." (https://schoolware.io/features/, accessed 2026-10-24)
- "Academics Exams, homework, grading, and report cards & transcripts" (https://schoolware.io/features/, accessed 2026-10-24)
- Roadmap item: "Coming soon AI homework checking Homework reviewed with specific, helpful feedback for each student, ready for the teacher to review and approve." (https://schoolware.io/ai/, accessed 2026-10-24)

## E2 Interfaces evidence
- MCP connector (vendor claim, no developer docs located): "SchoolWare speaks MCP, the open standard that connects AI assistants to live systems." (https://schoolware.io/features/, accessed 2026-10-24)
- "Point ChatGPT, Claude, or any MCP client at your school’s secure SchoolWare endpoint." (https://schoolware.io/ai/, accessed 2026-10-24)
- API mention: "Custom roles and fine-grained, module-level permissions" ... "enforced across navigation, pages, actions, and the API." (https://schoolware.io/security/, accessed 2026-10-24)
- Data import is by spreadsheet: "Students, staff, classes and fee records load from a spreadsheet template." (https://schoolware.io/, accessed 2026-10-24)
- No mention of LTI, OneRoster, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge or Open Badges found on the pages opened. /developers, /api, /docs return 404 (see Gaps).

## E3 Learner model evidence
- Records described: "Student information A complete, searchable record for every student: profile, guardians, classes, history, and documents." (https://schoolware.io/features/, accessed 2026-10-24)
- "Exams, homework, grading, and report cards & transcripts" (https://schoolware.io/features/, accessed 2026-10-24)
- Privacy policy data categories: "attendance, academic records and grades, fee and payment records, and similar information." (https://schoolware.io/privacy/, accessed 2026-10-24)
- No mastery, skill or knowledge-state model found.

## E4 Data protection evidence
- "Role-based access control Custom roles and fine-grained, module-level permissions" (https://schoolware.io/security/, accessed 2026-10-24)
- AI connector scope: "The assistant sees only what the person using it can already see. It inherits their role and permissions" (https://schoolware.io/security/, accessed 2026-10-24)
- "Your school enables the connection and can revoke it at any time." (https://schoolware.io/security/, accessed 2026-10-24)
- "Actions taken through the connector are logged, so you have a record of what was asked and done." (https://schoolware.io/security/, accessed 2026-10-24)
- "editions let you turn modules on or off per school" (https://schoolware.io/security/, accessed 2026-10-24)
- Privacy role: "the school is the data controller and SchoolWare is the data processor ." (https://schoolware.io/privacy/, accessed 2026-10-24)

## E5 Third-party tools evidence
- AI assistants connected from outside via MCP: "Connect SchoolWare to ChatGPT, Claude, or any assistant that speaks the Model Context Protocol" (https://schoolware.io/ai/, accessed 2026-10-24)
- Named sub-processors (infrastructure, not tools running inside): "Stripe Payment processing and subscription billing Amazon Web Services (AWS) Application hosting and data storage" (https://schoolware.io/security/, accessed 2026-10-24)
- Payment integrations: "a school in the United States might collect fees through Stripe, a school in Pakistan through its connected bank, and a school in India through a provider like Paytm." (https://schoolware.io/faq/, accessed 2026-10-24)
- No marketplace or third-party apps running inside the product found.

## Gaps
- 404: https://schoolware.io/developers, https://schoolware.io/api, https://schoolware.io/docs, https://schoolware.io/integrations, https://schoolware.io/partners
- 403 on https://schoolware.io/privacy (no trailing slash); https://schoolware.io/privacy/ loaded.
- https://schoolware.io/sitemap.xml returned no URLs.
- No public developer documentation for the MCP endpoint or the API found. App (app.schoolware.io) is behind login and was not opened.
