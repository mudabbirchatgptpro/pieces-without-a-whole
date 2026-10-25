# Dossier: MagicSchool (Magic School, Inc.)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentA

## Identity
- What it is, in the vendor's words:
  - "Save time, spark creativity, and support every student with safe, district-aligned AI." (https://www.magicschool.ai/, accessed 2026-10-24)
  - "An AI education platform for every classroom and learner" (https://www.magicschool.ai/, accessed 2026-10-24)
- Self-description as "operating system" (reproduced from own fetch):
  - "The AI Operating System for Schools Bringing teaching, learning, and guidance into one connected, district-ready platform." (https://www.magicschool.ai/ai-operating-system-for-schools, accessed 2026-10-24)
  - "One connected AiOS education platform for teaching and learning, built for trust and scale." (https://www.magicschool.ai/ai-operating-system-for-schools, accessed 2026-10-24)
  - "The AI Operating System for Schools We're bringing AI tools and workflows together in one safe, centralized platform built specifically for schools." (https://www.magicschool.ai/, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- Quiz results surface follow-up resources (own tools):
  - "Next Steps: the quiz results dashboard surfaces a curated set of follow-up resources based on quiz context, including relevant Student Rooms and Teacher Tools" (https://help.magicschool.ai/en/articles/13540346-quizzes, accessed 2026-10-24)
- Roadmap items listed under "WHAT’S NEXT?" on the OS page:
  - "Knowledge Graph Connects standards, lessons, assessments, and students" (https://www.magicschool.ai/ai-operating-system-for-schools, accessed 2026-10-24)
  - "so MagicSchool can explain why learning is happening and recommend what’s next, not just what." (https://www.magicschool.ai/ai-operating-system-for-schools, accessed 2026-10-24)
  - "Personalized learning profiles AI interactions tailored to each student’s level, activity, and learning needs" (https://www.magicschool.ai/ai-operating-system-for-schools, accessed 2026-10-24)
- Teacher scheduling of student access:
  - Help article title: "How to Schedule Start/End Times for Student Rooms" (https://help.magicschool.ai/en/articles/10671787-student-insights-understanding-engagement-and-progress-in-real-time, accessed 2026-10-24, listed under Related Articles)

## E2 Interfaces evidence
- LMS / SSO integrations (help center, documented setup steps):
  - "MagicSchool integrates with the following LMS platforms: Canvas, Schoology, Clever, and Classlink. All integrations are available to Enterprise partners only." (https://help.magicschool.ai/en/articles/14648845-what-lms-platforms-does-magicschool-integrate-with, accessed 2026-10-24)
  - "Add MagicSchool as an App on the Classlink Roster Server so user data is shared with MagicSchool." (same URL, accessed 2026-10-24)
  - "Add MagicStudent Rooms as course materials, streamline student access and review student work with SpeedGrader." (https://www.magicschool.ai/integrations, accessed 2026-10-24)
  - "Launch MagicStudent directly within the LMS with no additional tabs, access codes, or separate logins." (https://www.magicschool.ai/integrations, accessed 2026-10-24)
  - "Single Sign-On via Edlink: One login to rule them all." (https://www.magicschool.ai/blog-posts/schoology-integration, accessed 2026-10-24)
- Rostering through an intermediary:
  - "MagicSchool connects to your district's SIS through Edlink , MagicSchool's rostering provider." (https://help.magicschool.ai/en/articles/15634475-rostering, accessed 2026-10-24)
- One-way MCP connector (inbound from Claude):
  - "MCP stands for Model Context Protocol, an open standard that lets an AI assistant connect to outside applications. Today the MagicSchool connector works only with Claude, including Claude for Teachers." (https://help.magicschool.ai/en/articles/15786767-using-the-magicschool-connector, accessed 2026-10-24)
  - "Data moves in one direction only, from Claude into MagicSchool." (same URL, accessed 2026-10-24)
- Standards data sources (CASE):
  - "MagicSchool instead retrieves standards from established standards databases (Common Standards Project and the 1EdTech CASE Network), refreshed on a weekly automated schedule with manual review to keep entries accurate." (https://help.magicschool.ai/en/articles/12454976-how-magicschool-keeps-standards-up-to-date, accessed 2026-10-24)
- Vendor-claimed certification (not checked against the 1EdTech directory):
  - "MagicSchool is a proud supporter of the 1EdTech TrustEd Apps Pledge and holds the 1EdTech TrustEd Apps Certification" (https://www.magicschool.ai/privacy/trust, accessed 2026-10-24)
  - "Top-ranked by Common Sense Media GDPR safeguards 1EdTech certified FERPA compliant COPPA compliant SOC 2 compliant" (https://www.magicschool.ai/privacy, accessed 2026-10-24)
- No page found naming LTI, OneRoster, Caliper, xAPI, QTI, Common Cartridge, Ed-Fi, CLR or Open Badges; no public developer/API documentation found (see Gaps).

## E3 Learner model evidence
- Engagement summaries and output history (Student Rooms):
  - Under "Thread summaries": "An overview of student interactions with tools, categorizing engagement as highly engaged, moderately engaged, minimally engaged, or distracted." (https://help.magicschool.ai/en/articles/10671787-student-insights-understanding-engagement-and-progress-in-real-time, accessed 2026-10-24)
  - "Generate a summary of a student's activity, highlighting strengths, areas for improvement, and suggestions for teacher engagement." (same URL, accessed 2026-10-24)
- Quiz results:
  - "View real-time student results and class-level insights" (https://help.magicschool.ai/en/articles/13540346-quizzes, accessed 2026-10-24)
- Knowledge graph and learner profiles are listed as future items under "WHAT’S NEXT?" (see E1 quotes).
- Outside writes: the only documented inbound path is the Claude MCP connector, which saves teacher content:
  - "The connector only saves new content that you choose to import into MagicSchool." (https://help.magicschool.ai/en/articles/15786767-using-the-magicschool-connector, accessed 2026-10-24)

## E4 Data protection evidence
- Org-level tool toggles:
  - "Toggle access on or off for specific tools for teachers and students within your organization." (https://help.magicschool.ai/en/articles/9940123-can-i-manage-which-tools-are-available-to-educators-and-students-in-my-organization, accessed 2026-10-24)
  - "Controls whether teachers and/or students can export the full content of student conversation threads out of MagicSchool." (https://help.magicschool.ai/en/articles/16786795-features-that-can-be-enabled-disabled-for-your-organization, accessed 2026-10-24)
- Connector scope and admin switch:
  - "The connector is import-only. It does not allow Claude to view or use existing MagicSchool content, student or classroom data, connected school systems, or district knowledge." (https://help.magicschool.ai/en/articles/15786767-using-the-magicschool-connector, accessed 2026-10-24)
  - "Org Admins can turn it on or off themselves from My Organization > Tools" (https://help.magicschool.ai/en/articles/16786795-features-that-can-be-enabled-disabled-for-your-organization, accessed 2026-10-24)
- Rostering-provider sharing controls (set in Clever/ClassLink):
  - "set sharing permissions to determine which schools, teachers and students to share with MagicSchool" (https://help.magicschool.ai/en/articles/14648845-what-lms-platforms-does-magicschool-integrate-with, accessed 2026-10-24)
  - "Select Permissions Type: Rule-Based or Full Permissions" (same URL, accessed 2026-10-24)
  - "MagicSchool only syncs data your district explicitly sends. Rostering is COPPA and FERPA compliant, and teachers can only see data for the students in their own classes." (https://help.magicschool.ai/en/articles/15634475-rostering, accessed 2026-10-24)
- Third-party AI vendors (policy level):
  - "We utilize application program interfaces ("API") to power the AI functionality of our Services from multiple AI vendors. A current list of these vendors can be found in our subprocessors list ." (https://www.magicschool.ai/privacy-security/privacy-policy, accessed 2026-10-24)
  - "Third-party AI providers are contractually prohibited from storing or using your data to train their models." (https://help.magicschool.ai/en/articles/9940161-how-is-my-data-used-inside-magicschool, accessed 2026-10-24)

## E5 Third-party tools evidence
- Adobe image generator inside MagicSchool (help collection "Adobe Image Generator Support"):
  - "How Can I Sign My Students Up for an Adobe Express Account for Free?" (https://help.magicschool.ai/en/collections/10538720-adobe-image-generator-support, accessed 2026-10-24)
  - "You can use the Image Generator without an Adobe account by continuing as a guest." (https://help.magicschool.ai/en/articles/11910883-can-i-use-the-image-generator-without-signing-in-to-adobe, accessed 2026-10-24)
- Anthropic Claude as an external source writing into the Resource Library (see E2/E4):
  - "The MagicSchool MCP connector lets you save teaching content you created in Anthropic’s Claude directly into your MagicSchool Resource Library" (https://help.magicschool.ai/en/articles/15786767-using-the-magicschool-connector, accessed 2026-10-24)
- LMS submission import (data sync from Canvas/Schoology/Drive/OneDrive):
  - "Allow teachers to import student submissions directly from Canvas." (https://help.magicschool.ai/en/articles/16786795-features-that-can-be-enabled-disabled-for-your-organization, accessed 2026-10-24)
  - "There is no option to share feedback directly back to students in Canvas or Schoology." (https://help.magicschool.ai/en/articles/15235553-class-writing-feedback-canvas-schoology-integrations, accessed 2026-10-24)
- No marketplace or developer program for independent tools found.

## Gaps
- https://www.magicschool.ai/developers (404).
- https://www.magicschool.ai/privacy-security/sub-processors (404); the sub-processor list is linked as https://go.magicschool.ai/sub-processors (not opened).
- No public API, developer portal or app marketplace located via sitemap.xml (https://www.magicschool.ai/sitemap.xml) or the help center collections (LMS & SSO Integrations, Data Privacy & Security, Platform Features & Customization, Student Rooms & Teacher Tools, District Admin Resources).
- Searched trust, privacy policy, student data policy, integrations and help pages for LTI, OneRoster, Caliper, xAPI: no matches.
