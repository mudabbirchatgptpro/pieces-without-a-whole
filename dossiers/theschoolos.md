# Dossier: schoolOS (School Operating System, Inc.)
Frame stratum: 5.1   Evidence collected: 2026-10-24   Collector: frame51-agentE

## Identity
- What it is, in the vendor's words:
  - "schoolOS is the operational intelligence platform for K-12, powered by agentic AI." (https://www.theschoolos.com/, accessed 2026-10-24)
  - "schoolOS builds agentic AI for operations, not instruction." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
  - "Our agents work on assets, tickets, and procurement." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
- Self-description as "operating system"/"OS": the product name "schoolOS" and the company name in the footer. No sentence on the opened pages calls the product an "operating system".
  - "© 2026 School Operating System, Inc. All rights reserved." (https://www.theschoolos.com/, accessed 2026-10-24)

## E1 Sequencing / scheduling evidence
- The opened pages describe routing of support requests and operational workflows, not learner activity:
  - "schoolAgent answers common questions, creates requests when support is needed, and automatically routes work to the right team." (https://www.theschoolos.com/, accessed 2026-10-24)
  - "Requests are triaged automatically. Workflows advance on their own." (https://www.theschoolos.com/, accessed 2026-10-24)
  - "They never run on academic records, behavioral records, or anything that decides a student's outcome." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
- None found regarding sequencing of what a learner does next.

## E2 Interfaces evidence
- Integrations page (vendor-described; no public developer docs or API reference found):
  - "Every integration is one click. Scoped OAuth consent, read-only by default, and no API keys to manage." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "Four methods: manual CSV, flat CSV over SFTP, OneRoster bundle over SFTP, or the OneRoster API" (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "OneRoster 1.1 and 1.2, over OAuth 2, OAuth 1 or a static token" (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - ClassLink SSO: "Matches people by their OneRoster identifier, so a rostered district connects cleanly" (https://www.theschoolos.com/integrations, accessed 2026-10-24)
- No mention of LTI, Caliper, CLR, CASE, xAPI, Ed-Fi, QTI, Common Cartridge or Open Badges found on the opened pages.

## E3 Learner model evidence
- None found. The vendor states its agents do not use academic records:
  - "What they never touch Academic records Behavioral records Anything that decides a student's outcome" (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
  - "Our agents run on infrastructure and operational data, not academic or behavioral records about individuals." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)

## E4 Data protection evidence
- Per-connection scopes and write access (for the integrations schoolOS itself makes into district systems):
  - "Each integration requests only the scopes it actually uses, and you see exactly which ones before you approve." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "Connections start read-only. Write access is enabled per connection, and only when you turn it on." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "Every sync leaves an audit trail you can inspect." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
- Agent permissions and policy:
  - "Agents operate inside scoped permissions you control by role." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
  - "Student-connected data, like a device assigned to a learner, is used only for the purpose you authorize and honors FERPA's redisclosure limits." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)
  - "When a user chooses to sign in with their Google account, schoolOS requests only the following limited, non-sensitive OAuth scopes:" (https://www.theschoolos.com/privacy, accessed 2026-10-24)
- Vendor states memberships: "schoolOS is a member of the Student Data Privacy Consortium (SDPC), a special interest group of the Access 4 Learning (A4L) Community." (https://www.theschoolos.com/trust-privacy-and-security, accessed 2026-10-24)

## E5 Third-party tools evidence
- Integrations page names outside systems that schoolOS connects to (data sync and actions into those systems, not tools running inside schoolOS):
  - "Lock, wipe, or deprovision from the asset record instead of from three consoles." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "Write-back pushes schoolOS field values into Jamf, not just reads out of it" (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - "A fine in schoolOS becomes a student fee in MySchoolBucks" (https://www.theschoolos.com/integrations, accessed 2026-10-24)
  - Knowledge sources: "schoolOS brings documents and help articles into the knowledge base schoolAgent answers from, keeps them in sync as they change, and cites the source on every answer, so people get your district's answer instead of the internet's. Nothing is written back." (https://www.theschoolos.com/integrations, accessed 2026-10-24)
- None found of independent developers' tools running inside schoolOS, or of a marketplace.

## Gaps
- https://www.theschoolos.com/developers : 404
- https://www.theschoolos.com/api : 404
- https://docs.theschoolos.com/ , https://help.theschoolos.com/ , https://support.theschoolos.com/ : no response (DNS/connection failure)
- Pages opened: home, /platform, /integrations, /schoolagent, /trust-privacy-and-security, /privacy, sitemap.xml. No public API reference, developer portal or help center found.
