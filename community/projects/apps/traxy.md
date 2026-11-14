# traxy

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted B2B service that scans LinkedIn engagement across your market for people who fit your ideal-customer profile, enriches and ranks them, and runs LinkedIn and email outreach; the founder says lead qualification is powered by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://traxy.ai) |
| Tags | `Closed source` · `Paid` · `Commercial` |
| Product homepage | [traxy.ai](https://traxy.ai) |
| Pricing and access | [Pricing](https://traxy.ai/pricing): Pro $149/month, Advanced $399/month, Scale $1,099/month (billed monthly, 20% off yearly), with a 7-day free trial. Checked **2026-11-14**; checkout and trial terms were not tested. |
| Jev evidence | Vendor claim: the founder posted ["Introducing Jev @typesafeai powered lead qualification in traxy"](https://x.com/benbuaron_/status/2121283448258314533) on 2026-11-13, describing leads drawn from about 2.5 million LinkedIn engagements analyzed each week. The homepage and pricing page did not mention Jev when checked. The implementation was not inspected. |
| Disclosure | Closed source. Source was not inspected; Jev use is the vendor's public claim, not independently observed API traffic. Independently curated for Awesome Jev; no affiliation or commercial relationship with traxy. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/benbuaron_/status/2121283448258314533)). |
| Maintainer | [Ben Buaron](https://x.com/benbuaron_) ([@traxy_ai](https://x.com/traxy_ai)). |
| Format | Hosted web application with an agent chat ("trax"), lead lists, campaigns and integrations (Slack, Meta Ads and others). |
| Platform and availability | Public web product with sign-up and a free trial. A LinkedIn GTM MCP is advertised on the homepage; not checked. |
| Jev's role | Vendor claim: Jev qualifies leads, deciding which people from LinkedIn engagement fit your ICP and buying intent. Enrichment, research and message writing are separate features; which models power them was not verified. |
| Requirements | Account and paid plan after the trial; a LinkedIn and email setup for outreach. |
| License | Proprietary hosted service. No public repository found. |

## When to use

Use traxy if you sell B2B on LinkedIn and want a paid service to find people who recently engaged with relevant topics, rank them against your ICP and prepare outreach you approve. It is a commercial product, not a library. Mismatch: if you need to inspect or self-host the qualification logic, or if automated LinkedIn outreach conflicts with your policies.

## How it works

You describe who you want to reach. The service scans engagement (comments, likes) on LinkedIn across your market and on profiles you track, checks who fits, ranks leads by fit and intent, adds verified work emails, and on higher plans researches each lead and prepares LinkedIn and email sequences for approval before launch. The founder's post says the qualification step is powered by Jev; no API calls, question schemas or confidence handling were observed for this listing.

## Get started

This path follows the public site; it was not executed (no sign-up or trial).

1. Open [traxy.ai](https://traxy.ai) and start the 7-day free trial.
2. Describe your ideal customer and add profiles to track.
3. Review the qualified lead list before approving any campaign.

## Examples and demos

The founder's [launch post with a demo video](https://x.com/benbuaron_/status/2121283448258314533) shows the Jev lead-qualification feature; the video was not independently reproduced. The homepage lists case studies, which are vendor material.

## Limits and data handling

Closed source: qualification prompts, Jev questions and thresholds were not inspected. The service processes public LinkedIn engagement about third parties and sends messages on your behalf; check LinkedIn's user agreement and the privacy and anti-spam rules where you and your leads are. Performance figures in the founder's post (acceptance and reply rates) are vendor claims and were not verified.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) with AI assistance. Primary sources: [traxy.ai](https://traxy.ai) and [traxy.ai/pricing](https://traxy.ai/pricing) (both fetched 2026-11-14) and the founder's [X post](https://x.com/benbuaron_/status/2121283448258314533) (2026-11-13). No sign-up, payment or live use. Catalog de-dupe found no existing traxy listing.
