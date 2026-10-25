# Dossier: Edpuzzle (Edpuzzle, Inc.)
Frame stratum: 5.4   Evidence collected: 2026-10-24   Collector: stratum-5.4 agent B
Frame source: Instructure, The Edtech Top 40: K-12 Edtech Engagement During the 2025-26 School Year, entry 'Edpuzzle' (list is alphabetical, unranked)

Method note: edpuzzle.com pages are behind a JavaScript/AWS WAF challenge, so curl returned only a shell; https://edpuzzle.com/ and https://edpuzzle.com/privacy were opened in a headless browser (Playwright) and their rendered text was saved. support.edpuzzle.com article pages returned HTTP 403 to curl; article text was retrieved from the help center's public Zendesk Help Center JSON (/api/v2/help_center/en-us/articles/<id>.json and /api/v2/help_center/articles/search.json), and the URL cited for each quote is the article's own html_url from that JSON.

## Identity
- "Everything you need to engage your students all in one place, now from video learning and beyond." (https://edpuzzle.com/, accessed 2026-10-24)
- "Edpuzzle is a simple, easy-to-use educational platform that helps teachers engage their students." (https://edpuzzle.com/privacy, accessed 2026-10-24)
- "Edpuzzle is an online learning platform targeted at teachers and educational institutions (or other organizations engaged in teaching or training)." (https://support.edpuzzle.com/hc/en-us/articles/360012390292-Obtaining-parental-consent, accessed 2026-10-24)
- "This Policy applies to all products and services offered by Edpuzzle, Inc. (hereinafter referred to as “Edpuzzle,” “we,” “us,\" “our,” also including our subsidiaries or affiliates)." (https://edpuzzle.com/privacy, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages listed in this dossier.

## E1 Sequencing / scheduling evidence
Teacher-assigned lessons:
- "It lets students view interactive lessons -assigned by their teacher- either in class or at home." (https://support.edpuzzle.com/hc/en-us/articles/360012390292-Obtaining-parental-consent, accessed 2026-10-24)
- "We have guardrails in place, including highly advanced content moderation filters and the added layer of protection that students can only watch videos assigned by their teachers." (https://support.edpuzzle.com/hc/en-us/articles/360024281491-What-is-Edpuzzle, accessed 2026-10-24)
Recommended follow-up activities (teacher-approved):
- "Once assignment insights are collected, Edpuzzle recommends follow-up tasks based on where the class encountered challenges. With one click, you can generate a short reinforcement quiz or a bite-sized reading that reviews the tricky concepts, preview it, and assign it - no building from scratch!" (https://support.edpuzzle.com/hc/en-us/articles/47169208533005-Edpuzzle-Supported-Assignments, accessed 2026-10-24)
- "Determining next steps, such as re-teaching or targeted student grouping." (https://support.edpuzzle.com/hc/en-us/articles/47169208533005-Edpuzzle-Supported-Assignments, accessed 2026-10-24)
Adaptive or automatic sequencing of learner activities: none found on the pages listed in this dossier.

## E2 Interfaces evidence
LMS integrations (LTI 1.1 consumer key/secret pattern):
- "Search for the Edpuzzle app in the App Center (type it in the search bar or scroll down until you find it), and click on it." (https://support.edpuzzle.com/hc/en-us/articles/360025042091-Using-Edpuzzle-With-Canvas, accessed 2026-10-24)
- "Now you'll need two pieces of information: the consumer key and shared secret." (https://support.edpuzzle.com/hc/en-us/articles/360025042091-Using-Edpuzzle-With-Canvas, accessed 2026-10-24)
- "In the Integrations section, click on “Register LTI 1.1 Provider” under “LTI Tool Providers”." (https://support.edpuzzle.com/hc/en-us/articles/360030651332-Using-Edpuzzle-With-Blackboard, accessed 2026-10-24)
- "Click on the blue \"Install LTI\" button and choose \"I agree\" from the pop-up window." (https://support.edpuzzle.com/hc/en-us/articles/360027999011-Using-Edpuzzle-With-Schoology, accessed 2026-10-24)
- "Enter your Consumer Key in the LTI Key field and Shared Secret in the LTI Secret field." (https://support.edpuzzle.com/hc/en-us/articles/9477304852621-Using-Edpuzzle-with-D2L-Brightspace, accessed 2026-10-24)
Grade passback:
- "For Google Classroom, Microsoft Teams, Canvas, Schoology, Moodle, and D2L Brightspace:" followed by "Grades are exported automatically for all the assignments you create directly from your LMS." (https://support.edpuzzle.com/hc/en-us/articles/360025265811-How-do-I-export-grades-to-my-LMS, accessed 2026-10-24)
- "Best of all, once students complete the lessons, their grades will automatically sync with Canvas!" (https://support.edpuzzle.com/hc/en-us/articles/360025042091-Using-Edpuzzle-With-Canvas, accessed 2026-10-24)
- "Grades are exported automatically for your students when they complete an assignment and you grade all of their answers." (https://support.edpuzzle.com/hc/en-us/articles/360045702451-How-do-I-export-grades-to-Google-Classroom, accessed 2026-10-24)
Google Classroom add-on:
- "With this first integration method, your IT admin will install the Edpuzzle add-on for your school/district and you’ll create and manage your assignments directly from Google Classroom." (https://support.edpuzzle.com/hc/en-us/articles/10617629370765-Integrating-with-Google-Classroom, accessed 2026-10-24)
Privacy policy mention of LTI:
- "for authentication purposes we may collect and process information related to this kind of use of the Service, such as your school user ID, your profile picture, information on the LMS interface and the LTI version used and/or your school domain name." (https://edpuzzle.com/privacy, accessed 2026-10-24)
Public developer API documentation, LTI 1.3, OneRoster, and other named standards: none found on the pages listed in this dossier.

## E3 Learner model evidence
- "If you assigned video lessons with questions, you'll want to see the grade that each student got in each video, which is exactly what Edpuzzle shows." (https://support.edpuzzle.com/hc/en-us/articles/360007261212-How-does-the-Gradebook-work, accessed 2026-10-24)
- "Under each grade, you'll see a thin line showing the percentage of the video watched by that student." (https://support.edpuzzle.com/hc/en-us/articles/360007261212-How-does-the-Gradebook-work, accessed 2026-10-24)
- "Insights automatically analyze student performance to provide you with an at-a-glance summary of class progress, identifying who is struggling and why." (https://support.edpuzzle.com/hc/en-us/articles/47169208533005-Edpuzzle-Supported-Assignments, accessed 2026-10-24)
- "To provide teachers with AI-assisted teacher-support and advanced analytics features, where enabled by the school, district, or authorized teacher, including features that generate teacher-facing summaries about student progress, class performance patterns, and common learning gaps based on assignment responses, grades, attempts, and related lesson context, in order to support instructional review" (https://edpuzzle.com/privacy, accessed 2026-10-24)
Skill/mastery or knowledge-state model, and outside vendors' tools writing into one: none found on the pages listed in this dossier.

## E4 Data protection evidence
- "Those who use Google Workspace for Education and have students under the age of 18 will need to approve the use of Edpuzzle as a third-party app." (https://support.edpuzzle.com/hc/en-us/articles/360007745411-Connecting-your-Google-account, accessed 2026-10-24)
- "If Edpuzzle has not been approved by your Google Workspace admin, you and your students may not be able to access your Edpuzzle accounts." (https://support.edpuzzle.com/hc/en-us/articles/360007745411-Connecting-your-Google-account, accessed 2026-10-24)
- "Edpuzzle collects the minimal amount of information from students necessary to create accounts on our Service: we ask students to provide a unique username, a unique email (the student email is only collected when using our Service through an LMS integration or Single Sign-On solution), a password, their first and last name and a unique code they have been given by their teacher to join a class." (https://edpuzzle.com/privacy, accessed 2026-10-24)
- "Where available, certain advanced analytics or AI-assisted teacher features may be enabled or disabled by the school, district, or authorized teacher." (https://edpuzzle.com/privacy, accessed 2026-10-24)
- "Additionally, as discussed above, we will never sell or rent your personal information to advertisers or other third parties." (https://edpuzzle.com/privacy, accessed 2026-10-24)
- "Typically, schools are exempted from obtaining parental consent under FERPA when Edpuzzle is identified as a \"school official,\" meaning Edpuzzle is performing an institutional service or function for which the school would otherwise use its own employees." (https://support.edpuzzle.com/hc/en-us/articles/360012390292-Obtaining-parental-consent, accessed 2026-10-24)
- "This Policy does not apply to websites, services or practices of companies that Edpuzzle does not own or control, such as third-party services you might access through links or other features (e.g., social media buttons; third-party integrations) on the Service." (https://edpuzzle.com/privacy, accessed 2026-10-24)
Specific OAuth scope list, or per-tool permission controls over other apps inside Edpuzzle: none found on the pages listed in this dossier.

## E5 Third-party tools evidence
Third-party video content embedded in lessons:
- "Select the “YouTube” tab to browse videos only from YouTube, and use the channel filters at the top of the page to find content created by popular educational channels like Khan Academy, National Geographic, Crash Course, and more." (https://support.edpuzzle.com/hc/en-us/articles/360007501711-How-do-I-search-for-videos, accessed 2026-10-24)
- "We have a partnership with YouTube for Education, which means no ads, no tracking, and no distractions while they're learning from interactive educational videos." (https://support.edpuzzle.com/hc/en-us/articles/360024281491-What-is-Edpuzzle, accessed 2026-10-24)
- Specification sheet lists "YouTube" with purpose "Embed and play videos from YouTube" (https://support.edpuzzle.com/hc/en-us/articles/43214581166221-Edpuzzle-Specification-Sheet, accessed 2026-10-24)
Third-party integrations receiving content:
- "When, as a teacher, you use third-party apps, websites or other services that use, or are integrated with, our Service, they may receive information about the content you post or share." (https://edpuzzle.com/privacy, accessed 2026-10-24)
Edpuzzle running inside LMSs (reverse direction):
- "When your teacher has connected their LMS to Edpuzzle, video lessons will be posted to and viewed directly from the LMS." (https://support.edpuzzle.com/hc/en-us/articles/4422780214029-Using-Edpuzzle-with-your-LMS, accessed 2026-10-24)
App marketplace or plugin framework for independent developers' software tools inside Edpuzzle: none found on the pages listed in this dossier.

## Gaps
- https://edpuzzle.com/integrations (rendered "This page doesn't exist")
- https://trust.edpuzzle.com/ (Vanta trust center; JavaScript-only, not rendered; curl returned only the title)
- https://support.edpuzzle.com/hc/en-us/articles/... (HTTP 403 to curl; content read via Zendesk JSON API, see method note)
- No public developer or API documentation located.
- Edpuzzle LTI 1.3 support not documented in the articles opened (only LTI 1.1 consumer key/secret setups).
