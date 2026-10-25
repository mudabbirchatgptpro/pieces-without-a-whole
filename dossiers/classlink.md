# Dossier: ClassLink (ClassLink, Inc.)
Frame stratum: 5.2   Evidence collected: 2026-10-24   Collector: evidence agent, stratum 5.2 (Claude Opus 5.5)

Note on sources: https://developer.classlink.com/ redirects to the partner help site https://help.classlink.com/s/classlink-partners-home, which renders client-side; those help pages were read in a browser.

## Identity
- "Create an environment where education and technology work together so learning can flourish. From access and analytics to cybersecurity and identity management, ClassLink's affordable and reliable solutions help you use technology in ways that promote and support learning." (https://www.classlink.com/, accessed 2026-10-24)
- "LaunchPad provides your entire institution with quick SSO access to a personalized portal of digital apps and resources" (https://www.classlink.com/products/launchpad, accessed 2026-10-24)
- Self-description as "operating system"/"OS": none found on the pages opened.

## E1 Sequencing / scheduling evidence
- No page opened describes ClassLink deciding or sequencing what a learner does next.
- Teacher-assigned app access: "My Classes is also a virtual backpack where students can see all of their classes and launch apps assigned by teachers to specific classes." (https://www.classlink.com/products/launchpad, accessed 2026-10-24)
- Usage analytics, not sequencing: "Education leaders can measure edtech usage and adoption across the entire school system and provide educators with a tool to see which students are disengaged and require intervention." (https://www.classlink.com/solutions/learning-analytics, accessed 2026-10-24)

## E2 Interfaces evidence
- "Connect your application to ClassLink for free using OneClick for single sign-on, Roster Server for rostering, or both. OneClick supports sign-in and authorized data access, while Roster Server provides OneRoster data shared by school systems." (https://help.classlink.com/s/article/pp-about-oc-rs, "Get started with ClassLink OneClick and Roster Server", dated Oct 19, 2026 on the page, accessed 2026-10-24)
- "ClassLink APIs support OAuth 2.0 for authentication and data access. After authentication, your application can request data through ClassLink APIs based on the scopes that have been authorized." (same URL, accessed 2026-10-24)
- "ClassLink Roster Server gives your application access to OneRoster® data shared by an enabled school system." and "They can also give your application programmatic access to class roster data through the REST API or provide uploaded OneRoster® CSV files." (same URL, accessed 2026-10-24)
- "Access roster data shared with your application by connecting directly to a school system's Roster Server using OAuth1 or through the ClassLink OAuth2 Proxy." (https://help.classlink.com/s/article/pp-access-rs-data, accessed 2026-10-24)
- The partner help home lists "Roster Server Request Libraries" for .NET, Python, Node, PHP, Java and Go, and SSO API endpoints "/v2/my/info", "/v2/my/students", "/v2/my/district", "/v2/my/profiles", "/my/groups" (https://help.classlink.com/s/classlink-partners-home, accessed 2026-10-24)
- "Support SAML/OAUTH/LTI for any vendor with no fees to vendors or your district" (https://www.classlink.com/products/roster-server, accessed 2026-10-24)
- Vendor states: "ClassLink Roster Server is certified by the 1EdTech Consortium to comply with the 1EdTech OneRoster® standard and the TrustEd Apps Seal of Data Privacy." (https://www.classlink.com/products/roster-server, accessed 2026-10-24). Not checked against the 1EdTech directory.

## E3 Learner model evidence
- Data described is roster and usage data: "Roster Server provides OneRoster data shared by school systems" (https://help.classlink.com/s/article/pp-about-oc-rs, accessed 2026-10-24); "Find a summary of logins, users, and engagement for each app for any time period, then drill down to view and compare those reports by building, grade level, classroom, and individual for deeper insights." (https://www.classlink.com/products/analytics, accessed 2026-10-24)
- No mastery, skill, outcome or competency record was found on the pages opened. No page opened describes OneRoster gradebook (results) exchange through Roster Server.

## E4 Data protection evidence
- "With Roster Server, school systems gain control over which data they choose to share." (https://www.classlink.com/products/roster-server, accessed 2026-10-24)
- "School systems can identify your application through its Roster Server connection and choose to provision access." (https://help.classlink.com/s/article/pp-about-oc-rs, accessed 2026-10-24); "The school system needs to grant your application access before you can retrieve its data." (https://help.classlink.com/s/article/pp-access-rs-data, accessed 2026-10-24)
- "Share only essential Personally Identifiable Information (PII) with vendor partners. Mask, replace, or substitute other key fields to secure sensitive student and staff data." (https://www.classlink.com/products/dataguard, accessed 2026-10-24)
- "DataGuard masks key fields like names and classes with dynamic alphanumeric scrambles, ensuring sensitive information stays secure." and "TrueView is a Chrome/Edge extension that lets authorized teachers and admins see student names in app dashboards while vendors receive masked data." (same URL, accessed 2026-10-24)
- "PAWs let your organization grant vendor partners temporary full visibility into the rostered data available to them when needed for testing, troubleshooting, or support." and "Setting a PAW to inactive immediately removes the vendor's access, even if the original expiration date has not yet been reached." (https://www.classlink.com/blog/partnering-with-classlink-sep-2026, accessed 2026-10-24)
- Scopes are mentioned ("based on the scopes that have been authorized", quoted under E2); no list of ClassLink scopes was opened.

## E5 Third-party tools evidence
- "Leading education technology providers such as Turnitin, Mackin, BrainPOP, and Renaissance Learning explain how integrating with ClassLink helps them offer affordable, easy-to-access learning solutions to schools." (https://www.classlink.com/company/partners, accessed 2026-10-24)
- "Learn why edtech vendors like Canva for Education, Khan Academy, Wakelet, SmartPass, and more choose ClassLink to quickly and securely deliver their apps and resources to learners and educators worldwide." (same URL, accessed 2026-10-24)
- "We connect to more than 6,000 digital learning resources, including publishers, reference providers, supplemental products, and learning management systems." (same URL, accessed 2026-10-24)
- "Partners pay nothing to integrate with our single sign-on and rostering platforms." (same URL, accessed 2026-10-24)
- Khan Academy states it receives rostering from ClassLink: "Khan Academy accounts who are part of a partner district in the Khan Academy Classroom program have access to automated rostering via Clever and ClassLink." (https://support.khanacademy.org/hc/en-us/articles/360031158952-How-does-automated-rostering-work-for-Khan-Academy-Districts-accounts, accessed 2026-10-24)
- Apps are reached by SSO launch from LaunchPad and by roster sync; no page opened describes third-party tools running inside ClassLink beyond launch.

## Gaps
- https://www.classlink.com/products/rostering returned 404.
- The DataGuard vendor-partner list on https://www.classlink.com/products/dataguard renders client-side; no vendor names were present in the served HTML.
- Partner help articles listing scopes, OneRoster versions and gradebook support (for example https://help.classlink.com/s/article/pp-oneclick-api-matrix) were not opened.
