# fhir-jev (proof-of-concept FastAPI service that uses Jev to score, route and flag FHIR R4 resources on synthetic data)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Exploration project that parses FHIR R4 Patient, Observation, Condition and Bundle resources, flattens them into a small state and uses Jev's Score, Choice and Noul primitives to auto-accept or send for review, route Bundles to one of five pipelines and flag notifiable conditions. Includes benchmarks against hand-written rules on 204 synthetic records, a mock client and Prometheus metrics. Not for production use.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/budityw23/fhir_jev) |
| Maintainer | [budityw23](https://github.com/budityw23). Independently curated. |
| Format | Python FastAPI service (Pydantic v2) |
| Requirements | Python and a `JEV_API_KEY`; the repo ships a mock client for offline tests. |
| License | [MIT](https://github.com/budityw23/fhir_jev/blob/400f6e891e16a61e99b6850771643ace6e90a6d9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_fhir/jev_client/client.py`](https://github.com/budityw23/fhir_jev/blob/400f6e891e16a61e99b6850771643ace6e90a6d9/src/jev_fhir/jev_client/client.py) at the pinned commit. |

## When to use

- Study conformance-first, decision-second pipelines for structured clinical data.
- See how a routing question was reframed to lift accuracy (the author's DEV post).
- Mismatch: synthetic data only; the author says it is a portfolio proof of concept, not connected to any production system.

## How it works

Serializers validate each resource, flatten it, then `jev_client/client.py` sends the typed questions to `https://api.typesafe.ai` (`jev-latest`); thresholds convert answers into accept, route, flag or human review. Integration evidence: [`src/jev_fhir/jev_client/client.py`](https://github.com/budityw23/fhir_jev/blob/400f6e891e16a61e99b6850771643ace6e90a6d9/src/jev_fhir/jev_client/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
# from the upstream repo (not run): copy .env.example to .env (JEV_BASE_URL, JEV_MODEL and your key), then follow the README to run the FastAPI app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with modules and architecture: [github.com/budityw23/fhir_jev/blob/400f6e891e16a61e99b6850771643ace6e90a6d9/README.md](https://github.com/budityw23/fhir_jev/blob/400f6e891e16a61e99b6850771643ace6e90a6d9/README.md)
- DEV Community write-up by the author: [dev.to/budiwidhiyanto/fhir-validation-doesnt-tell-you-what-to-do-next-so-i-built-a-decision-layer-1gff](https://dev.to/budiwidhiyanto/fhir-validation-doesnt-tell-you-what-to-do-next-so-i-built-a-decision-layer-1gff)

## Limits and data handling

Synthetic records only; the author reports latency above his target. Do not send real patient data to any hosted model without the right agreements. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 400f6e891e16](https://github.com/budityw23/fhir_jev/tree/400f6e891e16a61e99b6850771643ace6e90a6d9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
