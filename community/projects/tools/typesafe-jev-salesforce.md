# TypeSafe Jev × Salesforce

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Salesforce DX project that calls Jev from Apex for Service Cloud case triage (classify, score, route) and as an Agentforce guardrail that screens each guest message before the agent may act, with a switchable OpenAI Decisions provider for comparison.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/divingsbysangam/typesafe-jev-salesforce) |
| Maintainer | [divingsbysangam](https://github.com/divingsbysangam). Independently curated. |
| Format | Salesforce DX project (Apex, custom metadata, Agent Script) |
| Requirements | A Salesforce org (Developer Edition works), the `sf` CLI, a TypeSafe API key (and optionally an OpenAI key). |
| License | [MIT](https://github.com/divingsbysangam/typesafe-jev-salesforce/blob/1194aaf522b99602a65e652af355b19a7f3e89e5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`force-app/main/default/classes/TypeSafeClient.cls`](https://github.com/divingsbysangam/typesafe-jev-salesforce/blob/1194aaf522b99602a65e652af355b19a7f3e89e5/force-app/main/default/classes/TypeSafeClient.cls) at the pinned commit. |

## When to use

- Add typed, probability-backed case triage to Service Cloud without parsing LLM text.
- Screen Agentforce guest messages before the agent takes an action.
- Mismatch: a demo project built for a video; review the permission sets, thresholds and callout setup before using it in a real org.

## How it works

`TypeSafeClient.cls` posts Choice, Score and Noul questions to `https://api.typesafe.ai/v1/systemone`; a provider interface lets the same questions run against OpenAI Decisions, each with its own thresholds in custom metadata. The README reports a warm p50 of about 150 to 210 ms measured from inside the org. Integration evidence: [`force-app/main/default/classes/TypeSafeClient.cls`](https://github.com/divingsbysangam/typesafe-jev-salesforce/blob/1194aaf522b99602a65e652af355b19a7f3e89e5/force-app/main/default/classes/TypeSafeClient.cls).

## Get started

From the upstream README (not run on the review host):

```sh
sf org login web --alias jev --set-default
sf project deploy start --source-dir force-app
sf org assign permset --name TypeSafe_User
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Slide deck in `video/`; demo scripts and tests in the repository.
- Made for the Deep Dives by Sangam video series.

## Limits and data handling

Case and chat text leave the org for TypeSafe (and OpenAI when that provider or the image check is enabled) on your keys.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 1194aaf522b9](https://github.com/divingsbysangam/typesafe-jev-salesforce/tree/1194aaf522b99602a65e652af355b19a7f3e89e5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
