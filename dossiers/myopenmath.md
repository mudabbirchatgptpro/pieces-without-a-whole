# Dossier: MyOpenMath (MyOpenMath, non-profit; IMathAS software)
Frame stratum: 5.4   Evidence collected: 2026-10-24   Collector: stratum-5.4 agent D
Frame source: Instructure, The Edtech Top 40: K-12 Edtech Engagement During the 2025-26 School Year, entry 'MyOpenMath' (list is alphabetical, unranked)

## Identity
- "MyOpenMath is an online course management and assessment system for mathematics and other quantitative fields." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
- "MyOpenMath.com provides managed hosting of the open source IMathAS online assessment software." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
- "MyOpenMath.com is operated by the non-profit organization MyOpenMath." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
- "And it can do so much more, providing a full course management system, including file posting, discussion forums, and a full gradebook, all designed with mathematics in mind." (https://www.myopenmath.com/info/classroom.php, accessed 2026-10-24)
- "IMathAS is an Internet Mathematics Assessment System." (http://www.imathas.com/, accessed 2026-10-24)
- "It is distributed under the GPL." (http://www.imathas.com/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages listed in this dossier.

## E1 Sequencing / scheduling evidence
- "Show based on another assessment: Use this to hide this assessment until a specific score is achieved on another assessment." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Minimum Score for Credit: A minimum score which must be achieved to receive credit for the assessment." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Students can receive immediate feedback on algorithmically generated questions with numerical or algebraic expression answers." (https://www.myopenmath.com/info/classroom.php, accessed 2026-10-24)
- "If in practice test or homework mode, when students request a similar problem, different students will receive different versions of the questions." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
Adaptive sequencing or recommendations, or sequencing of other vendors' tools: none found on the pages listed in this dossier.

## E2 Interfaces evidence
LTI (vendor-stated certification):
- "MyOpenMath uses the industry-standard Learning Tools Interoperability (LTI) standard to integrate with Learning Management Systems (LMSs)." (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- "MyOpenMath supports LTI 1.1, using college-wide or course-level configurations, and LTI 1.3 using college-wide configuration." (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- Vendor states: "MyOpenMath is certified compliant with LTI 1.3, and is TrustEd Apps certified." (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- Canvas: "Select LTI Version 1.3, Install Method Dynamic Registration, and for Dynamic Registration URL enter: https://www.myopenmath.com/lti/dynreg.php" (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- Blackboard: "set Allow grade service access and Allow Membership Service Access to Yes." (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
Grade passback, deep linking, Common Cartridge:
- "If configured, grades will be sent from IMathAS to the LMS immediately every time the student completes a question, but the LMS may delay updating the grade." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Note that LTI 1.3 does not support a "whole course link" option, since that option does not allow grade passback." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Alternatively, you can setup individual links to assignments, using your LMS's "deep linking" feature." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "go to Course Items -> Export, select the items you want to export, your LMS, and Download the CC Export." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
Source code:
- "The most recent code can be obtained from GitHub" (http://www.imathas.com/, accessed 2026-10-24)
- Repository: https://github.com/drlippman/IMathAS (opened 2026-10-24; directory listing includes "bltilaunch.php" and "ltihome.php")
OneRoster, Caliper, QTI, or a documented REST API for outside developers: none found on the pages listed in this dossier.

## E3 Learner model evidence
- "Gradebook Category: If you have created gradebook categories, you can assign the assessment to one of those categories." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Show question categories?: If you plan to categorize questions and would like the categories displayed while the student is taking the test" (https://www.myopenmath.com/help.html, accessed 2026-10-24)
Outcomes feature (interface strings in IMathAS source code, not in the help documentation):
- "Course Outcomes" (https://raw.githubusercontent.com/drlippman/IMathAS/master/course/addoutcomes.php, accessed 2026-10-24)
- "View Outcomes Report" (https://raw.githubusercontent.com/drlippman/IMathAS/master/course/addoutcomes.php, accessed 2026-10-24)
- "No outcomes are defined in this course." (https://raw.githubusercontent.com/drlippman/IMathAS/master/course/outcomereport.php, accessed 2026-10-24)
A mastery or knowledge-state model, or other vendors' tools writing into MyOpenMath records: none found on the pages listed in this dossier.

## E4 Data protection evidence
LMS-side data sharing settings during LTI setup:
- "Confirm the Permissions and Data Sharing options (the default selections are recommended)" (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- "Also ensure User Fields to Send includes Name and Role in Course" (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- "Edit the MyOpenMath tool, and under Privacy set the "Accept grades from the tool" setting to Always" (https://www.myopenmath.com/info/lti.php, accessed 2026-10-24)
- "If the last digit of your LTI key is 1, then a student account will automatically be created the first time a student accesses the LTI placement, and that account will be linked with the host LMS account." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
Privacy policy:
- "For example, if you login to your MyOpenMath account through an Learning Tools Interoperability ("LTI") connection from a School's Learning Management System, we may collect the Personal Data that third party service shares." (https://www.myopenmath.com/info/policies/privacy.php, accessed 2026-10-24)
- "We do not use any third-party cookies, and do not use cookies for advertising." (https://www.myopenmath.com/info/policies/privacy.php, accessed 2026-10-24)
- "MyOpenMath will never use Student Data to engage in targeted advertising" (https://www.myopenmath.com/info/policies/privacy.php, accessed 2026-10-24)
Per-tool permissions over external tools that MyOpenMath itself launches (see E5): none found on the pages listed in this dossier.

## E5 Third-party tools evidence
- "IMathAS can also be an LTI 1.1 consumer, using the External Tool option for Link items." (https://www.myopenmath.com/help.html, accessed 2026-10-24)
- "Questions and pre-built courses are all created by faculty in the user community and shared with others in the spirit of openness." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
- "XYZ Homework is an IMathAS compatible online homework system." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
- "Some of these sites are MyOpenMath compatible, meaning most courses on MyOpenMath can be moved to that platform." (https://www.myopenmath.com/info/aboutus.php, accessed 2026-10-24)
Named independent third-party tools documented as running inside MyOpenMath, or an app marketplace: none found on the pages listed in this dossier.

## Gaps
- http://www.imathas.com/features.html : 404.
- The help file opened (https://www.myopenmath.com/help.html) is titled "IMathAS Help Documentation"; no MyOpenMath-specific help page on outcomes or mastery reporting was found, so outcomes evidence comes only from source-code interface strings.
- The WAMAP copy of the LTI page (https://www.wamap.org/info/lti.php) was fetched but not quoted.
- The Student Data Privacy Statement linked from the privacy policy was not opened.
