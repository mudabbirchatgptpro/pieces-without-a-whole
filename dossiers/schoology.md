# Dossier: Schoology Learning (PowerSchool)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: support.schoology.com article URLs now redirect to PowerSchool's documentation site (uc.powerschool-docs.com/en/schoology/latest/...), which was used for help-center evidence.

## Identity
- "Collaboration is a key part of Schoology. If you've got an idea for a tool that will enrich the Schoology experience, use our developer resources to bring it to life!" (https://developers.schoology.com/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": the parent company's Schoology product page states "From home to classroom to central office, PowerSchool connects  every part of your district with the K-12 Connected Operating System." and carries the heading "THE K-12 CONNECTED OPERATING SYSTEM" (https://www.powerschool.com/classroom/schoology-learning/, accessed 2026-10-24). The phrase describes PowerSchool's product suite; no page opened applies it to Schoology alone.

## E1 Sequencing / scheduling evidence
- "Student Completion Rules are requirements placed on course folders and course materials that enable teachers to structure their course flow and create self-paced learning for students. Depending on the item type, the following requirements are available: Must complete Must view the item Must post a comment/reply Must make a submission Must score at least" (https://uc.powerschool-docs.com/en/schoology/latest/student-completion-rules, accessed 2026-10-24)
- "By default, the setting Requirements must be completed in sequential order is selected for top-level folders." (same URL, accessed 2026-10-24)
- "The order in which students must complete the items in the course depends on the order in which the folders and course materials are listed on the materials or within the folder." (same URL, accessed 2026-10-24)
- "Schoology does not trigger submission notifications, grading reminders, or overdue notifications for LTI and External Tool materials with grading enabled. Schoology cannot automatically detect submissions from these tools." (https://uc.powerschool-docs.com/en/schoology/latest/external-tools-add-and-grade, accessed 2026-10-24)
- No page opened states which completion-rule types apply to external tool materials.

## E2 Interfaces evidence
- REST API: "Realms are entities that have controllable privacy settings. Many objects can belong to any realm." (https://developers.schoology.com/api-documentation/rest-api-v1, accessed 2026-10-24)
- App platform: "When the user opens the application, Schoology sends along a SAML 2.0 package containing the user's Schoology ID, name, role, and more in a secure fashion." and "Once the user has been identified, your application can obtain a set of OAuth access tokens in order to communicate with the Schoology API." (https://developers.schoology.com/app-platform, accessed 2026-10-24)
- LTI: "While Schoology still currently supports LTI 1.1 we recommend you use LTI 1.3 for new app development." and "We are in compliance with the following IMS Specs, which LTI 1.3 App Developers must follow as well." (https://developers.schoology.com/app-platform/lti-apps, accessed 2026-10-24)
- "LTI Advantage Extensions The following are optional LTI services that we support." The services listed on the page include "Assignment and Grade Services v2.0", "Deep Linking v2.0" and "Names and Roles Services v2.0". (same URL, accessed 2026-10-24)
- "Learning Tools Interoperability (LTI) is a sign-on standard developed by IMS Global that allows web-based resources to be accessed from within a learning platform." and "Is the content compliant with LTI versions 1.0, 1.1, 1.2, or 1.3" (https://uc.powerschool-docs.com/en/schoology/latest/course-materials-external-tools, accessed 2026-10-24)
- Clever LMS Connect writes to Schoology: "Currently, the LMSs supported are Canvas, Schoology, and Google Classroom." (https://dev.clever.com/docs/api-v31.md, accessed 2026-10-24)
- Certification: not checked (1EdTech directory not queried). The vendor states compliance with "IMS Specs" (quoted above).

## E3 Learner model evidence
- "Align district learning objectives to personal resources, group resources, and all materials in a course allowing alignments, including assignments, assessments, tests, quizzes, discussions, pages, files, links, external tools, and grade columns." (https://uc.powerschool-docs.com/en/schoology/latest/align-and-grade-materials-with-the-standards-based-gradebook-and-district-mastery, accessed 2026-10-24)
- "When course materials are aligned with district learning objectives, the system automatically generates a grading rubric based on those objectives. You can evaluate the student's submission by each learning objective according to your district's mastery scale." (same URL, accessed 2026-10-24)
- "You must grade each aligned objective for the material. You cannot change the total or overall score for the material." and "When grading, select the grading rubric icon to enter a score for each aligned district objective." (same URL, accessed 2026-10-24)
- "After materials are aligned to objectives and submissions are graded, use the standards-based gradebook to evaluate students based on skill mastery and measure student learning while assessing the efficacy of instruction." (https://uc.powerschool-docs.com/en/schoology/latest/use-the-standards-based-gradebook-instructors, accessed 2026-10-24)
- "The student's point values or proficiency levels for each objective are based on the mastery grading scale set at the system level." (same URL, accessed 2026-10-24)
- External tool grading: "Enable grading on external tool items to add the material to your gradebook, allowing you to assign a grade for each student who completes the activity or assignment launched via the external tool." (https://uc.powerschool-docs.com/en/schoology/latest/external-tools-add-and-grade, accessed 2026-10-24)
- No page opened describes an external tool writing per-objective mastery scores (as distinct from an assignment grade) into the standards-based gradebook.

## E4 Data protection evidence
- External tool provider setting: "Privacy The information sent to the publisher upon the tool's launch"; setup checklist: "What personal information is required when launching an external tool? For example: User's name Email or username Both the user's name and their email or username" (https://uc.powerschool-docs.com/en/schoology/latest/course-materials-external-tools, accessed 2026-10-24)
- "System administrators can install the tool provider at the course or district level." (same URL, accessed 2026-10-24)
- LTI services: "You can enable any of these for your App, and as part of the installation process, organizations will be alerted that your app uses the enabled services." (https://developers.schoology.com/app-platform/lti-apps, accessed 2026-10-24)
- App Center: "Optionally, after selecting a course, make the app available only to the Course Admin." (https://uc.powerschool-docs.com/en/schoology/latest/app-center-instructors, accessed 2026-10-24)
- "PowerSchool places great importance and value on the proper handling of personal data that flows within our product as we provide services to our customers." (https://www.powerschool.com/classroom/schoology-learning/, accessed 2026-10-24)

## E5 Third-party tools evidence
- "Schoology's App Center provides instructors with access to software developed by other companies directly within Schoology. You can install apps directly into a course or group, or onto your Home Page." (https://uc.powerschool-docs.com/en/schoology/latest/app-center-instructors, accessed 2026-10-24)
- App platform: "it is an iFrame canvas which links to one or more pages on your application server." (https://developers.schoology.com/app-platform, accessed 2026-10-24)
- Documentation pages exist for third-party apps "Google Drive Assignments app", "OneDrive Assignments app (instructors)" and "Use the Microsoft Teams quick meet app" (page tree on https://uc.powerschool-docs.com/en/schoology/latest/app-center-and-partner-apps, accessed 2026-10-24)
- Formative (independent vendor): "Once installed, you will be able to create Schoology assignments that include formatives. Students will then be able to log in to Schoology to take formatives." and "You can pass grades back from Formative to Schoology's grade book, too!" (https://help.formative.com/en/articles/4496022-partner-schools-how-to-assign-a-formative-through-schoology, accessed 2026-10-24)
- Khan Academy (independent vendor): "Khan Academy now syncs directly with Canvas, Google Classroom, and Schoology for Clever districts." (https://blog.khanacademy.org/whats-new-for-the-2025-26-school-year-big-updates-from-khan-academy-districts, accessed 2026-10-24)

## Gaps
- https://support.schoology.com/hc/en-us/articles/201001113-System-Management-of-External-Tools-Enterprise- returned 404.
- The Schoology help center search API redirected to a PowerSchool login portal (customercentral.powerschool.com).
- No public App Center listing of partner apps was opened; the app-center index pages served only navigation text.
- The REST API v1 resource list (for any mastery or learning-objective endpoints) was not found on the served page.
