# dsh-tool-audit (DeepSeek Harness bundle that audits every tool call, pins binary hashes and can gate unruled commands with Jev or Gemini Decision 1)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness bundle that writes one audit line per tool call (tool, session, command, resolved binaries, matching rule, decision), resolves and hashes each shell executable, and trusts reviewed release hashes without any model call. Commands no rule covers can go to a decision model that answers five fixed yes/no questions (within instruction, external effect, destructive, data egress, in scope) with probabilities; thresholds turn them into allow, ask or deny. Modes: observe (default, no provider calls), ask and enforce. A sidebar page lists waiting reviews, binary updates, rules and recent decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/minetake01/dsh-tool-audit) |
| Maintainer | [minetake01](https://github.com/minetake01). Independently curated. |
| Format | DeepSeek Harness plugin bundle (JavaScript, MIT) |
| Requirements | DeepSeek Harness; for the model gate, a Jev/TypeSafe endpoint and key or a Gemini Decision 1 key. |
| License | [MIT](https://github.com/minetake01/dsh-tool-audit/blob/b80de660fd7d39b76c1da424db1b051278e49353/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/gate.js`](https://github.com/minetake01/dsh-tool-audit/blob/b80de660fd7d39b76c1da424db1b051278e49353/src/gate.js) at the pinned commit. |

## When to use

- Add an audit trail and a cheap typed gate to a coding agent's shell and tool calls.
- Mismatch: users who need Jev on by default; the shipped default is observe with no provider.

## How it works

`src/gate.js` sends the five gate questions with a Bearer key to the configured Jev endpoint (model `jev-1.13` by default in `src/config.js`) or to Gemini's decisions API. The provider is `off` and the endpoint empty by default, so Jev is optional and must be configured. Integration evidence: [`src/gate.js`](https://github.com/minetake01/dsh-tool-audit/blob/b80de660fd7d39b76c1da424db1b051278e49353/src/gate.js).

## Get started

Install the bundle from the Plugins page, then choose mode, provider, endpoint and key in its settings.

```sh
git clone https://github.com/minetake01/dsh-tool-audit
# DSH Web -> Plugins -> install the bundle
# settings: provider = jev, endpoint = https://api.typesafe.ai/v1/systemone, key -> DSH_TOOL_AUDIT_JEV_API_KEY, mode = ask
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/minetake01/dsh-tool-audit/blob/b80de660fd7d39b76c1da424db1b051278e49353/README.md](https://github.com/minetake01/dsh-tool-audit/blob/b80de660fd7d39b76c1da424db1b051278e49353/README.md)

## Limits and data handling

With a provider on, command text and context go to Jev or Gemini on your key, kept in the Host credential store and never written to state or audit lines. Audit data stays under `$DSH_HOME`.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit b80de660fd7d](https://github.com/minetake01/dsh-tool-audit/tree/b80de660fd7d39b76c1da424db1b051278e49353). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
