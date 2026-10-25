# Dossier: Ed-Fi Data Standard and ODS / API (Ed-Fi Alliance)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: Ed-Fi documentation pages wrap text across lines; quotations below join those lines. The Ed-Fi certification registry quoted under E2 and E5 is the Ed-Fi Alliance's own registry, not the 1EdTech directory.

## Identity
- "The Ed-Fi Unifying Data Model (UDM) is the widely adopted, CEDS-aligned, open-source data standard developed by the Ed-Fi community for the improvement of the community, and for the broader purpose of helping the K–12 education community in using data as a strategic asset to improve educational outcomes of students." (https://docs.ed-fi.org/reference/data-exchange/data-standard/5/, accessed 2026-10-24)
- "The Ed-Fi Data Standard creates a common language for moving data from one system to another." (https://www.ed-fi.org/ed-fi-data-standard/, accessed 2026-10-24)
- "The Ed-Fi Data Standard is backed by powerful open-source tools like the Ed-Fi Application Programming Interface (API), the Ed-Fi Operational Data Store (ODS), and community-sourced solutions." (https://www.ed-fi.org/ed-fi-data-standard/, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- No page opened describes Ed-Fi or the ODS / API deciding or sequencing what a learner does next.
- The data model records prescribed interventions: "The InterventionPrescription entity, which describes an activity intended to address a specific problem or diagnosis. It identifies the kinds of students targeted and how the intervention should be delivered." and "A StudentInterventionAssociation entity, which links students to interventions in which they participate." (https://docs.ed-fi.org/reference/data-exchange/data-standard/5/model-reference/intervention-domain/overview, accessed 2026-10-24)
- Ed-Fi's own description of use: "In Michigan, MiRead brings together assessment data and reading plans in one system" (https://www.ed-fi.org/, accessed 2026-10-24)

## E2 Interfaces evidence
- "The Ed-Fi UDM, along with the normative and non-normative guidance in the Ed-Fi Standards, serve as the foundation for enabling interoperability among secure" [systems; sentence continues past the quoted text] (https://docs.ed-fi.org/reference/data-exchange/data-standard/5/, accessed 2026-10-24)
- "Please note that the current version of Data Standard v5 is v5.2" (same URL, accessed 2026-10-24)
- "Each consumer of the API must be issued a key and secret by a system administrator. The key and secret allow the ODS / API system to issue a security token at runtime." (https://docs.ed-fi.org/reference/ed-fi-api/6.2/platform-dev-guide/security/api-claim-sets-resources, accessed 2026-10-24)
- "Leading technology providers like Skyward, PowerSchool, Infinite Campus, Education Analytics, and EdGraph have implemented the Ed-Fi Data Standard." (https://www.ed-fi.org/ed-fi-data-standard/, accessed 2026-10-24)
- Ed-Fi Alliance certification registry sections include "Ed-Fi Student Information Systems API for Data Standard v5 Certification", "Ed-Fi Assessment Outcomes API for Data Standard 4 Certification" and "Ed-Fi Domain API for Data Standard v4 Certification" (https://docs.ed-fi.org/partners/certification/registry-of-ed-fi-certified-products, accessed 2026-10-24)
- Assessment providers' documentation path: "Assessment Vendor Ed-Fi Native Integration Playbook", "Assessment Vendor Domain API Tutorial", "Ed-Fi ODS API Authorization for Assessment Providers" (navigation on https://docs.ed-fi.org/getting-started/provider-playbook/specifics-by-provider-type/assessment-providers/domain-api-tutorial/assessment-providers-data-model/learning-standards-and-learning-objective-entities, accessed 2026-10-24)
- Ed-Fi is not a 1EdTech standard; 1EdTech certification not applicable and not checked.

## E3 Learner model evidence
- "A LearningStandard entity that drives the curriculum and the assessments." and "The LearningStandard entity models the hierarchical organization of learning standards for skills and comprehension that are used to drive instruction and assessment." (https://docs.ed-fi.org/reference/data-exchange/data-standard/5/model-reference/assessment-domain/overview, accessed 2026-10-24)
- "The ObjectiveAssessment entity reflects a subset of items on an assessment that may have its own score, performance levels, or academic subject and that can be tied to learning standards." and "For each ObjectiveAssessment that is defined in the metadata, the student's results are reflected in  separate parallel instances of the complex attribute StudentAssessment." (same URL, accessed 2026-10-24)
- "The assessment model is flexible enough to convey results from complex tests such as the SAT and ACT exams, large summative assessments such as state-level standardized tests, formative assessments, and simple tests such as classroom" [quizzes; sentence continues] (same URL, accessed 2026-10-24)
- "The overall domain is primarily designed to collect and exchange data that is useful in the interpretation of student assessment results at a classroom and school-level. The domain is therefore not designed to deliver on use" [cases; sentence continues] (same URL, accessed 2026-10-24)
- "A gradebook contains grades and competencies for classroom quizzes, tests, homework, and projects. Each student's score for an assignment is a StudentGradebookEntry, which can be a Grade or a CompetencyLevel entity." (https://docs.ed-fi.org/reference/data-exchange/data-standard/5/model-reference/student-academic-record-domain/overview, accessed 2026-10-24)
- "A ReportCard entity and a GradingPeriod entity, which contain information for grading period grades and competencies." (same URL, accessed 2026-10-24)
- "Generally, most APIs are pre-configured with learning standards data published by the state education agency or other academic standards bodies important to an education agency." and "To complete our mapping, we need to add the reference from each ObjectiveAssessment to the LearningStandard. Note that in this case, we are not writing/creating LearningStandards; we are just referencing existing ones." (https://docs.ed-fi.org/getting-started/provider-playbook/specifics-by-provider-type/assessment-providers/domain-api-tutorial/assessment-providers-data-model/learning-standards-and-learning-objective-entities, accessed 2026-10-24)
- Writers of assessment results, per the Ed-Fi registry: products listed under "Ed-Fi Assessment Outcomes API for Data Standard 4 Certification" include "Cambium Assessment", "Amplify mCLASS DIBELS 8th Edition and mCLASS Lectura" and "i-Ready Math and ELA Diagnostic" (https://docs.ed-fi.org/partners/certification/registry-of-ed-fi-certified-products, accessed 2026-10-24)

## E4 Data protection evidence
- "Ed-Fi recommends implementing a robust authorization system based on the principle of "least privilege" and following several other guidelines." (https://docs.ed-fi.org/getting-started/provider-playbook/implementation/ed-fi-api-fundamentals/authorization, accessed 2026-10-24)
- "The first component of this approach is relationship-based, whereby vendors are associated with one or more local education agencies for which they can submit and access education data." and "Using this approach, vendors are given the right to access or perform operations against specific resources." (https://docs.ed-fi.org/reference/ed-fi-api/6.2/platform-dev-guide/security/api-claim-sets-resources, accessed 2026-10-24)
- "When the consumer calls the Ed-Fi ODS / API, the server will add a collection of claims to the request's context based on the associated claim set, and the security infrastructure will subsequently use those claims to make authorization decisions." (same URL, accessed 2026-10-24)
- "Access to these resources is primarily controlled by two mechanisms: claims and profiles." and "Claims and claim sets provide fine-grained access control over the resources available in the API." (https://docs.ed-fi.org/reference/ed-fi-api/6.2/platform-dev-guide/security/, accessed 2026-10-24)
- "An API Profile enables the creation of a data policy for a particular set of API Resources, generally in support of a specific usage scenario (such as for Nutrition or Special Education specialty applications). The Profile can then be assigned to API consumer applications in the ODS / API Admin App" (https://docs.ed-fi.org/reference/ed-fi-api/6.2/platform-dev-guide/security/api-profiles, accessed 2026-10-24)

## E5 Third-party tools evidence
- Ed-Fi is a data standard and data store that vendors' systems write to and read from; no page opened describes tools running inside it.
- Products listed in the Ed-Fi registry as certified include SIS products "PowerSchool", "EduPoint Synergy", "EschoolPlus", "Aeries" and assessment products "Cambium Assessment", "Amplify mCLASS DIBELS 8th Edition and mCLASS Lectura", "i-Ready Math and ELA Diagnostic" (https://docs.ed-fi.org/partners/certification/registry-of-ed-fi-certified-products, accessed 2026-10-24)
- ClassLink case study: "The district had already made strides with interoperability, working with Ed-Fi and LTI standards" (https://www.classlink.com/products/roster-server, accessed 2026-10-24)

## Gaps
- https://docs.ed-fi.org/llms.txt returned 404; pages were located through the site's sitemap.xml.
- The Learning Standards Sync page (https://docs.ed-fi.org/getting-started/community-tools/technology/learning-standards-sync/) served only navigation text; its content was not read.
- The "How Ed-Fi API Platforms Secure Student Data" overview linked from the authorization page was not opened.
- The Data Standard v5 entity-level pages for gradebook and competency objectives were not opened; only domain overviews were read.
