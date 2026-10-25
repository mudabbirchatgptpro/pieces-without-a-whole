# Coder A reasons

One line per product per function. Code first, then the dossier quotation (or its absence) that decides it. Where I was unsure between two codes I chose the lower one and say so. Rules I applied uniformly, stated once:

- F1: 1 requires that the system itself generates or recommends next activities for a learner or class (even if a teacher approves), or claims to. Teacher-facing reports that leave the choice of activity to the teacher, static curriculum orderings, and adaptivity within a single activity (adaptive quiz, hints) are 0. 2 requires documentation that the sequence includes activities delivered by tools from two or more vendors other than the product vendor.
- F2: 2 requires public documentation of a named open standard interface (LTI, OneRoster, Ed-Fi and so on) with concrete technical detail and a named outside system using it, or a vendor-stated or directory certification plus outside use. A named standard without such documentation, an unnamed LMS or rostering integration, or a proprietary API (with or without public docs) is 1. No interface at all is 0.
- F3: 2 requires a documented mastery or knowledge-state record that tools from two or more vendors other than the product vendor write to. A standards, skill or mastery record written only by the vendor's own tools, or a claimed per-student mastery or learner record, is 1. Gradebooks, completion, engagement and generic analytics are 0.
- F4: 2 requires documented per-tool or per-app permissions or scopes over student data. Privacy policy, role-based access, district-level or feature-level settings, or controls that only govern what the product itself requests from Google or an LMS, are 1. Nothing documented is 0.
- F5: 2 requires at least two named tools from independent vendors documented as executing inside the product or as working on the product's platform services. SSO launch, rostering or grade sync alone ("links out or data sync only") is 1. Infrastructure providers named only as subprocessors (hosting, payments, SMS, AI model APIs) do not count.
- Marketing copy alone caps a function at 1.

## academic-ai-solutions
- F1=1: Claimed without documentation: "Optimal course paths connected to career outcomes from day one" and "connects them to the right resource at the right moment". No documentation of what is sequenced.
- F2=0: No API or standard named; only "Secure connections to your existing systems of record" and "Tailored integrations". Docs wiki is behind a Cloudflare login. No documented interface.
- F3=1: Claimed persistent record: "A persistent learner record built to travel with the student across institutions, credentials, and life stages." Nothing on mastery or on outside writers; a claimed record of credentials fits level 1 at most.
- F4=0: "None found. The footer 'Privacy Policy' link points to '#'". No documented control.
- F5=0: Only "Verified merchants, housing partners, dining, transportation" named as a category; no named third-party tool.
- SUFF=0: Not all functions at 2.

## access-pearson
- F1=1: Own courseware only: "Assess what students do and don't know and then recommend modules to help them build mastery." "No documentation found of Access Pearson sequencing activities from other vendors' tools."
- F2=2: "Pearson meets industry standards and is recognized by IMS Global as LTI Certified." plus support documentation of "Access Pearson (LTI 1.3)" grade sync and setup for Canvas, Blackboard, Brightspace, Moodle, Schoology and Sakai.
- F3=1: Own model only: "When you have correctly answered all of the questions in the module, you have mastered all the material." "No documentation found of outside vendors' tools writing mastery or skill data into Pearson."
- F4=1: Privacy statements only: "Pearson uses LMS Standards and does NOT store any institutional data"; "No per-app permission or scope list for Access Pearson found".
- F5=1: Integrations listed (Canvas, Clever, ClassLink, bookstores) but Pearson is the tool inside them: "From your Canvas course, add the Access Pearson link." "None found of independent developers' tools running inside Access Pearson".
- SUFF=0: Not all functions at 2.

## amplify
- F1=1: Own programs only: "mCLASS automatically places students on an adaptive path within Boost Reading". "No documentation found of Amplify sequencing activities delivered by other vendors' tools."
- F2=2: Published LTI 1.3 configuration with AGS and NRPS scopes at my.amplify.com/ltiv1p3/setup/amplify, Canvas and Schoology setup and grade sync; "contributing member of the 1EdTech Consortium" with "a variety of certifications".
- F3=1: Own tools only: "mCLASS instantly scores and analyzes student response patterns to provide you with diagnostic data"; "No documentation found of outside vendors' tools writing skill or mastery data into Amplify."
- F4=1: Policy level: "we enable Schools to control the use, access, sharing, and retention of Student Data". ClassLink rule-based permissions are ClassLink's control, not Amplify's.
- F5=1: Integrations listed (Clever, Google, Canvas, Schoology); Amplify runs inside Canvas. "None found of independent developers' tools running inside Amplify programs".
- SUFF=0: Not all functions at 2.

## apkaos
- F1=0: Automations are administrative: "messaging parents after 3 absences". "no page found describing the system deciding a learner's next learning activity".
- F2=0: "None found: no developer docs, API reference or open standards"; data moves by Excel import and export.
- F3=0: Marks and report cards; the one phrase "Academic Intelligence Topic-level insights on student performance" is marketing and ambiguous between performance analytics and a knowledge model, so the lower code is taken. "No mention of a mastery or skill model found".
- F4=1: Role-based controls and privacy policy: "Roles and permissions control who sees what"; "No page found describing per-app or per-tool permission scopes".
- F5=0: Razorpay, WhatsApp, SMS, Cloudflare R2 are payment, messaging and storage providers; "no app directory, marketplace or named independent learning tools found".
- SUFF=0: Not all functions at 2.

## appcorp-ai-os-school
- F1=1: Claimed without documentation: "AI builds a unique learning path for every student" adjusting "pace, content format, and difficulty in real time". "No documentation found on whose content or tools the pathways draw from."
- F2=1: Proprietary API claimed without public docs: "White-label AI tutoring engine via REST API", "Custom integrations & API access". No open standard named.
- F3=0: Risk analytics, not a knowledge model: "AI identifies at-risk students weeks before they fail. Engagement scores, attendance patterns..." "No documentation found of a mastery or knowledge-state model".
- F4=1: Marketing claim only: "granular data access controls, and full audit trails"; privacy policy covers agency website visitors. "No per-tool or per-app permission documentation found."
- F5=0: "None found. The product page names no third-party tools running inside the product."
- SUFF=0: Not all functions at 2.

## big-ideas-math
- F1=0: Adaptivity is within a single test or item: "adapts based on student responses to the questions"; "immediate remediation on homework questions". Teachers assign; no system sequencing across activities documented.
- F2=2: "BigIdeasMath.com can be integrated into the Canvas LMS platform ... LTI 1.3"; "Deep linking and grade pass back between BigIdeasMath.com and Schoology"; scores "pass from BigIdeasMath.com to Canvas".
- F3=1: Own adaptive assessment only: Progression Benchmark report shows "the specific objectives the student was tested on ... and if that student answered correctly or incorrectly". "No documentation found of outside vendors' tools writing data into these reports."
- F4=1: Privacy policy: "giving the educational institution direct control with respect to the use and maintenance of the education records". No per-tool control.
- F5=1: "Dynamic Investigations, powered by Desmos and GeoGebra ... can be found in the online teacher Dynamic Classroom or as embedded links in the student eBook app." Unsure whether these run inside or are links; lower code chosen.
- SUFF=0: Not all functions at 2.

## blackboard
- F1=1: Release conditions and forced sequences within the LMS: "You can set a forced sequence to a module"; "No page opened states whether external (LTI) tool items or their returned grades can serve as release conditions."
- F2=2: Developer docs for REST APIs, LTI 1.3 and AGS; "Learn has been certified to meet the LTI standards."; App Catalog of outside apps.
- F3=1: Outcomes mastery is computed by Blackboard from aligned assessments: "A weighted median is used to calculate each student's mastery level." AGS gives tools only "the columns created by the LTI tool itself"; "No page opened states whether a score returned by an LTI tool aligned to a goal is counted in the Outcomes mastery calculation."
- F4=2: Per-provider authorization documented: "You may be asked to authorize the provider's access to certain user information, such as your name and email address. Note Your institution may choose to automatically share your user information with content providers." plus limited-entitlement REST integrations.
- F5=2: "The App Catalog enables anyone to browse ... Apps"; Content Market pages for Cengage, Kaltura, McGraw-Hill, Macmillan; "You can use Kaltura integrations to present rich media content in your courses."
- SUFF=0: Not all functions at 2.

## blended-os
- F1=0: Only "Access scheduling, grading, analytics, and AI personalization" and a "personalization AI engine"; "No page found describing how the product decides or orders a learner's next activity".
- F2=0: "we can integrate with any 3rd party platform" with "no public API documentation or developer pages; no named open standard".
- F3=0: Grades and progress only: "Enrollment, grades, attendance, and timetables in one place." "None found describing a mastery / skill / knowledge-state model".
- F4=1: "Blended's platform enables role-based access control, allowing for tiered permissions." No per-tool controls.
- F5=0: Microsoft Clarity and Sentry are analytics infrastructure; "no named independent education tools running inside Blended OS".
- SUFF=0: Not all functions at 2.

## brightspace
- F1=1: Release conditions across Brightspace tools: "Release conditions provide the ability to dynamically release resources to users that have satisfied one or more conditions." "No page opened states whether a grade written by an external LTI tool can serve as a release condition."
- F2=2: Valence developer docs with OAuth 2 scopes, LTI Advantage services ("AssignmentAndGradeServices ... DeepLinking ... NamesAndRoleProvisioningServices"), IntegrationHub dynamic registration, partner program.
- F3=1: Outcomes and Mastery View exist; alignments to "LtiLink" documented, but "no route for writing a learner's outcome evaluation or achievement level was found" and "No page opened describes an external tool writing outcome achievement levels into Brightspace".
- F4=2: "The scope value you provide must be a subset of the scopes you provided when you registered your application"; "Data Access Transparency: Review a summary of exactly what information ... the app will access before finalizing the installation."
- F5=2: "Brightspace IntegrationHub is an integrated app catalog ... Panopto enables you to record, upload, and share video directly from within IntegrationHub. Similarly, Zoom ..." plus Turnitin, Kaltura, Bongo and others.
- SUFF=0: Not all functions at 2.

## canvas
- F1=2: Modules API: "Module items can be accessed linearly or sequentially"; item types include "'ExternalTool'" with "completion_requirement": {"type":"min_score"...}; "require_sequential_progress" and "prerequisite_module_ids". EduAppCenter lists independent LTI apps "ALEKS", "Apex Learning", "Amplify", "Assignment Review by FeedbackFruits", "Atomic Assessments". Re-checked: the documented mechanism covers external tool items from any vendor in a forced sequence; Mastery Paths (adaptive) excludes external tools, so only linear module sequencing earns the 2.
- F2=2: Public developer documentation for LTI, AGS ("POST /api/lti/courses/:course_id/line_items/:line_item_id/scores"), developer keys, xAPI and Caliper; 1000+ external tools.
- F3=1: Outcome results and rollups exist, but "No endpoint for an external tool to create an outcome result was found"; tools write only "scoreGiven", "scoreMaximum" via AGS; "Currently Mastery Paths does not support association with outcomes."
- F4=2: "Developer key scopes allow root account administrators to restrict the tokens issued from developer keys to a subset of Canvas API endpoints"; per-tool "privacy_level" ("name_only", "email_only", "public", "anonymous").
- F5=2: "Canvas integrates with 1000+ external tools"; tools "can be surfaced as links in course modules or used to deliver custom assignment experiences"; EduAppCenter names ALEKS, Apex Learning, Amplify, FeedbackFruits, Atomic Assessments.
- SUFF=0: F3 is 1; no independent vendor's tool is documented writing to the outcomes model that modules act on.

## cengage-learning
- F1=1: Learning path is instructor-ordered and Mastery Training adapts within its own activity: "Customize your course by adding, removing, and reordering your units and activities." Turnitin and Bongo appear only as activity types in help navigation; no quoted page documents third-party activities inside the sequenced path, so the lower code is taken.
- F2=2: "New institutions will be integrated using LTI Advantage"; "Deep linking from Canvas to Cengage activities"; MindTap scores "sync to LTI Advantage LMS"; Canvas, Google Classroom and Schoology link guides.
- F3=1: Cerego-powered Mastery Training and the personal study plan are inside MindTap: "The personal study plan identifies areas for improvement based on students' performance." "No documentation found of outside vendors' tools writing mastery or skill data into MindTap."
- F4=1: K-12 privacy notice only; "No per-app permission or scope list found on the pages opened."
- F5=2: Turnitin inside MindTap ("Feedback Studio and PeerMark are not accessible by screen readers") and Bongo ("View and evaluate student presentations with Bongo."), two independent tools documented as running inside.
- SUFF=0: Not all functions at 2.

## ck-12-foundation
- F1=1: Own content only: "advancing the student to the next concept if they're getting questions correct"; "suggesting personalized CK-12 content based on a student's need". "No documentation found of CK-12 sequencing activities from other vendors' tools."
- F2=2: "In the install app window, select LTI version 1.3."; launch URL "https://www.ck12.org/auth/launch/lti/ltiApp"; roster sync from Canvas, Schoology, Google Classroom; score passback ("CK-12 will send the matching percentage over").
- F3=1: Own skill meter: "based on an algorithm that takes into account the difficulty level of each question answered"; "No documentation found of outside vendors' tools writing skill or mastery data into CK-12."
- F4=1: Data sharing options are Canvas's and Clever's; CK-12 itself offers "Student Privacy Pledge" and DPA on request. No per-tool control inside CK-12.
- F5=1: Bookmarklet embeds external resources into the library ("Prezi ... and SlideRocket ... require a manual copy and paste of the media embed code"); teacher-added embeds, no tools documented as running inside for students. "No app marketplace or plugin program".
- SUFF=0: Not all functions at 2.

## classlink
- F1=0: "No page opened describes ClassLink deciding or sequencing what a learner does next."
- F2=2: "ClassLink Roster Server is certified by the 1EdTech Consortium to comply with the 1EdTech OneRoster standard"; partner docs with OAuth 2.0 scopes, SDKs; "more than 6,000 digital learning resources".
- F3=0: "No mastery, skill, outcome or competency record was found"; data is roster and usage.
- F4=2: "school systems gain control over which data they choose to share"; "The school system needs to grant your application access"; DataGuard masks fields per vendor; PAWs grant and revoke vendor access.
- F5=1: Apps are launched by SSO and rostered: "no page opened describes third-party tools running inside ClassLink beyond launch." This is the codebook's "links out or data sync only"; the section 4 example of a rostering layer as an external platform would imply 2, but the table text is literal and the lower code is taken.
- SUFF=0: Not all functions at 2.

## clever
- F1=0: "No page opened describes Clever deciding or sequencing what a learner does next."
- F2=2: "Clever API v3.1 OpenAPI Spec"; "Clever LMS Connect ... grade passback and LTI 1.3 SSO"; partners Khan Academy, HMH, McGraw Hill, Prodigy shown using it.
- F3=0: Pass-through of assignments and submissions to the LMS gradebook; "No mastery, skill, outcome or competency object was found". The record lives in the LMS, not in Clever.
- F4=2: "you can set up sharing permissions on an app-by-app basis"; "Clever provides each application with only the data necessary for its operation"; "Share by Rules".
- F5=1: Apps receive rostering and SSO and are launched from the portal: "Clever provides a platform that enables Schools to securely provision the accounts with the third-party applications". Launch plus data sync is the codebook's level-1 example; lower code taken as for ClassLink.
- SUFF=0: Not all functions at 2.

## commonlit
- F1=0: Curriculum is a static order ("we do not recommend using units out of order") and teachers assign; "Adaptive or automatic sequencing of learner activities: none found". The marketing phrase "what to teach next" describes reports to teachers.
- F2=2: "LTI only allows CommonLit to import a Canvas course as one class."; Canvas "External Tool" setup and "we will automatically send scores to Canvas"; Clever, ClassLink, Google Classroom.
- F3=1: Own standards-level record: "students' performance on specific standards categories", "Growth Data". "Outside vendors' tools writing mastery or skill data into CommonLit: none found".
- F4=1: Privacy policy only: "a Student's data ... will only be visible to the Student's School Officials". "per-tool permission controls inside CommonLit: none found".
- F5=1: "Independent third-party tools running inside CommonLit ... none found"; integrations listed are Canvas, Clever, ClassLink, Google Classroom.
- SUFF=0: Not all functions at 2.

## delta-math
- F1=1: Own remediation generated from own tests: "an individualized remediation assignment is generated for each student." Outside tests enter only by manual entry.
- F2=2: "Make sure 'Canvas 1.1' is selected."; "Config URL: https://www.deltamath.com/s3/canvas-configuration.xml"; "LTI 1.3 Infinite Campus Learning Suite integration"; Schoology "Install LTI 1.1 App".
- F3=1: Own data: "Performance reports against standards"; "strengths and weaknesses". "Outside vendors' tools writing mastery or skill data into DeltaMath: none found".
- F4=1: Privacy policy and FERPA/COPPA statements; "Per-tool permission controls inside DeltaMath over other apps: none found".
- F5=1: YouTube videos assignable; otherwise "Independent third-party tools running inside DeltaMath ... none found". One embedded service at most.
- SUFF=0: Not all functions at 2.

## derivita
- F1=0: Teachers assign; reports sort standards by mastery for the teacher ("Reteach from the top of the list down"). "Automatic or adaptive sequencing of learner activities: none found".
- F2=2: "Built on the IMS Global LTI 1.3 and LTI Advantage standards."; published Canvas JSON with AGS and NRPS scopes and "oidc_initiation_url"; ClassLink rostering.
- F3=1: Own mastery score: "the platform computes a mastery score from that student's results." "Outside vendors' tools writing mastery or skill data into Derivita: none found".
- F4=1: Privacy policy; LTI scopes are what Derivita requests from Canvas. "Per-tool permission controls inside Derivita over other apps: none found".
- F5=1: One independent tool inside: "you can turn on Proctorio-powered lockdown settings"; TI calculators are hardware photographed by students. Two required for 2.
- SUFF=0: Not all functions at 2.

## discovery-education
- F1=1: DreamBox sequences its own lessons: "picking the next best lesson for the student based on how they answered previous questions." NWEA data is input selected by teachers; the activities sequenced are DreamBox's.
- F2=2: "Paste the following URL in the JSON URL field: https://app.discoveryeducation.com/learn/lti/configuration" (LTI 1.3 Canvas); grade passback; "manage user and class data via OneRoster" through ClassLink.
- F3=1: DreamBox proficiency model is own; NWEA scores are chosen manually ("student data will need to be selected for each student"). "Outside vendors' tools writing mastery data into a Discovery Education learner model: none found beyond the NWEA item".
- F4=1: Google service account permissions describe Discovery's own access; "Classroom Product Filters" govern which classrooms appear per DreamBox product. "per-tool permission controls over other vendors' apps: none found".
- F5=1: Partner media (MythBusters, NBA, EA Sports) is content, not tools; twelve integrations listed. "Independent developers' software tools running inside Experience or DreamBox ... none found".
- SUFF=0: Not all functions at 2.

## ed-fi
- F1=0: "No page opened describes Ed-Fi or the ODS / API deciding or sequencing what a learner does next."
- F2=2: Open data standard with public API docs and an Ed-Fi certification registry; "Leading technology providers like Skyward, PowerSchool, Infinite Campus, Education Analytics, and EdGraph have implemented the Ed-Fi Data Standard."
- F3=2: The ODS holds standards-referenced outcomes beyond grades: "ObjectiveAssessment ... may have its own score, performance levels ... tied to learning standards"; "StudentGradebookEntry, which can be a Grade or a CompetencyLevel entity". Independent writers certified for the Assessment Outcomes API: "Cambium Assessment", "Amplify mCLASS DIBELS 8th Edition and mCLASS Lectura", "i-Ready Math and ELA Diagnostic". Re-checked: three independent vendors documented as writing performance-level data to one persistent record; the level-1 alternative ("grades or completions only") does not fit performance levels and competency levels.
- F4=2: "Claims and claim sets provide fine-grained access control over the resources available in the API."; "An API Profile enables the creation of a data policy ... assigned to API consumer applications".
- F5=1: "Ed-Fi is a data standard and data store that vendors' systems write to and read from; no page opened describes tools running inside it." Data sync only.
- SUFF=0: F1 is 0; nothing sequences on the record.

## edlink
- F1=0: "No page opened describes Edlink deciding or sequencing what a learner does next."
- F2=2: "The Edlink API is organized around REST"; "we are compatible with various API, LTI, and OneRoster implementations"; LTI deep-linking guide; Clever LMS Connect built on it; "150+ edtech companies".
- F3=0: "No learner mastery or knowledge-state entity was found."; grades are synced through to the LMS, which holds the record.
- F4=2: "Sharing rules are the primary way that data is filtered between a school's data source and a company's application."; "Developers can request (and district can control) what fields are shared for each integration."
- F5=1: "no page opened describes applications running inside Edlink itself"; apps connect through its API (data sync and launch).
- SUFF=0: Not all functions at 2.

## edmo
- F1=0: Admissions workflow only: "triggers tailored follow-ups by profile". "None found of sequencing of learning activities."
- F2=1: Proprietary agent-builder OpenAPI spec published; connectors to Canvas and Blackboard claimed; "No mention of LTI, OneRoster ..." No open standard.
- F3=0: Applicant profile normalization only: "Normalize and map records into a single student profile". "None found on a model of what the learner knows."
- F4=1: "Role-based access, audit trails, and encrypted data flows"; institution-level policy.
- F5=1: Twilio and Zoom connectors and Canvas/Blackboard sync listed; EDMO itself runs inside Salesforce. "None found of independent developers' tools running inside EDMO."
- SUFF=0: Not all functions at 2.

## edpuzzle
- F1=1: System recommends own follow-up activities: "Edpuzzle recommends follow-up tasks based on where the class encountered challenges. With one click, you can generate a short reinforcement quiz or a bite-sized reading".
- F2=2: LTI 1.1 setup for Canvas ("consumer key and shared secret"), Blackboard ("Register LTI 1.1 Provider"), Schoology, Brightspace; "Grades are exported automatically" to six LMSs.
- F3=0: Gradebook and engagement only: "the grade that each student got in each video"; AI summaries of "common learning gaps" are teacher-facing analytics. "Skill/mastery or knowledge-state model ... none found".
- F4=1: Privacy policy; school may enable or disable AI features; Google Workspace approval is Google's control.
- F5=1: One embedded third-party service: "YouTube ... Embed and play videos from YouTube". Two required for 2.
- SUFF=0: Not all functions at 2.

## edunation-os
- F1=1: Own apps: "In TRACKER Recommends targeted interventions when a student's attainment data signals a gap." "No page found describing sequencing of learner activities across other vendors' tools."
- F2=1: Proprietary REST API with ReadMe docs and access request form; SAML 2.0 and OIDC SSO. "no LTI, OneRoster, Caliper, xAPI, QTI or other learning-data standard named".
- F3=1: Own record: "Every app reads from and writes to the same institutional record." plus TRACKER attainment tracking. "None found describing outside vendors' tools writing attainment data into the record."
- F4=1: "Permissions Role-based access across every module."; "no per-third-party-app scope or consent controls".
- F5=1: "500+ Connected apps" by SSO; "No named independent education tools (by product name) that run inside EdunationOS." Links out and roster flow.
- SUFF=0: Not all functions at 2.

## edynamic-learning
- F1=0: Static tracks and pacing lights: "sequenced learning tracks aligned to national and examination standards"; "No page found describing adaptive paths, automatic recommendations, or automatically generated assignments".
- F2=2: "content ... resides on eDynamic Learning's LTI server"; "Domain: lti.edynamiclearning.com"; LTI 1.3 configuration pages; "Agilix Buzz supports the 1EdTech ... OneRoster standard."
- F3=0: Points-based: "As eDynamics utilizes a point system, we do not use these [mastery] reports." Assessments stored in the customer's LMS.
- F4=1: Google scopes listed and "Privacy: Anonymous" describe eDynamic's own access; privacy policy. No per-tool control.
- F5=1: "None found running inside eDynamic Learning products. The documented relationship runs the other way". Integrations listed.
- SUFF=0: Not all functions at 2.

## formative
- F1=1: Own next steps: "Luna analyzes student performance against learning standards and instantly recommends Luna Next Steps". "No page found describing automatic sequencing of activities across other vendors' tools."
- F2=2: "We have LTI 1.3 setup available for Canvas and Schoology."; "LTI Grade Passback"; OneRoster 1.1 or 1.2 API; ClassLink Roster Server REST API; Clever.
- F3=1: Own standards tracking: "You can see each student's average for each standard you've tagged"; Newsela results stay separate. "No page found describing other vendors' tools writing mastery or standards data into Formative."
- F4=1: Service grants are what Canvas gives Formative; privacy policy. No per-tool control inside Formative.
- F5=2: "the embedded content is displayed within an iFrame ... allows your students to interact with the other website without leaving Formative" with instructions for "Geogebra, Flipgrid, Wakelet, NewsELA, Edpuzzle"; plus "Respondus LockDown Browser".
- SUFF=0: Not all functions at 2.

## google-classroom
- F1=0: "No page opened describes Classroom deciding or sequencing what a learner does next across activities."
- F2=2: Public Classroom API developer documentation; add-ons framework used by named outside developers; "OneRoster for Student Information Systems" guide listed; CASE identifiers for learning goals. Proprietary core API, but public docs plus open-standard components and outside developers using them; not merely "claimed".
- F3=1: Cross-tool record of grades only: add-ons "pass a grade back to Google Classroom programmatically, which appears in the teacher's grade book"; learning goals tag content; "no per-student mastery record was described".
- F4=2: Per-app OAuth scopes ("classroom.addons.teacher", "classroom.addons.student") and admin per-app access settings ("Trusted, Limited, Specific Google data, or Blocked").
- F5=2: "We partnered with 20+ EdTech companies, including Kahoot!, Pear Deck, IXL, ReadWorks, and Nearpod, to build Google Classroom add-ons"; attachments "open third-party content in iframes in Google Classroom."
- SUFF=0: Not all functions at 2.

## h5p
- F1=0: Branching is inside one content item: "Learners make choices that determine the content they will see." "No page found describing H5P deciding or sequencing what a learner does next across separate activities".
- F2=2: "Choose LTI v1.3" for Canvas; LTI setup for Schoology, Brightspace, Blackboard, Moodle; grades "stored in Canvas"; xAPI statements; open-source developer docs.
- F3=0: "H5P.com doesn't store xAPI statements, it's only forwarded to the LRS." "No page found describing a mastery, skill or knowledge-state model".
- F4=1: Organization-level LRS anonymity setting and report-visibility roles; a single endpoint control, not per-tool scopes. Lower code taken.
- F5=2: Community content types run inside H5P: "developed by Jithin under Learning and Media Lab of ICFOSS"; "created by Lumenia"; "Timeline.js developed by Knight Lab, packaged as an H5P content type".
- SUFF=0: Not all functions at 2.

## hmh
- F1=1: "HMH Personalized Path connects MAP Growth scores directly to proven programs, placing every student into ... Read 180, Math 180, and Waggle." "All programs named ... are HMH or NWEA products".
- F2=2: "For Canvas, the integration uses LTI Advantage (LTI v.1.3 plus related services)"; redirect URI published; "At this time, we are fully certified for OneRoster 1.1."; TCC and QTI.
- F3=1: Own standards proficiency: "Proficiency Date Date student acquired proficiency in the Practice assignments for the standard." "No page found describing independent (non-HMH) vendors' tools writing skill or mastery data into HMH Ed."
- F4=1: "you may be asked to activate a partnership and approve a data sharing agreement" is a one-time per-partner approval of connected HMH programs; thin for per-app scopes, so lower code taken.
- F5=1: Connected programs Amira, Waggle, Writable; Waggle and Writable are HMH's and "no page found stating Amira's ownership". Illustrative Mathematics content "is not hosted on the Ed platform".
- SUFF=0: Not all functions at 2.

## ibl-ai
- F1=1: "A pathway is a guided sequence of courses and outside resources toward a specific goal."; outside items "are outside links and open in a new browser tab." Own courses plus generic links; no independent vendors' tools documented in the sequence.
- F2=1: Proprietary REST API ("1,867 endpoints") and LTI 1.3 tool endpoints documented, but no named outside system shown using them ("your LMS instances"). Lower code taken.
- F3=1: Own skills record: "skills you have earned by completing courses, skills you self-reported". "No page found describing outside vendors' tools writing into the skills record."
- F4=1: RBAC with field-level data actions and per-connector scope badges govern agents and users, not third-party tools' access to student data. Lower code taken.
- F5=1: MCP connectors (Asana, GitHub ...) are external systems the agent calls; "5,700 community-contributed skills" is a marketing claim with no named plugin. "No independent third-party education tools (by name) found running inside the OS".
- SUFF=0: Not all functions at 2.

## ixl-learning
- F1=1: Own skills: "IXL Recommendations are personalized suggestions for math and language arts skills."; MAP scores entered manually. "no page found describing sequencing of other vendors' activities."
- F2=1: Canvas "External Tool" and grade sync, ClassLink, Clever, Google Classroom, but "the pages opened do not name LTI, OneRoster, Caliper, QTI, or any other standard by name" and no developer docs.
- F3=1: Own model: "The SmartScore is based on IXL's proprietary algorithm". "No page found describing other vendors' tools writing skill or mastery data into IXL automatically."
- F4=1: Privacy policy; ClassLink permissions are ClassLink's. "No page found listing per-app OAuth scopes requested by IXL or per-tool permission controls inside IXL."
- F5=1: "None found ... Integrations documented run IXL inside other platforms".
- SUFF=0: Not all functions at 2.

## k12-tutoring-by-stride
- F1=1: Own sessions recommended: "Beacon by K12 Tutoring generates a numbered list of Recommended Next Sessions"; educators assign. "Sequencing of other vendors' activities: none found".
- F2=1: Canvas access is an "External URL" or "Redirect Tool" link; "Clever securely connects students and educators to K12 Tutoring through single sign-on"; "LTI, OneRoster ... none found".
- F3=1: Own AI summaries of knowledge state: "summaries that describe specific concepts the student has demonstrated mastery in and specific gaps". "Outside vendors' tools writing into a learner model: none found".
- F4=1: Clever sharing rules are Clever's; privacy policy; transcript visibility rules. No per-tool control.
- F5=1: "Your live tutoring sessions take place in Engageli." One third-party tool; ownership not stated. Two required for 2.
- SUFF=0: Not all functions at 2.

## khanmigo
- F1=1: Own content: "Offers suggestions on what Khan Academy content your students should work on next"; "No page opened describes Khan Academy or Khanmigo sequencing activities delivered by other vendors' tools."
- F2=1: Clever and ClassLink rostering, Clever LMS Connect sync, Google Classroom roster import; "no statement of LTI, OneRoster, Caliper, CLR or CASE support by Khan Academy" and no developer API.
- F3=1: Own Mastery System: "Not started ... Attempted ... Familiar ... Proficient ... Mastered". "No page opened describes ... other vendors' tools writing into Khan Academy's mastery system."
- F4=1: Data requirements and FERPA permission levels; "no page opened describes Khan Academy granting per-app permissions to other tools."
- F5=1: "No page opened describes independent developers' tools running inside Khan Academy or Khanmigo."; integrations listed (Canvas, Google Classroom, Schoology via Clever).
- SUFF=0: Not all functions at 2.

## kiddom
- F1=1: Atlas recommends activities within Kiddom's IM math: "makes recommended small-group or whole-class activities available. Teachers decide whether to use the recommendation". "Atlas is built for IM math classrooms".
- F2=2: "Kiddom is 1EdTech, OneRoster 1.1, and LTI 1.3 Certified to support ClassLinks rostering and SSO." (vendor statement); "Teachers assign and grade in Kiddom, which triggers pass back to the Canvas dashboard."
- F3=1: Own standards mastery reports: "detailed insights on standard-specific performance for your class as well as individual students." Assessment partners listed with "no documentation of data writes found".
- F4=1: Roles; "No per-app scope or consent screen for embedded third-party tools documented."
- F5=2: "17 math manipulatives powered by BrainingCamp"; "Kiddom partners with the award-winning GeoGebra for graphing"; "these tools are integrated right into Kiddom, so students can see and solve the problem on one screen".
- SUFF=0: Not all functions at 2.

## kiinara-os
- F1=0: "No page found describing how the system decides or sequences a learner's next activity".
- F2=0: "custom integrations" purchasable; "no developer docs, API reference or open standards".
- F3=0: "builds a living understanding of every entity in your institution" is a vague marketing claim with no mastery, skill or knowledge-state wording; "No mention of a mastery or skill model found". Lower code taken.
- F4=1: "Student data is visible only to authorised users of that institution, and access is limited by role."
- F5=0: Only "payment, messaging and cloud providers"; "no named independent tools, app directory or marketplace."
- SUFF=0: Not all functions at 2.

## kira-learning
- F1=1: Own platform: "Student Dashboard provides one place that tells every student exactly what to do next"; "identified skill gaps automatically trigger personalized practice." Kira "operates alongside existing LMSs"; no other vendors' tools sequenced.
- F2=2: Canvas LTI 1.3 documented: "OpenID Connect Initiation Url: https://app.kira-learning.com/api/lti/login"; "LTI Advantage services: ... Can view assignment data in the gradebook"; grade passback; Clever and ClassLink.
- F3=1: Own model: "Each skill gets one of six mastery levels"; "No documentation found of outside vendors' tools writing into Student Atlas."
- F4=1: "Features & AI tab in Settings is where you control which tools your organization's teachers and students can access" governs Kira's own features, not tools' access to student data.
- F5=1: "None found" running inside; integrations listed (Canvas, Clever, ClassLink, PowerSchool, Skyward).
- SUFF=0: Not all functions at 2.

## knomadix
- F1=0: Marketing only: "work through them at their own pace"; "No documentation of how next activities are chosen". No explicit next-activity claim.
- F2=0: "None found. No developer, API, integration or standards ... pages on the vendor site."
- F3=1: Marketing claim of mastery tracking: "providing a clear picture of student progress and mastery of key concepts." Capped at 1; "No documentation of a learner/mastery data model or of outside writes."
- F4=1: Website privacy text only: "We will not sell, distribute, or lease your personal information to third parties".
- F5=0: "None found. The site describes content creation by publishers and educators, not named independent tools".
- SUFF=0: Not all functions at 2.

## learning-os
- F1=0: "None found." Printable products only.
- F2=0: "None found."
- F3=0: "None found."
- F4=0: "None found. No privacy page on the site".
- F5=0: "None found."
- SUFF=0: Not all functions at 2.

## macmillan-learning
- F1=0: Adaptivity is within assignments and quizzes: "modifies questions, feedback, and resources based on students' performance as they work through assignments"; "personalized review plan ... between attempts". No cross-activity sequencing.
- F2=2: "setting up a deep integration of LTI Advantage (LTI 1.3) with Canvas"; two developer keys; "three sync levels" of grades; Canvas, Blackboard, Brightspace, D2L, Moodle.
- F3=0: Gradebook and "Insights and Reporting"; "Instructor-facing learning objective reporting" is a feature-list bullet "in select courses". "A documented persistent mastery or knowledge-state model ... none found". Lower code taken.
- F4=1: LTI service grants are Canvas-side; privacy notice. "Per-tool permissions over third-party tools inside Achieve ... none found".
- F5=1: "Achieve features native integration with Respondus LockDown Browser"; "iClicker is available with most Achieve courses" but "Ownership of iClicker and Respondus is not stated". One clearly independent tool.
- SUFF=0: Not all functions at 2.

## magicschool
- F1=1: Own tools: "the quiz results dashboard surfaces a curated set of follow-up resources based on quiz context, including relevant Student Rooms and Teacher Tools". Knowledge graph and "recommend what's next" are roadmap items.
- F2=1: "MagicSchool integrates with the following LMS platforms: Canvas, Schoology, Clever, and Classlink." with no standard named; rostering through Edlink; MCP connector is inbound content only. "No page found naming LTI, OneRoster ..." and no API docs.
- F3=0: Engagement categories and on-demand summaries ("highly engaged, moderately engaged ..."); "Personalized learning profiles" are listed under "WHAT'S NEXT?". No persistent knowledge-state model documented.
- F4=1: Tool toggles govern MagicSchool's own tools; connector on/off is a single switch; rostering permissions are set in Clever/ClassLink. No per-tool scopes over student data.
- F5=1: One tool inside: Adobe Image Generator ("You can use the Image Generator without an Adobe account"). Claude connector writes content in from outside. "No marketplace or developer program".
- SUFF=0: Not all functions at 2.

## mastery-connect
- F1=0: Curriculum maps and pathways are planning structures; "Automatic selection of a learner's next activity ... none found".
- F2=2: Public developer docs for "The MasteryConnect REST API (v2)" with OAuth 2.0; "Mastery Connect supports data connections ... via Ed-Fi v2.5.0"; Canvas LTI (same vendor) and Clever/ClassLink SSO.
- F3=1: Own mastery by standard with "Proficiency calculations ... default cut scores and decay rates"; "Independent vendors' tools writing mastery or scores into Mastery Connect trackers: none found (the REST API is documented as read-only".
- F4=2: Per-credential scopes documented: "Each endpoint requires one scope. All scopes are read-only."; "Request the narrowest set that does the job."; scope table "assessments:read", "reports:read".
- F5=2: "some assessments or items allow you to use a Desmos calculator" ("only available in districts that have a paid Desmos subscription") and "Respondus LockDown Browser (Mastery Connect OEM version)". The separate subscription and OEM wording indicate separate vendors, although the dossier notes ownership is not stated.
- SUFF=0: Not all functions at 2.

## mcgraw-hill
- F1=1: Own content: "ALEKS helps the student work on the topics they are ready to learn."; "Sequencing of other vendors' tools: none found".
- F2=2: "We currently support the Assignment Sync and Grade Passback portion of the IMS Global LTI Advantage Standard functionality within Canvas, Schoology, and Google Classroom."; OneRoster CSV 1.0/1.1 and REST; QTI 2.1.
- F3=1: Own knowledge model: "ALEKS ... maintain a detailed map of each student's knowledge." "Outside vendors' tools writing into a McGraw Hill learner model: none found".
- F4=1: Third-party list and privacy policy; "per-tool permission controls: none found".
- F5=2: "McGraw Hill partners with Proctorio to provide remote proctoring and browser-locking capabilities within Connect." and "ALEKS course product integrates Respondus browser-locking capabilities".
- SUFF=0: Not all functions at 2.

## moodle
- F1=1: "The availability API controls access to activities and sections ... unless users have a certain grade in a quiz." "No page opened states whether external (LTI) tool activities can serve as the condition for, or the target of, availability restrictions."
- F2=2: Web services framework, LTI Advantage consumer and provider ("Add LTI Advantage", "Supports Deep Linking"), xAPI plugin, developer plugin docs; 1912 plugins by outside developers.
- F3=1: Core competency functions ("Grade a competency.") with evidence from activity completion; "no documentation of an external tool writing competency ratings directly through LTI was found."
- F4=2: Per-tool sharing: "Specify whether the full name of the user launching the tool should be shared with the tool provider"; "whether the tool provider can add, update, read, and delete grades associated only with this external tool instance."
- F5=2: "Showing 1-24 of 1912 results"; Certified Integrations MathType, Cloud Poodll, BigBlueButton by Blindside Networks; "Plugins run inside the Moodle server".
- SUFF=0: Not all functions at 2.

## myopenmath
- F1=1: Own conditional release: "Use this to hide this assessment until a specific score is achieved on another assessment." "Adaptive sequencing or recommendations, or sequencing of other vendors' tools: none found".
- F2=2: "MyOpenMath is certified compliant with LTI 1.3"; Canvas "Dynamic Registration URL ... https://www.myopenmath.com/lti/dynreg.php"; Blackboard grade and membership services; Common Cartridge export.
- F3=0: Gradebook; outcomes appear only as "interface strings in IMathAS source code, not in the help documentation". "A mastery or knowledge-state model ... none found". Lower code taken.
- F4=1: LMS-side settings and privacy policy; "Per-tool permissions over external tools that MyOpenMath itself launches ... none found".
- F5=1: "IMathAS can also be an LTI 1.1 consumer, using the External Tool option for Link items." Mechanism exists but "Named independent third-party tools documented as running inside MyOpenMath ... none found".
- SUFF=0: Not all functions at 2.

## nearpod
- F1=0: Teacher-driven delivery ("you decide when it's time to move on"); "No documentation found of Nearpod itself choosing or sequencing a learner's next activity".
- F2=2: "Nearpod is LTI (Learning Tool Interoperability) Advantage certified" (vendor states); Canvas LTI 1.3 with Client ID, Deep Linking, SpeedGrader column; Blackboard LTI 1.3; Clever and ClassLink SSO.
- F3=0: Per-lesson reports only: "Each report is tied to your unique lesson code or link"; "No documentation found of a persistent per-student mastery or knowledge-state model".
- F4=1: Google scopes are Nearpod's own requests; website privacy notice. "No documented per-tool or per-app permission controls inside Nearpod found".
- F5=2: PhET "directly embedded in your Nearpod lesson" ("Add slide, add content, click PhET simulations.") and "embed a Desmos graph into their lesson" (dated changelog); YouTube video embedding.
- SUFF=0: Not all functions at 2.

## newsela
- F1=0: Level selection within a text, not sequencing: "a student's article level is a recommendation of the best level for the articles they will read next"; assignments remain teacher-selected. Lower code taken.
- F2=2: "LMS integration through LTI is reserved for subscribed districts"; Canvas "single sign on (SSO), rostering, content embedding, and Speedgrader access"; Schoology; "a Clever or OneRoster connection" for MAP data.
- F3=1: Own article-level model written also by one outside source: "Newsela allows districts to sync NWEA MAP Growth data to help us recommend initial article levels". One independent vendor, not two; lower code taken.
- F4=1: Google trusted-app and add-on scopes are Newsela's own requests; privacy policy. "No per-tool permission controls inside Newsela found."
- F5=2: PhET ("The simulation will be embedded on the Newsela page") and Tuva ("Exclusive Tuva interactive datasets ... for students to explore, manipulate, and analyze data").
- SUFF=0: Not all functions at 2.

## noredink
- F1=1: Own recommendations: "NoRedInk will show students a recommended mastered topic for which they can complete a Mastery Review." "all sequencing evidence found concerns NoRedInk's own content".
- F2=2: "Copy the numeric value found under the Details column for NoRedInk LTI." (Canvas Client ID setup); "Automatic grade passback from NoRedInk to your Canvas gradebook"; Schoology and Google Classroom passback; Clever and ClassLink.
- F3=1: Own mastery: "students progress through proficiency levels: Starting Off, Level 1, Level 2, Level 3, and Mastery." "No documentation found of other vendors' tools writing mastery or skill data into NoRedInk."
- F4=1: Google trusted-app step and Clever data list; privacy policy. No per-tool control inside NoRedInk.
- F5=1: "None found ... NoRedInk runs inside those systems rather than hosting other vendors' tools."
- SUFF=0: Not all functions at 2.

## odoo-schoolos
- F1=1: Claimed in listing: "LMS gamification, peer review, plagiarism scanning, learning paths & group submissions"; "None found of sequencing across other vendors' tools."
- F2=1: Proprietary REST API Gateway ("/api/v1/students , /students/<id> , /attendance ...") on a store listing; SCORM/xAPI playback is content consumption. "No mention of LTI, OneRoster, Caliper ..."
- F3=1: Own outcomes record: "A progress view and learning-outcomes page show how the student is performing against curriculum targets and goals." "None found of outside vendors' tools writing into the outcomes data."
- F4=1: "Issue narrowly-scoped API keys (read students, attendance, fees or academics" is a store-listing claim (marketing cap); role registry and consent register. Lower code taken.
- F5=1: "real meeting-provider connectors for Zoom, Microsoft Teams, Google Meet and BigBlueButton"; "None found of named independent developers' tools running inside SchoolOS."
- SUFF=0: Not all functions at 2.

## os-for-schools
- F1=0: "Pupils at Risk ... lists pupils whose attendance or marks are slipping"; "No sequencing of learner activities found."
- F2=1: An undocumented API panel exists ("Panel Api", "Dedicated guidance for this page hasn't been written yet.") and an integrations screen for a payment provider; "No public API documentation or open standard found."
- F3=0: "Each pupil's report card makes itself from their marks and the register." "No mastery, skill or knowledge-state model found."
- F4=1: Role-based access and a privacy policy that states what each provider receives; no per-tool controls.
- F5=0: Arkesel (SMS) and Paystack (payments) are service providers; "No third-party learning tools running inside the product found."
- SUFF=0: Not all functions at 2.

## pear-assessment
- F1=1: Own interventions generated from mastery data: "Generate a lesson (Pear Deck), practice set (Pear Practice), assessment (Pear Assessment) ... automatically aligned to the average mastery". "No documentation found of sequencing activities delivered by other vendors' tools."
- F2=2: Canvas launch URL "https://assessment.peardeck.com/api/auth/Lti"; "installs Pear Assessment once as an external (LTI) tool" in Schoology with grade sync; "ClassLink uses OneRoster to provision classes and users".
- F3=1: Own standards mastery ("Decaying Average", "Power law", "Student Mastery Profile"); external assessment data arrives by CSV upload for display "alongside Pear Assessment results", not written by outside tools.
- F4=1: Google trusted-app and Meet consent are Pear's own requests; "Data Operations permission" is a user role; privacy policy. No per-tool control.
- F5=1: "Google Hangouts Meet is now integrated with Pear Assessment."; calculator provider not named; partner names not rendered. One independent tool.
- SUFF=0: Not all functions at 2.

## savvas-realize
- F1=1: Cross-vendor data but own resources recommended: "one-click access from Renaissance Next and Renaissance Intelligence to a list of recommended enVision resources on Savvas Realize". The sequenced activities are Savvas's; the recommendation engine is Renaissance's.
- F2=2: "Savvas Realize is 1EdTech certified." (vendor states); "LTI 1.3 with LTI Advantage standard" with "Canvas, Schoology, Agilix Buzz, and D2L Brightspace"; grade sync.
- F3=1: Own mastery data ("Check standards mastery data for auto-scored assessments"); Star Math scores are viewed within enVision from one outside vendor, not written by two.
- F4=1: FAQ compliance statements and privacy policy; "No per-tool or per-app permission or scope documentation found".
- F5=1: Google Docs inside Realize ("complete assignments and submit responses seamlessly in Google Docs, all within the same platform"); Rubicon is content. One independent tool documented.
- SUFF=0: Not all functions at 2.

## schoology
- F1=1: "Student Completion Rules ... enable teachers to structure their course flow"; "Schoology cannot automatically detect submissions from these tools" and "No page opened states which completion-rule types apply to external tool materials."
- F2=2: Developer site with REST API, app platform (SAML and OAuth), "LTI Advantage Extensions ... Assignment and Grade Services v2.0, Deep Linking v2.0, Names and Roles Services v2.0".
- F3=1: Standards-based gradebook with district objectives aligned to materials including external tools, graded by teachers ("You must grade each aligned objective"); "No page opened describes an external tool writing per-objective mastery scores".
- F4=2: Per-tool privacy setting: "Privacy The information sent to the publisher upon the tool's launch ... User's name Email or username"; "organizations will be alerted that your app uses the enabled services."
- F5=2: "Schoology's App Center provides instructors with access to software developed by other companies directly within Schoology."; Formative and Khan Academy documented; Google Drive, OneDrive, Teams apps.
- SUFF=0: Not all functions at 2.

## schoolos-ai
- F1=0: Engagement scoring for admissions and advancement; "No sequencing of learner activities found."
- F2=1: Proprietary API claimed without docs: "API access for everything. Build custom integrations".
- F3=0: "Weighted average" gradebook; "No mastery, skill or knowledge-state model found."
- F4=1: "11 configurable user roles with granular permissions"; row-level isolation; privacy page.
- F5=0: "None found. The home page shows a 'Platform Integrations' count but names no integrations".
- SUFF=0: Not all functions at 2.

## schoolos-live
- F1=0: "None found."
- F2=0: "None found. No API, developer page or standard named".
- F3=0: "performance trend analytics for every class"; "No mastery, skill or knowledge-state model found."
- F4=1: Claimed control: "Role-based access for Admins, Teachers, and Parents, ensuring data privacy and security." Privacy page 404.
- F5=0: "None found."
- SUFF=0: Not all functions at 2.

## schoolos-net
- F1=0: "Smart Promotion System" is administrative; "No sequencing of learner activities found."
- F2=0: "None found. No API, developer page or open standard named".
- F3=0: "CA + exams automatically calculated. Termly and cumulative results."; "No mastery, skill or knowledge-state model found."
- F4=1: "roles and permissions configured by the school"; DPA and privacy policy.
- F5=0: Resellers and generic subprocessors; "No named third-party tools running inside the product found."
- SUFF=0: Not all functions at 2.

## schoolos-systems
- F1=0: Built-in LMS "progress tracking" and approval workflows; "No documentation of sequencing learner activities found."
- F2=1: "Secure API Routes" counter and "Custom integrations"; "API Reference" link points to "#". Proprietary API claimed, no docs.
- F3=0: "One student record. All views." and "at-risk prediction"; "No mastery, skill or knowledge-state model found".
- F4=1: Claimed controls: "RBAC + ABAC Hybrid 11 system roles"; "granular access controls"; no privacy policy reachable. Marketing cap.
- F5=0: "Full LMS Built In ... no third-party needed."; "No named third-party tools running inside the product found."
- SUFF=0: Not all functions at 2.

## schoolware
- F1=0: "None found."; AI homework checking is "Coming soon".
- F2=1: "SchoolWare speaks MCP, the open standard that connects AI assistants to live systems." Standard claimed; "No public developer documentation for the MCP endpoint or the API found."
- F3=0: "Exams, homework, grading, and report cards & transcripts"; "No mastery, skill or knowledge-state model found."
- F4=1: "Custom roles and fine-grained, module-level permissions"; the connector "inherits their role and permissions" and "can revoke it at any time" is a single connection switch, not per-tool scopes.
- F5=1: "Connect SchoolWare to ChatGPT, Claude, or any assistant that speaks the Model Context Protocol" are outside assistants connecting in; Stripe and AWS are infrastructure. "No marketplace or third-party apps running inside the product found."
- SUFF=0: Not all functions at 2.

## scoolio
- F1=0: Teacher-authored ordering: "Arrange the curriculum into a sequence learners can follow."; "No page found describing the system choosing a learner's next activity automatically".
- F2=0: "Do not assume that a generic third-party connector or a public developer API is supported"; CSV exports; "/developers and /api return 404."
- F3=0: "gradebook information and learner progress"; "No mention of a mastery, skill or knowledge-state model found."
- F4=1: "Authorized administrators use Users & Access and Roles & Permissions to manage access."; "Permissions described are per user role".
- F5=1: Links out to meeting providers: "validated links for Google Meet, Zoom, Microsoft Teams, Jitsi"; "Automatic provider meeting creation is not implied by storing a meeting link." No app directory.
- SUFF=0: Not all functions at 2.

## shoofly-ai
- F1=0: "None found of sequencing what a learner does next."
- F2=0: "None found (no API, developer docs or standards)."
- F3=0: "None found."
- F4=1: "We deploy systems with role-based access and data-handling controls"; privacy policy.
- F5=0: "None found of independent tools running on it."; partner page is resellers.
- SUFF=0: Not all functions at 2.

## skodle
- F1=0: AI tutors "adjust difficulty, examples, and pacing" within a tutoring session; teacher insights. No cross-activity sequencing; "No page found describing sequencing across other vendors' tools."
- F2=1: "skodle does not come with pre-built connectors ... What it has is an integration framework"; OIDC SSO with Google or Microsoft; "no public API or developer docs ... no LTI, OneRoster ... named".
- F3=1: Own record: "ATL progression Per-student Introduced → Demonstrated, tracked with evidence."; "stored as a record a student carries between years". "None found describing outside vendors' tools writing into the learner record."
- F4=1: "Connection, configuration, permissions and disconnect per integration" governs skodle's own outbound connections on a product page; role capability layer. Lower code taken.
- F5=1: "Available means catalogued, not running."; Google Classroom, Drive, Calendar frameworks listed; "no independent education tools named as running inside skodle".
- SUFF=0: Not all functions at 2.

## spyral-aios
- F1=1: Own labs: "AI-powered quizzes, personalised learning paths, 2D/3D Labs"; "AI Challenge Engine with adaptive difficulty". "no page found describing sequencing of other vendors' tools."
- F2=1: Proprietary REST API documented ("Base URL: https://tryspyral.com/api/v1 ... Auth via X-Api-Key"); Google Classroom import; "No mention of LTI, OneRoster ...". No outside system shown using it.
- F3=1: Own competency model: SPI endpoint "Returns a 0-100 score, grade, and per-competency mastery breakdown"; "the developer page does not state whether these results are stored in a school's AiOS student record."
- F4=1: Roles; "403 API_NOT_ENABLED This API is not enabled on your key"; "No page found describing per-app or per-tool scopes over student data for third-party tools."
- F5=1: Google Classroom import (data sync); service providers; embeds are outbound. "No page found naming independent developers' tools that run inside AiOS."
- SUFF=0: Not all functions at 2.

## string-os
- F1=1: Own adaptive challenges and an agent acting in apps on request: "Students move through their textbook's units in challenges that adapt to their level."; "Post the fractions lesson to Grade 8A: a video, then a quiz." Marketing only; no documentation of learner sequencing across named vendors' tools.
- F2=1: "Six APIs to build your product on." described on a marketing page; "No developer documentation site, API reference, or App Store listing page found"; SAML and OAuth SSO.
- F3=1: "A skill map that tracks mastery of each concept in the curriculum." Outside apps write "results to the unified gradebook" (grades) and "Kahoot quiz results" appear in an illustration; all marketing, so capped at 1.
- F4=1: "the String DNA API reaches students' profiles only with their school's consent" is a marketing FAQ claim; role-based access. Capped at 1.
- F5=1: Fifteen named apps "String connects to" and a claimed "String App Store", all on marketing pages; String's assistant runs inside Scratch (reverse direction). Capped at 1.
- SUFF=0: Not all functions at 2.

## tci
- F1=0: Teacher-paced and teacher-assigned; AI remediation is "developing". "AI-generated content is only available to students when assigned by a teacher."
- F2=2: "TCI's LTI 1.3 integration with Canvas"; "OneRoster API ... v1.1"; QTI export; grades "sync over to your Canvas grade book"; "1EdTech CERTIFIED" logo.
- F3=1: Own standards record: "turning scores into a clear picture of standards mastery for your whole class"; "a running record". "Outside vendors' tools writing into TCI's standards or mastery data: none found."
- F4=1: Privacy policy; "district- and teacher-level control to opt into features that display AI-generated content". No per-tool control.
- F5=1: Partner logos (Aeries, Clever, Infinite Campus, Teams, GG4L) are rostering and LMS integrations; "Independent developers' tools running inside TCI ... none found".
- SUFF=0: Not all functions at 2.

## theschoolos
- F1=0: Operational routing only ("Requests are triaged automatically."); "None found regarding sequencing of what a learner does next."
- F2=1: OneRoster 1.1 and 1.2 consumption described on a marketing integrations page ("Four methods: manual CSV, flat CSV over SFTP, OneRoster bundle over SFTP, or the OneRoster API"); "no public developer docs or API reference found". Marketing cap.
- F3=0: "What they never touch Academic records"; "None found."
- F4=1: "Each integration requests only the scopes it actually uses" and "Write access is enabled per connection" describe schoolOS's own outbound connections on a marketing page; roles and Google scopes. Lower code taken.
- F5=1: Jamf, MySchoolBucks and knowledge sources are "data sync and actions into those systems, not tools running inside schoolOS".
- SUFF=0: Not all functions at 2.

## timeback
- F1=2: PowerPath Course Sequence API: "query course sequence to get the next stage in the student learning path"; stage types "course - assessment - hole-filling"; "learningAppId ... examples: - alpha_write - mobymax"; "'literably' selects the PK-2 Reading screener stage"; "the platform can route them to remediation (from your app or another) and bring them back to retry." Re-checked: the sequence is documented to route students into learning apps including third-party developers' apps and names two non-first-party apps (mobymax, literably); first-party apps carry the alpha_ prefix and the docs distinguish "first-party and third-party" apps. Vendor caveats ("This is a conceptual map", "A score below 90% does not universally or immediately create a hole-filling course") qualify deployment, not the documented contract.
- F2=2: OpenAPI specs for "caliper-api", "case-api", "clr-api", "oneroster-api", "powerpath-api", "qti-api", "openbadges-api"; Partner Events API; outside apps named in the docs (mobymax, literably, edulastic). "the existence of an implementation is not a certification claim".
- F3=2: "The middle layer provides mastery tracking"; third-party apps write to it: "Level 1 (existing third-party apps) feature row: Core learning events (XP, mastery)"; SDK: "If your app tracks mastery at the lesson level, pass masteredUnits"; EduBridge: "highest grade mastered by a student ... across different data sources (currently edulastic, placement and test out datasets)". Re-checked: the write path for independent vendors' apps is documented as a class and edulastic is named as a mastery source; the vendor warns "It does not automatically make two apps' identifiers, progress scales, or mastery policies interchangeable."
- F4=2: Per-client OAuth2 scopes documented in the OpenAPI: "roster-core.readonly", "roster-demographics.readonly", "gradebook.createput", "powerpath.readonly", "caliper/v1p2/scope/events.write". "No page was found stating how a school or parent grants or limits a specific app's access", so control sits with the platform operator, but scopes are per app.
- F5=2: "learning apps (both first-party and third-party)"; "Your app works on the Timeback platform"; Level 2 apps "use Timeback's learning systems instead of building their own"; named apps mobymax, literably, edulastic. Beyond launch and data sync because the platform supplies the apps' sequencing and mastery engine.
- SUFF=0: The documentation names only one independent tool (edulastic) as a mastery data source and describes other third-party writers generically; it does not show two named independent vendors' tools writing to the model that the course sequencer acts on, and the vendor states that routing "vary by subject, app, and workflow", that "An adapter or configured workflow must support the required content and routing", and that the how-it-works map "does not establish a live deployment or universal automation". Unsure, so the lower code is taken.

## vista-higher-learning
- F1=0: Marketing addressed to the teacher ("Create a personalized learning path for your multilingual learners ... point you to the right resources"); within-activity "try again or move on"; teacher reordering. No system sequencing documented; lower code taken.
- F2=2: "This integration works with the universal 1EdTech ... LTI Advantage 1.3 standard ... and is certified by 1EdTech"; Thin Common Cartridge, OneRoster CSV; grade exchange with Blackboard, Canvas, Brightspace, Moodle, Schoology.
- F3=1: Marketing claim of "standards-based progress monitoring and proficiency assessments that tell you exactly where each student needs support"; help search for "mastery" returned 0. Capped at 1; "Outside vendors' tools writing into a vhl central learner model: none found."
- F4=1: Privacy policy and data-security commitments; instructor AI toggle. "Per-tool or per-app permission or scope documentation: none found."
- F5=1: TeachShare and Wayground named as AI partners but "The page does not state whether these run inside vhl central."; TokBox and Pubnub are infrastructure; Clever rostering.
- SUFF=0: Not all functions at 2.

## wayground
- F1=1: Own VoyageMath: "VoyageMath uses an adaptive algorithm; it analyzes student performance data to personalize learning paths." "No documentation found of sequencing activities from other vendors' tools."
- F2=2: "Wayground x Canvas via LTI", Schoology, Blackboard, Moodle, Brightspace, Toddle via LTI; Canvas "Dynamic Registration flow"; "grades are synced to the LMS automatically"; Clever and ClassLink.
- F3=1: Own mastery: "Standards Mastery Report ... Decaying Average"; VoyageMath skill mastery. "Outside vendors' tools writing mastery or results into Wayground: none found."
- F4=1: Scopes listed are "scopes Wayground requests from Google; no documentation found of Wayground granting per-app scopes to other tools over its own student data."
- F5=2: "PhET Interactive Simulations are now integrated with Wayground! ... students to interact with the simulations and answer questions about them at the same time" and "Common Assessments on Wayground can be set up to use LockDown Browser by Respondus".
- SUFF=0: Not all functions at 2.

## writable
- F1=1: Own recommendations: "Writable makes targeted instruction easy with recommended assignments. Based on students' proficiency in skills, teachers can find and assign activities". No other vendors' tools sequenced.
- F2=2: Canvas "Step 2: Configure the LTI Key" with "JSON URL: https://app.writable.com/canvas-ltia" and automatic score sync; "Writable offers both LTI and API connections with Schoology."; Google Classroom grade sync.
- F3=1: Own proficiency report ("track skill mastery over time"); Canvas scores flow back as grades. "No documentation found of other vendors' tools writing skill or mastery data into Writable."
- F4=1: Google scopes are Writable's own requests; AI feature controls at district level; privacy policy. No per-tool control inside Writable.
- F5=2: "Writable's Originality Check (powered by Turnitin SimCheck)" with Turnitin EULA acceptance, and "embedded Google Docs" in assignments (help article title and scope rationale).
- SUFF=0: Not all functions at 2.
