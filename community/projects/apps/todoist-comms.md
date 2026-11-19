# Todoist Comms by Doist (team chat built into Todoist, with a Jev-powered inbox)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Team communication app from Doist, the company behind Todoist, and the successor to Twist (which retires in March 2027). Conversations are threads inside channels, plus private chats; any thread, comment or chat can become a Todoist task that stays linked to the conversation, and an inbox collects new activity to clear. It ships with an MCP server, a CLI, an API and an SDK. Doist's CEO lists a Jev-powered inbox among the public-beta features and earlier said the team was using the Jev decision model to classify the inbox.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://comms.todoist.com) |
| Tags | `Closed source` · `Pricing unverified` · `Commercial` |
| Product homepage | [comms.todoist.com](https://comms.todoist.com) |
| Pricing and access | Public beta, opened 2026-11-18. Doist's CEO says anyone with a Todoist account can start and that Todoist Business subscribers get Comms at no extra cost; Doist's help center says adding a member on a Business plan adds a paid seat. No separate Comms price page was found; Todoist plan prices are on [todoist.com/pricing](https://www.todoist.com/pricing). Checked **2026-11-19**; sign-up was not tested. |
| Jev evidence | Vendor claim: Doist founder and CEO Amir Salihefendić listed "a Jev-powered inbox" in the [public-beta announcement](https://x.com/amix3k/status/2123070438322397663) on 2026-11-18, after writing on 2026-10-23 that the team was experimenting with inbox classification using the Jev decision model. The help center and app pages did not mention Jev when checked. The implementation was not inspected. |
| Disclosure | Closed source, commercial product in beta. Source was not inspected; Jev use is the vendor's public claim, not independently observed API traffic. Independently curated for Awesome Jev; no affiliation or commercial relationship with the vendor. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/amix3k/status/2123070438322397663)). |
| Maintainer | [Doist](https://doist.com) (announced by [Amir Salihefendić](https://x.com/amix3k), founder and CEO). |
| Format | Hosted team chat with web, desktop and mobile apps, plus MCP server, CLI, API and SDK. |
| Platform and availability | Web, macOS, Windows, iOS and Android (public beta). |
| Jev's role | Vendor claim: Jev classifies inbox activity to decide what to surface first. Which other features (such as suggested tasks) use Jev or other models was not stated. |
| Requirements | A Todoist account; a Todoist Business plan for paid team seats. |
| License | Proprietary hosted service. No public repository found. |

## When to use

Use Todoist Comms if your team already runs on Todoist and wants threads that end in decisions and linked tasks, with an inbox that sorts what needs you. It is a commercial product, not a library. Mismatch: if you need to inspect or self-host the inbox logic, or need many built-in third-party integrations (Doist's FAQ says there are none yet).

## How it works

You post threads in channels and tag the people who should be notified; new activity lands in your inbox, and decisions become Todoist tasks linked back to the thread. According to Doist's CEO the inbox is Jev-powered, using the decision model to classify activity. No API calls, question schemas or thresholds were observed for this listing.

## Get started

This path follows Doist's public help center; it was not executed (no sign-up).

1. Open [comms.todoist.com](https://comms.todoist.com) and sign in with your Todoist account.
2. Follow Doist's [getting started guide](https://www.todoist.com/help/comms/get-started/get-started-with-todoist-comms-uU7zyeiXn) to invite your team and create channels.
3. Post a first thread and turn a follow-up into a Todoist task.

## Examples and demos

- [Public-beta announcement with a demo video](https://x.com/amix3k/status/2123070438322397663) (vendor material; video not reproduced).
- [Todoist Comms beta on TestFlight](https://testflight.apple.com/join/2XXEdZZu).

## Limits and data handling

Closed source: the inbox classification, the questions asked of Jev and any thresholds were not inspected. Team messages are processed by Doist and, per the vendor, by Jev for inbox classification; check Doist's privacy terms before moving sensitive conversations. Beta software; features may change.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) with AI assistance. Primary sources: the CEO's [X post](https://x.com/amix3k/status/2123070438322397663) (2026-11-18), Doist's [getting started guide](https://www.todoist.com/help/comms/get-started/get-started-with-todoist-comms-uU7zyeiXn) and [comms.todoist.com](https://comms.todoist.com) (fetched 2026-11-19). No sign-up or live use. Catalog de-dupe found no existing Todoist listing.
