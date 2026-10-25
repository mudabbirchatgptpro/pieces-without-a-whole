# Coder B reasons

One line per function: code and the dossier quotation (or its absence) that decides it. Where unsure between two codes, the lower was chosen and the reason is given. Interpretation used for F1 and F3 code 2: the sequenced activities, or the writers to the learner model, must include at least two named vendors independent of the product's own vendor; a generic mechanism that would admit external tools, without documented instances, is coded 1. Marketing copy alone is capped at 1.

## academic-ai-solutions
- F1=1 marketing claim only: "Optimal course paths connected to career outcomes"; no docs on whose tools.
- F2=1 claimed "Secure connections to your existing systems of record", no API docs, no standard named.
- F3=1 marketing claim of a learner model only: "A persistent AI companion that knows the student" and "A persistent learner record built to travel with the student"; no mastery model documented, marketing caps at 1.
- F4=0 no privacy policy (link is "#"), no controls found.
- F5=1 integrations/partners listed ("Verified merchants, housing partners...") but no tool documented running inside.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## access-pearson
- F1=1 own-tool adaptivity only: DSM sets of 8 questions; "recommend modules to help them build mastery"; "No documentation found of Access Pearson sequencing activities from other vendors' tools."
- F2=2 documented LTI 1.3 implementation used in outside LMSs: "Access Pearson (LTI 1.3) works with all LMSs"; "recognized by IMS Global as LTI Certified".
- F3=1 own-tool mastery only: "When you have correctly answered all of the questions in the module, you have mastered all the material"; no outside writes.
- F4=1 privacy notice only; "No per-app permission or scope list for Access Pearson found" (Google check boxes are Google's control, not Pearson's).
- F5=1 it runs inside others' LMSs; "None found of independent developers' tools running inside Access Pearson".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## amplify
- F1=1 own programs only: "mCLASS automatically places students on an adaptive path within Boost Reading"; "No documentation found of Amplify sequencing activities delivered by other vendors' tools."
- F2=2 published LTI 1.3 config used by Canvas: "Paste the JSON URL from Amplify ... This will enable both launch and grade sync"; 1EdTech certifications stated.
- F3=1 own-tool skill data: "Boost Reading helps students ... grow across 13 critical skills areas"; no outside writes.
- F4=1 privacy policy, school-level control: "we enable Schools to control the use, access, sharing"; no per-tool control by Amplify.
- F5=1 integration partners listed (Clever, Google, Canvas); "None found of independent developers' tools running inside Amplify programs".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## apkaos
- F1=0 automations are administrative: "messaging parents after 3 absences"; no learning-activity sequencing found.
- F2=0 "None found: no developer docs, API reference or open standards"; Excel import only.
- F3=1 own marks/insights only: "Academic Intelligence Topic-level insights on student performance"; no mastery model.
- F4=1 user roles and privacy policy: "Custom roles so every user sees only what they should"; "No page found describing per-app or per-tool permission scopes".
- F5=1 integrations listed (Razorpay, WhatsApp, SMS) as service providers, no independent tools running inside.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## appcorp-ai-os-school
- F1=1 marketing claim: "AI builds a unique learning path for every student"; no docs on whose tools.
- F2=1 claimed "White-label AI tutoring engine via REST API"; "No public developer documentation found"; no standard named.
- F3=1 marketing analytics only: "Engagement scores, attendance patterns, assessment trajectories"; no mastery model documented.
- F4=1 marketing claim and policy: "granular data access controls"; "No per-tool or per-app permission documentation found."
- F5=0 "None found. The product page names no third-party tools running inside the product."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## big-ideas-math
- F1=0 teacher assigns; adaptivity is within a single test: "Each test has an entry point ... and adapts based on student responses"; no system sequencing across activities documented (lower code chosen over 1).
- F2=2 documented LTI 1.3 with Canvas and Schoology: "Deep linking and grade pass back between BigIdeasMath.com and Canvas".
- F3=1 own-tool skill data: Progression Benchmark "assesses students on a continuum of skills"; "No documentation found of outside vendors' tools writing data into these reports."
- F4=1 privacy policy, institution-level control: "giving the educational institution direct control"; no per-tool control.
- F5=1 Desmos and GeoGebra investigations are "embedded links in the student eBook app"; unclear whether they run inside, so lower code; "No app marketplace or plugin mechanism".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## blackboard
- F1=1 release conditions and forced sequence over course items: "You can set a forced sequence to a module"; "No page opened states whether external (LTI) tool items or their returned grades can serve as release conditions."
- F2=2 public REST and LTI 1.3 developer docs: "AGS ... allows your tool to create columns ... grade user data".
- F3=1 Outcomes mastery computed in Blackboard: "A weighted median is used to calculate each student's mastery level"; LTI tools can be aligned to goals but "No page opened states whether a score returned by an LTI tool aligned to a goal is counted in the Outcomes mastery calculation"; AGS writes grades only.
- F4=2 per-provider authorization: "You may be asked to authorize the provider's access to certain user information"; 3LO limits per REST app.
- F5=2 App Catalog plus Kaltura ("The list of suggested tools contains the authorized tools for your institution, such as Kaltura"), Turnitin, McGraw-Hill.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## blended-os
- F1=1 marketing only: "Access scheduling, grading, analytics, and AI personalization"; no mechanism found.
- F2=1 claim only: "we can integrate with any 3rd party platform"; no API docs or standard.
- F3=0 own grades and progress only ("Enrollment, grades, attendance"; "track progress"); not a knowledge model and not a cross-tool record; "None found describing a mastery / skill / knowledge-state model".
- F4=1 "role-based access control, allowing for tiered permissions" (user roles); "no per-app or per-tool permission".
- F5=0 only analytics services (Clarity, Sentry); "no named independent education tools running inside".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## brightspace
- F1=1 release conditions "over its suite of tools"; "No page opened states whether a grade written by an external LTI tool can serve as a release condition."
- F2=2 Valence API with OAuth 2, LTI Advantage, IntegrationHub dynamic registration.
- F3=1 outcomes can align to LtiLink activities, but "No page opened describes an external tool writing outcome achievement levels into Brightspace"; mastery view computed internally.
- F4=2 OAuth scopes per app: "users:userdata:read"; "Data Access Transparency: Review ... exactly what information ... the app will access".
- F5=2 IntegrationHub: Panopto, Zoom; Turnitin, Kaltura listed.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## canvas
- F1=1 (lower of 1 and 2): modules can sequence items of type "'ExternalTool'" with "require_sequential_progress" and "min_score" completion requirements, so the mechanism admits external tools, but no documentation shows activities from two or more named independent vendors' tools being sequenced, and Mastery Paths excludes them ("Files, External URLs, and External Tool module items cannot be used as conditional items in Mastery Paths").
- F2=2 public API docs, LTI Advantage AGS Score API, developer keys.
- F3=1 outcome results are computed by Canvas; tools write scores only ("Can create and update submission results"); "No endpoint for an external tool to create an outcome result"; cross-tool record is grades only.
- F4=2 developer key scopes and per-tool privacy_level: "\"anonymous\" will not include any of these fields".
- F5=2 LTI tools delivered inside courses: ALEKS, Apex Learning, FeedbackFruits listed on EduAppCenter; "launches the student to a custom assessment".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## cengage-learning
- F1=1 MindTap learning path and Mastery Training sequence Cengage activities: "Customize your course by adding, removing, and reordering your units and activities"; Turnitin and Bongo appear only as activity types in help navigation, not documented as sequenced or gated items, so lower code.
- F2=2 documented LTI Advantage with Canvas and Google Classroom: "New institutions will be integrated using LTI Advantage".
- F3=1 own-tool model: "The personal study plan identifies areas for improvement based on students' performance"; "No documentation found of outside vendors' tools writing mastery".
- F4=1 K-12 privacy notice only; "No per-app permission or scope list found".
- F5=2 independent tools documented inside MindTap: Turnitin Feedback Studio/PeerMark and "View and evaluate student presentations with Bongo".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## ck-12-foundation
- F1=1 own content only: "advancing the student to the next concept"; "suggesting personalized CK-12 content"; "No documentation found of CK-12 sequencing activities from other vendors' tools."
- F2=2 documented LTI 1.3 install for Canvas, ClassLink and Clever SSO: "In the install app window, select LTI version 1.3."
- F3=1 own skill meter: "The skill meter ... takes into account the difficulty level of each question"; no outside writes.
- F4=1 data-sharing choices are made in the LMS/Clever, CK-12 itself has privacy pledge and DPA only.
- F5=1 external media can be embedded via bookmarklet (Prezi, SlideRocket) and partners listed; embedded media is not shown as tools running inside, lower code; "No app marketplace or plugin program".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## classlink
- F1=0 "No page opened describes ClassLink deciding or sequencing what a learner does next"; apps are teacher-assigned launches.
- F2=2 public partner docs for OneRoster Roster Server and OAuth 2 APIs with outside developers (Khan Academy rostering via ClassLink): "Roster Server provides OneRoster data shared by school systems".
- F3=0 roster and usage data only: "No mastery, skill, outcome or competency record was found".
- F4=2 per-application provisioning and field masking: "The school system needs to grant your application access before you can retrieve its data"; DataGuard masks fields per vendor; PAWs per vendor.
- F5=1 SSO launch and roster sync only: "no page opened describes third-party tools running inside ClassLink beyond launch".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## clever
- F1=0 "No page opened describes Clever deciding or sequencing what a learner does next"; resources are assigned to courses by admins.
- F2=2 public API v3.1 OpenAPI spec and developer docs used by app partners: "Use the Clever API to access district, school, roster, and user data based on your application's scopes".
- F3=0 grades only pass through to the LMS ("grade passback from your application, through Clever and into a district LMS"); "No mastery, skill, outcome or competency object was found"; no persistent learner model in Clever (lower code).
- F4=2 "you can set up sharing permissions on an app-by-app basis".
- F5=1 apps are launched by SSO and rostered (app gallery: Canva Education etc.), not running inside Clever.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## commonlit
- F1=0 fixed curriculum order and teacher assignment only: "Adaptive or automatic sequencing of learner activities: none found" (lower code chosen over 1; a recommended unit order is not the system sequencing the learner).
- F2=2 documented LTI External Tool integration with Canvas grade passback: "select External Tool under Submission Type. Then, click Find and select CommonLit"; "LTI only allows CommonLit to import a Canvas course".
- F3=1 own assessments only: "students' performance on specific standards categories"; no outside writes.
- F4=1 privacy policy only; "per-tool permission controls inside CommonLit: none found".
- F5=1 integrations listed (Canvas, Clever, ClassLink, Google Classroom) as links/sync; "Independent third-party tools running inside CommonLit ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## delta-math
- F1=1 own content only: "an individualized remediation assignment is generated for each student" from DeltaMath tests.
- F2=2 documented LTI 1.1 and 1.3 setup with Canvas, Schoology, Infinite Campus: "Our LTI 1.3 Infinite Campus Learning Suite integration ... allows for rostering and grade passback".
- F3=1 own skill and standards data: "Performance reports against standards are available"; outside data only by manual student entry.
- F4=1 privacy policy; "Per-tool permission controls inside DeltaMath over other apps: none found".
- F5=1 YouTube videos assignable (one external source); "Independent third-party tools running inside DeltaMath ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## derivita
- F1=0 teacher builds and assigns work; recommendations go to teachers ("Reteach from the top of the list down"); "Automatic or adaptive sequencing of learner activities: none found" (lower code).
- F2=2 published LTI 1.3/Advantage Canvas developer-key JSON with AGS and NRPS scopes; "Built on the IMS Global LTI 1.3 and LTI Advantage standards".
- F3=1 own mastery model: "the platform computes a mastery score from that student's results"; "Outside vendors' tools writing mastery or skill data into Derivita: none found".
- F4=1 privacy policy; the LTI scopes are what Derivita requests, not a control over other tools; "Per-tool permission controls inside Derivita over other apps: none found".
- F5=1 one third-party service (Proctorio lockdown) plus TI calculator images; not two independent tools running inside, and no app framework.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## discovery-education
- F1=1 own lessons only: DreamBox engine "picking the next best lesson for the student"; NWEA MAP scores are used as teacher-selected input but lessons delivered are DreamBox's own.
- F2=2 documented LTI 1.3 Canvas setup and OneRoster via ClassLink: "Paste the following URL in the JSON URL field".
- F3=1 own proficiency model: "number of standards in which students have become proficient, based on completed lessons"; NWEA data is teacher-selected for assignments, not written into the model by NWEA.
- F4=1 admin product filters and privacy policy; "per-tool permission controls over other vendors' apps: none found".
- F5=1 partner media content channels (MythBusters, NBA) are content, not independent tools; "Independent developers' software tools running inside ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## ed-fi
- F1=0 "No page opened describes Ed-Fi or the ODS / API deciding or sequencing what a learner does next"; InterventionPrescription only records interventions.
- F2=2 open standard with public API docs and named implementers: "Skyward, PowerSchool, Infinite Campus ... have implemented the Ed-Fi Data Standard"; certification registry.
- F3=1 (lower of 1 and 2): several certified vendors write assessment results tied to learning standards ("Cambium Assessment", "Amplify mCLASS", "i-Ready ... Diagnostic"), and gradebook entries "can be a Grade or a CompetencyLevel", but the documentation describes stored assessment results and grades ("designed to collect and exchange data that is useful in the interpretation of student assessment results"), not a modeled knowledge state, so unsure between 1 and 2 and chose 1.
- F4=2 per-consumer claim sets and profiles: "Claims and claim sets provide fine-grained access control"; "The Profile can then be assigned to API consumer applications".
- F5=1 vendors' systems sync data to it; "no page opened describes tools running inside it".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## edlink
- F1=0 "No page opened describes Edlink deciding or sequencing what a learner does next"; teacher-driven deep linking.
- F2=2 public REST API docs, LTI and OneRoster support, used by Clever LMS Connect.
- F3=1 cross-tool record of grades only: "Assignments, submissions, and grades can be synced and managed directly within Edlink"; "No learner mastery or knowledge-state entity was found".
- F4=2 per-integration controls: "Developers can request (and district can control) what fields are shared for each integration"; sharing rules.
- F5=1 data sync and launch between apps and LMSs; "no page opened describes applications running inside Edlink itself".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## edmo
- F1=0 admissions follow-ups only: "triggers tailored follow-ups by profile"; "None found of sequencing of learning activities."
- F2=1 public OpenAPI spec for its own proprietary agent builder API but no open standard and no outside developers shown using it; connectors (Canvas, Blackboard) are vendor claims.
- F3=0 admissions/student profile records only: "None found on a model of what the learner knows."
- F4=1 policy and user roles: "Role-based access, audit trails"; no per-tool control.
- F5=1 connected services by sync (Twilio, Zoom) and EDMO runs inside Salesforce; "None found of independent developers' tools running inside EDMO."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## edpuzzle
- F1=1 own-tool next-step recommendations only: "Edpuzzle recommends follow-up tasks based on where the class encountered challenges ... preview it, and assign it"; no sequencing across other vendors' tools.
- F2=2 documented LTI 1.1 setup in Canvas, Blackboard, Schoology, Brightspace with grade passback.
- F3=0 own grades and watch percentage only: "see the grade that each student got in each video"; "Skill/mastery or knowledge-state model ... none found"; not a cross-tool record.
- F4=1 privacy policy; school can enable/disable AI features; no per-tool control.
- F5=1 YouTube video embedding is one external source; "App marketplace or plugin framework ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## edunation-os
- F1=1 own-app recommendations only, marketing pages: "Recommends targeted interventions when a student's attainment data signals a gap".
- F2=1 proprietary API with thin ReadMe docs requiring an access request form, Getting Started page is template text; no learning-data standard named; no outside developers shown.
- F3=1 own-app record only: "Every app reads from and writes to the same institutional record" (Edunation apps); "None found describing outside vendors' tools writing attainment data".
- F4=1 user roles: "Role-based access across every module"; "no per-third-party-app scope or consent controls".
- F5=1 "500+ Connected apps" by SSO; "no named independent education tools ... that run inside EdunationOS".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## edynamic-learning
- F1=0 static curriculum tracks and pacing lights only: "sequenced learning tracks aligned to national and examination standards"; "No page found describing adaptive paths, automatic recommendations" (lower code).
- F2=2 documented LTI 1.1 and 1.3 and course cartridges for LMSs: "Learning Tools Interoperability is a standard that allows publishers to centralize content".
- F3=0 own points-based grades only: "As eDynamics utilizes a point system, we do not use these reports" (mastery); assessments stored in the customer LMS; no learner model.
- F4=1 lists its own Google scopes and privacy policy; no control over other tools.
- F5=1 "None found running inside eDynamic Learning products"; it is delivered inside LMSs and a hosted Buzz LMS (integrations only).
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## formative
- F1=1 own-tool next steps: "Luna analyzes student performance against learning standards and instantly recommends Luna Next Steps"; "No page found describing automatic sequencing of activities across other vendors' tools."
- F2=2 documented LTI 1.1/1.3 with grade passback and OneRoster 1.1/1.2 rostering.
- F3=1 own standards record: "You can see each student's average for each standard you've tagged"; Newsela results "only be visible within Newsela"; no outside writes.
- F4=1 LTI grants are configured in Canvas, Formative's own policy only; "level of access ... within an iFrame is contorlled solely by that website".
- F5=2 independent tools run inside via iFrame: "allows your students to interact with the other website without leaving Formative" (Geogebra, Flipgrid, Edpuzzle, Wakelet) plus Respondus LockDown Browser.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## google-classroom
- F1=0 "No page opened describes Classroom deciding or sequencing what a learner does next across activities"; teachers select and assign.
- F2=2 public Classroom API and add-on developer docs with partner developers.
- F3=1 add-ons write grades only ("pass a grade back ... as a draft grade"); learning goals tag content, "no per-student mastery record was described".
- F4=2 per-app OAuth scopes and admin access settings: "Apps configured with an access setting (Trusted, Limited, Specific Google data, or Blocked)".
- F5=2 add-ons run in iframes inside Classroom: "Kahoot!, Pear Deck, IXL, ReadWorks, and Nearpod".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## h5p
- F1=0 sequencing within a single content item only: Branching Scenario "Learners make choices that determine the content they will see"; "No page found describing H5P deciding or sequencing ... across separate activities".
- F2=2 open-source developer docs, LTI 1.3 setup docs for Canvas, Brightspace, Moodle, xAPI, community-built plugins.
- F3=0 no learner model: "H5P.com doesn't store xAPI statements, it's only forwarded to the LRS"; only own scores and answers.
- F4=1 organization-level settings (LRS forwarding disabled by default with an anonymity choice, report visibility by role); no per-tool permissions over student data (unsure between 1 and 2 for the single LRS endpoint, chose 1).
- F5=2 independent developers' content types run inside H5P: Image Pairing "developed by Jithin under ... ICFOSS", "The personality quiz is created by Lumenia", Timeline.js by Knight Lab.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## hmh
- F1=1 own programs only: "HMH Personalized Path connects MAP Growth scores directly to proven programs ... Read 180, Math 180, and Waggle"; NWEA is an HMH company; "no page found describing sequencing of independent vendors' activities".
- F2=2 documented LTI Advantage, OneRoster ("fully certified for OneRoster 1.1"), QTI, Common Cartridge.
- F3=1 own standards proficiency: "Proficiency is only measured in Waggle Practice assignments"; "No page found describing independent (non-HMH) vendors' tools writing".
- F4=1 one sentence on approving a partner data sharing agreement plus LMS/Google-side settings; no documented per-tool scopes controlled by HMH (unsure, chose lower).
- F5=1 connected programs Waggle and HMH Writable are HMH's, Amira's ownership not established; no independent tools documented running inside Ed.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## ibl-ai
- F1=1 own courses only: "A pathway is a guided sequence of courses and outside resources" but "items badged RESOURCE are outside links and open in a new browser tab" (links, not tools); skills used "to recommend courses".
- F2=1 public REST API reference and LTI 1.3 tool endpoint docs exist, but no outside developers or named outside platforms are shown using them and no other standard appears; unsure between 1 and 2, chose 1.
- F3=1 own skills record: "skills you have earned by completing courses, skills you self-reported"; "No page found describing outside vendors' tools writing into the skills record."
- F4=1 user RBAC and connector availability scopes ("Agent: available only to this agent"); no per-tool permissions over student data documented (lower code).
- F5=1 MCP connectors to business services (Asana, GitHub) and an unnamed "5,700 community-contributed skills" claim; "No independent third-party education tools (by name) found running inside the OS".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## ixl-learning
- F1=1 own skills only: "IXL Recommendations are personalized suggestions for math and language arts skills"; "all sequencing quoted above returns IXL skills".
- F2=1 Canvas/Schoology integration and grade sync documented, but "the pages opened do not name LTI, OneRoster, Caliper, QTI, or any other standard"; no public developer docs (lower code).
- F3=1 own model: "The SmartScore ... is the best possible measure of how well a student understands a skill"; MAP RIT scores are entered manually, "No page found describing other vendors' tools writing skill or mastery data into IXL automatically."
- F4=1 privacy policy; permissions are set in ClassLink; "No page found listing ... per-tool permission controls inside IXL."
- F5=1 integrations run IXL inside other platforms; "None found" inside IXL.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## k12-tutoring-by-stride
- F1=1 own sessions only: Beacon "generates a numbered list of Recommended Next Sessions"; "Sequencing of other vendors' activities: none found".
- F2=0 Canvas access is an External URL link and SSO via Clever; "Public developer docs/API, LTI, OneRoster ... none found"; no interface of its own documented.
- F3=1 own AI summaries: "describe specific concepts the student has demonstrated mastery in and specific gaps"; no outside writes.
- F4=1 Clever-side sharing rules and educator-only visibility; no per-tool control by the product.
- F5=1 one external service, Engageli, for live sessions; "independent developers' tools running inside K12 Tutoring or Beacon: none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## khanmigo
- F1=1 own content only: "Recommend Assignments Offers suggestions on what Khan Academy content your students should work on next"; "No page opened describes ... sequencing activities delivered by other vendors' tools."
- F2=0 it consumes Clever and ClassLink rostering and Clever LMS Connect; "No public Khan Academy developer API documentation, and no statement of LTI, OneRoster, Caliper, CLR or CASE support".
- F3=1 own mastery system: "Your skill level can move up or down based on your performance"; no outside writes and no mastery data sent out.
- F4=1 account permission levels by age and policy statements; "no page opened describes Khan Academy granting per-app permissions to other tools".
- F5=1 data-sync integrations only (Clever, ClassLink, LMS sync); "No page opened describes independent developers' tools running inside Khan Academy or Khanmigo."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## kiddom
- F1=1 own curriculum only: "Atlas ... makes recommended small-group or whole-class activities available. Teachers decide"; "Atlas is built for IM math classrooms".
- F2=2 "Kiddom is 1EdTech, OneRoster 1.1, and LTI 1.3 Certified" plus LTI app and Canvas passback documented.
- F3=1 own standards mastery: "standard mastery reports provide detailed insights on standard-specific performance"; assessment partners claimed, "no documentation of data writes found".
- F4=1 user roles and Clever-side sharing rules; "No per-app scope or consent screen for embedded third-party tools documented."
- F5=2 independent tools integrated inside: "17 math manipulatives powered by BrainingCamp", "Kiddom partners with ... GeoGebra for graphing", "these tools are integrated right into Kiddom"; Nearpod and PhET embeds.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## kiinara-os
- F1=0 "No page found describing how the system decides or sequences a learner's next activity"; AI recommendations are about students for staff.
- F2=1 claim of purchasable "custom integrations"; "None found: no developer docs, API reference or open standards".
- F3=1 marketing claim only: "builds a living understanding of every entity in your institution - every student"; "No mention of a mastery or skill model found".
- F4=1 role-limited access in privacy policy; "No page found describing per-app or per-tool permission scopes".
- F5=0 only unnamed service-provider categories ("payment, messaging and cloud providers"); "None found: no named independent tools".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## kira-learning
- F1=1 own platform only: "Student Dashboard ... tells every student exactly what to do next"; "identified skill gaps automatically trigger personalized practice"; no other vendors' activities.
- F2=2 documented LTI 1.3 Canvas setup with LTI Advantage services and grade passback.
- F3=1 own model: "Every student response updates a living mastery model"; "No documentation found of outside vendors' tools writing into Student Atlas."
- F4=1 admin enable/disable of Kira's own features and user roles; no per-tool permissions over student data for other tools (lower code).
- F5=0 "None found. Activity types documented are Kira's own".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## knomadix
- F1=1 marketing only: "Guided step-by-step tutoring by a virtual lesson bot"; "No documentation of how next activities are chosen".
- F2=0 "None found. No developer, API, integration or standards ... pages".
- F3=1 marketing only: "a clear picture of student progress and mastery of key concepts"; "No documentation of a learner/mastery data model".
- F4=1 website privacy text only, no per-tool control.
- F5=0 "None found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## learning-os
- F1=0 "None found"; the site sells printable resources, "no software that assigns or sequences learner activity".
- F2=0 "None found."
- F3=0 "None found."
- F4=0 "None found. No privacy page on the site".
- F5=0 "None found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## macmillan-learning
- F1=1 own adaptivity only: "LearningCurve, personalizes practice based on each student's performance"; "Sequencing of activities from other vendors' tools: none found".
- F2=2 documented LTI Advantage (LTI 1.3) Canvas admin guide and grade sync.
- F3=1 own grades and objective reporting: "Instructor-facing learning objective reporting" in select courses; "A documented persistent mastery or knowledge-state model ... none found" (own-tool objective data, lower of 1 vs 0 not needed).
- F4=1 privacy notice; LTI grants are set in Canvas; "Per-tool permissions over third-party tools inside Achieve ... none found".
- F5=1 one tool documented inside (Respondus LockDown Browser); "A second named independent tool documented as running inside Achieve ... none found" (iClicker availability only, ownership not stated).
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## magicschool
- F1=1 own tools only: "the quiz results dashboard surfaces a curated set of follow-up resources ... including relevant Student Rooms and Teacher Tools"; recommending "what's next" is a roadmap item.
- F2=1 Canvas/Schoology/ClassLink integrations documented but "No page found naming LTI, OneRoster ..."; no public API; the MCP connector carries teacher content only, not roster, launch, results or learner data (lower code).
- F3=0 engagement categories and on-demand activity summaries, quiz results; "Knowledge graph and learner profiles are listed as future items"; no persistent learner model documented.
- F4=1 org toggles for MagicSchool's own tools and the import-only connector; roster sharing set in Clever/ClassLink; unsure whether tool toggles count as per-tool data permissions, chose 1.
- F5=1 one third-party tool inside (Adobe Express image generator); Claude connector writes in from outside; "No marketplace or developer program".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## mastery-connect
- F1=0 curriculum maps and pathways are planned orders; "Automatic selection of a learner's next activity ... none found" (lower code).
- F2=2 public REST API v2 docs, LTI with Canvas, Ed-Fi v2.5.0 data connections.
- F3=1 standards mastery tracker computed by Mastery Connect ("Proficiency calculations ... decay rates"); only Instructure's own Canvas quizzes feed it; "Independent vendors' tools writing mastery or scores into Mastery Connect trackers: none found".
- F4=2 per-credential OAuth scopes over student data: "Each endpoint requires one scope. All scopes are read-only"; "Request the narrowest set".
- F5=2 two named outside tools run inside assessments: Desmos calculators ("assessments or items allow you to use a Desmos calculator") and Respondus LockDown Browser.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## mcgraw-hill
- F1=1 own products only: "ALEKS helps the student work on the topics they are ready to learn"; "Sequencing of other vendors' tools: none found".
- F2=2 documented LTI Advantage assignment sync and grade passback in Canvas, Schoology, Google Classroom; OneRoster, QTI 2.1 stated.
- F3=1 own knowledge-state model: ALEKS "develop and maintain a detailed map of each student's knowledge"; "Outside vendors' tools writing into a McGraw Hill learner model: none found".
- F4=1 third-party list and privacy notice; "per-tool permission controls: none found".
- F5=2 independent tools inside: "McGraw Hill partners with Proctorio to provide remote proctoring ... within Connect"; "ALEKS course product integrates Respondus browser-locking"; ROAR from Stanford "included in our core literacy programs".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## moodle
- F1=1 availability API restricts activities by date or grade within the course; "No page opened states whether external (LTI) tool activities can serve as the condition for, or the target of, availability restrictions."
- F2=2 web service framework, LTI Advantage consumer and provider, plugin developer docs.
- F3=1 core competency model with ratings and evidence ("Grade a competency"; "The activity ... was completed"), but "No page opened states whether completion of an external (LTI) tool activity, or a grade returned by such a tool, triggers these competency outcomes"; no documented outside vendors writing.
- F4=2 per-tool LTI sharing: "Specify whether the full name of the user launching the tool should be shared with the tool provider"; "accept grades" per tool instance.
- F5=2 plugins run inside the server: MathType, Cloud Poodll, BigBlueButton by Blindside Networks ("Certified Integration").
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## myopenmath
- F1=1 own assessments only: "Show based on another assessment: Use this to hide this assessment until a specific score is achieved on another assessment"; External Tool items not stated as gated.
- F2=2 documented LTI 1.1/1.3 with Canvas and Blackboard, "certified compliant with LTI 1.3", Common Cartridge export.
- F3=1 own gradebook and course outcomes report (source-code strings "View Outcomes Report"); "A mastery or knowledge-state model ... none found".
- F4=1 LMS-side settings and privacy policy; "Per-tool permissions over external tools that MyOpenMath itself launches ... none found".
- F5=1 it can be an "LTI 1.1 consumer, using the External Tool option", but "Named independent third-party tools documented as running inside MyOpenMath ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## nearpod
- F1=0 teacher-led or student-paced progression within a lesson; "No documentation found of Nearpod itself choosing or sequencing a learner's next activity".
- F2=2 "Nearpod is LTI ... Advantage certified" plus documented Canvas LTI 1.3 setup and deep linking.
- F3=0 per-session reports only: "capturing a time-stamped record of student participation and responses"; "No documentation found of a persistent per-student mastery or knowledge-state model".
- F4=1 privacy notice; listed Google scopes are those Nearpod requests; "No documented per-tool or per-app permission controls inside Nearpod".
- F5=2 independent tools embedded: PhET simulations "directly embedded in your Nearpod lesson" and "our new Desmos integration ... embed a Desmos graph into their lesson".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## newsela
- F1=1 own texts only: "continuously calculates customized article levels for each student and ... Presents students with articles at that level"; "no documentation found of Newsela sequencing activities from other vendors' tools".
- F2=2 documented Canvas LTI integration, OneRoster and ClassLink rostering ("LMS integration through LTI is reserved for subscribed districts").
- F3=1 own reading-level model; NWEA MAP Growth scores are imported by district sync to set initial levels ("sync NWEA MAP Growth data to help us recommend initial article levels"), but no independent vendor's tool writes to the model and the level is "a recommended level per article"; unsure between 1 and 2, chose 1.
- F4=1 Google trust is set by the admin in Google; "No per-tool permission controls inside Newsela found."
- F5=2 independent tools embedded: PhET ("The simulation will be embedded on the Newsela page") and "Tuva interactive datasets".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## noredink
- F1=1 own content only: "NoRedInk will show students a recommended mastered topic for which they can complete a Mastery Review"; "none found across other vendors' tools".
- F2=2 documented Canvas LTI setup ("NoRedInk LTI", "By Client ID") with grade passback to Canvas, Schoology, Google Classroom.
- F3=1 own mastery model: "students progress through proficiency levels: Starting Off, Level 1, Level 2, Level 3, and Mastery"; "No documentation found of other vendors' tools writing mastery".
- F4=1 Google trust set by admins in Google, user-level disconnect, privacy policy; no per-tool control by NoRedInk.
- F5=1 integrations only, NoRedInk "runs inside those systems rather than hosting other vendors' tools".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## odoo-schoolos
- F1=1 own modules only, listing copy: "LMS gamification, peer review, plagiarism scanning, learning paths"; "None found of sequencing across other vendors' tools."
- F2=1 proprietary REST API Gateway with endpoints listed on the store page ("/api/v1/students"), no open standard documented beyond a SCORM/xAPI playback claim, no outside developers shown.
- F3=1 own outcome-based grading: "A progress view and learning-outcomes page show how the student is performing against curriculum targets"; API is GET only, no outside writes.
- F4=1 store listing claims "narrowly-scoped API keys (read students, attendance, fees or academics" and role registry; this is listing copy, not developer documentation, so lower code.
- F5=1 meeting connectors (Zoom, Teams, Meet, BigBlueButton) are "connectors, not tools hosted inside the suite".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## os-for-schools
- F1=0 "No sequencing of learner activities found"; only at-risk lists.
- F2=0 spreadsheet import and an integrations screen for payment services; "No public API documentation or open standard found".
- F3=0 marks and report cards only ("report card makes itself from their marks and the register"); "No mastery, skill or knowledge-state model found."
- F4=1 role-based access and privacy policy statements of what each service provider receives; no per-tool controls.
- F5=1 named service providers Arkesel and Paystack connected; "No third-party learning tools running inside the product found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## pear-assessment
- F1=1 vendor's own products only: "Generate a lesson (Pear Deck), practice set (Pear Practice), assessment (Pear Assessment)"; "No documentation found of sequencing activities delivered by other vendors' tools."
- F2=2 documented Canvas and Schoology LTI tool setup with grade sync; OneRoster via ClassLink.
- F3=1 own mastery model ("Decaying Average", "Power law ... estimate the student's current level of mastery"); outside data (NWEA MAP, iReady) is CSV-uploaded by districts to "display external data alongside Pear Assessment results", not written into the mastery model by those vendors' tools.
- F4=1 Google-side trust and in-product role permission; no per-tool data permissions.
- F5=1 one integration (Google Meet) and generic multimedia embeds; calculator provider unnamed; "No app marketplace or plugin API".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## savvas-realize
- F1=1 only Savvas resources are sequenced or recommended: Star Math (Renaissance) data yields "a list of recommended enVision resources on Savvas Realize"; teacher-built scope and sequence and playlists; no activities from another vendor's tool are sequenced.
- F2=2 "Savvas Realize is 1EdTech certified" plus documented LTI 1.3 Advantage with Canvas, Schoology, Brightspace.
- F3=1 own standards mastery: "Check standards mastery data for auto-scored assessments"; Star Math scores are displayed ("view key Star Math assessment data"), not documented as written into a mastery model (lower code).
- F4=1 privacy policy only; "No per-tool or per-app permission or scope documentation found".
- F5=1 one third-party tool documented within (Google Docs); Rubicon is publisher content hosted on Realize; other integrations are connections; "No app marketplace".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoology
- F1=1 completion rules sequence course materials ("Requirements must be completed in sequential order"), but "No page opened states which completion-rule types apply to external tool materials" and Schoology "cannot automatically detect submissions from these tools"; not documented across independent tools.
- F2=2 public REST API, app platform, LTI 1.3 Advantage developer docs.
- F3=1 district mastery gradebook: external tools can be aligned to objectives, but teachers "enter a score for each aligned district objective"; "No page opened describes an external tool writing per-objective mastery scores".
- F4=2 per-tool privacy: "Privacy The information sent to the publisher upon the tool's launch"; apps restricted to course admins.
- F5=2 App Center: "software developed by other companies directly within Schoology" (Google Drive Assignments, Microsoft Teams), Formative assignments inside Schoology.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoolos-ai
- F1=0 engagement scores for admissions only; "No sequencing of learner activities found."
- F2=1 claim only: "API access for everything"; "No developer documentation and no open standard found."
- F3=0 gradebook "Weighted average" only; "No mastery, skill or knowledge-state model found."
- F4=1 user roles and privacy policy ("11 configurable user roles"); no per-tool control.
- F5=0 "None found. The home page shows a "Platform Integrations" count but names no integrations".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoolos-live
- F1=0 "None found."
- F2=0 "None found. No API, developer page or standard".
- F3=0 own grading and report cards only ("Automated grading, custom report card generation"); "No mastery, skill or knowledge-state model found."
- F4=1 marketing claim of "Role-based access for Admins, Teachers, and Parents"; no privacy policy, no per-tool control.
- F5=0 "None found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoolos-net
- F1=0 "Smart Promotion System" is administrative; "No sequencing of learner activities found."
- F2=0 "None found. No API, developer page or open standard".
- F3=0 CA and exam results only; "No mastery, skill or knowledge-state model found."
- F4=1 privacy policy and user roles; no per-tool control.
- F5=0 only resellers and generic subprocessors; "No named third-party tools running inside the product found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoolos-systems
- F1=0 built-in LMS with "progress tracking"; "No documentation of sequencing learner activities found."
- F2=1 claims "Secure API Routes" and "Custom integrations"; "API Reference" link points to "#"; no standard named.
- F3=0 "progress tracking" and at-risk analytics only; "No mastery, skill or knowledge-state model found".
- F4=1 marketing claims "RBAC + ABAC Hybrid" and "granular access controls"; no per-tool control, no privacy policy reachable.
- F5=0 "Full LMS Built In ... no third-party needed"; "No named third-party tools running inside the product found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## schoolware
- F1=0 "None found"; timetables and roadmap AI homework checking only.
- F2=1 vendor claim "SchoolWare speaks MCP" and an API mention, but "No public developer documentation for the MCP endpoint or the API found"; spreadsheet import.
- F3=0 records, grades and report cards only; "No mastery, skill or knowledge-state model found."
- F4=1 role and module permissions; the AI connector "inherits their role and permissions" and the school can revoke it; no per-tool scopes over student data documented (lower code).
- F5=1 outside AI assistants connect via MCP and payment providers (Stripe) are listed; "No marketplace or third-party apps running inside the product found."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## scoolio
- F1=0 teacher arranges course order ("Arrange the curriculum into a sequence learners can follow"); "No page found describing the system choosing a learner's next activity" (lower code).
- F2=0 "Do not assume that a generic third-party connector or a public developer API is supported"; CSV exports only; no standards.
- F3=0 marks, gradebook and report cards only; "No mention of a mastery, skill or knowledge-state model found."
- F4=1 user roles only; "no page found describing per-app or per-tool scopes".
- F5=1 meeting-link providers (Google Meet, Zoom, Teams, Jitsi) and WhatsApp/SMTP modules listed; "No app directory or marketplace found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## shoofly-ai
- F1=0 admissions and back-office agents; "None found of sequencing what a learner does next."
- F2=1 claim only: "Everything runs on top of Ellucian, Skyward, PowerSchool"; "None found (no API, developer docs or standards)".
- F3=0 "None found."
- F4=1 policy-level statements: "role-based access and data-handling controls"; no per-tool control.
- F5=0 "None found of independent tools running on it"; partners are resellers.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## skodle
- F1=0 AI tutors adjust "difficulty, examples, and pacing" within a tutor session (single activity); insights go to teachers; "No page found describing sequencing across other vendors' tools" (lower code).
- F2=1 integration framework without pre-built connectors: "skodle does not come with pre-built connectors"; "no public API or developer docs"; OIDC sign-in only.
- F3=1 own persistent progression record: "ATL progression Per-student Introduced → Demonstrated, tracked with evidence"; "stored as a record a student carries between years"; no outside writes.
- F4=1 page lists "Connection, configuration, permissions and disconnect per integration" but no integration exists out of the box and no scope detail is documented; unsure between 1 and 2, chose 1.
- F5=1 "Available means catalogued, not running."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## spyral-aios
- F1=1 own labs only: "personalised learning paths", "AI Challenge Engine with adaptive difficulty"; "no page found describing sequencing of other vendors' tools".
- F2=1 public REST API reference for its own proprietary API ("Base URL: https://tryspyral.com/api/v1"), no open standard and no outside developers shown using it.
- F3=1 own competency model: SPI "per-competency mastery breakdown"; the API computes from caller-submitted responses but "does not state whether these results are stored" in AiOS; no documented outside writes to a persistent record.
- F4=1 user roles and API key enablement; "No page found describing per-app or per-tool scopes over student data".
- F5=1 Google Classroom import and service providers; embeds go outward; "No page found naming independent developers' tools that run inside AiOS."
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## string-os
- F1=1 marketing copy only (cap 1): "Students move through their textbook's units in challenges that adapt to their level"; agent example "Picked a fractions video Built a quiz from the video Posted the lesson" is a teacher-requested workflow on a marketing page, no product documentation.
- F2=1 APIs described only on the startups marketing page ("Six APIs to build your product on"); "Explore the APIs" is an on-page anchor; "No developer documentation site, API reference" found; no open standard named.
- F3=1 marketing copy only: "A skill map that tracks mastery of each concept"; outside products write "results to the unified gradebook" (grades) per marketing page; no documentation, so capped at 1.
- F4=1 marketing statement "the String DNA API reaches students' profiles only with their school's consent" and role-based access; no documented per-app scopes.
- F5=1 apps "String connects to" (Kahoot!, Khan Academy, Scratch) and an "App Store" are marketing claims; String's assistant runs inside other apps, not the reverse; marketing caps at 1.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## tci
- F1=0 teacher-paced slideshows and teacher-assigned levels; AI remediation is "developing"; "AI-generated content is only available to students when assigned by a teacher" (no system sequencing).
- F2=2 LTI 1.3 Canvas integration, OneRoster API v1.1, QTI, "1EdTech CERTIFIED" logo.
- F3=1 own standards report: "turning scores into a clear picture of standards mastery"; records reset each summer; "Outside vendors' tools writing into TCI's standards or mastery data: none found".
- F4=1 district/teacher feature opt-in for AI content and privacy policy; "Per-app or OAuth scope lists ... none found".
- F5=1 partner logos for rostering and LMS (Clever, Aeries, Teams) and Google Drive save; "Independent developers' tools running inside TCI ... none found".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## theschoolos
- F1=0 routes support tickets and operational workflows; "None found regarding sequencing of what a learner does next."
- F2=1 vendor integration page states it consumes "OneRoster 1.1 and 1.2" from district systems; no developer docs or API of its own and no certification (standard claimed, not certified).
- F3=0 "None found"; agents "never touch Academic records".
- F4=1 per-connection scopes cover what schoolOS itself requests from district systems ("Write access is enabled per connection"), not control over other tools' access to a child's data in schoolOS; unsure, chose 1.
- F5=1 data sync and write-back to outside systems (Jamf, MySchoolBucks); "None found of independent developers' tools running inside schoolOS".
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## timeback
- F1=2 documented cross-vendor sequencing in the PowerPath API: course sequence stages "course - assessment - hole-filling" with "The id of the learning app that should be used for the hole-filling course. examples: - alpha_write - mobymax" and "'literably' selects the PK-2 Reading screener stage"; "the platform can route them to remediation (from your app or another)". Two named non-Alpha apps (MobyMax, Literably) are sequenced.
- F2=2 public OpenAPI docs for OneRoster, Caliper, QTI, CASE, CLR, Open Badges with a third-party integration path ("Level 1 ... add event tracking and rostering to your existing app").
- F3=1 (lower of 1 and 2): Timeback keeps a mastery state ("updates mastery state"; "Mastery ... Tracked by PowerPath") and the SDK lets third-party apps send "Core learning events (XP, mastery)", but the only named outside source is "edulastic" among "data sources (currently edulastic, placement and test out datasets)"; documentation does not show two named independent vendors' tools writing mastery, and the vendor cautions "A shared data model ... does not automatically make two apps' ... mastery policies interchangeable".
- F4=2 per-client OAuth scopes over student data: "roster-core.readonly", "roster-demographics.readonly", "gradebook.createput", "events.write" (no school-facing consent page found).
- F5=2 third-party learning apps run on the platform ("learning apps (both first-party and third-party)", launched "through the Timeback Desktop App"), named MobyMax and Literably. SUFF=0 because F3 is below 2 and no documentation shows two independent vendors' tools writing to the PowerPath mastery model the scheduler acts on (Level 1 apps "keep your own ... no PowerPath").

## vista-higher-learning
- F1=1 own content and marketing: "Create a personalized learning path ... point you to the right resources"; teacher individualized assigning; Wayground "intelligent pathways" is a partner claim.
- F2=2 "LTI Advantage 1.3 ... certified by 1EdTech" with LMS guides, Thin Common Cartridge, OneRoster CSV.
- F3=1 marketing claim of "standards-based progress monitoring and proficiency assessments"; help center search for "mastery" returned 0; gradebook and progress only; no outside writes.
- F4=1 privacy policy and instructor AI control; "Per-tool or per-app permission or scope documentation: none found."
- F5=1 AI partners "does not state whether these run inside vhl central"; TokBox and Pubnub are infrastructure; Clever integration; no marketplace.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## wayground
- F1=1 own content only: "VoyageMath uses an adaptive algorithm ... to personalize learning paths"; "No documentation found of sequencing activities from other vendors' tools."
- F2=2 documented LTI integrations with Canvas (Dynamic Registration), Schoology, Blackboard, Moodle, Brightspace with grade sync.
- F3=1 own standards mastery: "Standards Mastery Report ... Decaying Average"; "Outside vendors' tools writing mastery or results into Wayground: none found."
- F4=1 scopes listed are those Wayground requests from Google; "no documentation found of Wayground granting per-app scopes to other tools".
- F5=2 independent tools inside: "PhET Interactive Simulations are now integrated with Wayground" (students interact with them inside questions) and "LockDown Browser by Respondus" for Common Assessments.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

## writable
- F1=1 own activities only: "Based on students' proficiency in skills, teachers can find and assign activities"; "recommended assignments will not include HMH-based content".
- F2=2 documented Canvas LTI and API key setup ("JSON URL: https://app.writable.com/canvas-ltia"), Schoology "LTI and API connections", grade sync.
- F3=1 own proficiency model: "track skill mastery over time"; Canvas grades flow back as scores; "No documentation found of other vendors' tools writing skill or mastery data into Writable."
- F4=1 Writable's own Google scope list and district AI toggles; no per-tool control over other tools.
- F5=2 independent tools inside: "Originality Check (powered by Turnitin SimCheck)" and "embedded Google Docs" in assignments.
- SUFF=0: sufficiency rule not met (not all five functions coded 2).

