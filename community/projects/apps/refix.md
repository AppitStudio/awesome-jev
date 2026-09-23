# Refix

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted growth application that keeps a product improving: it investigates product, search, content, and ad signals against a goal, then proposes and runs growth work with a person approving each change.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://www.refix.ai) |
| Tags | `Closed source` · `Paid` · `Commercial` |
| Product homepage | [Refix](https://www.refix.ai) |
| Pricing and access | [Pricing](https://www.refix.ai/pricing/) lists a launch-week free plan (7,000 credits/week, 2 active integrations) and Pro at $150/month (150,000 credits, unlimited integrations); Enterprise is quote-based. Checked **2026-09-23**. Because free access is limited to launch week, the primary access path is treated as paid. An account is required; there is no bring-your-own-key path. |
| Jev evidence | Vendor documentation: the Refix [Jev for AI agents](https://www.refix.ai/news/jev-for-ai-agents/) article states "Refix watches your product, scores what it finds with Jev". This is a vendor claim; the implementation was not inspected and no live API traffic was observed. |
| Disclosure | Closed source. The implementation was not inspected; Jev use is a vendor claim in the linked Refix article, not independently observed API traffic. Commercial product with paid hosted plans and a launch-week free tier; check current pricing. Affiliation: this submission is from Refix. Not an endorsement. |
| Maintainer | Refix ([refix.ai](https://www.refix.ai), [@refix_ai](https://x.com/refix_ai)); catalogue submission by [christiina02](https://github.com/christiina02). |
| Format | Hosted web application with account sign-in. |
| Platform and availability | Public web app at [refix.ai](https://www.refix.ai). Account required; no public source or self-hosted build was found. |
| Jev's role | Vendor-stated: Refix scores what it finds with Jev as part of an investigate → decide → approve loop over growth signals. Other models and services handle generation and outreach; whether Jev is required for every path was not verified. |
| Requirements | A modern browser, an account, and a product to work on. No bring-your-own-key option is documented. |
| License | Proprietary hosted service. Access is governed by the [Terms](https://www.refix.ai/privacy/terms/) and [Privacy Policy](https://www.refix.ai/privacy/). |

## When to use

Use Refix when a product team wants a hosted teammate that keeps working toward a growth outcome — for example conversion or activation — instead of producing a one-off report. It is a hosted product, not a self-hosted library, and a person still approves anything that ships.

It is a poor fit when the requirement is offline, open-source, or fully autonomous execution with no human review: all three are out of scope for this listing.

## How it works

Vendor materials describe a loop in which Refix watches product and revenue signals around a stated goal, scores what it finds with Jev, prioritises the current constraint, coordinates a fix or experiment, and verifies the result. The Refix article links Jev to bounded decisions such as routing, tool selection, and confidence-based human review, with application code owning state, control flow, and side effects.

Jev involvement is documented only by vendor statements. This catalogue entry does not claim to have inspected TypeSafe API calls, question schemas, or confidence handling.

## Get started

This path follows the public site; it was not executed end-to-end during review (no account creation and no live run).

1. Open [refix.ai](https://www.refix.ai) and choose **Get started**.
2. Create an account through the sign-up flow shown by the product.
3. Give Refix a goal and set the guardrails the product asks for.
4. Review proposed changes before approving anything that ships, and check the [pricing](https://www.refix.ai/pricing/) page for current credit and plan limits.

Paid plans and provider/hosting costs apply. Do not submit confidential material until you have reviewed the [Terms](https://www.refix.ai/privacy/terms/) and [Privacy Policy](https://www.refix.ai/privacy/).

## Examples and demos

The [product homepage](https://www.refix.ai) is the verified public entry point. The vendor [news](https://www.refix.ai/news/jev-for-ai-agents/) section documents how Refix positions Jev, and the [goals index](https://www.refix.ai/goals/) lists the outcomes the product is built around. No separate public API docs or open sample repository for Refix itself were found; the org's public GitHub repositories ([github.com/refixai](https://github.com/refixai)) were not a product integration sample.

## Limits and data handling

Closed source: backend prompts, Jev questions, and scoring were not inspected. The product is a hosted service, so workspace and product data are processed by Refix and any services it uses; the [Privacy Policy](https://www.refix.ai/privacy/) governs that processing. A person must approve changes, and the vendor states some work may occur without extra approval, so teams should confirm the exact boundaries for their workspace. Exact retention, subprocessors, and paid-plan limits were not independently audited.

## Review and maintenance

Reviewed **2026-09-23** with AI assistance. Primary sources: [refix.ai](https://www.refix.ai) (HTTP 200), [pricing](https://www.refix.ai/pricing/) (Free launch-week, Pro $150/month, Enterprise), [Jev for AI agents](https://www.refix.ai/news/jev-for-ai-agents/) (vendor statement of Jev use), [Terms](https://www.refix.ai/privacy/terms/), and [github.com/refixai](https://github.com/refixai). No signup, payment, or live run was performed. Catalogue de-dupe found no existing Refix listing.

Related: none in this directory yet for hosted growth-automation apps.
