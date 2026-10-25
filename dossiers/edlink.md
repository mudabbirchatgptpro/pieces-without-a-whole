# Dossier: Edlink (Edlink)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

## Identity
- "Edlink helps companies build and scale integrations with districts and universities. Our unified API enables teams to integrate quickly with all major LMS and SIS providers." (https://ed.link/, accessed 2026-10-24)
- "Edlink is designed to bridge the gap between various educational data systems, offering a unified way for applications to connect with Learning Management Systems (LMS), Student Information Systems (SIS), identity providers (like Clever and ClassLink), and other educational data standards." (https://ed.link/docs/providers, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- No page opened describes Edlink deciding or sequencing what a learner does next. The documented functions are "SSO, Rostering, Data Enrichment, Coursework, and Grade Sync" (https://ed.link/, accessed 2026-10-24).
- Coursework creation is described as an LMS workflow driven by the teacher: "The user signs into their LMS, selects a course, and clicks "Create Assignment" (or similar). The user indicates to the LMS that they want to create an assignment that is connected to a piece of external content (i.e. from your platform)." (https://ed.link/docs/guides/v2.0/lti/deep-linking, accessed 2026-10-24)

## E2 Interfaces evidence
- "The Edlink API is organized around REST. ... The purpose of this API is to enable educational software developers to quickly connect to a variety of school data sources in order to provide a smooth workflow for teachers, students, and administrators." (https://ed.link/docs/api, accessed 2026-10-24)
- "Edlink data connections create an instant bi-directional data flow between your platform and the school's LMS, SIS, or related system." (same URL, accessed 2026-10-24)
- "Currently, we are compatible with various API, LTI, and OneRoster implementations." (same URL, accessed 2026-10-24)
- "The Graph API enables you to access LMS information at the school or district level. All requests are made with a district-level access token." and "The User Data API enables you to make changes on behalf of a user and fetch data relevant to them. All requests documented in this section are scoped to the authenticated user." (same URL, accessed 2026-10-24)
- Provider categories: "Platforms like Canvas, Schoology, Google Classroom, Blackboard, Brightspace, and Moodle." ; "Systems such as PowerSchool, Aeries, Skyward, Infinite Campus, and Veracross." ; "Platforms like Clever, ClassLink, Google Workspace, Microsoft Entra ID, and other OAuth/OIDC compliant systems." ; "We also support standards like OneRoster and LTI, which provide common frameworks for data exchange and tool interoperability." (https://ed.link/docs/providers, accessed 2026-10-24)
- "Whether data comes from Canvas or PowerSchool, it's mapped to Edlink's standard entities (e.g., People, Classes, Enrollments, Assignments)." (same URL, accessed 2026-10-24)
- "Even though it is possible to "push" grades into the LMS via what the LTI spec calls "Assignment & Grade Services" (AGS), this process typically only creates a column in the gradebook for a given resource - it doesn't create the resource itself. ... This limitation requires that we provide support for the LTI deep linking flow." (https://ed.link/docs/guides/v2.0/lti/deep-linking, accessed 2026-10-24)
- Clever LMS Connect: "Clever LMS Connect, using part of Edlink's Unified API, enables school IT admins to initiate a connection to their district's LMS from the Clever dashboard." (https://ed.link/community/new-client-announcement-clever/, accessed 2026-10-24)
- Certification: not checked (1EdTech directory not queried). No vendor statement about certification was found on the pages opened.

## E3 Learner model evidence
- Data model scope: "This guide explains the Edlink Education Data Model: how districts, schools, people, coursework, schedules, attendance, and supporting types relate to each other." (https://ed.link/docs/guides/v2.0/data-model/education-data-model, accessed 2026-10-24)
- Rubric object: "A PerformanceLevel represents a specific level of achievement for a grading criterion." and "The name of the performance level (e.g., "Excellent", "Needs Improvement")." (https://ed.link/docs/api/v2.0/rubrics/overview, accessed 2026-10-24)
- Canvas provider page: "Assignments, submissions, and grades can be synced and managed directly within Edlink, maintaining alignment with Canvas' grading system." (https://ed.link/docs/providers/canvas/functionality, accessed 2026-10-24)
- The terms "outcome", "mastery" and "competency" did not appear on the API overview, data model or Canvas provider pages opened. No learner mastery or knowledge-state entity was found.

## E4 Data protection evidence
- "Sharing rules are the primary way that data is filtered between a school's data source and a company's application." (https://ed.link/docs/platform/sharing/sharing-rules, accessed 2026-10-24)
- "Both companies and schools can create sharing rules, but they are applied in order of priority. School rules are applied first, followed by company rules, so that companies cannot access more data than the school has allowed." (same URL, accessed 2026-10-24)
- "Person rules allow you to include specific people by one or more attributes (e.g. email address, grade level)." and "Class rules allow you to include a set of classes based on their attributes (e.g. class name, teacher email)." (same URL, accessed 2026-10-24)
- "The data privacy mask is designed to help protect both the school and the developer from sharing unauthorized or unwanted data. Developers can request (and district can control) what fields are shared for each integration." (https://ed.link/docs/platform/sharing/data-privacy-mask, accessed 2026-10-24)
- "This setting will generate a random name for each person in a stable way ... For example, "John Doe" might become "Red Dog", so teachers can still identify students without sharing the actual PII to your application." (same URL, accessed 2026-10-24)
- "The Graph API can limit your exposure to unnecessary or sensitive student data through Sharing Rules." (https://ed.link/docs/api, accessed 2026-10-24)
- "At first, we're focused on automating DPAs." (https://ed.link/docs/platform/privacy/why-we-built-this, accessed 2026-10-24)

## E5 Third-party tools evidence
- "Join 150+ edtech companies that can focus on growing their company because we handle their integrations" (https://ed.link/, accessed 2026-10-24)
- "Clever launched LMS integrations for Clever Complete with Edlink." (https://ed.link/, accessed 2026-10-24)
- "Clever, the platform providing access to learning applications for schools, has decided to work with Edlink, an integration platform for edtech companies" (https://ed.link/community/new-client-announcement-clever/, accessed 2026-10-24)
- Edlink connects third-party applications to LMSs and SISs through its API (data sync and launch); no page opened describes applications running inside Edlink itself. Apart from Clever, no named client application was found on the pages opened.

## Gaps
- https://ed.link/docs/guides/v2.0/permissions returned HTTP 500.
- https://ed.link/integrations returned an empty page (18 characters).
- No public list of named Edlink client applications was found.
