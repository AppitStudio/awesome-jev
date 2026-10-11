# VerdictKit

[All projects](../README.md) · [Web apps](README.md#web-apps)

Independent hosted playground and field guide for TypeSafe Jev: enter text or JSON state, define Choice, Score, or Noul questions, and inspect typed JSON responses and probabilities. Preset demo outputs are labelled as illustrations; live runs are labelled separately.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://verdictkit.com) |
| Tags | `Closed source` · `Freemium` · `Commercial` |
| Product homepage | [verdictkit.com](https://verdictkit.com) |
| Pricing and access | [Pricing](https://verdictkit.com/pricing): two free live runs per UTC day without signup or five with Google sign-in; paid Run Pack, Pro, and Batch plans add saved judges, history, CSV export, and batch files. VerdictKit does not resell API keys or credits. Checked 2026-10-11. |
| Jev evidence | Public [JSON response guide](https://verdictkit.com/json) and homepage document Jev Choice/Score/Noul request and response shapes; vendor states live runs relay to the hosted Jev API. Closed source — implementation not inspected. |
| Disclosure | Closed source: implementation not inspected; review limited to public pages. Commercial: paid plans offered. Self-submitted by the VerdictKit operator through JevList ([issue #1344](https://github.com/AppitStudio/awesome-jev/issues/1344)); not affiliated with TypeSafe AI. AI-assisted catalog review. Listing is not an endorsement. Live runs not executed on the review host. |
| Maintainer | VerdictKit (operator). Independently curated. |
| Format | Hosted web app |
| Platform and availability | Web browser. |
| Jev's role | Core: live runs send your state and questions to Jev and display the typed result. |
| Requirements | Browser; Google account for the larger free allowance or paid plans. |
| License | Closed source. |

## When to use

- Try Jev Choice, Score, and Noul questions on your own text before writing integration code.
- Mismatch: not a local inference tool or API gateway; use your own TypeSafe or OpenRouter account for production integration.

## How it works

You build a request (state plus questions) in the browser; live evaluations pass through VerdictKit's server to the hosted Jev API, and the page shows the typed JSON and probabilities. Paid plans save question configurations as reusable judges and run CSV batches.

## Get started

Open [verdictkit.com](https://verdictkit.com), load an example or enter your own state and question, and run it.

## Limits and data handling

Live evaluations send the supplied state and questions through VerdictKit to the hosted Jev API. Free run content is not saved as history, per the vendor; paid history is retained until deleted. See the site's privacy terms. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) from the public homepage, JSON guide, and pricing page. Closed source; no live runs executed on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not product claims. AI-assisted review.
