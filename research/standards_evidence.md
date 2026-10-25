# Standards audit evidence (RQ1, P4)

Evidence only. No V-levels are assigned here; coders assign them.

**Collected:** 24 October 2026 (all URLs below accessed 2026-10-24).
**Method:** each page was fetched once with curl and read as text. Quotations are verbatim except that line breaks and runs of whitespace were collapsed to single spaces, and "..." marks an omission. Raw page text for every quoted page is saved in `study/research/std_scratch/pages/` (file names given in brackets) and the two scholarly PDFs in `study/research/std_scratch/dl/`.
**Not touched:** the 1EdTech TrustEd Apps / certification directory (site.imsglobal.org/certifications) and its Algolia index were not opened or queried. Certification counts in the brief (LTI 197, OneRoster 94, Open Badges 48, Common Cartridge 28, QTI 23, CASE 16, CLR 9, Edu-API 8, Caliper 6, LIS 1; seen 14 Oct 2026) are context only and were not re-read.

**Compliance flag for the author (read first).** The 1EdTech legal clause quoted in section 0 has two sentences. The second bans systematic retrieval to compile a collection or directory, which is the directory concern. The first is broader: it bars "any robot, spider, scraper ... or other automated means to access, acquire, copy, or monitor any portion of the website". Read literally, that covers scripted fetching of the public spec and certification pages too, which is how this evidence was collected (about 60 page fetches from 1edtech.org, imsglobal.org and standards.1edtech.org, one copy each, for research quotation). I did not retry pages that returned 403 or try to get around any block. Before publication, decide whether to (a) re-open the quoted pages by hand in a browser and confirm each quote, or (b) ask 1EdTech for written permission. Either way, the quotes themselves are short excerpts of public specifications.

---

## 0. 1EdTech terms on automated retrieval

**URL:** https://www.1edtech.org/about/legal [legal.txt], section "Prohibition on Automated Data Collection":

> "You agree not to use any robot, spider, scraper, data mining tools, data gathering or extraction tools, or other automated means to access, acquire, copy, or monitor any portion of the website or its content. You also agree not to bypass or circumvent the navigational structure or presentation of the website or its content, or to engage in any activity that interferes with the proper working of the website, or places an unreasonable or disproportionately large load on our infrastructure."

> "Any attempt to systematically retrieve data or other content from the website to create or compile, directly or indirectly, a collection, database, or directory without our prior written permission is strictly prohibited."

The same page carries "Copyright © 2001-2025, 1EdTech Consortium, Inc." and notes that site materials "may be downloaded or copied provided that ALL copies retain the copyright and any other proprietary notices contained on the materials for personal use."

## 0b. What 1EdTech says certification means (all standards)

**URL:** https://www.1edtech.org/certification/get-certified [getcert.txt]

> "Pass a rigorous set of tests to guarantee interoperability across the widest range of product integrations."

> "Buyers trust 1EdTech as neutral arbiter of truly interoperable products and content."

> "Products must be recertified annually. Active 1EdTech membership is required to maintain certification."

**URL:** https://www.imsglobal.org/spec/oneroster/v1p2 [or12.txt], section 1.3 (the same boilerplate appears in CLR 1.0, section 1.4):

> "Certification designates passing a set of tests that verify the standard has been implemented correctly and guarantees a product's interoperability across hundreds of other certified products."

**URL:** https://www.imsglobal.org/spec/clr/v1p0/ [clr1.txt], section 1.4:

> "while conformance certification provides a "seal" for passing prescribed tests it is much more than that. It is a commitment by a supplier to the 1EdTech community for continuous support for achieving "plug and play" integration."

Every standard-specific certification page (OneRoster, Open Badges, CLR, CASE, QTI, Common Cartridge) uses the same four steps (Assess, Test, Submit, Receive). Most say: "Our 1EdTech staff manually reviews your test results with a fine-tooth comb." (OneRoster, CLR, CASE, Common Cartridge pages.)

---

## 1. LTI (Learning Tools Interoperability) / LTI Advantage

### A. Referent
**URL:** https://www.1edtech.org/standards/lti [lticert.txt]

> "1EdTech's LTI standard is a technical standard (not a product) used to connect learning tools with an institution's learning environment without logging into each tool. LTI supports a high level of security for passing data about the users, their institutional enrollment, and roles."

> "Assignment and Grade Services (AGS) provides a way to create a gradebook column and post grades associated with a resource link. Names and Role Provisioning Services 2.0 (NRPS) provides access to data about users and their roles within organizations ... Deep Linking 2.0 (DL) allows a teacher or platform (LMS) user to integrate content gathered from an external tool."

**URL:** https://www.imsglobal.org/spec/lti/v1p3 [lti.txt], section 3.1.5:

> "An LTI Launch refers to the process in which a user interacts with an LTI Link within the platform and is subsequently "launched" into a tool."

**URL:** https://www.imsglobal.org/spec/lti-nrps/v2p0 [lti_nrps.txt], Abstract:

> "The Learning Tools Interoperability (LTI)® Names and Role Provisioning Services is an LTI™ specification for providing access to a list of users and their roles within context of a course, program or other grouping."

**URL:** https://www.imsglobal.org/spec/lti-ags/v2p0/ [lti_ags.txt], section 1:

> "The Basic Outcomes service introduced in LTI 1.1 provides a simple facility for associating a single gradebook column with each resource link and allows a tool to manage results in these columns as decimal normalized values."

### B. What certification tests
**URL:** https://www.imsglobal.org/spec/lti/v1p3/cert/ (LTI Advantage Conformance Certification Guide) [lti_certguide.txt]

Scope:
> "Certification to LTI Advantage requires implementation of: LTI Core Version 1.3 Deep Linking Version 2.0 Names and Role Provisioning Services Version 2.0 Assignment and Grade Services Version 2.0"

> "NOTE: All tests MUST be passed for either the Platform or the Tool to be considered compliant and apply for certification."

Security / provenance requirements:
> "Security of the JWT is achieved through the use of TLS-secured web channels, as well as signing of the JWT with asymmetric cryptosystems."

> "All Learning Platforms and Tools MUST provide the mechanisms (the libraries) for signing and verification of signatures for JWTs signed with RSA 256. ... The use of Symmetric Cryptosystems SHALL NOT be considered legal and use of them is expressly forbidden."

Test table for the Full Student Payload (section 5.1.1), quoted as "Test Name Test Description":
> "Payload is LTI 1.3 Tests that JWT received conforms to format of 1.3 Core Launch JWT Payload Timestamps Valid The iat and exp Timestamps are valid Payload Signed with RSA 256 Header for JWT confirmed that signing done is RSA 256 Payload Signature Valid The KID in the JWT Header corresponds to the correct Public Key on the Well-Known URL and the Public Key for this KID correctly verifies the JWT Signature Payload is Complete All Required 1.3 Core Launch Claims are present Payload LTI Version Required LTI Version Claim is set correctly to 1.3.0 Payload Roles Correct The Roles in the JWT are those of the Learner/Student and not an Instructor Payload is Free of Extra Whitespace There MUST NOT be extra Whitespace before or after any values in the JWT Payload Expected Received You MUST Affirm that All Expected Values in the JWT were received"

NRPS test (section 5.3):
> "Names and Roles Payload Test confirms Payload type complete and formatted correctly for Names and Role Verify Names and Roles Headers Test Parses the Headers in the NRPS Response and displays what (if any) were Found. You MUST verify that what is found is what the GET return sent in the headers"

AGS test (section 5.4), behavior against the live platform:
> "Create Line Item 1 Test Attempts to use new Bearer Token to Create First Line Item Retrieve Line Item 1 Test Attempts to use new Bearer Token to Retrieve just created First Line Item Create Line Item 2 ..."

> "This means that at least two gradable (in our testing case) items will exist in the tested platform. (It is a good time to double-check that this is indeed true before continuing.)"

> "the idea is to prove that the AGS implementation can differentiate between calls to different contexts in the platform."

### C. Independent check of the referent
No 1EdTech text found that discusses checking an LTI launch against an outside source. The certification itself runs live launches and live gradebook writes against the certification suite (quotes in B: the tester affirms "All Expected Values in the JWT were received" and is told to "double-check that this is indeed true" that line items exist in the platform). Coders may judge whether "the launch opens" or "the column appears in the gradebook" is a reachable check.

### D. Version and certification dates
- LTI 1.3 Core: "IMS Final Release ... Date Issued: 16 April 2019" (https://www.imsglobal.org/spec/lti/v1p3, [lti.txt]). AGS 2.0: "Date Issued: 16 April 2019" ([lti_ags.txt]).
- History, same page section 2: "LTI has its origins in the IMS Tools Interoperability specifications released in 2006. ... In May 2010, IMS released a version named Basic LTI ... When IMS added a simple outcomes service in March 2011, it renamed Basic LTI as LTI 1.0, with the new release including the simple outcomes service named as LTI 1.1."
- **URL:** https://www.imsglobal.org/lti-advantage-adoption [lti_adoption.txt]: "LTI 1.3 and LTI Advantage are now available for public adoption and 1EdTech member certification." and "1EdTech continues to issue conformance certification for LTI 1.0 and 1.1. but, we strongly recommend that all suppliers move to LTI 1.3". The page gives no date for when LTI certification first opened.

---

## 2. OneRoster

### A. Referent
**URL:** https://www.1edtech.org/standards/oneroster [oneroster.txt]

> "1EdTech's OneRoster standard solves a school's need to securely and reliably exchange roster information, course materials, and grades between systems."

> "OneRoster defines information about people (users), courses, enrollments, organizations, and grades."

> "Rostering : Provides the ability to manage class rosters, including student, teacher, organization, course, and related enrollment information between various platforms such as a student information system (SIS) and a learning management system (LMS). Gradebook : Provides the ability to manage the exchange of information about grade books in the form of results, lineItems, collections of lineItems (categories), and score scales. ... Resource : Provides the ability to manage the allocation of resources to classes, courses, and users. It does not enable access to the resources themselves."

**URL:** https://www.imsglobal.org/spec/oneroster/v1p2 [or12.txt], section 1:

> "The IMS OneRoster®(OR) specification supports securely sharing class rosters and related data between a student information system (SIS) and any other system, typically a content application or learning information system (LMS)."

### B. What certification tests
**URL:** https://www.imsglobal.org/oneroster-conformance-testing [or_conf.txt]

> "Go to the 1EdTech Conformance Test Suite for OneRoster for either the REST or CSV version of OneRoster. ... Once the test has been successfully run, submit a print out of the test results, complete this form, and send the test results and the completed form to conformance@imsglobal.org 1EdTech will review the results and issue a conformance certification number."

> "Consumers of CSVs: ... Import the valid Reference csv files and validate that they import correctly. Log that you have detected problems in the reference tests with known errors."

> "Comment: Detailed explanation of why each of the CSV files were rejected. This must explain the set of detected errors in the CSV file. Explanation of syntactic and semantic errors is required."

> "CSV Export Test that your csv data sets meet OneRoster 1.2 compliance"; "REST Service Provider Testing of OneRoster 1.2 Service provider systems for conformance"; "REST Service Consumer Testing of OneRoster 1.2 Service consumer systems for conformance"

**URL:** https://www.imsglobal.org/ims-oneroster-v11-final-conformance-guide (OneRoster 1.1 Conformance and Certification) [or11_conf.txt]

> "All Tests for either the REST version or the CSV version must be passed successfully to be considered 1EdTech OneRoster compliant."

> "It should be noted that all filenames, column headers and data values are case sensitive. Incorrect use of case will result in the corresponding conformance error being reported."

> "Next it will check the accompanying data CSV files for correctness. Finally it will provide a report on the correctness of the set of CSV files. Note that ONLY the 'manifest.csv' file is required in the zip file i.e. any combination of accompanying data model CSV files is permitted provided that these are semantically complete and self-consistent."

> "The OneRoster CSV validator is definitive when establishing whether or not a set of CSV files is conformant to the OneRoster specification."

> "This set of zip files consists of two types of test files: CSV files that are syntactically correct and semantically consistent; CSV files which are syntactically incorrect and/or semantically inconsistent. In the case of the files with known errors, a system must indicate that the files are incorrect."

> "For 'GET' requests a service provider must supply all of the required data fields for the action and may supply any of the optional data fields."

Note for coders: in these documents "semantic" refers to internal consistency of the data set (for example the minimum file set "ensures semantic consistency for rostering information"), not to agreement with the school's actual enrollment.

### C. Independent check of the referent
The spec names the SIS as the source system (quotes in A). No 1EdTech text found that describes a receiver checking a OneRoster record against the SIS. The TPLC draft (section 13) describes source systems as "authoritative sources" and the SIS-to-LMS exchange as system-of-record interoperability.

### D. Version and certification dates
- OneRoster 1.2: "IMS Final Release Document Version: 2 Date Issued: September 19, 2022" ([or12.txt]). Revision history: "OneRoster 1.2 Candidate Final Public July 01, 2021 First release ... June 06, 2022 OneRoster 1.2 first final release ... September 19, 2022 OneRoster 1.2 Final Release."
- OneRoster 1.1 Conformance and Certification: "1EdTech Final Release Version 1.1 Date Issued: 31st December 2020" ([or11_conf.txt]); the same document says "several 1EdTech Members have aleady successfully completed con[formance]".
- Earliest OneRoster certification date not found on pages opened.

---

## 3. Open Badges (2.0, 2.1, 3.0)

### A. Referent
**URL:** https://www.1edtech.org/standards/open-badges [badges.txt]

> "1EdTech's Open Badges specification describes a method for packaging information about a single recognition or achievement, such as an earned microcredential, skill, competency, or degree."

> "Open Badges 3.0 and CLR Standard 2.0 assertions are specific to one earner and are a claim that the earner has made a particular achievement with metadata about the achievement, the issuer, and the earner, including possible evidence that provides support for the claim."

> "An Issuer makes a claim that an earner has met the criteria of a particular defined Achievement. Each Open Badges OpenBadgeCredential is digitally signed by its issuing organization as Verifiable Credentials compatible with the Verifiable Credentials Data Model 2.0."

> "credentials can be augmented with an EndorsementCredential from a third party to lend the support of another individual or organization to the quality or relevance of an issuer or credential data."

### B. What certification and verification check
**URL:** https://www.imsglobal.org/spec/ob/v3p0/ (Open Badges 3.0 spec) [ob3.txt], section 9:

> "Verification is the process to determine whether a verifiable credential or verifiable presentation is an authentic and timely statement of the issuer or presenter respectively. This includes checking that: the credential (or presentation) conforms to the specification; the proof method is satisfied; and, if present, the status check succeeds. Verification of a credential does not imply evaluation of the truth of claims encoded in the credential. Validation is the process of assuring the verifiable credential or verifiable presentation meets the needs of the verifier and other dependent stakeholders. Validating verifiable credentials or verifiable presentations is outside the scope of this specification. Note The 1EdTech Validator performs verification as described here."

Section 9.1 steps (excerpts): "check that the credential conforms to JSON Schema"; "If the signature cannot be verified, the proof method is not satisfied."; "A Credential is revoked if the credentialStatus property is present ... If the current date and time is after the validUntil , the OpenBadgeCredential is expired."; "Optionally verify the subject (recipient): ... The id or identifier value to use for verification must be shared with the verifier in an out-of-band process such as by email."

**URL:** https://www.imsglobal.org/spec/ob/v3p0/cert/ (OB 3.0 Conformance and Certification Guide) [ob3_cert.txt]

> "Gaining this certification is expected to be more difficult than simply meeting the minimum requirements for producing a valid Open Badge. Certification may be achieved in one or more of the following services: Open Badges Issuer Open Badges Displayer Open Badges Host"

> "A badge is deemed valid if it successfully passes JSON-LD validation in safe mode and meets the verification requirements specified in Open Badges Specification v3.0."

Issuer tests: "Create a valid 3.0 badge and issue it to the recipient conformance@imsglobal.org and submit the issued badge to the conformance test system. Demonstrate through video the candidate platform's methodology for a recipient to retrieve their badge."

Displayer tests: "The conformance test system will display the URL of three badges. One of them is neither expired nor revoked, other is expired but not revoked and the last one is not expired but revoked. The candidate platform must verify these badges and submit the status in the conformance test system. Demonstrate through separate videos that the platform allows viewers of badges to see the following data in all provided badges: image (if the badge provided is a baked badge) name description issuer name issuedOn Date status (expired and/or revoked)"

Terms section: "Verifiable Credential (VC): A tamper-evident credential whose issuer can be cryptographically verified."

Attestation: "you must agree that there is no misrepresentation or manipulation of result[s]".

**URL:** https://www.imsglobal.org/clr/faq (Open Badges and CLR FAQ) [obclr_faq.txt]

> "A verifiable credential, or VC, is cryptographically signed to be secure (tamper-resistant) and immediately machine-verifiable. Issuing Open Badges and Comprehensive Learner Records as verifiable credentials means the credential's authorship and the credential's owner can be verified and ensured to be authentic."

> "Verifiable credentials are high-level packaging standard (like an envelope) that contains data governed by other standards (like a letter within the envelope). When consumers view an issued Open Badge or CLR, they may initiate a verification process that communicates with the server that hosts the original badge metadata. The server verifies that the badge is valid and communicates back to the consumer with confirmation details."

### C. Independent check of the referent; trust and meaning
OB 3.0 spec (above): "Verification of a credential does not imply evaluation of the truth of claims encoded in the credential. ... Validating verifiable credentials ... is outside the scope of this specification."

FAQ on endorsements (https://www.imsglobal.org/clr/faq):
> "Organizations with recognized authority over a subject domain, such as an accrediting agency or a licensing body, can endorse an issuer's credential program as meeting their required quality standards. Issuers can be endorsed as meeting or exceeding specific performance expectations the endorser may define. The recipient of an achievement credential can also be endorsed to signal agreement with the claims of knowledge, skills, and abilities expressed within."

> "Endorsements are authenticated using the same cryptographic proofing met[hods]"

Scholarly (see section 14) on what a badge means to different receivers.

### D. Version and certification dates
- OB 2.0 Conformance and Certification Guide: "IMS Final Release Date Issued 12 April 2018" (https://www.imsglobal.org/sites/default/files/Badges/OBv2p0Final/cert/index.html [ob2_cert.txt]). That guide: "Beginning with Open Badges 2.0, the candidate platform must issue a valid baked badge and demonstrate how the badge is retrieved by the recipient."
- OB 3.0 revision history ([ob3.txt]): "Candidate Final 1.0 July 14, 2022 Open Badges 3.0 first Candidate Final release Candidate Public Final 1.0.1 February 9, 2023 ... Final 1.0 May 27, 2024 Open Badges 3.0 Final Release". Current spec page: "Date Issued: June 29, 2026".
- OB 3.0 cert guide: "Final Release Document Version: 1.5 Date Issued: June 15, 2026" ([ob3_cert.txt]).
- The 1EdTech certification page lists "Open Badges 2.0 Certification Testing System Open Badges 2.1 Certification Testing Suite Open Badges 3.0 Testing Suite" (https://www.1edtech.org/certification/open-badges [ob_certpage.txt]).

---

## 4. CLR (Comprehensive Learner Record) 1.0 and 2.0

### A. Referent
**URL:** https://www.1edtech.org/standards/clr [clr.txt]

> "1EdTech's Comprehensive Learner Record Standard (CLR Standard) is the new generation of secure, verifiable learning and employment records supporting all academic and workplace recognition and achievements, including courses, competencies, skills, and employer-based achievements and milestones."

> "an assertion is specific to one learner. It contains a claim that the learner has made a particular achievement and metadata about the achievement, the issuer, and the learner, including possible evidence supporting the claim. A comprehensive learner record (CLR) allows many achievement credentials to be bundled ... Individual component credentials are verifiable, and the wrapping CLR is also verifiable."

**URL:** https://www.imsglobal.org/spec/clr/v1p0/ [clr1.txt]

> "The 1EdTech Comprehensive Learner Record (CLR) Standard supports interoperability in that CLR publishers and consumers can consistently send, receive, and verify records among conformant systems. The CLR Standard describes an information model, service definition, and implementation guide to allow institutions, suppliers, and others to 'extend' the traditional transcript with records and types of information that are typically not found in a traditional transcript, such as competency attainment, co-curricular activities, ..."

> "Issuer The profile of an organization or entity that has made a particular Assertion about a Learner. The Issuer of an Assertion is the authoritative source for that specific Assertion."

> "Inspector A Consumer that inspects a CLR to verify or validate the data."

### B. What certification and verification check
**URL:** https://www.imsglobal.org/spec/clr/v2p0/ [clr2.txt], section 8 (same wording as OB 3.0):

> "Verification is the process to determine whether a verifiable credential is an authentic and timely statement of the issuer or presenter respectively. This includes checking that: the credential conforms to the specification; the proof method is satisfied; and, if present, the status check succeeds. Verification of a credential does not imply evaluation of the truth of claims encoded in the credential. Validation is the process of assuring the verifiable credential meets the needs of the verifier and other dependent stakeholders. Validating verifiable credentials is outside the scope of this specification. Note The 1EdTech Validator performs verification as described here."

**URL:** https://www.imsglobal.org/spec/clr/v2p0/cert/ [clr2_cert.txt]

> "Gaining this certification is expected to be more difficult than simply meeting the minimum requirements for producing a valid CLR Credential. Certification may be achieved in one or more of the following services: CLR Issuer CLR Displayer CLR Host"

> "The candidate platform must issue a valid baked ClrCredential and demon[strate] ..." ; "3.1 Tests Create a valid baked ClrCredential and issue it to the recipient conformance@imsglobal.org and submit the issued badge to the conformance ..."

> "An CLR Displayer is an application that displays and verifies ClrCredentials for viewers. The candidate platform must support viewer-initiated verification of a ClrCredential. ... A Credential is revoked if the credentialStatus property is present, and the type of the CredentialStatus object is "1EdTechRevocationList". A Credential is expired if the current date and time is aft[er] ..."

**URL:** https://www.1edtech.org/certification/clr [clr_certpage.txt]: "Use the CLR Validator to run the product through the certification test suite. CLR 1.0 Validator CLR 2.0 Validator"; "Select multiple product types (Consumer, Provider, or Host) and multiple authorization tokens to test simultaneously".

### C. Independent check of the referent
Same as Open Badges: the spec states that verification "does not imply evaluation of the truth of claims". CLR 1.0 names the Issuer as "the authoritative source for that specific Assertion" (quote in A). No 1EdTech text found that describes a receiver checking a CLR achievement against anything other than the issuer.

### D. Version and certification dates
- CLR 1.0: "1EdTech Final Release Date Issued: January 14, 2021"; revision history "CLR 1.0 Final January 14, 2021 First release of CLR 1.0 Final. Incorporates changes since May 2020." ([clr1.txt])
- CLR 1.0 Conformance and Certification Guide: "1EdTech Final Release Date Issued: February 5, 2021" (https://www.imsglobal.org/spec/clr/v1p0/cert/ [clr1_cert.txt]).
- CLR 2.0 revision history: "Base Document 1.0 May 27, 2022 IPR Review Candidate Final 1.0 July 14, 2022 Comprehensive Learner Record 2.0 first Candidate Final release Final 1.0 February 26, 2025 Comprehensive Learner Record 2.0 Final Release Final 1.0.1 March 14th, 2025". Current page: "Document Version: 1.1 Date Issued: October 14, 2025" ([clr2.txt]).

---

## 5. CASE (Competencies and Academic Standards Exchange)

### A. Referent
**URL:** https://www.imsglobal.org/spec/case/v1p1 [case11.txt]

> "The 1EdTech Competencies and Academic Standards Exchange® (CASE®) 1.1 specification defines how systems can exchange academic standards, competencies, and/or skills in a standardized way. The goal for CASE is to replace the current ways of documenting a learning standard and competency, typically a PDF or HTML document, by a method that is both human and machine-readable. These digital versions are called CASE Frameworks."

**URL:** https://www.1edtech.org/standards/case [case.txt]

> "A CASE framework is a hierarchically structured digital version of the static versions (PDF, Word, Excel, or HTML) of academic standards, learning objectives, or competencies documents."

> "Institutions can associate academic standards with course content and verify the existence of resources aligned to all the academic standards associated with a course or program."

> "Educators and learners can track progress toward mastery via tagged activities, assignments, and assessment results."

**URL:** https://www.imsglobal.org/spec/CASE/v1p1/impl (CASE 1.1 Best Practices and Implementation Guide) [case_impl.txt]

> "standards issuing agencies and institutions (e.g. Georgia Department of Education, Gwinnett Public Schools, Colleges and Universities, WIDA, The College Board, and AACN) encode their competency frameworks using the standardized CASE JSON format, then publish this JSON data on a 1EdTech-certified CASE publishing webserver, making the data available via a set of standardized CASE REST APIs to anyone who wants to retrieve it. Systems that provide educational services ... can then retrieve the CASE JSON representing any competency framework of interest from the issuing agency's CASE server using these standardized APIs. Resources (instructional videos, test items, report cards, badges, etc.) can then be aligned to the canonical CASE identifiers representing competencies"

> "fullStatement (required): the fullStatement is the official statement of the competency, as defined by the issuing agency (creator)."

> "publisher (optional): the entity responsible for publishing this competency framework in CASE format. ... For example, CASE Network currently includes many frameworks for whom the creator is a state department of education, but the publisher is Common Good Learning Tools, who has coded the state's frameworks in CASE format."

> "The Competencies and Academic Standards Exchange (CASE)'s Work Group mission is to create a globally adopted technical specification and support shared tools within 1EdTech community, that enables trusted agents to manage and publish Academic Standards and Competency Framework Documents."

### B. What certification tests
**URL:** https://www.imsglobal.org/spec/case/v1p1/cert (CASE 1.1 Conformance and Certification) [case_cert.txt]

> "All of the REQUIRED feature tests MUST be passed successfully to be considered 1EdTech CASE Service compliant. ... The conformance test systems will then test ALL of the REQUIRED and identified OPTIONAL features to confirm their correct implementation."

> "The functional capabilities of such systems are: They must support all of the required endpoints; They may support any of the optional endpoints; They must supply all of the required data fields in the JSON payloads; They must be capable of supplying all of the optional data fields in the JSON payloads (conformance testing requires ALL data fields to be populated); They must not provide extension data fields in the JSON payloads"

> "Rich text with Markdown and LaTeX X Will be reviewed, if included in the CASE v1.1 certification submission"; "CASE Consumer Certification Requirements X Required as a minimum either a CFPackage or CFItem must be supported"

**URL:** https://www.1edtech.org/certification/case [case_certpage.txt]: "Run your product through the CASE 1.0 or CASE 1.1 Certification Test Suite"; "The CASE certification process for Service Providers is available to 1EdTech Contributing, Affiliate, and CASE Alliance members."

Not opened: https://www.imsglobal.org/competencies-and-academic-standards-exchange-conformance-certification returned HTTP 403.

### C. Independent check of the referent
The framework itself has a named issuing agency and a canonical URI on that agency's CASE server (quotes in A). Whether a resource is correctly aligned to a CASE item is a separate claim; the implementation guide leaves meaning changes to the issuing agency: "Change to an Item that Substantially - in the judgment of the issuing agency - changes the meaning of the item: Create a new CFItem/GUID" (original uses a dash between "Substantially" and "in"; [case_impl.txt] section 4.3.5). No 1EdTech text found that tests whether an alignment is correct.

### D. Version and certification dates
- Implementation guide revision history ([case_impl.txt]): "CASE Final Release 1.0 1 7th July, 2017 The first formal Final Release that is ready for public adoption and implementation. CASE Final Release 1.1 1 1st November, 2024".
- CASE 1.1 spec page revision history ([case11.txt]): "CASE 1.1 Final Release February 28th, 2024 CASE 1.1 first Final Release."
- CASE 1.1 cert guide: "Final Release Document Version: 1 Date Issued: January 24th, 2025" ([case_cert.txt]).

---

## 6. QTI (Question and Test Interoperability)

### A. Referent
**URL:** https://www.1edtech.org/standards/qti [qti.txt]

> "1EdTech's Question & Test Interoperability (QTI) ® standard is a way of packaging and moving tests and questions from one application to another."

> "The QTI specification is a technical standard for the exchange of assessment items and tests, usage data, and results reporting."

> "QTI is MUCH richer than HTML forms because it has: Context (metadata) Response details Scoring logic Can include usage data (including item difficulty and other statistics)"

### B. What certification tests
**URL:** https://www.imsglobal.org/spec/qti/v3p0/impl (QTI 3 Best Practices and Implementation Guide) [qti3.txt], section 1.1.3:

> "The QTI 3 standard is comprised of a collection of specification documents designed to ensure that the exchangeable package of assessment content adheres to a rigorous set of file structure expectations. ... This revised item specification is enforced by a newer, more rigorous conformance process. User experience interoperability will enable content authors to produce questions and tests that render and behave consistently across systems implementing QTI 3."

> "Interoperability for QTI 3 is also supported by the use of an 1EdTech governed conformance and certification process, which employs 1EdTech provided online automated validation tools, and requires certified systems to demonstrate validation. The validation tools assist organizations by examining exchange files for structural consistency against the QTI 3 standard."

**URL:** http://www.imsglobal.org/1edtech-qti-conformance-certification [qti_conf.txt]

> "For an outline of the conformance approaches for each of the QTI versions, use the Conformance and Certification documents. These include tables that indicate the minimum requirements for each certification profile. ... If you're looking to test content against the various schemas, visit the QTI online validator."

**URL:** https://www.1edtech.org/certification/qti [qti_certpage.txt]

> "Run the application or exported content through the member validator."; "There are test files available to Affiliate and Contributing Members in GitHub, per version. QTI 3: Test Set Content QTI 2.2 Level 1 Entry: Import Test Set Content ..."; "Don't forget to return the completed QTI Certification Checklist to conformance@imsglobal.org"

Not opened: the QTI 3 Conformance and Certification document itself; https://github.com/1EdTech/qti-conformance returned 404 (members-only repository).

### C. Independent check of the referent
No 1EdTech text found on checking item correctness or psychometric quality. The guide states the aim that items "render and behave consistently across systems" (quote in B).

### D. Version and certification dates
- QTI 3 implementation guide revision history ([qti3.txt]): "Final Release 2.0 1 October 2024 The first final release of this document as part of the QTI version 3.0.1. ... Final Release 1.0 1 May 2022 The first final release of this document as part of the QTI 3.0 specification set."
- QTI 2.1 wind-down ([qti_conf.txt]): "No new QTI 2.1 product (applications & content package) certifications issued after December 31, 2023. No recertifications for QTI 2.1 products after September 30, 2024. All QTI 2.1 product (application) certifications expire December 31, 2024. Existing QTI 2.1 Content Package certifications will remain in the product directory."

---

## 7. Common Cartridge (CC) and Thin Common Cartridge

### A. Referent
**URL:** https://www.1edtech.org/standards/cc [cc.txt]

> "Common Cartridge (CC) is a standardized way to: Package and exchange digital learning materials and assessments Import and export course materials to and from your certified learning management system (LMS), portal, learning object repository (LOR), or other learning platform Exchange links and provide authorization to third-party learning tools using Learning Tools Interoperability ® (LTI ®)"

> "To build a Common Cartridge, a publisher packages an entire digital textbook. This includes all the digital content, multimedia objects, interactive tools, activities, and assessments."

> "Thin Common Cartridge ... is a standard way to exchange a collection of links that, combined, would make up your digital textbook."

### B. What certification tests
**URL:** https://www.imsglobal.org/spec/cc/v1p4/impl (CC 1.4 Implementation Guide) [cc_impl.txt]

> "The primary focus of the Common Cartridge specification is achieving error-free import of content into any conforming LMS platform (see figure above). No runtime model is expressed, but any conforming LMS must support (either directly, or via a call-out to a suitable external service) all of the functionality implied by the Common Cartridge schema set."

> "The resulting Common Cartridge profile should be easier for developers to implement and lends itself to more routine conformance testing of these implementations."

> "By definition, any system that has Full CC v1.4 import certification will have corresponding Thin CC v1.4 certification."

**URL:** https://www.1edtech.org/certification/common-cartridge [cc_certpage.txt]

> "Cartridges Read Tools - Tools that read in cartridges. Write Tools - Tools that export or create cartridges. Read/Write Tools - Tools that both read cartridges and export cartridges and are able to import and export the same cartridge(s). Runners - Tools that allow you to import and play common cartridges."

> "Run product through the 1EdTech Member Validator."

> "Do you have over 25 cartridges that are all generated the same way? If so, test a subset (at least 25%) of the cartridges."

> "Make sure to send your cartridge(s), your results, and the form document in the email with your certification submission."

Not opened (HTTP 403): https://www.imsglobal.org/spec/cc/v1p4 , https://www.imsglobal.org/spec/cc/v1p4/cert , https://www.imsglobal.org/common-cartridge-conformance-testing-process .

### C. Independent check of the referent
No 1EdTech text found beyond the import focus quoted in B. The "Runners" category ("import and play") is the closest certification wording to rendering the package.

### D. Version and certification dates
- CC 1.4 implementation guide: "1EdTech Candidate Final Spec Version 1.4 ... Date Issued: September 15, 2021" ([cc_impl.txt]).
- Version history in the same guide: "Final v1.0 29 January 2009 The first formal release of the CC specification. Public Draft v1.1 9 November 2010 ..."

---

## 8. Caliper Analytics

### A. Referent
**URL:** https://www.1edtech.org/standards/caliper [caliper.txt]

> "Caliper Analytics enables institutions to collect learning data from digital resources to understand better and visualize learning activity and product usage data and present this information to students, instructors, and advisors in meaningful ways."

> "Annotating a reading, playing a video, taking a test, or grading an assignment submission represent a few examples of the many activities or events that Caliper's metric profiles attempt to describe."

**URL:** https://www.imsglobal.org/spec/caliper/v1p2 [cal12.txt], section 1:

> "The Caliper Analytics® specification seeks to address a number of the issues outlined above by providing a structured approach to describing, collecting and exchanging learning activity data. Establishing a common vocabulary for describing learning interactions is a central objective. ... Caliper also defines an application programming interface (the Sensor API™) for marshalling and transmitting event data from instrumented applications to target endpoints for storage, analysis and use. Industry-wide adoption of Caliper offers the tantalizing prospect of a more unified learning data environment in which to build new and innovative services designed to measure, infer, predict, report and visualize."

### B. What certification tests
**URL:** https://www.imsglobal.org/spec/caliper/v1p2/cert (Caliper Conformance and Certification Guide 1.2) [cal_cert.txt]

> "This document is the certification guide for Caliper Sensors. In this release of the Caliper specification, certification services are not provided for Caliper endpoints. Endpoint implementors should take note that it is the intent of the Caliper Working Group to add endpoint certification in forthcoming releases of the specification."

> "Initiate the product test, sending messages to the certification service endpoint. ... As messages are processed metric profile certifications that have been attained will be indicated by check marks."

> "Certain Event properties are required and MUST be specified. Required properties include: id , type , actor , action , object and eventTime . ... The actions vocabulary is limited to the supported actions described in the Caliper Analytics® Specification , version 1.2, Actions Appendix , and no other. Serialized Events and Entities MUST conform to the syntactical requirements defined in the Caliper specification, and be contained within a Caliper Envelope using proper JSON-LD context and serialization"

> "If a Caliper sensor sends a message with a Content-Type other than "application/json", the certification service will reply with a 415 Unsupported Media Type response."

> "The tests MUST be completed by a designated representative of the member organization and you MUST agree that there is no misrepresentation or manipulation of the results in the submitted report."

Not opened (HTTP 403): https://www.imsglobal.org/caliper-analytics-conformance .

### C. Independent check of the referent
No 1EdTech text found on checking that a reported event happened. The spec frames the downstream use as services that "measure, infer, predict, report and visualize" (quote in A).

### D. Version and certification dates
- Caliper 1.2 spec and cert guide: "1EdTech Final Release Version 1.2 1EdTech Final Release Date Issued: 27 March 2020" ([cal12.txt], [cal_cert.txt]). Cert guide revision history: "21 October, 2020 Base Document Release 27 March, 2020 Candidate Final Release". Its reference list cites "Caliper Analytics® Specification, version 1.2. 12 January 2018."
- Earlier Caliper versions (1.0, 1.1) and their certification dates: not found on pages opened.

---

## 9. Edu-API

### A. Referent
**URL:** https://standards.1edtech.org/edu-api/specifications/standards/v1p0 [eduapi_spec.txt]

> "Edu-API addresses the need for standardized, interoperable data exchange between an institution's systems of record like a Student Information System and the downstream systems that consume that data, such as learning management systems, assessment platforms, and student service tools. The specification covers core academic entities including persons, organizations, academic sessions, course offerings, and enrollments"

> "Edu-API is designed to address key provisioning/rostering use cases from the Student Information System (SIS) to consumers in a Higher Education context."

> "SIS Student Information System: The system that stores and tracks all student information, including grades, attendance records, and more. The SIS is the most common Edu-API Provider."

### B. What certification tests
**URL:** https://standards.1edtech.org/edu-api/specifications/standards/v1p0/cert (Edu-API Conformance and Certification Guide v1.0) [eduapi_cert.txt]

> "For Provider Systems Enter the details for your hostname, clientID, and clientSecret ... At this point, the testing applications will query your product for its OpenAPI Service Definition file and use the details contained therein to make the appropriate REST-API requests against your provider instance. For Consumer Systems use the information presented on the testing screen to configure your product. make the relevant service calls which will be recorded in the testing application."

> "All Tests for the appropriate operational modes must be passed successfully to be considered Edu-API conformant and be issued a certification ID."

> "They MUST support the OAuth 2.0 Bearer Token authentication mechanism. Systems seeking certification for service 'provider - delta' mode must support the use of dateLastModified attribute."

### C. Independent check of the referent
Same structure as OneRoster: the SIS is named as the system of record (quotes in A). No text found on receivers checking records against it.

### D. Version and certification dates
- Spec revision history ([eduapi_spec.txt]): "Base Document 2022-01-01 First release of Edu-API 1.0 Base Document. Candidate Public Final 2022-03-01 First release of Edu-API 1.0 Candidate Final Draft Document. Final 2026-10-01 Final Release".
- Cert guide revision history ([eduapi_cert.txt]): "Base Document 2022-05-22 First draft of Edu-API 1.0 cert document. Candidate Public Final 2025-03-12 Candidate Final draft of Edu-API 1.0 cert document. Candidate Public Final 2025-10-07 Bug Fixes Final 2026-10-14 Final Release version of t[he cert document]".
- Discrepancy: the 1EdTech standards page (https://www.1edtech.org/standards/edu-api [eduapi.txt]) still says "Edu-API is currently in Candidate Final Public status and moving towards the release of its first version." Any existing Edu-API certifications therefore predate the 14 October 2026 Final cert guide.

---

## 10. LIS (Learning Information Services)

### A. Referent
**URL:** https://www.1edtech.org/standards/lis [lis.txt]

> "1EdTech's Learning Information Services (LIS) specification defines how systems manage the exchange of information that describes people, groups, memberships, courses, and outcomes within the context of learning."

> "The LIS v2.0 can be implemented using a Web Services infrastructure (based on a SOAP http transport mechanism) and the Lightweight Directory Access Protocol (LDAP)."

### B. What certification tests
Same page: "Core Profiles & Conformance Specification - a set of profiles of the LIS specification has been created. The Core Profiles identify the minimal subset of the functionality that must be supported by systems developed for deployment in HE. ... Each profile contains its Conformance Specification against which compliant systems are tested"

**URL:** https://www.imsglobal.org/node/52416 (LIS Best Practice and Implementation Guide) [lis_impl.txt], section 7.3:

> "An implementation of an LIS system is expected to accurately complete a LIS Implementation Matrix (see Appendix E) and a Conformance Statement (see Table 7.2 for the format). The Conformance Statement lists the level of compliance claimed for each of the behaviors defined within the LIS specification. Interoperability between two systems is then identified by comparing their Conformance Statements"

Section 7.5: "For the LIS, compliance and certification will be against an appropriate profile ... Organizations wishing to obtain certification must become members of the LIS Alliance".

**URL:** https://www.imsglobal.org/node/52401 (LIS 2.0.1 spec) [lis_spec.txt]: "Core Profile & Conformance Specification - the Core Profile defines the minimal subset of the functionality that must be supported by systems developed for deployment between a Student Information System and a Learning Management System."

### C. Independent check of the referent
As OneRoster and Edu-API (SIS to LMS). No further text found.

### D. Version and certification dates
- "1EdTech Learning Information Services Specification Version 2.0.1 Final Release Date Issued: 30 September 2013" ([lis_spec.txt]).

---

## 11. Comparison only: xAPI (ADL; IEEE 9274.1.1)

### A. Referent
**URL:** https://raw.githubusercontent.com/adlnet/xAPI-Spec/master/xAPI-About.md [xapi_spec.txt]

> "The Experience API (xAPI) is a technical specification that aims to facilitate the documentation and communication of learning experiences. It specifies a structure to describe learning experiences and defines how these descriptions can be exchanged electronically."

> "The most significant object within the xAPI data model is the "Statement" object. This specification defines the properties of the Statement object (including "Actor", "Verb", "Object", "Result", and "Context") and the rules of syntax for the values of those properties"

**URL:** https://standards.ieee.org/ieee/9274.1.1/7321/ [ieee9274.txt]

> "This Standard describes a JavaScript Object Notation (JSON) data model format and a Representational State Transfer (RESTful) Web Service Application Programming Interface (API) for communication between Activities experienced by an individual, group, or other entity and a Learning Record Store (LRS)."

### B. What conformance tests; provenance
**URL:** https://raw.githubusercontent.com/adlnet/lrs-conformance-test-suite/master/README.md [lrs_conf_gh.txt]

> "This is a NodeJS project that tests the 'MUST' requirements of the xAPI Spec, determined by the governing documents for the various versions of the xAPI Spec."

The suite tests the LRS (the receiving store), not the activity providers that write statements.

**URL:** https://raw.githubusercontent.com/adlnet/xAPI-Spec/master/xAPI-Data.md [xapi_data.txt], Statement properties table and section 2.4.9:

> "authority Object Agent or Group who is asserting this Statement is true. Verified by the LRS based on authentication. Set by LRS if not provided or if a strong trust relationship between the Learning Record Provider and LRS has not been established."

> "The authority property provides information about whom or what has asserted that this Statement is true."

> "The LRS MAY leave the submitted authority unchanged but SHOULD do so only where a strong trust relationship has been established, and with extreme caution."

The same document defines "2.6 Signed Statements" (X.509 signatures; example only read, not the full requirements).

### D. Dates
IEEE page lists "IEEE 9274.1.1-2023" with dates "2018-05-14", "2023-03-30" and "Published: 2023-10-06", and an adopted "ISO/IEC/IEEE International Standard ... Part 1-1:xAPI using JSON serialization and RESTful data transport" (39274-1-1-2025). ADL project pages (adlnet.gov) did not load (connection failure).

---

## 12. Comparison only: Ed-Fi

**URL:** https://docs.ed-fi.org/partners/certification/ [edfi_docs.txt] (the ed-fi.org marketing pages tried returned 404).

### B and C. What certification tests and what it does not establish

> "Ed-Fi certification is a technical verification that a product conforms to an Ed-Fi API specification for a specific Ed-Fi Data Standard version. A certified product has shown that it: Implements the API specification, or can communicate with an implementation of it as a client, across all resources and fields marked "required" Meets all of the "must" requirements in the API specification Meets all of the "must" requirements of the certification itself"

> "Certification does not establish: Plug-and-play interoperability in every deployment. Local configuration, customizations, and business logic (for example, how a school counts attendance) still vary. ... Perfect semantic consistency in how a vendor maps its data to Ed-Fi definitions, since mapping always involves some interpretation."

> "Q: Does certification guarantee plug-and-play interoperability? No. Conformance is necessary for interoperability but not sufficient on its own."

> "A district in a supported region, using the certified data model on a recent supported version, can raise gaps with the Ed-Fi Alliance, which reviews them with the vendor. If gaps cannot be resolved, the vendor's certification no longer applies in that region."

### A. Referent (from the same page)
> "The Student Information Systems, Assessment Outcomes, and Domain API certifications are currently available for Data Standard v4 and v5"

### D. Dates
> "Certifications are valid for one year and are renewed through re-certification."
Start date of Ed-Fi certification: not on the page opened.

---

## 13. 1EdTech 2026 public draft: Trusted Portable Learning Context (TPLC)

**URL:** https://standards.1edtech.org/publications/rfc-trusted-contextv2 [tplc_rfc.txt]. "Trusted Portable Learning Context v1.0.1 · Public Draft"; "Published May 26, 2026"; "Author Tim Couper - Chief Architect (1EdTech)"; changelog entry "1.0.1 2026-07-20". Landing page: https://www.1edtech.org/ai/tplc [tplc.txt] ("1EdTech has released a Request for Public Comment on the principles of a trusted portable learning context").

Status:
> "This is a Public Comment Draft positioned as a principles paper. ... This document is non-normative."

On what existing standards do:
> "Traditional learning-data interoperability moves records between source systems and authoritative consumers. Agentic workflows demand something different: a runtime, composable, governed structure that any agent can read, verify, and act on without re-deriving consent, inference, or sovereignty rules each time."

> "A tplc is not a data standard in the traditional sense. It does not replace OneRoster, Caliper, CASE, OpenBadges, the Comprehensive Learner Record (CLR), or any other 1EdTech specification. It does not replace interoperability between systems of record, such as the data exchange between a Student Information System (SIS) and a Learning Management System (LMS)."

> "That contract serves system-of-record interoperability well. It cannot, in its current form, deliver a moment-bounded, learner-bounded context to an AI agent at the moment of action, nor carry that context safely from one agent to another."

Meaning of "trusted":
> "A learning context is trusted when the data came from authoritative sources, the institution's consent and disclosure policies were applied before the context was released, the context describes a real situation at a real time, and, where the use case requires it, the context can be verified by the recipient."

Provenance (section 4.3):
> "When a use case requires it, a tplc can be cryptographically signed so that a downstream consumer can verify who compiled the context, from which sources, under which policy, and at what time. Provenance is an optional layer because not every use case justifies its operational cost: a low-risk in-product AI assistant inside a single LMS may not need a signed context, while a cross-institutional credential decision almost certainly does. The candidate signing approach, based on W3C Verifiable Credentials Data Integrity, is described in Part 2, Section 11."

On inferred versus system-of-record facts (section 2.6):
> "In a memory store, every line of text looks the same to the consumer. There is no built-in way to distinguish a fact retrieved from an institutional system of record from a fact inferred or hallucinated by an upstream agent. A tplc keeps that distinction explicit, so a downstream agent can tell which data carries institutional authority and which is the residue of another agent's reasoning."

Realtime (section 4.4):
> "realtime compilation prevents it by ensuring that what an agent sees is what is true now, subject to the time bounds the institution attaches."

What the current stack cannot do (section 3.2):
> "It cannot, without bespoke engineering, do any of the following: compile a learner-and-moment-bounded view across multiple sources at the moment of action, apply institutional disclosure policy at the point of release, attach the consent that authorized the release to the artifact itself, or make the resulting artifact verifiable to a third-party agent."

---

## 14. Scholarly texts on what a badge means

**Ahn, J., Pellicone, A. and Butler, B. S. (2014). "Open badges for education: what are the implications at the intersection of open systems and badging?" Research in Learning Technology 22: 23563. https://doi.org/10.3402/rlt.v22.23563** (PDF opened: https://journal.alt.ac.uk/index.php/rlt/article/download/1510/pdf_1 ; [dl/rlt2014.pdf])

> "The ability for individuals to interpret and re-appropriate different badges for their own use may widen and diversify the recognition of learning across multiple settings. However, the same openness of interpretation may work to inhibit the usefulness of a badge as a credential. For example, a small community of practice (e.g. an after-school program or an online community) may interpret and value a given badge one way while employers do so in an entirely different fashion. Thus, the same badge may be valued internally as a signal in a small community, but be less effective as a credential in the broader, open community."

> "Learners may be more likely to pursue and earn badges if they are seen as credible artefacts, issued by trusted institutions and utilized by other stakeholders such as employers as vital elements of one's credentials."

Table 1 research questions include: "How important is the source of the badge to an employer or other interested party wishing to appraise the knowledge/skills acquired by the learner?" and "What will it take for badges to gain credibility and status as credentials among learners and other interested parties?" (cells reassembled from the PDF's two-column table; wording verbatim).

**Trepulė, E., Volungevičienė, A., Teresevičienė, M., Greenspon, R. and Costa, N. (2021). "How to Increase the Value of Digital Badges for Assessment and Recognition in Higher Education. A University Case." Informatics in Education 20(1): 131-152. https://doi.org/10.15388/infedu.2021.07** (PDF opened: https://infedu.vu.lt/journal/INFEDU/article/677/file/pdf ; [dl/infedu2021.pdf])

> "teachers at universities lack knowledge, procedures, or trust in DB development and face challenges (Kehoe and Goudzwaard, 2015; Waters, 2013), especially in the assessment strategy and recognition of the knowledge or skills that their students achieve."

Interview quote reported in the paper: "...very often, a person who is dealing with the recognition may not see the entire process of assessment and of awarding credentials, yet they know that they trust their end product" (I.7). Followed by the authors: "If information is a DB description metadata and evidence can be presented, it builds confidence in the assessment."

Interview quote: "...for learning to be recognized and to be assessed, you need to relate it to qualification frameworks that exist, that ensure trust, ensure standardization". (I.11)

---

## 15. Gaps and pages not obtained

- HTTP 403 (not retried): CASE conformance page; Common Cartridge 1.4 spec, cert guide and conformance-testing process; Caliper conformance page. The W3C VC Data Model 2.0 page (w3.org) also returned 403; the OB 3.0 and CLR 2.0 specs restate its verification language (sections 3B and 4B).
- Not opened: QTI 3 Conformance and Certification document; OneRoster 1.2 cert guide (https://www.imsglobal.org/spec/oneroster/v1p2/cert/); certification test-suite applications themselves (they need member login).
- First-certification dates per standard were not stated on any page opened; section D gives spec and cert-guide release dates only. Earliest dates found: CC 1.0 Final 29 Jan 2009; LIS 2.0.1 30 Sep 2013; CASE 1.0 7 Jul 2017; OB 2.0 cert guide 12 Apr 2018; LTI 1.3 16 Apr 2019; Caliper 1.2 cert guide 27 Mar 2020; OneRoster 1.1 cert guide (rev.) 31 Dec 2020; CLR 1.0 cert guide 5 Feb 2021; QTI 3.0 1 May 2022; Edu-API cert guide Final 14 Oct 2026 (Candidate Final from 12 Mar 2025).
- No 1EdTech text was found that tests whether a message's content is true for any standard. The explicit statements on that point are OB 3.0 section 9, CLR 2.0 section 8, and Ed-Fi's "does not establish" list.
