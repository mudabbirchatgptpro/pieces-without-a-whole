# Dossier: EDMO (EDMO, Boston USA / Pune India; affiliate Ischool India Private Limited)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentE

## Identity
- What it is, in the vendor's words:
  - "Unify admissions document processing, student engagement, and university systems with AI to automate enrollment workflows from inquiry to enrollment." (https://goedmo.com/, accessed 2026-10-24)
  - "EDMO brings document processing, student engagement, and system orchestration into one AI operating system." (https://goedmo.com/, accessed 2026-10-24)
- Self-description as "operating system":
  - "The AI Operating System for Higher Education" (https://goedmo.com/, accessed 2026-10-24)
  - "An Enrollment Operating System built for speed, scale, and yield" (https://goedmo.com/, accessed 2026-10-24)
  - "EDMO’s System Intelligence is the integration layer of our AI Operating System." (https://goedmo.com/system-intelligence/, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- Admissions workflow automation and follow-ups (applicant/prospect workflows, not course activity):
  - "EDMO reads documents, assesses potential, and triggers tailored follow-ups by profile." (https://goedmo.com/, accessed 2026-10-24)
  - "Real-time triggers for timely engagement" (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
  - "Automated status updates and checklist routing" (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
- None found of sequencing of learning activities.

## E2 Interfaces evidence
- Documented developer page: an OpenAPI-style spec for the agent builder is published in the knowledge base:
  - "url: https://agents.goedmo.com/api description: Production Edmo deployment" (https://goedmo.com/knowledge-base/edmo-agent-builder-api/, accessed 2026-10-24)
  - "name: Tools description: Manage integrations and tools that assistants can call." (https://goedmo.com/knowledge-base/edmo-agent-builder-api/, accessed 2026-10-24)
  - Tool types in the spec: "enum: - function - apiRequest - mcp" (https://goedmo.com/knowledge-base/edmo-agent-builder-api/, accessed 2026-10-24)
- Vendor-claimed connectors (marketing pages):
  - "Use prebuilt connectors (Salesforce, Slate, Element451, PeopleSoft, Canvas) or add custom endpoints" (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
  - "Canvas Connect course content and student activity from Canvas LMS." (https://goedmo.com/, accessed 2026-10-24)
  - "Blackboard Sync courses, rosters, and grades with your Blackboard LMS." (https://goedmo.com/, accessed 2026-10-24)
- No mention of LTI, OneRoster, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge or Open Badges found on the opened pages.

## E3 Learner model evidence
- Unified applicant/student profile (record normalization; no mastery or knowledge-state wording found):
  - "Normalize and map records into a single student profile your AI can act on" (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
  - "Keep student profiles, application statuses, and updates aligned across Slate and every connected platform." (https://goedmo.com/slate/, accessed 2026-10-24)
- None found on a model of what the learner knows.

## E4 Data protection evidence
- Security FAQ and subprocessors (institution-level policy; per-integration role-based access claimed):
  - "University data is not used for advertising , not sold , and not shared with other customers ." (https://goedmo.com/security/, accessed 2026-10-24)
  - "EDMO acts as a service provider processing data on behalf of universities and supports FERPA compliance through strict access controls, data minimization, encryption, monitoring, and contractual safeguards." (https://goedmo.com/security/, accessed 2026-10-24)
  - "Role-based access, audit trails, and encrypted data flows for compliant operations" (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
  - API spec user object: "description: High-level role for permissions (e.g., ADMIN, EDITOR, VIEWER)." (https://goedmo.com/knowledge-base/edmo-agent-builder-api/, accessed 2026-10-24)
- Vendor states security alignment: "EDMO aligns its security program with industry best practices and SOC 2 Trust Services Criteria" (https://goedmo.com/security/, accessed 2026-10-24)

## E5 Third-party tools evidence
- EDMO runs inside other vendors' platforms (the reverse direction):
  - "EDMO operates as a managed package/plugin within the customer's Salesforce instance." (https://goedmo.com/subprocessors/, accessed 2026-10-24)
  - Slate: "Data synchronization for admissions workflows as a Preferred Partner." (https://goedmo.com/subprocessors/, accessed 2026-10-24)
- Outside services connected by sync/messaging (named on the System Intelligence page): "Twilio Send SMS and automated text campaigns to students at scale." and "Zoom Connect Zoom Phone and meetings for student calls and advising." (https://goedmo.com/system-intelligence/, accessed 2026-10-24)
- None found of independent developers' tools running inside EDMO.

## Gaps
- https://goedmo.com/docs/ : loads (HTTP 200) but body shows only an unrendered "[wedocs]" shortcode, no documentation content.
- Knowledge base sitemap lists four articles only (gpa-calculator-usage-manual, advisor-copilot, edmo-agent-builder-api, archive); only the API article was opened.
- Pages opened: home, /system-intelligence/, /slate/, /security/, /subprocessors/, /docs/, /privacy-policy/, /knowledge-base/edmo-agent-builder-api/, sitemaps. No failed loads.
