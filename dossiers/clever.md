# Dossier: Clever (Clever, Inc.)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: dev.clever.com pages were opened as the Markdown versions the site serves (the site states "Append .md to any documentation page URL to get its markdown version." at https://dev.clever.com/llms.txt). The help center article was rendered in a browser.

## Identity
- "Clever's identity platform, uniquely designed for education, allows schools and applications to secure all identities, control your data, and power classroom learning." (https://www.clever.com/, accessed 2026-10-24)
- "Clever offers one secure place for teachers and students to access the applications they love and depend on." (https://www.clever.com/, accessed 2026-10-24)
- "Clever helps you integrate your app with school and district systems through rostering and single sign-on." (https://dev.clever.com/docs/what-is-clever.md, accessed 2026-10-24)
- "Clever Complete is the platform solution purpose-built for EdTech scalability [...] connecting our application partners to any school through a single, secure integration for rostering, SSO, and LMS connections." (collector's [...] replaces a dash in the original) (https://dev.clever.com/docs/what-is-clever.md, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- No page opened describes Clever deciding or sequencing what a learner does next. The documented integration paths are: "**Clever Secure Sync** for district-managed rostering data", "**SSO + Rostering** for district-managed login paired with roster data", "**Clever LMS Connect** for LMS workflows such as grade passback and LTI 1.3 SSO", "**AnySchool Rostering** for supporting schools that are not on Clever" (https://dev.clever.com/docs/what-is-clever.md, accessed 2026-10-24)
- Content mapping: "Resources are an optional data type - resources can be created by applications and assigned to courses by district admins." and "Resources can only be assigned to courses. Resources are not  assigned to sections directly, but to the course the section is associated with." (https://dev.clever.com/docs/resources.md, accessed 2026-10-24)

## E2 Interfaces evidence
- "Use the Clever API to access district, school, roster, and user data based on your application's scopes and integration type." (https://dev.clever.com/docs/api-overview.md, accessed 2026-10-24)
- "Clever API v3.1 OpenAPI Spec ... Machine-readable OpenAPI 3.0 specification for the Clever API v3.1" (https://dev.clever.com/llms.txt, accessed 2026-10-24)
- "Clever LMS Connect extends your existing Clever integration so your app can work with district LMS workflows such as grade passback and LTI 1.3 SSO." (https://dev.clever.com/docs/lms-connect-overview.md, accessed 2026-10-24)
- "Gradebook access: Your application can read and write assignments and gradebook entries in the LMS gradebook." and "District users can launch into your application from the LMS with LTI 1.3 SSO." (same URL, accessed 2026-10-24)
- "With API v3.1 of the Clever API, we introduce the LMS Connect integration. This integration extends our existing rostering capabilities and supports assignment and grade passback from your application, through Clever and into a district LMS. Currently, the LMSs supported are Canvas, Schoology, and Google Classroom." (https://dev.clever.com/docs/api-v31.md, accessed 2026-10-24)
- Edlink describes LMS Connect as "powered by Edlink technology" (https://ed.link/community/new-client-announcement-clever/, accessed 2026-10-24).
- OIDC: "Implement OpenID Connect (OIDC) with Clever, configure third-party identity services, and understand identity tokens and the `/userinfo` endpoint." (https://dev.clever.com/llms.txt, accessed 2026-10-24)
- Access is gated by agreement: "This feature is included with a Clever Complete subscription." and "This product is only available to existing Secure Sync partners." (https://dev.clever.com/docs/lms-connect-overview.md, accessed 2026-10-24)
- Clever runs its own partner certification: "Clever Secure Sync Certification Guide: Review Secure Sync integration requirements, the certification questionnaire, and edge-case sample data before submitting your integration for certification." (https://dev.clever.com/llms.txt, accessed 2026-10-24)
- No mention of OneRoster was found on the pages opened. 1EdTech certification: not checked (directory not queried).

## E3 Learner model evidence
- LMS Connect objects: "The grade passback API contains two new object types that don't appear in the Clever Data API Schema: Assignments and Submissions. An **assignment** is an activity that can be completed by a student. Amongst other fields, it includes a due date as well as a potential score. A **submission** is a specific student's attempt at completing the assignment." (https://dev.clever.com/docs/core-concepts.md, accessed 2026-10-24)
- Data schema pages listed: "Districts, Schools, Users, Sections, Courses, Terms, and Contacts" (https://dev.clever.com/llms.txt, accessed 2026-10-24). API v3.1 adds student demographic fields such as "`roles.student.gifted_status`" and "`roles.student.section_504_status`" (https://dev.clever.com/docs/api-v31.md, accessed 2026-10-24).
- No mastery, skill, outcome or competency object was found in the documentation index or pages opened.

## E4 Data protection evidence
- "With sharing permissions, you can control exactly which users get access to each application in Clever. Whether your whole school organization uses an app or just a handful of users (e.g., four 3rd-grade math sections), sharing permissions let you decide who gets access and what data the application receives from Clever to roster and maintain user accounts." (https://support.clever.com/hc/s/articles/203115007?language=en_US, "Sharing Permissions: Overview", accessed 2026-10-24)
- "We know that not all applications are utilized by the same subset of users, so you can set up sharing permissions on an app-by-app basis." (same URL, accessed 2026-10-24)
- "Clever provides each application with only the data necessary for its operation. To view or modify what's being shared, go to your Clever Dashboard > Applications > My Applications page and then click on the application's name to open the app overview page. Here, you can click the download icons next to each data type to see the exact data the application receives." (same URL, accessed 2026-10-24)
- "Share by Rules: Clever will only share data that meets the specific criteria you've set." (same URL, accessed 2026-10-24)
- "SSO bearer tokens are issued for individual users, such as students, teachers, district admins, and school admins. The data available to these tokens is scoped to the user who authorized the token and the data available around that user." (https://dev.clever.com/docs/api-overview.md, accessed 2026-10-24)
- "Please note that access to the resources endpoints requires additional scopes." (https://dev.clever.com/docs/resources.md, accessed 2026-10-24)
- "Clever does not facilitate the sharing of any Student Data with third parties on the Service except on behalf of the School after the School has authorized a third party or application to access Student Data through the Service." (https://clever.com/trust/privacy/policy, accessed 2026-10-24)

## E5 Third-party tools evidence
- "The world's leading applications partner with Clever." followed by app listings including "Canva Education", "GameChanger University" and "I Start Arabic (ISA)" (https://clever.com/app-gallery, accessed 2026-10-24)
- Site navigation lists partner resource hubs "Google + Clever", "HMH + Clever", "McGraw Hill + Clever", "Prodigy + Clever" (https://clever.com/app-gallery, accessed 2026-10-24)
- "Clever provides a platform that enables Schools to securely provision the accounts with the third-party applications that they use." (https://clever.com/trust/privacy/policy, accessed 2026-10-24)
- Applications are launched from the Clever portal or by SSO and receive rostered data; Khan Academy, for example, describes "our free Clever Library integration" and a "Clever Instant Login link" (https://support.khanacademy.org/hc/en-us/articles/360055408251-Can-I-access-Khan-Academy-from-my-school-LMS-using-the-Clever-instant-login-link, accessed 2026-10-24). Clever's own docs state: "Clever no longer offers Clever Library integrations." (https://dev.clever.com/docs/what-is-clever.md, accessed 2026-10-24)

## Gaps
- https://support.clever.com/hc/s/articles/203115007 returned only a shell to a direct request; read in a browser instead.
- The App Gallery is rendered partly client-side; only a few app names were present in the served HTML, and individual app pages were not opened.
- No public list of the specific OAuth scopes an application can request was found on the pages opened.
