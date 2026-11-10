# dsh-decide (DeepSeek Harness plugin adding decision-model tools over TypeSafe Jev and other System One providers)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DSH plugin that adds a pair of agent tools plus a Decisions settings page for decision models: TypeSafe Jev by default, TokenRhythm NeoHorse-Jev, OpenAI Decisions or a local System One server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/calmzealA/dsh-decide) |
| Maintainer | [calmzealA](https://github.com/calmzealA). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript, MIT) |
| Requirements | DeepSeek Harness desktop and a provider key (`TYPESAFE_API_KEY` for Jev; local servers can be keyless). |
| License | [MIT](https://github.com/calmzealA/dsh-decide/blob/8e693db313e566a7032115355174ac77b11cab1d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/AIchen6666/status/2119841267572002890)). |
| Jev evidence | [`lib/adapters/systemone.js`](https://github.com/calmzealA/dsh-decide/blob/8e693db313e566a7032115355174ac77b11cab1d/lib/adapters/systemone.js) at the pinned commit. |

## When to use

- Give a DSH agent typed decision tools.
- Switch between Jev and other decision models.
- Mismatch: provider website links carry the author's `aichen` referral tag; not yet on npm.

## How it works

`lib/adapters/systemone.js` speaks the System One dialect used for TypeSafe Jev (`jev-latest`); `lib/providers.js` lists providers, and the settings page covers thresholds, cache, audit and usage per provider. Integration evidence: [`lib/adapters/systemone.js`](https://github.com/calmzealA/dsh-decide/blob/8e693db313e566a7032115355174ac77b11cab1d/lib/adapters/systemone.js).

## Get started

Link the checkout with `dsh plugin --profile desktop add link:<path>`, restart DSH, and enable a provider under Settings → Decisions.

```sh
git clone https://github.com/calmzealA/dsh-decide.git
dsh plugin --profile desktop add link:./dsh-decide
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/calmzealA/dsh-decide/blob/8e693db313e566a7032115355174ac77b11cab1d/README.md](https://github.com/calmzealA/dsh-decide/blob/8e693db313e566a7032115355174ac77b11cab1d/README.md)

## Limits and data handling

Decision state goes to whichever provider you enable.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 8e693db313e5](https://github.com/calmzealA/dsh-decide/tree/8e693db313e566a7032115355174ac77b11cab1d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
