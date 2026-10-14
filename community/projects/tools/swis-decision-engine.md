# Decision Engine for PHP (swisnl)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PHP library for typed, probabilistic Choice / Score / Noul decisions in application code, with TypeSafe Jev as the default engine and OpenAI/Anthropic as alternatives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/swisnl/DecisionEngine) |
| Maintainer | [swisnl](https://github.com/swisnl). Independently curated. |
| Format | PHP library (Composer `swis/decision-engine`) |
| Requirements | PHP 8.x with Composer; TypeSafe API key for the Jev engine. |
| License | [MIT](https://github.com/swisnl/DecisionEngine/blob/cdb95fdd03700bd42af7ad1447dcadc74c5a4052/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/Decision.php`](https://github.com/swisnl/DecisionEngine/blob/cdb95fdd03700bd42af7ad1447dcadc74c5a4052/src/Decision.php) at the pinned commit. |

## When to use

- Ask narrow typed questions about application state (tickets, orders, messages) from Laravel or plain PHP.
- Keep thresholds and routing in your own code while a decision model supplies probabilities.
- Mismatch: a library, not a hosted service.

## How it works

A fluent `Decision::for(...)` builder compiles questions into a System One request; the Jev engine posts it to `api.typesafe.ai/v1/systemone` and returns typed outcomes. Other engines emulate the same primitives via structured output. Integration evidence: [`src/Decision.php`](https://github.com/swisnl/DecisionEngine/blob/cdb95fdd03700bd42af7ad1447dcadc74c5a4052/src/Decision.php).

## Get started

From the upstream README (not run on the review host):

```sh
composer require swis/decision-engine
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples: `examples/` (bootstrap, parallel requests) in the repository.

## Limits and data handling

Application state you pass is sent to TypeSafe (or the alternative provider) and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit cdb95fdd0370](https://github.com/swisnl/DecisionEngine/tree/cdb95fdd03700bd42af7ad1447dcadc74c5a4052). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
