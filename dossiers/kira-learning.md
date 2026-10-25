# Dossier: Kira (Kira Learning)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentA

## Identity
- What it is, in the vendor's words:
  - "Kira runs instruction, assessment, and intervention as one connected system, replacing the tool sprawl that keeps educators from focusing on what actually works." (https://www.kira-learning.com/, accessed 2026-10-24)
  - "Kira is an AI-powered teaching platform that helps K–12 educators build lessons, support students, and save time on routine tasks" (https://support.kira-learning.com/en/articles/13825241-what-s-kira, accessed 2026-10-24)
- Self-description as "operating system" (reproduced from own fetch):
  - "The AI operating system for education" (https://www.kira-learning.com/, accessed 2026-10-24)
  - "Meet the New Kira. The AI operating system for education" (https://www.kira-learning.com/2.0-launch, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- Student next-task selection (own platform):
  - "Student Dashboard provides one place that tells every student exactly what to do next based on their learning journey" (https://www.kira-learning.com/blog/kira-latest-platform-updates-k12-instruction, accessed 2026-10-24)
  - "The dashboard’s prioritization feature leverages due dates and performance data to surface the single most important task, cutting decision fatigue for students" (same URL, accessed 2026-10-24)
  - "When a student completes an assessment in Kira, identified skill gaps automatically trigger personalized practice." (same URL, accessed 2026-10-24)
- Teacher-set progression rules:
  - "Progression Setting - students may only progress in a lesson once they have completed all activities in a step." (https://support.kira-learning.com/en/articles/16607596-advanced-assignment-settings, accessed 2026-10-24)
  - "Control the flow of assignments by requiring students to complete specific tasks before unlocking new ones." (https://www.kira-learning.com/product/integrated-classroom-management, accessed 2026-10-24)
- Scope relative to other tools:
  - "Kira can replace fragmented LMS, assessment, tutoring, and analytics tools." (https://www.kira-learning.com/blog/kira-latest-platform-updates-k12-instruction, accessed 2026-10-24)
  - "Kira operates alongside existing LMSs, curriculum, and district infrastructure today, and can absorb more of the stack over time." (https://www.kira-learning.com/, accessed 2026-10-24)

## E2 Interfaces evidence
- LTI 1.3 setup in Canvas (documented admin steps in help center):
  - "Creation of Developer LTI key." (https://support.kira-learning.com/en/articles/14125739-canvas-onboarding-steps, accessed 2026-10-24)
  - "OpenID Connect Initiation Url: https://app.kira-learning.com/api/lti/login" (same URL, accessed 2026-10-24)
  - "LTI Advantage services: Can view LTI registrations associated with the tool. Can view assignment data in the gradebook associated with the tool." (same URL, accessed 2026-10-24)
- Grade passback:
  - "it only syncs one total score for the whole assignment." (https://support.kira-learning.com/en/articles/16648857-grade-passback-with-canvas, accessed 2026-10-24)
- Rostering / SIS / LMS (vendor statements):
  - "It supports Clever and ClassLink for automated roster and student syncing." (https://support.kira-learning.com/en/articles/13825241-what-s-kira, accessed 2026-10-24)
  - "Kira integrates seamlessly with existing SIS and LMS infrastructure like Canvas, PowerSchool, and Skyward." (https://www.kira-learning.com/blog/kira-latest-platform-updates-k12-instruction, accessed 2026-10-24)
- Certification: the homepage footer has a "Certifications" link pointing to a 1EdTech directory URL; per brief rule 6 it was not opened, and no vendor sentence describing the certification was found.
- No public Kira API or developer documentation found (see Gaps).

## E3 Learner model evidence
- Mastery model (vendor claim and help documentation):
  - "Every student response updates a living mastery model that drives grading, feedback, and what happens next." (https://www.kira-learning.com/, accessed 2026-10-24)
  - "Student Atlas uses graded work on questions tagged with standards and difficulty levels." (https://support.kira-learning.com/en/articles/16775763-student-atlas-and-progress-data, accessed 2026-10-24)
  - "Each skill gets one of six mastery levels, based on two things:" (same URL, accessed 2026-10-24)
  - "A standard's level is the median of its skills' levels." (same URL, accessed 2026-10-24)
- Skills generated from district standards:
  - "Once a collection is published, Kira automatically generates the underlying skills so that content created in your organization is aligned to those standards" (https://support.kira-learning.com/en/articles/16043087-organizations-standards-management, accessed 2026-10-24)
- Assessment results feed profiles (Kira's own ACT practice):
  - "ACT results instantly update student profiles, flag skill gaps, and auto-generate targeted practice for improvement." (https://www.kira-learning.com/blog/kira-latest-platform-updates-k12-instruction, accessed 2026-10-24)
- No documentation found of outside vendors' tools writing into Student Atlas.

## E4 Data protection evidence
- Per-feature admin controls, with grade/class exclusions:
  - "The new Features & AI tab in Settings is where you control which tools your organization's teachers and students can access" (https://support.kira-learning.com/en/articles/17121677-managing-ai-tools-in-kira, accessed 2026-10-24)
  - "Disabled means the feature is completely hidden from the product for everyone in your organization." (same URL, accessed 2026-10-24)
  - "AI Tutor, which supports excluding either grades or classes" (same URL, accessed 2026-10-24)
- Roles:
  - "Assign and adjust user roles with precision, ensuring educators and administrators have the right level of access to tools, data, and features." (https://www.kira-learning.com/product/integrated-classroom-management, accessed 2026-10-24)
- Canvas API key configuration instruction:
  - "Enforce scopes: Keep it disable" (https://support.kira-learning.com/en/articles/14125739-canvas-onboarding-steps, accessed 2026-10-24)
- Policy-level statements:
  - "Student data remains under district control" (https://www.kira-learning.com/, accessed 2026-10-24)
  - "To our third-party service providers who use that information to help us provide our Services." (https://www.kira-learning.com/legal/coppa-statement, accessed 2026-10-24)

## E5 Third-party tools evidence
None found. Activity types documented are Kira's own (e.g. "Kira's Platypus coding activities use a style similar to block-based coding-style interfaces to introduce students to algorithms and programming." https://support.kira-learning.com/en/articles/11981976-using-platypus-coding-activities, accessed 2026-10-24). Looked at: https://support.kira-learning.com/en/articles/14078247-types-of-activities, https://www.kira-learning.com/product/integrated-classroom-management, https://www.kira-learning.com/sitemap.xml.

## Gaps
- https://help.kira-learning.com/ (no response / DNS); help center is at support.kira-learning.com.
- No developer/API pages listed in https://www.kira-learning.com/sitemap.xml; no LTI, OneRoster, Caliper or xAPI mention outside the Canvas LTI onboarding article.
- 1EdTech certification link on homepage footer not opened (brief rule 6).
- Privacy pages checked: https://www.kira-learning.com/legal/privacy, https://www.kira-learning.com/legal/coppa-statement.
