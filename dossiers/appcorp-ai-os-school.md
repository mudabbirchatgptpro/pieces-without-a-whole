# Dossier: AI OS for School (App Corp)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentC (blocked) and frame51-coordinator (rendered-browser collection)

Collection note: the site returns a Cloudflare 403 challenge to curl and WebFetch. The quotations below were taken by the coordinating agent from the page text of a rendered Playwright browser session (document.body.innerText) on 2026-10-24 (UTC 2026-10-25). They are marked "(rendered browser)". The vendor is a software engineering agency in Lahore, Pakistan; AI OS for School is one of its two products (the other is "AI OS for Business").

## Identity
- What it is, in the vendor's words: "AI OS for School replaces disconnected tools with a single intelligent system: one platform that personalises every student's learning journey, automates routine admin, and gives leadership the real-time visibility to intervene before problems become failures." (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Self-description as "operating system"/"OS": page title "AI Operating System for School | App Corp"; heading "AI Operating System for School"; subheading "The intelligent backbone every modern school deserves" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Vendor description of itself: "A full-service software engineering agency trusted by startups, scale-ups, and enterprises across the US, UK, and EU." (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Use cases listed on the product page include "K-12 Schools", "Higher Education", "Corporate Training" and "Tutoring & EdTech Platforms" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)

## E1 Sequencing / scheduling evidence
- Feature heading "Personalised Learning Pathways": "AI builds a unique learning path for every student" followed by "adjusting pace, content format, and difficulty in real time based on performance signals, learning style, and engagement data." (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Higher-education use case: "Adaptive assessments calibrated to module learning outcomes" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- No documentation found on whose content or tools the pathways draw from.

## E2 Interfaces evidence
- Integration step: "We connect your existing SIS, LMS, and assessment platforms. Our team handles all data migration, validation, and historical data import" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Tutoring and EdTech use case: "Embed AI OS into your own platform as a white-label API." and "White-label AI tutoring engine via REST API" and "Student performance webhooks for real-time personalisation" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Enterprise pricing tier lists "Custom integrations & API access" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- No public developer documentation found. No open standard (LTI, OneRoster, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge, Open Badges) is named on the product page or the compliance page.

## E3 Learner model evidence
- Feature heading "Early Intervention Analytics": "AI identifies at-risk students weeks before they fail. Engagement scores, attendance patterns, assessment trajectories, and behavioural signals are synthesised into actionable alerts for teachers and pastoral leads." (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- Pro tier lists "Advanced academic analytics & GPA calculation" (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- No documentation found of a mastery or knowledge-state model, or of outside tools writing to one.

## E4 Data protection evidence
- Feature heading "Child Safety & FERPA/GDPR Compliance": "FERPA and GDPR compliant by design, with child-safe AI guardrails, granular data access controls, and full audit trails for regulatory requirements." (https://www.appcorp.org/product/ai-os-school, accessed 2026-10-24, rendered browser)
- The privacy policy covers the agency's website visitors and clients, for example: "When you contact us through our website, submit a project brief, or engage our services, we collect personal information that you voluntarily share" (https://www.appcorp.org/privacy, accessed 2026-10-24, rendered browser)
- Compliance page lists COPPA: "The US Children's Online Privacy Protection Act" followed by "regulating the collection of personal information from children under 13." (https://www.appcorp.org/compliance, accessed 2026-10-24, rendered browser)
- No per-tool or per-app permission documentation found.

## E5 Third-party tools evidence
- None found. The product page names no third-party tools running inside the product. The FAQ question "Does AI OS for School replace our existing LMS or SIS?" is shown, but its answer was not present in the page text (collapsed, not rendered).

## Gaps
- curl and WebFetch: HTTP 403 Cloudflare challenge on https://www.appcorp.org/product/ai-os-school, https://www.appcorp.org/, https://www.appcorp.org/sitemap.xml, https://www.appcorp.org/privacy-policy (agent C). Collected instead via rendered browser.
- FAQ answers on the product page not rendered in page text.
- "Download Prospectus" document not opened.
- No developer, API documentation, help center or integration directory found on the site (site navigation lists none for this product).
- Customer quotations on the product page (e.g. "Greenfield Academy", "LearnPath EdTech") not independently checked.
