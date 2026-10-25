# Dossier: anAIza School / AiOS (SPYRAL, AIRM Pvt. Ltd.)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentC

## Identity
- School page description:
  - "The Symbiotic Platform That Helps Schools Become Future-Ready" (https://tryspyral.com/school, accessed 2026-10-24)
  - "AiOS connects admins, teachers, students, and parents in a single real-time AI-powered loop" (https://tryspyral.com/school, accessed 2026-10-24)
  - "where data flows seamlessly between every stakeholder through a centralized AiOS hub." (https://tryspyral.com/school, accessed 2026-10-24)
  - Footer: "© 2026 AIRM Pvt. Ltd. · tryspyral.com · All rights reserved." (https://tryspyral.com/school, accessed 2026-10-24)
- Operating system self-description (reproduced from own fetch):
  - "The World's #1 AI Operating System for Schools" (https://tryspyral.com/school, accessed 2026-10-24)
  - "Most platforms solve one problem. anAIza School is the whole operating system." (https://tryspyral.com/school, accessed 2026-10-24)
  - "The AI Operating System for Schools" (https://tryspyral.com/school, accessed 2026-10-24)
- AiOS overview page:
  - "One AI engine. Four intelligent dashboards." (https://tryspyral.com/aios, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- School page:
  - "AI-powered quizzes, personalised learning paths, 2D/3D Labs, progress tracking and daily challenges" (https://tryspyral.com/school, accessed 2026-10-24)
  - "AI Challenge Engine with adaptive difficulty" (https://tryspyral.com/school, accessed 2026-10-24)
- Privacy policy, uses of data:
  - "AI-powered personalized learning recommendations" (https://tryspyral.com/privacy, accessed 2026-10-24)
- Workbench page:
  - "It offers 65+ interactive Physics and Mathematics simulations, AI-generated adaptive challenges, Student Performance Index (SPI) tracking, and 12 NEP 2020 competencies mapped in real-time" (https://tryspyral.com/workbench, accessed 2026-10-24)
- The pages opened describe these features within SPYRAL's own labs and tools; no page found describing sequencing of other vendors' tools.

## E2 Interfaces evidence
- Developer reference page (documented REST API):
  - "plug SPYRAL's intelligence engine directly into your platform. No ML infrastructure needed." (https://tryspyral.com/developer, accessed 2026-10-24)
  - "Base URL: https://tryspyral.com/api/v1 · All responses are JSON · Auth via X-Api-Key: spk_…" (https://tryspyral.com/developer, accessed 2026-10-24)
  - "Map any topic to CBSE, IB, Common Core, Cambridge, or ICSE learning objectives." (https://tryspyral.com/developer, accessed 2026-10-24)
- School page FAQ (vendor claim):
  - "Yes. We offer a REST API for school chains and education groups. Integrations with popular LMS platforms and ERPs are available on request." (https://tryspyral.com/school, accessed 2026-10-24)
  - Comparison table row: "Open Research API For researchers, governments, school chains" (https://tryspyral.com/school, accessed 2026-10-24)
- Google Classroom (vendor claim on school page):
  - "Link your Google Classroom account and AiOS instantly imports your courses, students and assignments" (https://tryspyral.com/school, accessed 2026-10-24)
- No mention of LTI, OneRoster, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge or Open Badges found on the pages opened.

## E3 Learner model evidence
- Developer reference, SPI endpoint:
  - "Compute a Student Performance Index (SPI) from a batch of question responses using a Kalman filter + IRT calibration. Returns a 0–100 score, grade, and per-competency mastery breakdown." (https://tryspyral.com/developer, accessed 2026-10-24)
  - "student_id * string Your internal student identifier" (https://tryspyral.com/developer, accessed 2026-10-24)
  - "prior_spi number Student's previous SPI (0–100, default: 50 for new students)" (https://tryspyral.com/developer, accessed 2026-10-24)
- School page:
  - "Real-time curriculum competency tracking" (https://tryspyral.com/school, accessed 2026-10-24)
- AiOS overview, student and parent dashboards:
  - "NEP skill & competency map" (https://tryspyral.com/aios, accessed 2026-10-24)
- The SPI endpoint accepts responses submitted by the calling platform and returns a computation; the developer page does not state whether these results are stored in a school's AiOS student record.

## E4 Data protection evidence
- Security page:
  - "Admin, Teacher, Student, and Parent roles each access only what they need" (https://tryspyral.com/security, accessed 2026-10-24)
  - "Each school's data is logically isolated. A user from one school cannot access another school's data." (https://tryspyral.com/security, accessed 2026-10-24)
- Developer reference, API key controls:
  - "403 API_NOT_ENABLED This API is not enabled on your key" (https://tryspyral.com/developer, accessed 2026-10-24)
- Privacy policy, sharing table:
  - "Mistral AI AI-generated questions and feedback Anonymized question context only" (https://tryspyral.com/privacy, accessed 2026-10-24)
- School page (vendor claim):
  - "Certified compliant · Last audited May 2026 · Role-based access & IP whitelisting" (https://tryspyral.com/school, accessed 2026-10-24)
- No page found describing per-app or per-tool scopes over student data for third-party tools.

## E5 Third-party tools evidence
- Privacy policy names service providers (processors, not tools that run on the platform):
  - "MongoDB Atlas (AWS) Database hosting" (https://tryspyral.com/privacy, accessed 2026-10-24)
  - "Brevo (ex-Sendinblue) Transactional email" (https://tryspyral.com/privacy, accessed 2026-10-24)
- Google Classroom import is quoted under E2.
- Embed direction is outbound (SPYRAL simulations into other sites):
  - "Generate a time-limited embed token and iframe URL for a SPYRAL simulation. Paste the iframe_snippet directly into your platform." (https://tryspyral.com/developer, accessed 2026-10-24)
  - "Add Interactive Simulations to Your School Website" (https://tryspyral.com/embed-tools, accessed 2026-10-24)
- No page found naming independent developers' tools that run inside AiOS.

## Gaps
- 404: https://tryspyral.com/developers, https://tryspyral.com/docs, https://tryspyral.com/integrations, https://tryspyral.com/marketplace, https://tryspyral.com/partners, https://tryspyral.com/trust
- Footer "Documentation" and "Developer API" both link to /developer; "Help Center" links to /contact (no separate help center found).
- Vendor states GDPR, COPPA, DPDP Act 2023 and PCI-DSS on the school page; no independent certification page opened.
- Several vendor sentences contain em dashes; quotes were cut before the dash rather than altered.
