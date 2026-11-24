# opencode-jev by aaaldo (OpenClaw decision provider for the Jev models on OpenCode's System One endpoint, including a free jev-1.13 tier)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

OpenClaw plugin that fills the `decisionModel` role and serves the core `decision_evaluate` tool with typed yes/no, choice and score answers from the Jev models that OpenCode exposes. `jev-1.13-free` needs no key; `jev-1.13` and `jev-1.14` need an OpenCode API key. Narrowed from the MIT `@psxxo/typed-decisions` provider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aaaldo/opencode-jev) |
| Maintainer | [aaaldo](https://github.com/aaaldo). Independently curated. |
| Format | OpenClaw plugin (JavaScript, no runtime dependencies) |
| Requirements | OpenClaw 2026.10.7 or newer and network access to `https://opencode.ai`; an OpenCode API key only for the paid models. |
| License | [MIT](https://github.com/aaaldo/opencode-jev/blob/1a2f81c78b435e97d4ececab0c9865423f41ab95/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.js`](https://github.com/aaaldo/opencode-jev/blob/1a2f81c78b435e97d4ececab0c9865423f41ab95/index.js) at the pinned commit. |

## When to use

- Give OpenClaw agents a Jev decision model through OpenCode, including a free tier for trying it out.
- Mismatch: direct TypeSafe API users or non-OpenClaw hosts; this plugin only speaks OpenCode's transport.

## How it works

`index.js` posts typed questions to `https://opencode.ai/inference/systemone/v1/systemone` and never sends an `Authorization` header for `-free` models; keys can come from a SecretRef or an owner-only key file. Integration evidence: [`index.js`](https://github.com/aaaldo/opencode-jev/blob/1a2f81c78b435e97d4ececab0c9865423f41ab95/index.js).

## Get started

Validate and link the plugin into OpenClaw, then set `agents.defaults.decisionModel` to one of the three model references.

```sh
git clone https://github.com/aaaldo/opencode-jev.git && cd opencode-jev
openclaw plugins validate --root .
openclaw plugins install --link .
# then set decisionModel: "opencode-jev/jev-1.13-free"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with configuration examples: [github.com/aaaldo/opencode-jev/blob/1a2f81c78b435e97d4ececab0c9865423f41ab95/README.md](https://github.com/aaaldo/opencode-jev/blob/1a2f81c78b435e97d4ececab0c9865423f41ab95/README.md)
- Tests (including an opt-in live test): [github.com/aaaldo/opencode-jev/tree/1a2f81c78b435e97d4ececab0c9865423f41ab95/test](https://github.com/aaaldo/opencode-jev/tree/1a2f81c78b435e97d4ececab0c9865423f41ab95/test)

## Limits and data handling

Questions and state go to OpenCode's endpoint (a third-party host for Jev, not TypeSafe directly); the paid models are billed by OpenCode. The free tier's limits are set by OpenCode and were not checked. The install command changes your OpenClaw configuration.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 1a2f81c78b43](https://github.com/aaaldo/opencode-jev/tree/1a2f81c78b435e97d4ececab0c9865423f41ab95). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
