# Moongate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that evaluates a pull-request diff against repository JSON rules using TypeSafe Jev, then emits annotations and an exit code from your thresholds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brickfrog/moongate) |
| Maintainer | [brickfrog](https://github.com/brickfrog). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | GitHub Action (`brickfrog/moongate@v0`) with a committed JavaScript runner under `dist/` (MoonBit sources). Reviewed module version **0.1.0**. |
| Requirements | Repository secret `TYPESAFE_API_KEY`; `.moongate.json` policy at the repo root; `actions/checkout` of the **base** commit so PRs cannot rewrite the rules that judge them. |
| License | [Apache-2.0](https://github.com/brickfrog/moongate/blob/cfe480ac5fb48bbcbe92bf4b24c1b519d4a0402f/LICENSE). |

## When to use

Use it for semantic CI checks a linter cannot see (credential logging, auth on new endpoints, reversible migrations). Prefer [semgate](semgate.md) for in-process Go HTTP middlewares, or [toolgate](toolgate.md) / [typesafe-agent-gates](typesafe-agent-gates.md) for agent tool gating. Moongate does not execute repository code and does not let the model edit rules.

## How it works

1. CI checks out the base SHA and runs the action with `base` / `head` inputs plus the API key via env only.
2. [`src/runner/jev.mbt`](https://github.com/brickfrog/moongate/blob/cfe480ac5fb48bbcbe92bf4b24c1b519d4a0402f/src/runner/jev.mbt) posts bounded request bodies to `https://api.typesafe.ai/v1/systemone` with a fixed prompt preamble treating repo text as untrusted evidence.
3. Each rule is a choice question (`violation` / `compliant` / `insufficient_evidence`) with probability/confidence thresholds; severity drives advisory vs failing conclusions and GitHub annotations.

Default model in the README example is `jev-1.13.0`. Fork PRs are expected to skip when secrets are unavailable.

## Get started

```sh
git clone https://github.com/brickfrog/moongate.git
cd moongate
git checkout cfe480ac5fb48bbcbe92bf4b24c1b519d4a0402f
```

Add `.moongate.json` and a workflow using `brickfrog/moongate@v0` as documented in the upstream README. Live CI evaluation sends selected diff evidence to TypeSafe and can incur charges. This listing did not call the API.

## Examples and demos

- README sample annotation output and workflow YAML.
- Integration scenarios under `src/cmd/itest/` (MoonBit). MoonBit toolchain tests were **not** run on the Linux review host.

## Limits and data handling

Diff snippets and rule questions leave CI for TypeSafe. Request bodies are byte-budget capped; oversized evidence becomes non-evaluation for that rule. Policy is always read from the base commit. Upstream treats the prompt preamble as a precaution, not a hard security boundary—fixed output labels are the control surface.

## Review and maintenance

Reviewed on **2026-09-20** at [commit cfe480a](https://github.com/brickfrog/moongate/tree/cfe480ac5fb48bbcbe92bf4b24c1b519d4a0402f): Apache-2.0, moon.mod **0.1.0**. AI-assisted source review of `action.yml`, `src/runner/jev.mbt`, README, and license. No MoonBit test run and no live TypeSafe CI invocation.

Related: [semgate](semgate.md), [toolgate](toolgate.md), [patdown](patdown.md).
