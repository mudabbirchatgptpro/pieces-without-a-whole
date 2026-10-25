# Frame 5.1 search log: self-described operating systems

Stratum rule (PREREGISTRATION.md section 5.1): every product whose own website describes it as an "operating system" (or "OS") for learning, for schools or for education, found by six fixed searches run 24 to 26 October 2026. Corporate-training-only products excluded.

Collector: frame 5.1 coordinating evidence agent. Searches run 2026-10-24 (US local date; some browser logs carry the UTC date 2026-10-25).
Tool: WebSearch (US index). Scratch files: study/dossiers/_scratch_51/.

## 1. Queries run

WebSearch has no "next page" control. "Two pages deep" was approximated as follows: run 1 = standard mode; run 2 = extended mode (the tool's thorough, fresh search); run 3 = standard mode repeated with every domain already returned in runs 1 and 2 blocked, so that the next tier of results surfaces. This approximation is a deviation in mechanics from a literal page 2 and is recorded here.

| # | Exact query | Run | Mode | Notes |
|---|---|---|---|---|
| Q1 | "operating system for schools" | 1 | standard | 9 results, mostly Red Hat 2000 press release copies |
| Q1 | "operating system for schools" | 2 | extended | 9 results |
| Q1 | "operating system for schools" | 3 | standard, prior domains blocked | 8 results |
| Q2 | "learning operating system" | 1 | standard | 9 results, all "learn about operating systems" courses |
| Q2 | "learning operating system" | 2 | extended | 9 results, same sense |
| Q2 | "learning operating system" platform K-12 OR students OR schools | 3 | standard, prior domains blocked | Disambiguating terms added because the bare phrase returned only CS-course results in runs 1 and 2; recorded as a deviation |
| Q3 | "AI operating system" schools | 1 | standard | 9 results |
| Q3 | "AI operating system" schools | 2 | extended | 9 results |
| Q3 | "AI operating system" schools | 3 | standard, prior domains blocked | 9 results |
| Q4 | "education operating system" | 1 | standard | 9 results, teaching kernels and Linux distributions |
| Q4 | "education operating system" | 2 | extended | 9 results |
| Q4 | "education operating system" | 3 | standard, prior domains blocked | 8 results |
| Q5 | "school OS" | 1 | standard | 9 results |
| Q5 | "school OS" | 2 | extended | 9 results |
| Q5 | "school OS" | 3 | standard, prior domains blocked | 9 results |
| Q6 | "OS for learning" | 1 | standard | 9 results |
| Q6 | "OS for learning" | 2 | extended | 9 results |
| Q6 | "OS for learning" | 3 | standard, prior domains blocked | 9 results |

Supplementary searches (to locate the OS page on known candidates' own sites, not to add candidates):
- `kiddom "operating system"` restricted to kiddom.co
- `SchoolAI "operating system"` restricted to schoolai.com
- `Involve OS "operating system for modern schools"`

Known candidates from earlier scans (task instruction): MagicSchool, Kira Learning, Knomadix, SchoolAI, Blended OS, ibl.ai, Kiddom, Timeback/Alpha. Timeback is assigned to stratum 5.2 and was skipped here. Of the others, MagicSchool, Knomadix, Blended OS, Kira and ibl.ai also surfaced in the fixed queries above (Q3, Q5); Kiddom surfaced in Q1 run 3 and Q2 run 3 (through a Medium essay, then confirmed on kiddom.co); SchoolAI did not surface in any fixed query.

## 2. Verification method

A search hit was never taken as evidence. Each candidate's own live page was opened (curl to text, or a Playwright-rendered page for JavaScript sites) and searched for "operating system", "OS" or "AiOS". Inclusion required the self-description on the vendor's own live page, in the school, learning or education sense. Where a product's name itself contains "OS" for a school product (for example "SchoolOS"), that name was treated as an "OS" self-description under the rule's "(or 'OS')" clause; these cases are flagged below so the author can reverse them.

## 3. Candidates and decisions

### Included (26)

| Slug | Product (vendor) | Surfaced by | Live page and self-description seen (2026-10-24) |
|---|---|---|---|
| magicschool | MagicSchool (Magic School, Inc.) | Q3 r1, r2; known list | https://www.magicschool.ai/ai-operating-system-for-schools : "The AI Operating System for Schools" |
| kira-learning | Kira (Kira Learning) | Q3 r3; known list | https://www.kira-learning.com/ : "The AI operating system for education" |
| knomadix | Knomadix AI OS (Knomadix) | Q3 r1 (k12dive press release); known list | https://www.knomadix.ai/ : "The AI Operating System for Learning and Education" |
| blended-os | Blended OS (Blended) | Q3 r1 summary, Q5 r3; known list | https://www.get-blended.com/ : "The AI School Operating System" |
| ibl-ai | ibl.ai Agentic OS (ibl.ai) | Q3 r3; known list | https://ibl.ai/solutions/k-12 : "Agentic AI Operating System for K-12"; https://ibl.ai/solutions/higher-education : "Agentic AI Operating System for Higher Education". Vendor also sells to corporate and other sectors; included because it has dedicated K-12 and higher-education offerings (not corporate-training-only) |
| kiddom | Kiddom (Kiddom, Inc.) | Q1 r3, Q2 r3 (Medium essay); known list | https://www.kiddom.co/impact/from-curriculum-investment-to-systemic-impact : "It is the instructional operating system that turns curriculum investment into controlled, repeatable, and equitable outcomes." The homepage (https://www.kiddom.co/) carries no OS wording |
| string-os | String OS (String) | Q3 r2 | https://string.education/en/schools : "The operating system for your school" |
| spyral-aios | anAIza School / AiOS (SPYRAL) | Q3 r2 | https://tryspyral.com/school : "The World's #1 AI Operating System for Schools" |
| kiinara-os | Kiinara OS | Q3 r2 | https://www.kiinaraos.com/ : "The AI Operating System for Education" |
| appcorp-ai-os-school | AI OS for School (App Corp) | Q3 r2 | https://www.appcorp.org/product/ai-os-school (Cloudflare 403 to curl; opened in rendered browser): "AI Operating System for School" |
| skodle | skodle | Q3 r1 (Product Hunt listing) | https://skodle.com/ : "The AI-powered operating system for schools." |
| schoolos-ai | SchoolOS (schoolos-ai.com) | Q1 r2, Q5 r2 | https://schoolos-ai.com/ (rendered): "The Operating System for Modern Schools" |
| schoolware | SchoolWare | Q1 r2 | https://schoolware.io/ : "The school operating system" |
| schoolos-systems | SchoolOS Institutional Operating System (schoolos.systems) | Q1 r2 | https://www.schoolos.systems/landing : "The Operating System for Modern Schools" |
| edunation-os | EdunationOS (Edunation) | Q1 r3, Q2 r3 | https://edu-nation.net/edunation-os/ : "The operating system that runs your school" |
| apkaos | ApkaOS | Q1 r3 (blog URL); homepage checked | https://www.apkaos.com/ : "The AI-Powered Operating System for Modern Schools." |
| schoolos-net | SchoolOS (schoolos.net) | Q5 r2 | https://schoolos.net/ : "The Operating System for Modern Schools" |
| schoolos-live | SchoolOS (schoolos.live) | Q5 r3 | https://www.schoolos.live/ : page title "SchoolOS – The System Modern Schools Operate On". FLAG: inclusion rests on the product name "SchoolOS" |
| os-for-schools | OS FOR SCHOOLS (Ghana) | Q5 r3 | https://osforschools.com/ : "Complete School Operating System" |
| theschoolos | schoolOS (School Operating System, Inc.) | Q5 r3 | https://www.theschoolos.com/ : product name "schoolOS"; footer "School Operating System, Inc."; tagline "Operational Intelligence for K-12". FLAG: inclusion rests on the product and company name; product is a district operations and support platform |
| odoo-schoolos | SchoolOS for Odoo (Binary Bridge Technology Services) | Q5 r1 | https://apps.odoo.com/apps/modules/19.0/schoolos_base : "SchoolOS: Core (Base)" (the original separates the two parts with a dash character, rendered here as a colon per the no-em-dash rule). FLAG: inclusion rests on the product name; it is an add-on module for Odoo ERP |
| academic-ai-solutions | Academic AI Solutions | Q3 r3 | https://academicaisolutions.com/ (rendered): "The AI Operating System for Higher Education" |
| edmo | EDMO | Q3 r3 | https://goedmo.com/ : "The AI Operating System for Higher Education" (admissions and enrollment) |
| shoofly-ai | ShooflyAI, education offering | Q3 r3 | https://shooflyai.com/education/ : "AI Operating System for Education". Vendor serves several industries; the education page is a dedicated schools and colleges offering |
| scoolio | Scoolio | Q4 r2 (blog URL); homepage checked | https://scoolio.io/ : "AI-Powered Education Operating System" |
| learning-os | Learning OS (learningos.app) | Q6 r2 | https://www.learningos.app/ : "An operating system for educators, families, and lifelong learners". FLAG: the products listed are printable Canva/PDF planning resources, not software |

### Excluded (with reason)

Known-list candidate:
- SchoolAI (schoolai.com). No OS self-description found on the live homepage (https://schoolai.com/) or school-leaders page (https://schoolai.com/school-leaders); a site-restricted search for "operating system" surfaced only a schema.org `"operatingSystem":"Web"` metadata tag, which is a software-category field, not a self-description. Reason: no OS self-description on own live page. (SchoolAI remains in stratum 5.3.)
- Timeback / Alpha School. Assigned to stratum 5.2 by instruction; not assessed here.

Vendor products whose OS page could not be confirmed live:
- Involve OS (Involve Education, involveeducation.com). https://involveeducation.com/products/os returns 404 (its page title reads "Involve: The operating system for modern schools" (dash rendered as colon), the site default title on the error page); the live homepage carries no OS wording. Reason: no live product page with the self-description.
- Toppr School OS (toppr.com). https://www.toppr.com/ and https://www.toppr.com/school-os/ failed (curl no response; browser ERR_CERT_DATE_INVALID). Only a LinkedIn showcase was found, which is not the vendor's own website. Reason: vendor page could not be opened.
- Skolrai (skolrai.com). DNS does not resolve (curl and browser). Reason: vendor page could not be opened.
- Skoolza (skoolza.com). Live homepage (rendered) reads "One card. Every door."; no OS wording found. Reason: no OS self-description on live page.
- School OS (Estonia; pitchbook, crunchbase, hundred.org). Listed as out of business; no vendor site surfaced. Reason: defunct, no own website.
- SchoolOS School ERP (Siji Technologies; Google Play app and sites.google.com page). Only an app-store listing and a Google Sites page surfaced; not opened as a vendor product site with OS wording. Reason: no vendor website with the self-description found (app-store listing only). FLAG for author: could be revisited.
- ShaalaOS (contra.com portfolio). Designer's portfolio concept, not a product. Reason: not a product.

Computer operating systems (device, desktop or teaching kernels). Excluded because they are operating systems in the computing sense (software that runs the hardware), not products describing themselves as an OS for schools in the platform sense the study tests. FLAG for author: this is an interpretive exclusion; reverse if the frame is meant to be literal.
- Windows 11 Education / Windows 11 SE (microsoft.com, intel.com)
- Endless OS (endlessglobal.com)
- Zorin OS Education (zorin.com)
- The Linux Schools Project / Karoshi (wikipedia; linuxschools.com did not load)
- Debian Edu / Skolelinux, Edubuntu, Puavo, LliureX, PrimTux, OLPC XS, KITE IT@School (Kerala), NCERT SchoolOS live DVD (zyxware.com, soft112.com), Red Hat Linux for schools (redhat.com 2000 release), ChromeOS
- Teaching kernels: eXpOS, MiniOS, OSP, TOS, eduOS-rs, MentOS, PortOS, xv6, Minix, Xinu, Pintos, EOS Project

Not products (articles, guides, courses, listings):
- Essays and commentary: hprtechchief.substack.com "Can AI become a school's operating system?"; gettingsmart.com 2024 essay; medium.com "The Case for a K-12 School Operating System"; michaelbhorn.substack.com Kira profile; osforyour.business explainer; picovoice.ai and hatchworks.com AI OS explainers; apkaos.com and scoolio.io blog guides (their products are included separately); ibl.ai book chapter (product included separately)
- Courses, books and OS-learning guides: careerkarma, opencourser, placementpreparation, careers360, coursera, udemy, edx, ucertify, freecodecamp, scaler, netacad, oreilly, dominikrys.com, AWS builder, LinkedIn advice, laptopmag, quora, stonegroup.co.uk, convergetp.co.uk, tecmint, nces.ed.gov survey, prrcomputers, fluentin3months, homepage.net, glasp.co "Learning OS" article, dev.to posts
- Academic papers and patents: arxiv, acm, ncbi, uspto, academia.edu, mahidol repository, kaznpu bulletin, dlsu thesis archive, simmons wiki
- Unrelated: Tracxn "School OS" profile (slot-game company), Oakland School for the Arts, Open-space learning (Wikipedia), SchoolTool (open-source SIS; no OS self-description in result), Cengage Explore and Moodle K-12 and other LMS round-ups (no OS self-description; LMSs belong to stratum 5.2), Microsoft K-12 showcase page

Corporate-training-only exclusions: none encountered.

## 4. Counts

- Distinct product candidates assessed (vendor products, known-list items, and computer operating systems; excluding articles, courses, papers and unrelated hits): 26 included + 7 vendor-product exclusions (SchoolAI, Involve OS, Toppr School OS, Skolrai, Skoolza, School OS Estonia, SchoolOS Siji ERP) + 1 not-a-product (ShaalaOS) + 1 reassigned (Timeback) + 26 computer operating systems and teaching kernels (14 device or desktop OSes, 12 teaching kernels).
- Included: 26.
- Excluded vendor or platform products: 8 (the seven above plus ShaalaOS); computer operating systems excluded as a class: 26 items; Timeback skipped (stratum 5.2).
