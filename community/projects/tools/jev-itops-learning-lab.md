# Jev IT Ops Learning Lab by davidtoby (bilingual Chinese/English local site that teaches Jev's primitives on 12 synthetic IT operations scenarios)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Interactive local website for learning how to put structured AI judgments into operations workflows. Pick fictional UPS, network, server-room, meeting-room or CMDB scenarios (routine requests, critical alerts, stale evidence, data conflicts, change authorization, prompt injection), edit the context and thresholds, and inspect the questions, classification probabilities, impact scores, code guardrails, suggested runbooks and minimal audit records. The default offline mode is a deterministic rule simulation, clearly labelled as not real Jev inference; an optional live mode calls the hosted API with per-request consent, on built-in synthetic fixtures only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davidtoby/jev-itops-learning-lab) |
| Maintainer | [davidtoby](https://github.com/davidtoby). Independently curated. |
| Format | Local Node.js website and CLI (no npm dependencies) |
| Requirements | Node.js; for live mode a TypeSafe key with `JEV_ENABLE_LIVE=1`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers.mjs`](https://github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/src/providers.mjs) at the pinned commit. |

## When to use

- Learn how Choice, Score and Noul fit an ops workflow before wiring Jev into real tooling.
- Mismatch: real operations automation; it has no executor and accepts synthetic fixtures only.

## How it works

`src/providers.mjs` enables live mode only when `JEV_ENABLE_LIVE=1` and `TYPESAFE_API_KEY` are set, posting to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default; `src/contracts.mjs` builds the Choice, Score and Noul requests. Integration evidence: [`src/providers.mjs`](https://github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/src/providers.mjs).

## Get started

Start the site offline, then optionally enable live mode with your key.

```sh
git clone https://github.com/davidtoby/jev-itops-learning-lab && cd jev-itops-learning-lab
npm start    # offline simulation, no key
# live mode: JEV_ENABLE_LIVE=1 TYPESAFE_API_KEY=... npm start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (English): [github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/README.en.md](https://github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/README.en.md)
- README (Chinese): [github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/README.md](https://github.com/davidtoby/jev-itops-learning-lab/blob/74bd5eaea3d86a11344529ae534675b21275b5f0/README.md)

## Limits and data handling

Offline mode makes no API calls and does not measure Jev. Live mode sends only built-in synthetic scenarios to TypeSafe on your key, after consent per request. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 74bd5eaea3d8](https://github.com/davidtoby/jev-itops-learning-lab/tree/74bd5eaea3d86a11344529ae534675b21275b5f0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
