# Dossier: Moodle LMS (Moodle Pty Ltd and the Moodle open-source project)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: the Moodle user documentation wiki (docs.moodle.org) returned a captcha challenge (HTTP 403) to both direct requests and a browser, and the Wayback Machine refused requests (HTTP 429), so no user-documentation pages were read. Evidence below comes from the developer documentation (moodledev.io), the Moodle source code on GitHub (the web-service registry and the English interface language strings, which are the text shown to users), moodle.com, and the Moodle Marketplace. Source-code quotes are from the main branch as served on the access date.

## Identity
- "Moodle Marketplace is the new home for Moodle plugins and integrations, replacing the Plugins Directory." (https://moodle.org/plugins/, accessed 2026-10-24)
- "The place to get support, ask and answer questions and contribute to the open source learning platform, Moodle LMS." (https://moodle.com/products/lms/, accessed 2026-10-24)
- "Engage your learners with flexible, secure, and accessible online learning spaces." (https://moodle.com/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- "The availability API controls access to activities and sections. For example, a teacher could restrict access so that an activity cannot be accessed until a certain date, or so that a section cannot be accessed unless users have a certain grade in a quiz." (https://moodledev.io/docs/5.1/apis/subsystems/availability, accessed 2026-10-24)
- "Moodle will automatically prevent users from accessing your module if they do not meet the availability conditions (unless they have the ability to access hidden activities)." (same URL, accessed 2026-10-24)
- Availability conditions are themselves a plugin type: https://moodledev.io/docs/5.1/apis/plugintypes/availability (page opened, accessed 2026-10-24; not quoted).
- No page opened states whether external (LTI) tool activities can serve as the condition for, or the target of, availability restrictions.

## E2 Interfaces evidence
- "Moodle has a full-featured Web Service framework, allowing you to use and create web services for use in external systems." (https://moodledev.io/docs/5.1/apis/subsystems/external, accessed 2026-10-24)
- "Moodle uses these web services internally for: AJAX interactions in the Moodle Web Interface; and The official Moodle Mobile App." (same URL, accessed 2026-10-24)
- LTI consumer interface strings: "$string['add_ltiadv'] = 'Add LTI Advantage';" and "$string['contentitem_deeplinking'] = 'Supports Deep Linking (Content-Item Message)';" (https://raw.githubusercontent.com/moodle/moodle/main/public/mod/lti/lang/en/lti.php, accessed 2026-10-24)
- "$string['accept_grades_help'] = 'Specify whether the tool provider can add, update, read, and delete grades associated only with this external tool instance." (same URL, accessed 2026-10-24)
- Moodle as an LTI tool (provider): "$string['endpointltiversionnotice'] = 'The tool endpoints below are for manual LTI 1.3 setup only. For earlier versions (1.1/2.0), details for consumers can be found on the \'Published as LTI tools\' page, accessible via course navigation.';" and "Member and grade sync services will also be removed for these resources." (https://raw.githubusercontent.com/moodle/moodle/main/public/enrol/lti/lang/en/enrol_lti.php, accessed 2026-10-24)
- xAPI via a third-party plugin: "Logstore xAPI captures Moodle activity and sends it to a Learning Record Store (LRS) as xAPI (Tin Can) statements." (https://moodle.org/plugins/, accessed 2026-10-24)
- Certification: not checked (1EdTech directory not queried). No vendor statement about 1EdTech certification was found on the pages opened.

## E3 Learner model evidence
- Competency web-service functions registered in core, for example: "'core_competency_grade_competency' => array( ... 'description'  => 'Grade a competency.', 'type'         => 'write', 'capabilities' => 'moodle/competency:competencygrade'," and "'core_competency_grade_competency_in_course' ... 'description'  => 'Grade a competency from the course page.', 'type'         => 'write'," (https://raw.githubusercontent.com/moodle/moodle/main/public/lib/db/services.php, accessed 2026-10-24). The same file registers 83 lines matching "competency ... => array".
- "'core_competency_create_user_evidence_competency' ... 'description'  => 'Create an evidence of prior learning relationship with a competency.'," (same URL, accessed 2026-10-24)
- Competency evidence strings shown to users: "$string['evidence_coursemodulecompleted'] = 'The activity \'{$a}\' was completed.';", "$string['evidence_coursecompleted'] = 'The course \'{$a}\' was completed.';", "$string['evidence_competencyrule'] = 'The rule of the competency was met.';", "$string['evidence_manualoverride'] = 'The competency rating was manually set.';" (https://raw.githubusercontent.com/moodle/moodle/main/public/lang/en/competency.php, accessed 2026-10-24)
- Activity-completion outcome options for a linked competency: "$string['coursemodulecompetencyoutcome_complete'] = 'Complete the competency';", "$string['coursemodulecompetencyoutcome_evidence'] = 'Attach evidence';", "$string['coursemodulecompetencyoutcome_recommend'] = 'Send for review';", "$string['coursemodulecompetencyoutcome_none'] = 'Do nothing';" (same URL, accessed 2026-10-24)
- No page opened states whether completion of an external (LTI) tool activity, or a grade returned by such a tool, triggers these competency outcomes; no documentation of an external tool writing competency ratings directly through LTI was found.

## E4 Data protection evidence
- "Before operating on any data in an external function, you must ensure that the user: has access to context that the data is located in has permission to perform the relevant action" (https://moodledev.io/docs/5.1/apis/subsystems/external/security, accessed 2026-10-24)
- Per-tool LTI sharing settings: "$string['share_name_help'] = 'Specify whether the full name of the user launching the tool should be shared with the tool provider." and "$string['share_email_help'] = 'Specify whether the e-mail address of the user launching the tool will be shared with the tool provider. ... Note that this setting may be overridden in the tool configuration.';" (https://raw.githubusercontent.com/moodle/moodle/main/public/mod/lti/lang/en/lti.php, accessed 2026-10-24)
- "$string['accept_grades_help'] = 'Specify whether the tool provider can add, update, read, and delete grades associated only with this external tool instance." (same URL, accessed 2026-10-24)
- Tool approval states: "* **Active** - These tool providers have been approved and configured by an administrator. ... * **Rejected** - These tools providers are flagged as ones which an administrator has no intention of making available on the site." (same URL, accessed 2026-10-24)
- Web-service functions declare required capabilities, e.g. "'capabilities' => 'moodle/competency:competencygrade'," (https://raw.githubusercontent.com/moodle/moodle/main/public/lib/db/services.php, accessed 2026-10-24)

## E5 Third-party tools evidence
- "Showing 1–24 of 1912 results" and "Explore Moodle Certified Integrations" (https://moodle.org/plugins/, accessed 2026-10-24)
- Listings marked "Certified Integration" on that page include: "Type and handwrite mathematical notation in Moodle with MathType." ; "Cloud Poodll for Atto - audio and video recording ... An audio and video recorder for Moodle." ; "Take BigBlueButton in Moodle to a five-star experience with enhanced workflows, a modern interface, and extensible capabilities from Blindside Networks." (https://moodle.org/plugins/, accessed 2026-10-24)
- "Extend your online learning ecosystem with powerful and trusted add-ons." (https://moodle.com/, accessed 2026-10-24)
- Plugin types documented for developers include activity modules, availability conditions, blocks, enrolment, AI providers and others (https://moodledev.io/docs/5.1/apis/plugintypes listed in https://moodledev.io/sitemap.xml, accessed 2026-10-24). Plugins run inside the Moodle server; LTI tools run externally and launch from Moodle.

## Gaps
- docs.moodle.org (Competencies, Learning plans, Restrict access, External tool, Publish as LTI tool, Competency frameworks, Using web services, LTI and Moodle): HTTP 403 captcha, in curl and in a browser.
- https://moodle.org/ returned HTTP 403 captcha.
- Wayback Machine copies of docs.moodle.org/405/en/... returned HTTP 429.
- https://moodledev.io/docs/apis/subsystems/competency returned 404; no developer page on the competency subsystem was found in the 5.1 sitemap.
- https://raw.githubusercontent.com/moodle/moodle/main/lib/db/services.php returned 404 (file moved under public/ on main).
