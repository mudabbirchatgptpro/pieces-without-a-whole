# Dossier: Brightspace (D2L)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: the developer reference at docs.valence.desire2learn.com is labeled "Developer Platform (October 2026)". community.d2l.com knowledge-base articles render client-side and were read in a browser.

## Identity
- "D2L Brightspace is the LMS built to focus on the learning moment, bringing artificial intelligence, learning science, and human ingenuity together to improve learner achievement." (https://www.d2l.com/brightspace/, accessed 2026-10-24)
- "Leverage Brightspace's open standards, APIs and Integration Hub to deliver solutions in the flow of learning" (https://www.d2l.com/partners/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- "Release conditions provide the ability to dynamically release resources to users that have satisfied one or more conditions. Several types of resources can be the target of release conditions, including content, discussions and quizzes. Brightspace offers a broad range of conditions over its suite of tools, ranging from activity completion, such as posting to discussions and submitting assignments, to receiving evaluations in the form of grades and quizzes." (https://docs.valence.desire2learn.com/res/releaseconditions.html, accessed 2026-10-24)
- Condition types listed include "Content CompletesContentTopic Completed content topic", "Grades ReceivesScoreOnGradeItem Grade value on a grade item", "Quizzes ReceivesScoreOnQuiz Score on a quiz", "Awards EarnsAward Award Earned", "Checklist CompletesChecklist Completed checklist" (same URL, accessed 2026-10-24)
- "Create personalized educational experiences that adapt to each learner's performance." (https://www.d2l.com/brightspace/, accessed 2026-10-24)
- The Valence reference also documents Intelligent Agents (https://docs.valence.desire2learn.com/res/intelligentagents.html, opened 2026-10-24; not quoted). No page opened states whether a grade written by an external LTI tool can serve as a release condition.

## E2 Interfaces evidence
- OAuth 2: "Note that, as part of the registration process you must also declare the OAuth 2 scopes that your application will use to identify the particular API actions it will later want access to." (https://docs.valence.desire2learn.com/basic/oauth2.html, accessed 2026-10-24)
- LTI Advantage extension types: "AssignmentAndGradeServices 1 DeepLinking 2^ NamesAndRoleProvisioningServices 3 ActivityItemProfile 4 SubmissionReview 5 PlatformNotificationService 6 AssetProcessor 7" (https://docs.valence.desire2learn.com/res/ltiadvantage.html, accessed 2026-10-24)
- LTI management routes carry OAuth 2 scopes, e.g. "Oauth2 Scopes : ltiadvantage:registrations:delete" (same URL, accessed 2026-10-24)
- Outcomes source standard: "SourceType The source where this outcome was defined. Currently supported values are asn for outcomes defined in the Achievement Standards Network and lores for outcomes authored within Brightspace." (https://docs.valence.desire2learn.com/res/outcomes.html, accessed 2026-10-24)
- "With Brightspace's unique Javascript SDK, comprehensive APIs, standards-based integrations and the Integration Hub, connecting your solutions has never been easier." (https://www.d2l.com/partners/, accessed 2026-10-24)
- Installation workflow: "This consolidated experience brings LTI 1.3 registration, deployment, and link management into a single view" and "Dynamic Registration: Automate the exchange of security keys and URLs between Brightspace and the tool provider." (https://community.d2l.com/brightspace/kb/articles/23805-about-brightspace-integrationhub, accessed 2026-10-24)
- Certification: not checked (1EdTech directory not queried). "D2L is a recognized leader in learning innovation and integration standards." (https://www.d2l.com/partners/, accessed 2026-10-24)

## E3 Learner model evidence
- Activity types that outcomes can be aligned to: "We categorize the types of activities, and use the term ALIGNEDACTIVITYTYPE_T to stand in for an appropriate string name. Activity Types ContentObject DiscussionTopic Assignment LtiLink Quiz Survey Checklist SelfAssessment QuizQuestion RubricCriterion" (https://docs.valence.desire2learn.com/res/outcomes.html, accessed 2026-10-24)
- Alignment routes: "GET /d2l/api/le/ ( version ) / ( orgUnitId ) /lo/alignments/activity/ ( activityType ) / ( objectId ) Retrieve all the alignments to a given activity." and "POST /d2l/api/le/ ( version ) / ( orgUnitId ) /lo/alignments/activity/ ( activityType ) / ( objectId ) Modify the alignments to a given activity." (same URL, accessed 2026-10-24)
- The routes documented on the Learning Outcomes page cover outcome sets, bulk import/export, alignments and outcome scales; no route for writing a learner's outcome evaluation or achievement level was found on that page. (same URL, accessed 2026-10-24)
- "Achievement thresholds are only available to clients who have purchased the Achievement Plus add-on." (same URL, accessed 2026-10-24)
- "These actions and structures provide access to the structure in a course offering containing its learning competencies and learning objectives." and "GET /d2l/api/le/ ( version ) / ( orgUnitId ) /competencies/structure Retrieve the structure of course competencies and objectives as visible to the calling user." (https://docs.valence.desire2learn.com/res/competency.html, accessed 2026-10-24)
- "The Mastery View provides visibility into additional details of learner performance beyond what is available through the traditional grade associated with an activity." and "By using outcomes associated with various elements of the assessment, such as quiz questions or rubric criterion rows, it is possible to investigate additional dimensions of performance." (https://community.d2l.com/brightspace/kb/articles/34131-best-practices-for-using-grade-book-mastery-view, accessed 2026-10-24)
- "nothing displays in the mastery view until at least one outcome has been aligned to an assessment activity (either directly or indirectly via a rubric)." (same URL, accessed 2026-10-24)
- No page opened describes an external tool writing outcome achievement levels into Brightspace through LTI or the API.

## E4 Data protection evidence
- "Our API actions that have specific scopes assigned to them will have a scope of this form: <resource-group>:<resource>:<action> For example, the action to retrieve the details for a user has the associated specific scope users:userdata:read." (https://docs.valence.desire2learn.com/basic/oauth2.html, accessed 2026-10-24)
- "The scope value you provide must be a subset of the scopes you provided when you registered your application within Brightspace" and "Note that you will only be able to use your access token for API actions that correspond to the various scopes you have been granted for use with your token." (same URL, accessed 2026-10-24)
- "Data Access Transparency: Review a summary of exactly what information (such as user names or classlists) the app will access before finalizing the installation." (https://community.d2l.com/brightspace/kb/articles/23805-about-brightspace-integrationhub, accessed 2026-10-24)
- "administrators with the Create and Manage Brightspace Apps and Manage LTI Tools permissions can install and configure the tool using a unified workflow." (same URL, accessed 2026-10-24)

## E5 Third-party tools evidence
- "Brightspace IntegrationHub is an integrated app catalog that enables users to easily discover partner solutions. For example, Panopto enables you to record, upload, and share video directly from within IntegrationHub. Similarly, Zoom helps your organization connect internally and externally with flawless video communications, chat, and webinars." (https://community.d2l.com/brightspace/kb/articles/23805-about-brightspace-integrationhub, accessed 2026-10-24)
- The integrations documentation navigation on that page lists third-party integrations including "Turnitin", "Kaltura", "Copyleaks", "Credly", "FeedbackFruits", "Respondus LockDown Browser", "ReadSpeaker", "Class Technologies" and "Virtual Classroom and Video Assignments by Bongo" (same URL, accessed 2026-10-24)
- "D2L's Integration Partner programs are for ed-tech developers and companies that want to unlock new business opportunities by adding their app or point-solution to Brightspace's open learning ecosystem." (https://www.d2l.com/partners/, accessed 2026-10-24)
- "D2L has been one of Class's earliest and most impactful partners" (partner quote attributed to "VP of Partnerships & Business Development, Class", https://www.d2l.com/partners/, accessed 2026-10-24)

## Gaps
- https://integrationhub.brightspace.com/ and https://integrationhub.brightspace.com/partners/Adobe served an empty shell (8 characters) to a direct request and were not read in a browser.
- https://community.d2l.com/brightspace/kb/articles/1148-partner-solutions-and-unofficial-integrations returned only a title to a direct request; not read.
- https://www.d2l.com/brightspace/competency-based-education/ returned 404.
- The Valence routing and scopes tables were not opened in full.
