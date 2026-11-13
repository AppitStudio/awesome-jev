# dsh-jev-auto-approve (DeepSeek Harness plugin where Jev reviews pending approval requests and answers the safe ones)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for DeepSeek Harness (`dsh`) that asks Jev whether each pending approval request is safe to run and answers `allowed-once` when the review passes; anything it does not approve still reaches the normal human prompt, and a Usage card shows reviews, auto-approvals, tokens and estimated cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vultwo/dsh-jev-auto-approve) |
| Maintainer | [Vultwo](https://github.com/Vultwo). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript, no npm dependencies, MIT) |
| Requirements | DeepSeek Harness 0.2.2-rc.1 (tested) and a TypeSafe key, stored in the DSH credential store. |
| License | [MIT](https://github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/classify.js`](https://github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/lib/classify.js) at the pinned commit. |

## When to use

- Cut approval prompts for routine agent actions in DeepSeek Harness.
- Mismatch: a security boundary; the author warns Jev can be wrong or manipulated by text in tool arguments.

## How it works

`lib/classify.js` posts `{model, state, questions}` to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`, both configurable in `lib/index.js`); `/jev-auto test` makes one minimal call to check the key and latency. It never changes the session permission preset or the sandbox. Integration evidence: [`lib/classify.js`](https://github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/lib/classify.js).

## Get started

Add the plugin from GitHub, then configure the key and test the connection in the Web UI.

```sh
dsh plugin --profile web add github:Vultwo/dsh-jev-auto-approve
# Plugins → Jev auto-approve → Configure → paste key → Test connection
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/README.md](https://github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/README.md)
- Security notes: [github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/SECURITY.md](https://github.com/Vultwo/dsh-jev-auto-approve/blob/0bc5d252da3e77521264075bf34e20b8067f6e2c/SECURITY.md)

## Limits and data handling

Pending tool calls and their arguments go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 0bc5d252da3e](https://github.com/Vultwo/dsh-jev-auto-approve/tree/0bc5d252da3e77521264075bf34e20b8067f6e2c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
