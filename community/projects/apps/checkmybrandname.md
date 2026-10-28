# CheckMyBrandName (free brand-name checker where rules gather evidence and Jev judges what rules can't)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free web app, no sign-up, that tests a proposed brand name for spelling and pronunciation, distinctiveness and trademark strength, meaning in six languages, naming fashions, unwanted associations and availability across 22 domain extensions, and gives separate name and availability scores. Rules collect the evidence and Jev judges what rules cannot, such as whether listeners in the US, UK, Canada and Australia would spell the name right; report sentences are written in advance. Also usable from AI agents through a no-key MCP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://www.checkmybrandname.com/) |
| Tags | `Closed source` · `Free` |
| Product homepage | [checkmybrandname.com](https://www.checkmybrandname.com/) |
| Pricing and access | Free, no sign-up and no API key on the public site and the MCP endpoint, with usage limits applied per IP address (limits not measured). Checked **2026-10-28**. |
| Jev evidence | Live homepage copy ("How scores work"): "Rules collect the evidence; Jev, an AI model that answers with probabilities instead of text, judges what rules cannot", and the pronunciation and radio test says "Jev answers for listeners in the US, the UK, Canada and Australia." The maker's launch post on X ([post](https://x.com/LukasvanUden/status/2115430043362918864)) says it was built with Jev. Implementation was **not** inspected (no public source); TypeSafe API traffic was **not** captured on the review host. |
| Disclosure | Closed source. Jev use is a claim from the live site and the maker's X post, not independently observed System One calls. AI-assisted catalog review; no affiliation with the maker. Listing is not an endorsement. Discovered via X ([post](https://x.com/LukasvanUden/status/2115430043362918864)). |
| Maintainer | Lukas van Uden (named as provider in the site's [imprint](https://www.checkmybrandname.com/imprint); X [@LukasvanUden](https://x.com/LukasvanUden)). Independently curated. |
| Format | Hosted web application with an MCP server (`https://www.checkmybrandname.com/api/mcp`). |
| Platform and availability | Web browser; MCP clients such as Claude Code, Codex and Cursor. HTTP 200 on review. |
| Jev's role | Vendor claim: Jev answers the judgment questions in the scoring, for example pronunciation and spelling by listeners, while rules and registry lookups handle the rest. |
| Requirements | A modern browser, or an MCP client for agent use. |
| License | Proprietary hosted product; no public repository. |

## When to use

- Screen a shortlist of startup or product names before paying for trademark advice.
- Mismatch: a screen, not a legal clearance; the site itself says to check trademarks and ask native speakers.

## How it works

Per the public site: rules and registry lookups collect evidence (domain availability for 22 extensions, known brands, naming-fashion lists drawn from about 6,300 startup names, cross-language word lists), Jev judges the questions rules cannot, and fixed report sentences explain each score. Serious problems such as a vulgar reading cap the score. Question schemas and thresholds were not inspected.

## Get started

1. Open [checkmybrandname.com](https://www.checkmybrandname.com/) and enter a name, optionally with what it is for.
2. Or add it to an agent: `claude mcp add --transport http checkmybrandname https://www.checkmybrandname.com/api/mcp`, then ask "Check the brand name Velmora."

## Examples and demos

- Live product: [checkmybrandname.com](https://www.checkmybrandname.com/)
- Launch post with demo video: [x.com/LukasvanUden/status/2115430043362918864](https://x.com/LukasvanUden/status/2115430043362918864)

## Limits and data handling

Per the site, each checked name is kept with its scores, the country it was checked from, a daily-changing network code and the check's cost for one year; Jev answers are reused for 90 days, and IP addresses are held in memory for at most a day to apply limits ([privacy policy](https://www.checkmybrandname.com/privacy)). Names you check are processed by the site and its model providers.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia). Primary sources: live homepage, imprint and privacy pages (HTTP 200), and the maker's X launch post. AI-assisted curation; no account, key or paid feature was needed, and no automated checks were run against the service beyond loading the public pages. De-dupe: no existing Awesome Jev listing for checkmybrandname.com.

**X attribution:** `https://x.com/LukasvanUden/status/2115430043362918864`
