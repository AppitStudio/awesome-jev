# oc-one-guard (OpenCode plugin that asks a System One judge before tool calls that could leak data)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode v1 plugin that checks proposed tool calls for possible data exfiltration (uploading keys, dumping environment variables, staging a script that sends files out). Local checks let ordinary calls through; calls that need review go to a System One judge as one `noul` question, and configurable bands allow, hold for review, deny or stop the run. Reviewed calls block when the judge is offline. A heuristic guardrail, not a firewall.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HumanFace-Tech/oc-one-guard) |
| Maintainer | [HumanFace-Tech](https://github.com/HumanFace-Tech). Independently curated. |
| Format | OpenCode plugin (JavaScript) |
| Requirements | OpenCode v1 (1.19.4 tested; v2 not supported) and a `/v1/systemone` endpoint such as llama.cpp's llama-server or another Jev-compatible server. |
| License | [MIT](https://github.com/HumanFace-Tech/oc-one-guard/blob/c5085d39a790b75d8aed33c04bb4e47e4b7a223f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge.js`](https://github.com/HumanFace-Tech/oc-one-guard/blob/c5085d39a790b75d8aed33c04bb4e47e4b7a223f/src/judge.js) at the pinned commit. |

## When to use

- Add a second check against secret leaks in agent tool calls.
- Mismatch: OpenCode v1 only; the docs target local System One servers, so check that your chosen endpoint is one you trust.

## How it works

`src/judge.js` sends the rendered tool arguments (and sometimes staged file contents) to the configured `POST /v1/systemone` endpoint and turns the `noul` probability into allow, hold, deny or stop using the cutoffs in `src/defaults.js`. Integration evidence: [`src/judge.js`](https://github.com/HumanFace-Tech/oc-one-guard/blob/c5085d39a790b75d8aed33c04bb4e47e4b7a223f/src/judge.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/HumanFace-Tech/oc-one-guard
# then follow docs/installation.md to register the plugin and set the judge endpoint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Explainer: [github.com/HumanFace-Tech/oc-one-guard/blob/main/docs/explainer.md](https://github.com/HumanFace-Tech/oc-one-guard/blob/main/docs/explainer.md)
- Security notes: [github.com/HumanFace-Tech/oc-one-guard/blob/main/docs/security.md](https://github.com/HumanFace-Tech/oc-one-guard/blob/main/docs/security.md)

## Limits and data handling

Tool arguments under review go to the judge endpoint you configure. Cutoffs are not calibrated probabilities.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit c5085d39a790](https://github.com/HumanFace-Tech/oc-one-guard/tree/c5085d39a790b75d8aed33c04bb4e47e4b7a223f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
