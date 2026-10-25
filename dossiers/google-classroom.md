# Dossier: Google Classroom (Google)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

## Identity
- "The Google Classroom API provides a programming interface for software developers, administrators, and school leaders to manage Google Classroom resources." (https://developers.google.com/workspace/classroom/guides/get-started, accessed 2026-10-24)
- "Easily find, add, use and grade content with add-ons from popular EdTech tools, right within Classroom." (https://edu.google.com/workspace-for-education/classroom/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- No page opened describes Classroom deciding or sequencing what a learner does next across activities. Documented API use cases: "Managing courses, rosters, and guardians Adding assignments, announcements, and course materials Assigning grades and modifying grading settings Generating data for analysis Making content or tools from an outside provider discoverable and accessible within Classroom" (https://developers.google.com/workspace/classroom/guides/get-started, accessed 2026-10-24)
- "Teachers can select, assign, and grade third-party content within Google Classroom." (https://developers.google.com/workspace/classroom/add-ons, accessed 2026-10-24)

## E2 Interfaces evidence
- Classroom API (REST), described above. "Some Classroom API features are only available to users with particular Google Workspace for Education license types." (https://developers.google.com/workspace/classroom/guides/get-started, accessed 2026-10-24)
- "Classroom add-ons allow educators to integrate their favorite EdTech tools within the Google Classroom interface." and "These attachments open third-party content in iframes in Google Classroom. Developers create add-on applications distributed through Google Workspace Marketplace." (https://developers.google.com/workspace/classroom/add-ons, accessed 2026-10-24)
- "Classroom add-ons are available to all teachers with Teaching & Learning or Plus Google Workspace for Education licenses." (same URL, accessed 2026-10-24)
- LTI relationship: "Learning Tools Interoperability (LTI) is an open framework for building third-party integrations in learning management systems. While Classroom add-ons and LTI tools support similar user journeys, the two frameworks are not directly compatible." (https://developers.google.com/workspace/classroom/add-ons/get-started/addons-lti-comparison, accessed 2026-10-24)
- "LTI tools typically use HTTP POST to transmit payloads to an LTI platform, while Classroom add-ons create and retrieve resources using the Google Classroom REST API." and table rows "Post grades Assignment & Grade Services Patch CourseWork and AddOnAttachment student submissions" and "Read course rosters Names & Role Provisioning Services Retrieve Student and Teacher profiles in a course" (same URL, accessed 2026-10-24)
- The developer guide navigation lists "OneRoster for Student Information Systems" (https://developers.google.com/workspace/classroom/guides/get-started, accessed 2026-10-24); that page was not opened.
- "Learning goals in Classroom rely on stable globally unique identifiers (GUIDs) provided by the Satchel Rosetta Exchange (formerly CASE Network)." (https://developers.google.com/workspace/classroom/guides/manage-learning-goals, accessed 2026-10-24)
- Certification: not checked (1EdTech directory not queried). No vendor statement about 1EdTech certification was found on the pages opened.

## E3 Learner model evidence
- "Users can set learning goals for courses and assignments in Google Classroom. The same learning goals are also exposed in Classroom API. You can set, retrieve, and modify learning standard sets on Course resources and learning goals on CourseWork, CourseWorkMaterial, and Rubric resources." (https://developers.google.com/workspace/classroom/guides/manage-learning-goals, accessed 2026-10-24)
- "Preview: API support for learning standard sets on Courses and learning goals on CourseWork, CourseWorkMaterials, and Rubrics is now available as part of the Google Workspace Developer Preview Program. These features are available in V1_20260316_PREVIEW and later. We expect these features to be generally available in Classroom API in early Q4 2026." (same URL, accessed 2026-10-24)
- "Learning goals attached to a CourseWork, CourseWorkMaterial, or Rubric resource represent the standard or skills associated with that assignment, question, material, or specific rubric criterion." (same URL, accessed 2026-10-24). The page describes tagging content with standards; no per-student mastery record was described on the page.
- Grades written by add-ons: "You also pass a grade back to Google Classroom programmatically, which appears in the teacher's grade book as a draft grade." and "Modify the previous attachment creation requests to the Classroom API to also set the attachment's grade denominator. Programmatically score the student's submission and set the attachment's grade numerator." (https://developers.google.com/workspace/classroom/add-ons/walkthroughs/grade-passback, accessed 2026-10-24)
- Classroom analytics for admins: "View Classroom analytics to understand data such as assignment completion, grade trends, and Classroom adoption." (https://developers.google.com/workspace/classroom/guides/key-concepts/admin-actions, accessed 2026-10-24)

## E4 Data protection evidence
- "An authorization scope is an OAuth 2.0 URI string that contains the Google Workspace app name, what kind of data it accesses, and the level of access. ... When your app is installed, a user is asked to validate the scopes used by the app. Generally, you should choose the most narrowly focused scope possible and avoid requesting scopes that your app doesn't require." (https://developers.google.com/workspace/classroom/guides/auth, accessed 2026-10-24)
- Scope examples: "https://www.googleapis.com/auth/classroom.addons.teacher See, create, and update the requesting Google Cloud project's attachments to stream items in classes you teach in Google Classroom." and "https://www.googleapis.com/auth/classroom.addons.student See and update the requesting Google Cloud project's attachments to stream items in Google Classroom." (same URL, accessed 2026-10-24)
- "Administrators must configure third-party applications in the Google Admin console for users under 18. If an administrator has not configured an application, users under 18 will be unable to access that application with their Google Workspace for Education account." (https://developers.google.com/workspace/classroom/guides/key-concepts/admin-actions, accessed 2026-10-24)
- Under "Configured apps": "Apps configured with an access setting (Trusted, Limited, Specific Google data, or Blocked)." Under "Restricted": "Only internal and third-party apps configured with a Trusted or Specific Google data access setting can access data." (https://support.google.com/a/answer/7281227, accessed 2026-10-24)
- "If your public application uses scopes that permit access to certain user data, it must complete a verification process." (https://developers.google.com/workspace/classroom/guides/auth, accessed 2026-10-24)

## E5 Third-party tools evidence
- "We partnered with 20+ EdTech companies, including Kahoot!, Pear Deck, IXL, ReadWorks, and Nearpod, to build Google Classroom add-ons. Today, we're excited to make Classroom add-ons generally available to all developers." (https://workspaceupdates.googleblog.com/2024/06/google-classroom-add-ons-now-generally-available-for-developers.html, dated June 24, 2024, accessed 2026-10-24)
- "We partnered with 15+ EdTech companies to build custom add-ons, including Kahoot!, Pear Deck, IXL, and Nearpod." and "District admins must enable access to add-ons in order for educators to use these features." (https://workspaceupdates.googleblog.com/2022/08/classroom-add-ons.html, accessed 2026-10-24)
- "Add-ons let teachers and students experience your content without having to leave Google Classroom." (https://developers.google.com/workspace/classroom/add-ons, accessed 2026-10-24)
- "Google offers a Partner program for all Google Workspace for Education developers. We work closely with hundreds of developer partners to build a thriving EdTech ecosystem." (https://developers.google.com/workspace/classroom/guides/partnerships, accessed 2026-10-24)
- LMS-sync vendors also write to Classroom: "Clever LMS Connect enables Clever application partners to connect to a district's Canvas, Schoology, or Google Classroom instance." (https://ed.link/community/new-client-announcement-clever/, accessed 2026-10-24)

## Gaps
- https://developers.google.com/workspace/classroom/add-ons/overview and https://developers.google.com/workspace/classroom/add-ons/developer-guides/grade-passback returned 404 (the walkthrough URL above was used instead).
- https://edu.google.com/intl/ALL_us/workspace-for-education/add-ons/ returned 404. No current official list of add-on partners was found; the partner names above come from 2022 and 2024 Workspace Updates posts.
- The "OneRoster for Student Information Systems" guide and the Google for Education App Hub were not opened.
