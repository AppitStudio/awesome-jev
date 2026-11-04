# dsh-decision-engine (DeepSeek Harness plugin that asks a System One decision model, TypeSafe by default, to allow, ask, block or reroute before the main model acts; Chinese and English)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Judgement layer for DeepSeek Harness: before the main model acts, the plugin sends the current state and a set of structured questions to a cheap decision model and uses the probabilities to allow, ask, block, reroute to another model or skip an expensive call. Tool authorization, for example, asks four questions (risk, reversibility, task relevance, injection suspicion). It defaults to a record-only `shadow` mode and fails open on errors. Any endpoint with the same request shape works, including self-hosted servers, and it has a config page, a decisions tab and cost statistics.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zuosus/dsh-decision-engine) |
| Maintainer | [zuosus](https://github.com/zuosus). Independently curated. |
| Format | DeepSeek Harness (DSH) plugin (JavaScript), Chinese and English UI |
| Requirements | DeepSeek Harness and an API key for a System One endpoint (TypeSafe by default; SiliconFlow presets and custom base URLs are also built in). |
| License | [MIT](https://github.com/zuosus/dsh-decision-engine/blob/c0bffb74db513eb3b752a7ddeeae6338e1ed591d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/providers.js`](https://github.com/zuosus/dsh-decision-engine/blob/c0bffb74db513eb3b752a7ddeeae6338e1ed591d/lib/providers.js) at the pinned commit. |

## When to use

- Add shadow-mode or enforced decision checks to a DeepSeek Harness setup and compare what the decision model would have done.
- Mismatch: TypeSafe is the default provider but one of several presets, and the plugin starts disabled.

## How it works

`lib/providers.js` defines the `systemone` provider as the default (`POST /v1/systemone` on `https://api.typesafe.ai/v1`, `TYPESAFE_API_KEY`); the same `{model, state, questions}` request goes to any other preset or custom endpoint, and every decision point can be off, observe or enforce. Integration evidence: [`lib/providers.js`](https://github.com/zuosus/dsh-decision-engine/blob/c0bffb74db513eb3b752a7ddeeae6338e1ed591d/lib/providers.js).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin add dsh-decision-engine
# add "dsh-decision-engine" to dsh.profile.bundles in the profile's package.json, restart DSH, then open the plugin's config page
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the providers, decision points and config page: [github.com/zuosus/dsh-decision-engine#readme](https://github.com/zuosus/dsh-decision-engine#readme)
- Project page: [dsh.zuos.us/dsh-decision-engine/](https://dsh.zuos.us/dsh-decision-engine/)

## Limits and data handling

State and questions go to the provider you choose. By default the plugin also sends anonymous daily usage stats (random install ID, plugin and host version, platform, decision count) to the maintainer's endpoint; the README says no keys, prompts or paths are sent and that `telemetryLevel: off` stops it. An optional mode can take the endpoint, model and key from the maintainer's server. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit c0bffb74db51](https://github.com/zuosus/dsh-decision-engine/tree/c0bffb74db513eb3b752a7ddeeae6338e1ed591d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
