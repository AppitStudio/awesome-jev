# claude-router (alexei-led)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code Mod that picks the model and effort for each main-conversation turn (and one model per routed subagent), advised by TypeSafe Jev by default or another prompt classifier—distinct from [jev-claude-router](jev-claude-router.md) hooks and [Jev Model Router](jev-model-router.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexei-led/claude-router) |
| Maintainer | [alexei-led](https://github.com/alexei-led). Submitted by the maintainer via [#1382](https://github.com/AppitStudio/awesome-jev/issues/1382); independently reviewed. Not an endorsement. |
| Format | Claude Code plugin / Mod (`router@alexei-led-claude-router`, npm `@alexeiled/claude-router` 1.10.5). No local proxy or gateway since 1.0. |
| Jev's role | Default classifier: Jev answers tier (micro/low/medium/high) and activity (`code`, `debug`, `explore`, `plan`, `review`, `ops`, `docs`) `choice` questions; Clef, Clef Flash, OpenAI, or local Ollama are alternatives. |
| Jev evidence | [`lib/config.mjs`](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/lib/config.mjs) (Jev classifier endpoint and key option) and [`lib/classifier-apis.mjs`](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/lib/classifier-apis.mjs) (typed-questions request and confidence parsing) at the pinned commit. |
| Requirements | Claude Code 2.1.289+; Node ≥ 22 for development; a TypeSafe API key (`typesafe_api_key` plugin option) or credentials for another classifier. |
| License | [MIT](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/LICENSE). Classifier and Anthropic usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, classifier code). Plugin install and live Jev calls **not** run on the review host. Savings are not measured upstream. |

## When to use

- Let a classifier move Claude Code between cheaper and stronger models/efforts per turn instead of pinning one model.
- Route by what a turn produces (code, debug, ops, docs…) as well as by difficulty.
- Mismatch: Claude Code only; routing defaults are the author's choices, not measured quality or savings.

## How it works

At the start of each logical turn the Mod sends a bounded prompt and dialogue to the active classifier, which returns tier and activity advice; a background review repeats every 4 requests (`policy.reviewEveryRequests`). A local policy applies vote, context, failure, and cache-cost rules (for example, a cheaper route waits for a dwell and a passed test/build/lint run) before changing the model and effort in Claude Code's turn hook. Claude Code still builds the request, holds model credentials, runs tools, and streams the reply. (Summarized from the upstream [README](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/README.md) and [architecture doc](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/docs/architecture.md).)

## Get started

From the upstream README (not run on the review host): `claude plugin marketplace add alexei-led/claude-router`, then `claude plugin install router@alexei-led-claude-router`, start Claude Code on a routed baseline model, run `/plugin configure router` to save the key, and open `/router` for the status pane. Users upgrading from 0.8 must remove the old gateway settings first (see the [user guide](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/docs/user-guide.md)).

## Examples and demos

- README status-band and pane screenshots (SVG) in [`docs/`](https://github.com/alexei-led/claude-router/tree/6cce84b16ab793b14c50555d0ba3d594ab503aaa/docs).
- [Evaluation](https://github.com/alexei-led/claude-router/blob/6cce84b16ab793b14c50555d0ba3d594ab503aaa/docs/evaluation.md): historical gateway results and a native shadow replay (upstream report, not reproduced here).

## Limits and data handling

Only the active classifier receives prompt text; with subagent routing on (default) it also receives routed subagent task descriptions. Prompts go to TypeSafe when Jev is selected, and to Anthropic via Claude Code for completion. The Usage tab is a list-price estimate, not a bill. No live spend here.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 6cce84b](https://github.com/alexei-led/claude-router/tree/6cce84b16ab793b14c50555d0ba3d594ab503aaa) (v1.10.5, MIT), refreshing the 2026-09-23 listing that described the pre-1.0 local gateway. Inspected the upstream README, LICENSE, and the Jev classifier code linked above; install and live Jev calls were not run. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.

Related: [jev-claude-router](jev-claude-router.md), [jev-model-router](jev-model-router.md).
