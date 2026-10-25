# Dossier: Academic AI Solutions (Academic AI Solutions LLC)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentE

Retrieval note: the site is a JavaScript single-page app. curl of the HTML returns an empty shell; WebFetch of / and /platform returned only the page title. All page text below was read verbatim from the site's own JavaScript bundle (https://academicaisolutions.com/assets/index-ChPBupjF.js, fetched with curl), which holds the rendered strings for every route (/, /platform, /why-aas, /future, /licensing, /financial-impact, /team, /contact). Citations give the bundle URL.

## Identity
- What it is, in the vendor's words:
  - "A proprietary, patent-secured Institutional Intelligence and Coordination Layer, the only one of its kind in higher education." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "A four-layer system that preserves existing investments while delivering AI-powered coordination across your entire institution." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
- Self-description as "operating system":
  - Page title in the HTML: "Academic AI Solutions - The AI Operating System for Higher Education" (https://academicaisolutions.com/, accessed 2026-10-24; also returned by WebFetch)
  - Footer: "The patent-secured AI operating system for higher education." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- Student assistant and planning features (vendor claims; no product docs):
  - "Optimal course paths connected to career outcomes from day one" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "A persistent AI companion that knows the student, anticipates their needs, and connects them to the right resource at the right moment, at the scale of an entire institution." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "Flags risk before anyone else sees it and connects students to support instantly" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "AI-powered coordination through our patent-secured multi-agent architecture" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
- None found specifying whose tools learner activity is sequenced across.

## E2 Interfaces evidence
- Vendor claims only; no API reference, developer page or standards named:
  - "Secure connections to your existing systems of record" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - Systems listed: "SIS · LMS · CRM · ERP · Housing · Dining · Financial Aid · Career Services · Events · Athletics · Parking · Transportation · Health Services · Campus Safety · Payment Systems · Marketplace" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "Tailored integrations for institution-specific tools and workflows unique to your campus" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
- No mention of LTI, OneRoster, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge or Open Badges found. The footer "Wiki" link (/docs) is behind a login (see Gaps).

## E3 Learner model evidence
- Learner record (vendor description of a layer; no data model documented):
  - "A persistent learner record built to travel with the student across institutions, credentials, and life stages." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "Sovereign, portable, and verifiable." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - Future-page heading: "The Lifelong Learner Record" (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
- None found on mastery/skill/knowledge-state modelling, or on outside vendors writing into the record.

## E4 Data protection evidence
- None found. The footer "Privacy Policy" link points to "#" (no page): source string `{title:"Privacy Policy",href:"#"}` (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24). No FERPA, privacy, scope or permission text found in the bundle.

## E5 Third-party tools evidence
- Marketplace layer described as connecting outside parties (vendor claim):
  - "The institutional integration with the city and the broader economy around it." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
  - "Verified merchants, housing partners, dining, transportation, healthcare, and civic services connected to the institutional environment." (https://academicaisolutions.com/assets/index-ChPBupjF.js, accessed 2026-10-24)
- None found naming any independent third-party tool that runs on the platform.

## Gaps
- https://academicaisolutions.com/docs ("Wiki" in footer): 302 redirect to a Cloudflare Access login (academicaisolutions.cloudflareaccess.com); not accessible.
- https://academicaisolutions.com/sitemap.xml : 404
- /privacy, /privacy-policy, /terms return the SPA shell only (HTTP 200, no content); footer Privacy Policy, Terms of Service and Patent Disclosures links are "#".
- WebFetch of https://academicaisolutions.com/ and /platform returned only the title (JavaScript not rendered).
