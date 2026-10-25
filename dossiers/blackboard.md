# Dossier: Blackboard LMS (Anthology)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: docs.anthology.com redirects to the developer site https://docs.blackboard.com; help.blackboard.com redirects to https://help.anthology.com/blackboard/. The help pages carry long navigation menus; quotes are from article bodies.

## Identity
- "Built with educators and refined through millions of teaching interactions, Blackboard LMS puts AI, accessibility, and personalized learning at every institution's core." (https://www.blackboard.com/solutions/lms, accessed 2026-10-24; reached by redirect from https://www.anthology.com/products/teaching-and-learning/learning-effectiveness/blackboard)
- "Blackboard LMS integrations are similar to plugins or add-ons in other software platforms, and are designed to extend the core functionality of the Blackboard LMS platform to meet the specific needs of individual institutions." (https://docs.blackboard.com/docs/blackboard/rest-apis/learn-intro, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- "Select Activity to release an item or folder when a student completes a certain activity in your course such as opening a document or submitting an assignment. To define the activity required, choose the item and requirement." (https://help.anthology.com/blackboard/instructor/en/course-and-content-management/content-release-conditions.html, accessed 2026-10-24)
- "Example: Students must prove mastery of the Chapter 1 material before accessing the Chapter 2 module. They can prove mastery by scoring 90 points or higher on either a Chapter 1 writing assignment or a Chapter 1 test." (same URL, accessed 2026-10-24)
- "Learning modules let students navigate from one content item to the next without distractions or extra clicks. You can set a forced sequence to a module to make sure students know which content to access and in what order." (same URL, accessed 2026-10-24)
- No page opened states whether external (LTI) tool items or their returned grades can serve as release conditions.

## E2 Interfaces evidence
- "Starting with Java™ Building Blocks, SOAP Web Services, Learning Tools Interoperability (LTI), and adding RESTful APIs in 2016." and "REST APIs can be used to manage the Blackboard LMS Gradebook, including creating and editing grade columns, submitting and retrieving grades, and exporting grade data." (https://docs.blackboard.com/docs/blackboard/rest-apis/learn-intro, accessed 2026-10-24)
- "LTI 1.1 has been deprecated for over 10 years by 1EdTech and Blackboard LMS will no longer support it, hence, Blackboard LMS will only support LTI 1.3 Applications." (https://docs.blackboard.com/docs/blackboard/lti/welcome, accessed 2026-10-24)
- "The Assignments and Grades Service (AGS for short) is the gateway created by 1EdTech for LTI Advantage to interact with grades and grade column information. This service has additional functions within it that allows your tool to create columns, create attempts, grade user data or pull the existing grades from Blackboard LMS." (https://docs.blackboard.com/docs/blackboard/lti/1.3/lti-subsystems/ags/ags-start, accessed 2026-10-24)
- Developer documentation also covers Caliper events ("Caliper events guide", "grade events", "LTI events" in https://docs.blackboard.com/sitemap.xml; https://docs.blackboard.com/docs/blackboard/caliper/getting-started opened 2026-10-24, not quoted).
- Help navigation lists "QTI Packages" and "SCORM Packages" (https://help.anthology.com/blackboard/instructor/en/analytics/goals.html, accessed 2026-10-24).
- Vendor states: "Learn has been certified to meet the LTI standards." (https://docs.blackboard.com/docs/blackboard/rest-apis/getting-started/lti-or-rest, accessed 2026-10-24). Not checked against the 1EdTech directory.

## E3 Learner model evidence
- "In the Ultra Course View, you can align goals to multiple items in your course: Assignments Tests, including individual questions Discussions Rubrics Files Web links Teaching tools with LTI connection Documents Question banks Question pools Journals" (https://help.anthology.com/blackboard/instructor/en/analytics/goals.html, accessed 2026-10-24)
- "Your institution imports or creates goals and you can align them to your course content. Instructors can't create goals, but you can find and add goals that are available in the system." (same URL, accessed 2026-10-24)
- "Blackboard Outcomes extends Blackboard by integrating learning outcome measurement capabilities directly in to LMS workflows." and "In the gradebook, select the Mastery icon to open the overall mastery view. This view shows student mastery levels across outcomes, assignments, and competencies aligned to the course." (https://help.anthology.com/blackboard/instructor/en/analytics/blackboard-outcomes.html, accessed 2026-10-24)
- "Note Blackboard Outcomes must be provisioned for the institution." (same URL, accessed 2026-10-24)
- "Mastery for Outcomes is calculated using a dynamic, flexible approach that reflects student performance across multiple assessments aligned to a specific learning outcome." and "A weighted median is used to calculate each student's mastery level. Here's how it works: Student results are aggregated across all assessments aligned to a particular outcome. Each assessment is weighted proportionally based on its maximum score." (https://help.anthology.com/blackboard/instructor/en/analytics/blackboard-outcomes/performance-results-scale-and-key-assessments/how-mastery-is-calculated.html, accessed 2026-10-24)
- AGS scope of tool writes: "This service will not give you the information of all the grades and columns created in the course but rather, it will give you the access and data of the columns created by the LTI tool itself" (https://docs.blackboard.com/docs/blackboard/lti/1.3/lti-subsystems/ags/ags-start, accessed 2026-10-24)
- No page opened states whether a score returned by an LTI tool aligned to a goal is counted in the Outcomes mastery calculation.

## E4 Data protection evidence
- "You may be asked to authorize the provider's access to certain user information, such as your name and email address. Note Your institution may choose to automatically share your user information with content providers." (https://help.anthology.com/blackboard/instructor/en/course-and-content-management/add-content/add-content-from-external-sources.html, accessed 2026-10-24)
- "A Learn administrator can set up your tool in Learn, following documentation that you provide." (https://docs.blackboard.com/docs/blackboard/rest-apis/getting-started/lti-or-rest, accessed 2026-10-24)
- "a Learn admin should never be told to associate a user with Learn admin privileges with any REST API integration" and "3LO guarantees that the user using your REST Application can only do what they can do via the Learn UX when they are logged into Learn." (https://docs.blackboard.com/blog/2021/01/06/2021/How%20to%20Create%20a%20User%20With%20Limited%20Entitlements%20For%20REST%20API%20Calls, dated January 6, 2021, accessed 2026-10-24)
- "SOC 2, FERPA, GDPR, ISO 27001/27017/27018, FedRAMP Class C, and WCAG 2.2 AA: all maintained by Blackboard, all audited externally, all in a single Trust Center." (https://www.blackboard.com/solutions/lms, accessed 2026-10-24)

## E5 Third-party tools evidence
- "The App Catalog enables anyone to browse, search, or filter the Apps by integration type (LTI + REST, Building Block, Partner Cloud) or Category (Accessibility, Admin/Support Tool, Assessment, Classroom Tool, Consulting/Dev Services, Content, Data Insights, Multimedia, Safety/Security, SIS/System Integrator)." (https://docs.blackboard.com/docs/partners/blackboard-app-catalog-faq, accessed 2026-10-24)
- "Submitted Apps are reviewed by the Blackboard App Catalog team and appear in the App Catalog upon approval." (same URL, accessed 2026-10-24)
- "The Content Market is your gateway to access valuable learning materials from content providers." (https://help.anthology.com/blackboard/instructor/en/course-and-content-management/add-content/add-content-from-external-sources.html, accessed 2026-10-24); the help section "Add Content from External Sources" has pages for "Blended Schools Network", "Cengage", "Kaltura", "McGraw-Hill Education", "Macmillan Learning" and "Mediasite" (navigation on the same page).
- "You can use Kaltura integrations to present rich media content in your courses." and "The list of suggested tools contains the authorized tools for your institution, such as Kaltura." (https://help.anthology.com/blackboard/instructor/en/course-and-content-management/add-content/add-content-from-external-sources/kaltura.html, accessed 2026-10-24)
- Help navigation also lists "Turnitin" under Plagiarism Tools and "Badgr Badges" (https://help.anthology.com/blackboard/instructor/en/analytics/goals.html, accessed 2026-10-24).

## Gaps
- https://docs.anthology.com/docs/blackboard/rest-apis/hands-on/ returned 404.
- https://help.blackboard.com/Learn/Instructor/Ultra/Performance/Goals_and_Standards redirected to an analytics index page; the relocated goals page was used.
- The Blackboard App Catalog listing itself was not opened; no app list was read.
- Administrator documentation for LTI tool registration (user-field sharing settings per tool) and REST integration entitlements was not opened.
