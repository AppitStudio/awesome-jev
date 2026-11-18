# System One gates for DSH by Kara AI (DeepSeek Harness plugin where Jev checks conclusions, shell commands and fetched text)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for the DeepSeek Harness (DSH) agent loop that moves three judgements out of the agent's own head into a separate decision call: does the turn's raw tool output support the final claim, how risky and out of scope is a shell command, and is a block of fetched text data or an injected instruction. Each answer is a probability that the plugin turns into policy (return the turn, deny the command, drop the paragraph). The same checks are exposed as three tools the model can call, with a thresholds form on the Plugins page. The default model is `typesafe/jev`; an OpenAI-compatible chat API can be used instead, with the author noting those numbers are prompted, not calibrated. English and Brazilian Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools) |
| Maintainer | [kara-aiassistant-aquelegabes](https://github.com/kara-aiassistant-aquelegabes). Independently curated. |
| Format | DSH plugin bundle (JavaScript) |
| Requirements | DeepSeek Harness 0.2.1+ with pnpm on its PATH, and a key for a System One endpoint serving `typesafe/jev` (or an OpenAI-compatible chat API) in `DECISION_API_KEY`. |
| License | [MIT](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/blob/cdb2f28587db4e022970411597cfa05e58f56389/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/adapters/systemone.js`](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/blob/cdb2f28587db4e022970411597cfa05e58f56389/lib/adapters/systemone.js) at the pinned commit. |

## When to use

- Stop a DSH agent from approving its own unsupported conclusions, risky shell commands or injected web text.
- Mismatch: other agent harnesses; it is built for DSH's hooks and plugin format.

## How it works

`lib/adapters/systemone.js` posts `{ model, state, questions }` to a `/systemone` endpoint with `typesafe/jev` as the default model (reference provider: Command Code); `cordis.patch.yml` holds the provider, model and thresholds. Integration evidence: [`lib/adapters/systemone.js`](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/blob/cdb2f28587db4e022970411597cfa05e58f56389/lib/adapters/systemone.js).

## Get started

Add the repository as a plugin from the DSH Web UI or CLI, then set the provider key and thresholds.

```sh
git clone https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools
dsh plugin --profile web add /absolute/path/to/dsh-systemone-tools
# set DECISION_API_KEY for the decision endpoint; npm test runs offline against a fake endpoint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/blob/cdb2f28587db4e022970411597cfa05e58f56389/README.md](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/blob/cdb2f28587db4e022970411597cfa05e58f56389/README.md)

## Limits and data handling

Each inspected command, completion claim and judged paragraph is sent to the configured decision provider. A privacy guard refuses states containing strings you list, and the audit log keeps a hash of the state rather than the state. The default reference endpoint is a third-party provider (Command Code), not TypeSafe directly; cost figures in the README are the author's.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit cdb2f28587db](https://github.com/kara-aiassistant-aquelegabes/dsh-systemone-tools/tree/cdb2f28587db4e022970411597cfa05e58f56389). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
