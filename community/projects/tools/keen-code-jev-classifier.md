# Keen Code (terminal coding agent with a Jev task classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-aware terminal coding agent in Go with multi-provider support, MCP and subagents; its decision layer can use Jev to classify each turn as simple, standard or complex so `/model router` picks the model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mochow13/keen-code) |
| Maintainer | [mochow13](https://github.com/mochow13). Independently curated. |
| Format | Terminal agent (Go, MIT) |
| Requirements | The Keen Code CLI, your model providers, and a TypeSafe key for the `typesafe` decision provider. |
| License | [MIT](https://github.com/mochow13/keen-code/blob/9db0ec814dfa7a9dc9c29044e807895012b64bd7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/decision/typesafe/evaluator.go`](https://github.com/mochow13/keen-code/blob/9db0ec814dfa7a9dc9c29044e807895012b64bd7/internal/decision/typesafe/evaluator.go) at the pinned commit. |

## When to use

- Route coding-agent turns to cheaper models by typed complexity.
- Mismatch: Jev is one of two decision providers.

## How it works

`internal/decision/typesafe/evaluator.go` posts to `/v1/systemone`; `docs/task-classification-using-decision-models.md` describes the request and the `typesafe` and `liquid` providers. Integration evidence: [`internal/decision/typesafe/evaluator.go`](https://github.com/mochow13/keen-code/blob/9db0ec814dfa7a9dc9c29044e807895012b64bd7/internal/decision/typesafe/evaluator.go).

## Get started

Install with the script, then configure the decision provider and enable the model router.

```sh
curl -fsSL https://raw.githubusercontent.com/mochow13/keen-code/main/scripts/install.sh | bash
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Task-classification doc: [github.com/mochow13/keen-code/blob/9db0ec814dfa7a9dc9c29044e807895012b64bd7/docs/task-classification-using-decision-models.md](https://github.com/mochow13/keen-code/blob/9db0ec814dfa7a9dc9c29044e807895012b64bd7/docs/task-classification-using-decision-models.md)

## Limits and data handling

Turn text for classification goes to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 9db0ec814dfa](https://github.com/mochow13/keen-code/tree/9db0ec814dfa7a9dc9c29044e807895012b64bd7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
