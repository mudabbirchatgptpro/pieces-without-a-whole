# AI integration audit (RQ3, prediction P3): evidence dossier

Collected 2026-10-24 and 2026-10-25 for the pre-registered study "Pieces Without a Whole" (PREREGISTRATION.md, sections 3 (P3), 5.3 and 7). Evidence only; no coding.

## Method and rules followed

- Every quotation below comes from a page I opened in full, not from a search snippet. Raw page text sits in `study/research/ai_scratch/pages/` under the file name given in brackets.
- How each site was read: plain HTTP fetch for most vendor pages. The OpenAI Help Center blocks scripted fetches, so I opened it in a headless browser. The Khan Academy and Brisk help centers (Zendesk) and the Instructure Community (Vanilla) were read through each platform's public JSON article API. That API returns the same article body and URL the public page shows.
- I did not query the 1EdTech certification directory. 1EdTech material comes only from its own published announcements and its public draft.
- What counts as P3 "learner evidence": mastery, competency or learning-activity data, not only a numeric grade. A record that "other vendors' tools can read through an open standard" means one of CLR, Caliper, xAPI, Open Badges, CASE-aligned assertions or Ed-Fi.
- Write levels, per section 7: **none**; **own store**; **one platform's store** (for example an LMS gradebook); **cross-vendor open record**.
- I searched adversarially for refuting evidence. Searches and site searches run: "Khanmigo Caliper", "MagicSchool xAPI", "SchoolAI LTI", "Claude Canvas LTI grade", "Gemini Classroom grade export", "Instructure IgniteAI outcomes mastery". I also searched the OpenAI Help Center for "Canvas", "LTI", "Google Classroom" and "Clever". The Khan Academy help center was searched for "LTI", "Canvas" and "Schoology", and the MagicSchool and SchoolAI help centers for "grade", "export", "mastery", "standards" and "Caliper". Searches that returned nothing are reported where they matter.

---

## 1. Claude for Education (Anthropic), including Claude for Teachers, the Canvas LTI and MCP connectors

**Q1. How it connects to schools.**
- SSO plus JIT or SCIM provisioning. "Set up single sign-on (SSO)" and "Set up JIT or SCIM provisioning". Source: https://support.claude.com/en/articles/11139094-get-started-with-claude-for-education-at-your-university-for-owners-admins (accessed 2026-10-24) [claude_getstarted].
- Canvas LTI 1.3. The setup article says "Enter a short description for the Canva LTI 1.3 app" (sic). It lists "OpenID Connect Initiation Url: https://claude.ai/api/lti/login" and "JWK method: https://claude.ai/api/lti/keys". It recommends "adding 'Course Navigation' and 'Assignment Edit' as the options". Admins then go to "Organization settings > Connectors. Find Canvas and click 'Enable.'" Source: https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure (dated March 16, 2026; accessed 2026-10-24) [claude_lti]. The article covers launch only. It names no Assignment and Grade Services (AGS), grade passback or Names and Roles service.
- Announcement: "Claude now supports Canvas LTI (Learning Tools Interoperability), allowing students to use Claude directly within their Canvas courses without switching between platforms." It adds: "Students and educators will be able to connect Wiley and Panopto to Claude using pre-built MCP servers." Source: https://www.anthropic.com/news/advancing-claude-for-education (accessed 2026-10-24) [anth_adv].
- K-12 MCP connectors (Claude for Teachers). "Claude for Teachers connects to Learning Commons, giving Claude access to academic standards across all 50 states." Connectors are listed in the same post: "ASSISTments: Generate auto-scored, standards-aligned math problems for practice and assessment." "Brisk Teaching: Create interactive student activities and standards-aligned lessons". "MagicSchool: Make instructional content classroom-ready." "Snorkl: Get insights about your classes, assignments, and student progress to inform your instruction." Source: https://www.anthropic.com/news/claude-for-teachers (accessed 2026-10-24) [anth_teachers].
- District setup: "standard Enterprise admin controls (verified domains, SSO, automatic account creation, roles, usage, and the Compliance API)". Also: "Claude for Teachers is for educators, not students. Student accounts aren't part of this offering." Source: https://support.claude.com/en/articles/16559896-set-up-claude-for-teachers-for-your-school-or-district (accessed 2026-10-24) [claude_teachers].

**Q2. What it writes back and where.**
- Conversations and files stay in Claude's own store, exportable only by the institution on request. "On Claude for Education, by default, the following capabilities are disabled by default: Primary Owner Data Exports". The article adds that an export "may contain your conversations with Claude, uploaded files, and usage patterns." Source: https://support.claude.com/en/articles/11732894-who-owns-and-manages-the-data-of-my-claude-for-education-account (accessed 2026-10-24) [claude_data].
- Writes into another vendor's store happen only for teaching content, and only through MCP. The MagicSchool connector page (vendor documentation for the Claude side) says: "The MagicSchool MCP connector lets you save teaching content you created in Anthropic's Claude directly into your MagicSchool Resource Library". It also says: "The connector is import-only. It does not allow Claude to view or use existing MagicSchool content, student or classroom data". Source: https://help.magicschool.ai/en/articles/15786767-using-the-magicschool-connector (accessed 2026-10-24) [msch_connector]. The ASSISTments connector likewise creates problems (content), not learner evidence.
- No opened page documents Claude writing grades, mastery or activity data to Canvas or to any learner record.

**Q3. Learner model.** None documented. The Learning Commons connector supplies standards and "the smaller learning competencies it's built from and the order students typically learn them" [anth_teachers]. That is a curriculum graph Claude reads, not a model of an individual learner.

**Q4. Plans and standards.** Anthropic's 2025 launch says: "We're proud to join Internet2". It lists "working with Instructure to embed AI into teaching & learning with Canvas LMS". Source: https://www.anthropic.com/news/introducing-claude-for-education (accessed 2026-10-24) [anth_edu]. No opened Anthropic page mentions 1EdTech membership, Caliper, CLR, xAPI or Open Badges.


---

## 2. ChatGPT Edu and ChatGPT for Teachers (OpenAI)

**Q1. How it connects.**
- ChatGPT Edu: "Robust security, data privacy, and administrative controls such as group permissions, SSO, SCIM, and GPT management". Source: https://help.openai.com/en/articles/9377311-chatgpt-edu-at-openai (opened in browser 2026-10-25) [oai_edu].
- ChatGPT for Teachers: "If you're an admin, you can then invite other verified educators in your district and configure SSO, roles, and other workspace settings." The page adds: "Note: This plan is not for students. Student accounts and student-facing features may come later." Features listed include "File uploads, apps, file search, and deep research" and "Memory for more personalized, consistent help". Source: https://help.openai.com/en/articles/12844995-chatgpt-for-teachers (opened 2026-10-25) [oai_teachers].
- No LMS integration is documented. Help Center searches for "Canvas", "LTI" and "Clever" returned no LMS or rostering article. The closest OpenAI material is a do-it-yourself cookbook for a Canvas REST API custom action: https://developers.openai.com/cookbook/examples/chatgpt/gpt_actions_library/gpt_action_canvas [oai_canvas_cookbook].
- Education plugins (release notes, August 2026): "College Educator: Helps faculty design and update courses and syllabi ... and package content for their LMS. K–12 Educator: Helps teachers create lesson materials, assignments, rubrics, and instructional resources, with Learning Commons context". Source: https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes (opened 2026-10-25) [oai_more].
- MCP: "Connecting custom MCP servers in ChatGPT" is a general article (title seen in the help center search), not education-specific. Brisk documents a "ChatGPT plugin" that creates Brisk activities (see section 8).

**Q2. Writes.** Own store. "Members request and download their own exports from their own accounts. Each member can export only their own data." Source: https://help.openai.com/en/articles/20001279-exporting-data-from-a-chatgpt-edu-workspace (opened 2026-10-25) [oai_more].
- Related but not ChatGPT Edu: Instructure's LLM-Enabled Assignment runs on OpenAI models inside Canvas and writes evidence to the Canvas Gradebook. That product belongs to Instructure and is coded under IgniteAI (section 4). The joint release says: "The learner information remains private to the Canvas user and is not shared with OpenAI." Source: https://www.nasdaq.com/press-release/instructure-and-openai-announce-global-partnership-embed-ai-learning-experiences (July 23, 2025; accessed 2026-10-24) [inst_openai_nasdaq].

**Q3. Learner model.** None documented. "Memory" personalizes the assistant; it is not a skills or mastery model. Study mode and flashcards exist (Help Center article titles) with no mastery export.

**Q4. Plans and standards.** No opened OpenAI page mentions 1EdTech, Caliper, CLR, xAPI, Open Badges or LTI.


---

## 3. Gemini for Education and Gemini in Google Classroom (Google), including NotebookLM / Gemini Notebook, the Classroom API and grade export

**Q1. How it connects.**
- Native to Google Workspace for Education and Classroom. Gemini in Classroom is "available to all educators with Google Workspace for Education accounts, free of charge" and "includes more than 30 new features". Source: https://blog.google/products-and-platforms/products/education/classroom-ai-features/ (accessed 2026-10-24) [g_blog_ai].
- Student access: "Starting August 10, 2026, Gemini in Classroom will also be made available to K-12 and higher education students of all ages who have already been granted access to Gemini in Classroom, Gemini and Gemini Notebook by their admin". Source: https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html (accessed 2026-10-24) [g_wu_students].
- Classroom MCP server (developer preview). "Google Classroom offers a remote Model Context Protocol (MCP) server that allows AI agents to securely interact with Google Classroom data." It says AI applications "like Google Antigravity and Claude" can "Read data: List courses, retrieve course content and metadata, and view submissions and grades" and "Take action: Create and update coursework and announcements." Tools include "create_course_work_rubric" and "search_course_standards". Source: https://developers.google.com/workspace/classroom/guides/mcp/configure-mcp-server (accessed 2026-10-24) [g_mcp].
- SIS rostering and grade export use OneRoster. The admin article says "Select OneRoster 1.2." and "Set up Google as a OneRoster Partner Vendor". Source: https://support.google.com/edu/classroom/answer/9356588?hl=en (accessed 2026-10-24) [g_sis_admin]. Teacher FAQ: "Grades must be in a returned state. Draft grades don't export to your SIS." Source: https://support.google.com/edu/classroom/answer/9476458?hl=en [g_sis_faq].

**Q2. What Gemini writes and where (Classroom store).**
- Feedback drafts: "educators can select 'Help me write' to have Gemini suggest written feedback for the assignment. Teachers can then review, edit, and refine before sharing with students". Source: https://workspaceupdates.googleblog.com/2026/02/educators-now-get-help-drafting-personalized-guidance-on-written-assignments-with-AI.html (accessed 2026-10-24) [g_wu_feedback].
- Rubrics: "generate a new Classroom-ready rubric with help from Gemini based on their assignment. Educators can review and edit the proposed rubric criteria before adding it to the assignment". Source: https://workspaceupdates.googleblog.com/2026/08/streamlining-rubric-generation-in-Google-Classroom-with-Gemini.html (August 5, 2026; accessed 2026-10-24) [g_wu_rubric].
- CASE-tagged learning goals with AI suggestion, May 2026. "Google Classroom now allows educators to tag coursework and rubrics with learning goals ... educators can search for available, established standards and skills or click on suggested goals, which use AI to analyze assignment and course content. By tagging coursework with these goals, teachers can view analytics that visualize student performance". The same post: "Learning standards from around the world are made available in Classroom through partnerships with 1EdTech and Common Good Learning Tools ... that leverage the 1EdTech® Competencies and Academic Standards Exchange® (CASE®) standard specification." Source: https://workspaceupdates.googleblog.com/2026/05/keep-track-of-student-progress-with-learning-standards-and-skills-in-Google-Classroom.html (accessed 2026-10-24) [g_wu_standards].
- Classroom API exposure of standard-tagged evidence (this is Classroom, not Gemini). "Learning goals in Classroom rely on stable globally unique identifiers (GUIDs) provided by the Satchel Rosetta Exchange (formerly CASE Network)." "Learning goals attached to a CourseWork, CourseWorkMaterial, or Rubric resource represent the standard or skills associated with that assignment, question, material, or specific rubric criterion." "Each Rubric Criterion can have 1 learning goal." Source: https://developers.google.com/workspace/classroom/guides/manage-learning-goals (accessed 2026-10-24) [g_api_goals]. The rubric guide adds: "a student submission graded with a rubric has draftRubricGrades and assignedRubricGrades properties ... For now, these properties are read-only. This means that the API can't be used to grade submissions, but you can read submissions graded in the Classroom UI." Source: https://developers.google.com/workspace/classroom/rubrics/limitations (accessed 2026-10-24) [g_rub_lim].

**Q3. Learner model.** Classroom (not Gemini) keeps standards-tagged performance analytics [g_wu_standards]. Per-criterion rubric grades are readable by any authorized Classroom API client, and each criterion can carry one CASE GUID [g_api_goals, g_rub_lim]. Gemini's role is upstream: it suggests goals, drafts rubrics and drafts feedback. No opened page documents a Gemini-owned mastery model.

**Q4. Plans and standards.** Google names a 1EdTech partnership for CASE content [g_wu_standards]. The Classroom MCP server is in developer preview [g_mcp]. No opened page mentions Caliper, CLR, xAPI or Open Badges for Gemini or Classroom.




---

## 4. IgniteAI and the IgniteAI Agent (Instructure)

**Q1. How it connects.** Native to Canvas, opted in through feature options. "This guide applies to institutions that have opted in for IgniteAI related feature options." Source: https://community.instructure.com/en/kb/articles/664510-what-are-the-available-ai-features-in-canvas (updated 2026-09-30; accessed 2026-10-24) [inst_664510]. MCP is planned in two directions:
- Partner agents into IgniteAgent: "Using the Model Context Protocol (MCP) standard, trusted partners can seamlessly integrate their own agents and workflows". Source: https://community.instructure.com/en/discussion/651284/product-announcements-from-instructurecon-2025 (July 31, 2025; accessed 2026-10-24) [icon25].
- Canvas as an MCP server for outside assistants: "We're building an MCP server for Canvas, so that the AI assistants your institution already uses can work with and in Canvas". The post asks whether an assistant should "only read and suggest, or can it also act, such as posting a grade". Source: https://community.instructure.com/en/discussion/667483/mcp-explained-how-ai-assistants-can-connect-and-work-in-your-tools (October 19, 2026; accessed 2026-10-24) [inst_667483].
- Current limit: the agent "can't yet route tasks to other IgniteAI tools, connect to question banks, or integrate directly with third-party tools, LTIs, or institution-built language models." Source: https://community.instructure.com/en/kb/articles/664334-what-igniteai-agent-can-t-do (updated 2026-04-21; accessed 2026-10-24) [inst_664334].

**Q2. What it writes and where (Canvas store).**
- IgniteAI Agent: "It won't modify grades in the Gradebook." [inst_664334]. It can "View outcome results and learning progress" (admin announcement, https://community.instructure.com/en/discussion/664639/announcing-igniteai-agent-availability-for-admins [inst_664639]).
- Grading Assistance: "auto-generate suggested scores and feedback for written assignments based on the associated rubric. Students see that an evaluation is AI-Assisted". Also: "You must review and approve all AI-generated scores, feedback, and comments before submitting the assessment." Source: https://community.instructure.com/en/kb/articles/664423-how-do-i-use-the-igniteai-grading-assistance-for-speedgrader (updated 2026-10-12; accessed 2026-10-24) [inst_664423].
- LLM-Enabled Assignment, built with OpenAI. "As students interact with AI in Canvas, key learning evidence is captured and returned to the Gradebook". It is "mapped to the learning objectives, rubrics and skills defined by the teacher." Source: [inst_openai_nasdaq]. InstructureCon post: "their progress is captured as meaningful learning evidence that is automatically integrated into the Gradebook" [icon25]. Status in July 2026: "Stage: Experimentation ... Functionality is prototype quality". Source: https://community.instructure.com/en/discussion/666652/llm-assignment (accessed 2026-10-24) [inst_666652].
- Where Canvas data goes beyond Canvas (platform plumbing, not IgniteAI documentation). The Caliper 1.1 live-events format lists profiles "Assessment, Basic, Forum, Grading, Navigation Events, Session". Its grading event is "grade_change ... emitted anytime when a submission is graded". Source: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/caliper-ims-1.1/file.data_service_caliper_grading (accessed 2026-10-24) [cal_grading]. Mastery-type events appear only in Canvas's own event format: "learning_outcome_result_created. Definition: The event is emitted anytime a submission is assessed against an outcome." Source: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_learning (accessed 2026-10-24) [canvas_fmt_learning]. The Caliper index page lists no outcomes profile [canvas_caliper].

**Q3. Learner model.** Canvas Outcomes and Mastery Connect hold mastery data. IgniteAI features align and generate items ("IgniteAI Suggestions for Quick Reassessments allows instructors to generate new standards-aligned questions" [inst_664510]) and read outcome results through the agent prompt builder. That article says: "you can use IgniteAI's prompt builder to build a prompt that reviews course outcomes and performance data." Source: https://community.instructure.com/en/kb/articles/664860-how-do-i-build-an-outcomes-and-performance-prompt-with-igniteai-agent (accessed 2026-10-24) [inst_664860]. Outside readers get outcome results through Canvas's proprietary API and Canvas-format events, not Caliper.

**Q4. Plans and standards.** Canvas emits Caliper 1.1 for grades and submissions (above). The Canvas MCP server is in experimentation "with 30+ institutions as well as several edtech partners" [inst_667483]. No opened IgniteAI page mentions CLR, Open Badges or xAPI for AI-produced evidence.


---

## 5. Khanmigo (Khan Academy)

**Q1. How it connects.**
- Clever and ClassLink rostering: "Khan Academy accounts who are part of a partner district in the Khan Academy Classroom program have access to automated rostering via Clever and ClassLink." Source: https://support.khanacademy.org/hc/en-us/articles/360031158952-How-does-automated-rostering-work-for-Khan-Academy-Districts-accounts (updated 2026-10-22; accessed 2026-10-24) [ka_360031158952].
- LMS access is SSO through a link: "your district admin can set up a Clever Instant Login link. That way, teachers and students can access Khan Academy directly from the school LMS." Source: https://support.khanacademy.org/hc/en-us/articles/360055408251 (accessed 2026-10-24) [ka_360055408251].
- Google Classroom is roster import only: "We're only importing your student roster from Google Classroom, not any assignment data. We also cannot send assignments from Khan Academy to your Google Classroom." Source: https://support.khanacademy.org/hc/en-us/articles/360030760852-How-do-I-import-my-Google-Classroom-roster-to-Khan-Academy (accessed 2026-10-24) [ka_360030760852].
- Khanmigo Teacher Tools in Canvas (teacher-facing, via an LTI app): "Khannmigo Teacher Tools can now be enabled directly within Canvas ... it can help co-create lesson plans, rubrics, exit tickets, and more." Source: https://community.instructure.com/en/discussion/617936/khanmigo-teacher-tools-now-available-in-canvas-for-us-k-12-and-higher-education-institutions (accessed 2026-10-24) [inst_617936]. The opened pages do not state the LTI version. Searches of the Khan Academy help center for "LTI", "Canvas" and "Schoology" returned no articles.

**Q2. Writes.** Own store, with CSV export. "Khan Academy offers administrators the option to export student data into downloadable CSV files". The categories include "Skills Progress: This option allows administrators to zoom in on students' Mastery progress" and "Khanmigo Use Data ... including number of flagged chats, and tokens used." Source: https://support.khanacademy.org/hc/en-us/articles/4407513378957-How-do-I-export-a-CSV-file-for-Khan-Academy-Districts-administrator-reports (accessed 2026-10-24) [ka_4407513378957].

**Q3. Learner model.** Yes, persistent and skill-level: "Below are the Mastery levels that each student can achieve within Khan Academy: Attempted ... Familiar ... Proficient ... Mastered ... Not Started". Source: https://support.khanacademy.org/hc/en-us/articles/5548760867853--How-do-Khan-Academy-s-Mastery-levels-work (accessed 2026-10-24) [ka_5548760867853]. It can be read outside Khan Academy only as CSV, not through an open standard.

**Q4. Plans.** "Upcoming LMS integrations through Clever will allow assignments, progress, and completion data to sync automatically with platforms like Canvas, Google Classroom, and Schoology". Also: "Improved filters and export options make it easier to analyze progress across courses, including Khanmigo AI activity in a single export." Source: https://blog.khanacademy.org/a-sneak-peek-at-whats-coming-next-for-khan-academy-districts/ (January 9, 2026; accessed 2026-10-24) [ka_blog_next]. That plan would put progress data in one platform's store (the LMS), routed through Clever, not into an open record. No opened Khan page mentions Caliper, CLR, xAPI, Open Badges or 1EdTech.


---

## 6. MagicSchool

**Q1. How it connects.** "MagicSchool integrates with the following LMS platforms: Canvas, Schoology, Clever, and Classlink. All integrations are available to Enterprise partners only." ClassLink: "add MagicSchool as an app via the ClassLink Roster Server so that your user data is shared with MagicSchool". Source: https://help.magicschool.ai/en/articles/14648845-what-lms-platforms-does-magicschool-integrate-with (accessed 2026-10-24) [msch_lms]. Schoology: "Single Sign-On via Edlink" and "Teachers can now add a MagicStudent Room as a course material." Source: https://www.magicschool.ai/blog-posts/schoology-integration (accessed 2026-10-24) [msch_schoology]. MCP: an import-only connector from Claude (see section 1) [msch_connector]. No opened page names an LTI version.

**Q2. Writes.**
- The help center says feedback does not go back to the LMS: "Limitation: There is no option to share feedback directly back to students in Canvas or Schoology." It adds: "The only ways to get feedback out of MagicSchool are via the PDF Download feature or by manually copying and pasting the feedback." Source: https://help.magicschool.ai/en/articles/15235553-class-writing-feedback-canvas-schoology-integrations (accessed 2026-10-24) [msch_cwf].
- Marketing copy claims more: "Add MagicStudent Rooms as course materials, streamline student access and review student work with SpeedGrader." Source: https://www.magicschool.ai/integrations (accessed 2026-10-24) [msch_integ]. No help article documents how, or whether, Room work or scores enter Canvas.

**Q3. Learner model.** Activity summaries in its own store, no mastery model: "On-demand student-level summaries ... highlighting strengths, areas for improvement". Source: https://help.magicschool.ai/en/articles/10671787-student-insights-understanding-engagement-and-progress-in-real-time (accessed 2026-10-24) [msch_insights]. Quizzes: "View real-time student results and class-level insights". Source: https://help.magicschool.ai/en/articles/13540346-quizzes [msch_quizzes]. No export to other vendors.

**Q4.** The site calls itself "THE AI OPERATING SYSTEM FOR SCHOOLS" (trademark line on [msch_integ]). This matters for the section 5.1 sampling frame. Help center searches for grade, export, LTI and similar terms returned nothing, and no opened page mentions 1EdTech, Caliper, CLR or xAPI.


---

## 7. SchoolAI

**Q1. How it connects.** LTI 1.3 with LTI Advantage in Schoology: "Registering SchoolAI as an LTI 1.3 tool inside your Schoology environment". Required services: "Deep Linking (auto-selected)", "Assignment and Grade Services", "Names and Roles Services". Source: https://help.schoolai.com/en/articles/15382194-schoology-lti-integration-guide (accessed 2026-10-24) [sai_schoology]. In Canvas, LTI is combined with Canvas REST API write scopes: "Create Assignment: POST /api/v1/courses/:course_id/assignments". The integration "enables teachers to launch and grade assignments directly within the Canvas interface." Source: https://help.schoolai.com/en/articles/14726696-canvas-api-and-lti-integration-for-tech-admins (accessed 2026-10-24) [sai_admin]. Canvas course-navigation TA: "This setup uses a resource link instead of a deep linking request." Source: https://help.schoolai.com/en/articles/12601254-create-a-persistent-course-teaching-assistant-with-an-lti-integration [sai_ta]. SSO and rostering: "Rostering through 30+ SIS partners", plus "SOC 2 Type 2 compliant and 1EdTech certified". Source: https://schoolai.com/integrations (accessed 2026-10-24) [sai_integ].

**Q2. Writes.** "Grades from SchoolAI Spaces can be passed back to the Schoology gradebook" [sai_schoology], over LTI AGS. That is one platform's store and a grade.

**Q3. Learner model.** Yes, in its own store: "you can view class-level learning mastery (based on outcomes)". "The Class Mastery Score (1–4) provides a real-time indicator of overall proficiency based on outcomes." Source: https://help.schoolai.com/en/articles/15243484-your-guide-to-mission-control (accessed 2026-10-24) [sai_mc]. No opened page documents export of these outcome mastery evaluations to other vendors.

**Q4.** The "1EdTech certified" claim [sai_integ] is not specified on the page and could not be checked against the directory under the study's rules. No opened page mentions Caliper, CLR, xAPI or Open Badges.


---

## 8. Brisk Teaching

**Q1. How it connects.** Chrome extension, LTI 1.3 for Canvas and Schoology (deep linking of Brisk resources), rostering, and MCP connectors.
- "Canvas - Dynamic Registration (Recommended)"; for Schoology, "Type of App: LTI 1.3 App" and "LTI Advantage Extensions: check Deep Linking". Source: https://help.briskteaching.com/hc/en-us/articles/50241408535060-LTI-Integration-Setup-for-Admins (accessed 2026-10-24) [br_50241408535060]. Only Deep Linking is selected; AGS is not.
- MCP: "Using the Model Context Protocol (MCP), the connector lets you ask an AI tool, in plain language, to build Boost activities, craft quizzes and lesson plans, set up batch feedback assignments". Source: https://help.briskteaching.com/hc/en-us/articles/50241696224020-Set-up-the-Brisk-Connector-for-Claude-and-ChatGPT (accessed 2026-10-24) [br_50241696224020].
- Rostering: "Rostered classes (ClassLink, Clever, CSV) appear in Brisk automatically" [br_54571571300116].

**Q2. Writes.**
- Google Classroom: "Brisk does not roster from Google Classroom or send grades back to it." "No grade or score passback. Google Classroom doesn't support sending grades back from Brisk. Scores appear inside the student's doc. To move scores into a gradebook, use the CSV download." Feedback is inserted into Google Docs or Slides: "Insert Feedback into the student's Google Doc or Slides". Source: https://help.briskteaching.com/hc/en-us/articles/54571571300116-How-does-Brisk-work-with-Google-Classroom (updated 2026-10-19; accessed 2026-10-24) [br_54571571300116].
- Canvas, through the extension: "Select Rubric Scoring ... Click on the Add to Speed Grader button to transfer scores back into Canvas." Source: https://help.briskteaching.com/hc/en-us/articles/40443517533588--How-does-Brisk-integrate-with-Canvas (accessed 2026-10-24) [br_40443517533588]. Quizzes leave as QTI content files ("create QTI Quizzes with Brisk to import into Canvas"), which is content, not learner evidence.

**Q3. Learner model.** None for students. Its dashboard metric measures teacher activity: "The Instructional Moments value is a weighted measure of teacher actions in Brisk". Source: https://help.briskteaching.com/hc/en-us/articles/48339694825364-Understanding-Instructional-Moments (accessed 2026-10-24) [br_48339694825364].

**Q4.** No opened page mentions 1EdTech, Caliper, CLR, xAPI or Open Badges.


---

## Cross-cutting: 1EdTech's 2026 work on portable learning context for AI (Q4)

- 1EdTech press release, October 21, 2025: "Building on the Model Context Protocol (MCP), this effort focuses on helping AI systems understand the structure and standards that define teaching and learning." Source: https://www.1edtech.org/1edtech-article/1edtech-leads-collaborative-effort-to-shape-responsible-ai-in-education/411336 (accessed 2026-10-24) [oned_ai_pr].
- Experiment group: "1EdTech is convening a new Use Cases for Learning Context in AI Experiment Group and invites all members to participate." It continues: "Its role is to surface and test ideas, not to decide implementations or converge on specifications." Source: https://community.1edtech.org/blogs/cara-jenkins/2026/02/26/use-cases-for-learning-context-in-ai-experiment-gr (accessed 2026-10-24) [oned_expgrp].
- Public draft, "Trusted Portable Learning Context v1.0.1 · Public Draft". It states: "This is a Public Comment Draft positioned as a principles paper ... The companion technical RFC (Part 2) will propose technical patterns, data models and standards ... This document is non-normative." It also states: "It is not a new data standard, not an agent's memory store, and not a replacement for existing vocabularies." On the current contract: "Education source systems today expose data through per-resource REST endpoints (often in OneRoster, an LMS-vendor REST API, or an SIS-vendor REST API) ... keeping rosters in sync, exporting grades, posting outcomes." Source: https://standards.1edtech.org/publications/rfc-trusted-contextv2 (accessed 2026-10-24) [oned_rfc].
- Labs Live event: "The RFC builds on community use cases from the Learning Context for AI Experiment group and early experimentation from the AI Hackathon". Source: https://www.1edtech.org/events/request-for-public-comment-on-trusted-learning-context (accessed 2026-10-24) [oned_rfc_ev].

---