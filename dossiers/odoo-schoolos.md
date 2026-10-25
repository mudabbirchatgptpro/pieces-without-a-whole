# Dossier: SchoolOS for Odoo (Binary Bridge Technology Services)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentE

## Identity
- What it is, in the vendor's words:
  - "This is the core foundation of SchoolOS." (https://apps.odoo.com/apps/modules/19.0/schoolos_base, accessed 2026-10-24)
  - "SchoolOS is a complete school management ERP for Odoo 19" (https://apps.odoo.com/apps/modules/19.0/schoolos, accessed 2026-10-24)
  - "SchoolOS is a unified school-management platform for the Gulf and international K-12 market" (https://apps.odoo.com/apps/modules/19.0/schoolos_base, accessed 2026-10-24)
- Self-description as "operating system"/"OS": product name only (module name "SchoolOS" plus "Core (Base)", separated on the listing by a dash). No sentence calling it an "operating system" found on the opened listing pages. The vendor's own site (bbtech.ae home and its school-system page) does not mention "SchoolOS"; its menu lists an "ISMS" school system.
  - Listing byline: "by Binary Bridge Technology Services https://bbtech.ae/" (https://apps.odoo.com/apps/modules/19.0/schoolos_base, accessed 2026-10-24)
- Note: the vendor's listing text uses em dashes; quotes below were chosen or cut at points that avoid them.

## E1 Sequencing / scheduling evidence
- Student-facing timeline and LMS progression features (within the suite's own modules):
  - "A personal timeline and calendar surface upcoming lessons, due assignments, exams and live classes so nothing" (https://apps.odoo.com/apps/modules/19.0/schoolos_student_portal, accessed 2026-10-24)
  - Release highlights list: "LMS gamification, peer review, plagiarism scanning, learning paths & group submissions" (https://apps.odoo.com/apps/modules/19.0/schoolos, accessed 2026-10-24)
  - "Generate term report cards, transcripts and a rules-driven promotion engine" (https://apps.odoo.com/apps/modules/19.0/schoolos_academics, accessed 2026-10-24)
- None found of sequencing across other vendors' tools.

## E2 Interfaces evidence
- REST API Gateway module (documented on its listing page with endpoints):
  - "turns your SchoolOS instance into an integration platform." (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
  - "Connect your SIS, BI tools, mobile back-ends and partner systems without ever exposing the database." (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
  - "/api/v1/students , /students/<id> , /attendance , /fees/invoices and /ping" (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
  - "Outbound webhooks notify partner systems the moment a student enrols, attendance is recorded or a fee is paid" (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
- Content standards (vendor claim on listing pages):
  - "Full SCORM 1.2 / xAPI playback with progress tracking" (https://apps.odoo.com/apps/modules/19.0/schoolos_student_portal, accessed 2026-10-24)
  - "Lesson assets support Text / HTML, Video, SCORM, External Link and File / PDF" (https://apps.odoo.com/apps/modules/19.0/schoolos_lms, accessed 2026-10-24)
- No mention of LTI, OneRoster, Caliper, CLR, CASE, Ed-Fi, QTI, Common Cartridge or Open Badges found on the opened pages.

## E3 Learner model evidence
- Outcomes and progress records (no "mastery" or knowledge-state wording found):
  - "A progress view and learning-outcomes page show how the student is performing against curriculum targets and goals." (https://apps.odoo.com/apps/modules/19.0/schoolos_student_portal, accessed 2026-10-24)
  - "Build curriculum units and topics, write measurable learning outcomes by Bloom level, and design rubrics for outcome-based grading." (https://apps.odoo.com/apps/modules/19.0/schoolos_curriculum_designer, accessed 2026-10-24)
  - "Attach an outcome rubric to assignments for criterion-based rubric grading tied to the Curriculum Designer's learning outcomes." (https://apps.odoo.com/apps/modules/19.0/schoolos_lms, accessed 2026-10-24)
  - "Per-student lesson completion with progress percentage rolls up to a course progress view teachers can monitor at a glance." (https://apps.odoo.com/apps/modules/19.0/schoolos_lms, accessed 2026-10-24)
- On outside writes: the API page's endpoint list contains GET endpoints only ("GET /api/v1/attendance"). None found of outside vendors' tools writing into the outcomes data.

## E4 Data protection evidence
- Per-key API scopes:
  - "Issue narrowly-scoped API keys (read students, attendance, fees or academics" (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
  - "Queries run scoped to the key's company, so a key for one branch can never read another branch's records." (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
- Role-based access and compliance module:
  - "A shared role registry of 45+ res.groups powers role-based access across the entire suite, so permissions stay consistent everywhere." (https://apps.odoo.com/apps/modules/19.0/schoolos_base, accessed 2026-10-24)
  - "maintain a consent register for photo / media, data-processing, marketing, trip, medical and third-party-sharing consents and withdrawals" (https://apps.odoo.com/apps/modules/19.0/schoolos_compliance, accessed 2026-10-24)

## E5 Third-party tools evidence
- Named outside services connected by the LMS module (connectors, not tools hosted inside the suite):
  - "Live classes use real meeting-provider connectors for Zoom, Microsoft Teams, Google Meet and BigBlueButton, with create / update / cancel and connection testing." (https://apps.odoo.com/apps/modules/19.0/schoolos_lms, accessed 2026-10-24)
- API audience statement:
  - "School IT teams integrating a third-party SIS or LMS" (https://apps.odoo.com/apps/modules/19.0/schoolos_api, accessed 2026-10-24)
- Suite runs on Odoo; listing dependencies: "Dependencies • Contacts (contacts) • Discuss (mail) • Employees (hr)" (https://apps.odoo.com/apps/modules/19.0/schoolos_base, accessed 2026-10-24)
- None found of named independent developers' tools running inside SchoolOS.

## Gaps
- Vendor site https://bbtech.ae/ and https://bbtech.ae/school-system-isms/ opened; neither mentions SchoolOS. No SchoolOS developer docs, help center or privacy page on bbtech.ae found (checked page-sitemap.xml).
- Only Odoo Apps Store listing pages are primary documentation: schoolos (suite), schoolos_base, schoolos_lms, schoolos_api, schoolos_curriculum_designer, schoolos_compliance, schoolos_student_portal, schoolos_academics.
- No failed page loads.
