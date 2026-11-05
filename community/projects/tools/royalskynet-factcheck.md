# factcheck (library that picks the fact claims out of an agent reply and checks each against the evidence the agent saw, with a Jev verifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small JavaScript library: select fact-like sentences deterministically, skip the model when the agent saw no evidence, then batch all claims into one verifier request that returns `supported`, `contradicted` or `not_addressed`. A `jevVerifier` adapter uses the `jevwire` Jev decision model; any other verifier with the same shape works.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royalskynet/factcheck) |
| Maintainer | [royalskynet](https://github.com/royalskynet). Independently curated. |
| Format | JavaScript module (ESM) |
| Requirements | Node.js; `jevwire` as an optional peer dependency and a Jev API key (`JEV_API_KEY`) for `jevVerifier`. |
| License | [MIT](https://github.com/royalskynet/factcheck/blob/7dcf3c908c898dd39125108e90434bdfb2fe563f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.js`](https://github.com/royalskynet/factcheck/blob/7dcf3c908c898dd39125108e90434bdfb2fe563f/index.js) at the pinned commit. |

## When to use

- Catch inferences that an agent presents as sourced facts.
- Plug Jev in as the verifier while keeping claim selection free and deterministic.
- Mismatch: very small library; separate from the already listed jev-factcheck by maksym771.

## How it works

`checkFacts({text, evidence, verify})` selects claims, gates on missing evidence and sends one batch; `jevVerifier(model)` maps Jev answers to verdicts, and verifier errors come back as `error`, never as a verdict. Integration evidence: [`index.js`](https://github.com/royalskynet/factcheck/blob/7dcf3c908c898dd39125108e90434bdfb2fe563f/index.js).

## Get started

From the upstream README (not run on the review host):

```sh
# from the README (not run):
import { checkFacts, jevVerifier } from './index.js';
import { JevDecisionModel } from 'jevwire';
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the claim-selection rules and limits: [github.com/royalskynet/factcheck/blob/7dcf3c908c898dd39125108e90434bdfb2fe563f/README.md](https://github.com/royalskynet/factcheck/blob/7dcf3c908c898dd39125108e90434bdfb2fe563f/README.md)

## Limits and data handling

Reply text and evidence are sent to the Jev provider you configure; a verdict is a probabilistic check, not proof.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 7dcf3c908c89](https://github.com/royalskynet/factcheck/tree/7dcf3c908c898dd39125108e90434bdfb2fe563f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
