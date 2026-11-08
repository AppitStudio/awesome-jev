# OpenLIT (OpenTelemetry observability platform with TypeSafe Jev instrumentation, pricing and evaluation judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source LLM observability: Python/TypeScript SDKs instrument the TypeSafe SDK, Manage Models seeds Jev pricing, and evaluations can use TypeSafe Jev as the judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/openlit/openlit) |
| Maintainer | [openlit](https://github.com/openlit). Independently curated. |
| Format | Python/TypeScript SDKs + self-hosted platform (Apache-2.0) |
| Requirements | Self-hosted OpenLIT, the SDK in your app, and a TypeSafe key (Vault) for Jev evaluations. |
| License | [Apache-2.0](https://github.com/openlit/openlit/blob/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sdk/python/src/openlit/instrumentation/typesafe/utils.py`](https://github.com/openlit/openlit/blob/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385/sdk/python/src/openlit/instrumentation/typesafe/utils.py) at the pinned commit. |

## When to use

- Trace and cost Jev calls alongside other providers.
- Use Jev as an evaluation judge in OpenLIT.
- Mismatch: observability only; it does not make your decisions.

## How it works

The SDKs add TypeSafe instrumentation (`instrumentation/typesafe/`) for System One calls; the platform lists `jev-1.13.0`, `jev-latest` and `jev-preview` with pricing and can post evaluations to the TypeSafe System One API. Integration evidence: [`sdk/python/src/openlit/instrumentation/typesafe/utils.py`](https://github.com/openlit/openlit/blob/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385/sdk/python/src/openlit/instrumentation/typesafe/utils.py).

## Get started

Deploy OpenLIT per README, call `openlit.init()` in an app that uses the TypeSafe SDK, and pick provider TypeSafe in evaluation settings.

```sh
git clone https://github.com/openlit/openlit.git && cd openlit
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evaluator docs: [github.com/openlit/openlit/blob/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385/docs/latest/openlit/evaluations/evaluators.mdx](https://github.com/openlit/openlit/blob/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385/docs/latest/openlit/evaluations/evaluators.mdx)

## Limits and data handling

Traces stay in your OpenLIT deployment; evaluation inputs go to TypeSafe on your Vault key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 1b8a274d3b0d](https://github.com/openlit/openlit/tree/1b8a274d3b0d3ac85e00ebb07cde880ac95b4385). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
