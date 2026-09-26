# fast-jev-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prune old tool activity from an agent conversation while preserving ordinary message text and the tool evidence selected for retention.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tamaratran/fast-jev-compaction) |
| Maintainer | [tamaratran](https://github.com/tamaratran). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript library with an optional Claude Code function-hook plugin. |
| Requirements | Node.js 18+, npm; TypeScript development dependencies for a source checkout. Offline examples need no account. Live use needs a TypeSafe account and `TYPESAFE_API_KEY`; the built-in HTTP client defaults to `jev-latest`. |
| License | [MIT](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/LICENSE). |

## When to use

Explore this when a coding agent accumulates repeated file reads, obsolete searches, or large tool outputs. It gives you an inspectable decision for each eligible tool call: retain it, shorten its result, or remove the pair.

Start with the library on a synthetic transcript. A simple age or size rule remains easier when that policy already expresses what can go. Jev adds a semantic judgment about relevance to the ongoing task. This project does not generate summaries, and conversations dominated by ordinary text may shrink very little.

## How it works

```text
Transcript → pair calls/results → protect recent activity
           → fit a view for Jev → ask two questions per candidate
           → apply keep/truncate/drop rules → return revised transcript
```

The [implementation](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/compact.ts) asks two independent [Noul](https://docs.typesafe.ai/primitives/noul) questions: does knowing this call and its input still matter, and does its full result need to remain? Each answer is a probability of yes, with no separate confidence score. Code applies the default `keepThreshold` of `0.5`:

| Answers | Application behavior |
| --- | --- |
| `keepResult ≥ 0.5` | Keep both call and result, even if `keepCall` is low. |
| Otherwise, `keepCall ≥ 0.5` | Keep the call; shorten a long result to its first 300 characters plus a note. |
| Both below `0.5` | Drop the call and its paired result. |

`drop_result` is the action name for truncation. Results no longer than `truncateHeadChars + 120` remain unchanged, so this decision does not always save space.

Pairs are matched by `tool_use_id`. Either half appearing in the first message or newest six messages protects the pair by default. Unanswered calls are excluded. The transformation preserves pair relationships in well-formed input; it does not validate or repair duplicate IDs or pre-existing orphan results.

**What Jev sees differs from what the next agent receives.** The [state builder](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/state.ts) replaces result bodies with status and character-count notes. Even its `full` stage caps each serialized tool input at 1,000 characters. Further fitting can abridge text, omit older text-only entries, and compress call descriptions. Jev therefore infers result importance without inspecting those result bodies. Ordinary message text stays verbatim in the returned transcript, although emptied tool-only messages can disappear.

## Get started

**Setup downloads source and npm packages; it makes no inference requests.** Use a separate working directory:

```sh
git clone https://github.com/tamaratran/fast-jev-compaction.git
cd fast-jev-compaction
git checkout e3f262a7f4d42bd8dd32ced30d26176f7cb545b0
npm install --ignore-scripts --no-audit --no-fund
npm run build
```

**Offline synthetic example**, from that checkout. All probabilities below are invented to demonstrate policy branches:

```sh
node --input-type=module <<'JS'
import { compact } from './dist/index.js';
const text = (role, text) => ({ role, text, toolUses: [] });
const pair = (id, path) => [
  { role: 'assistant', text: '', toolUses: [
    { tool_use_id: id, tool: 'Read', input: { file_path: path } }
  ] },
  { role: 'user', text: '', toolUses: [], toolResults: [
    { tool_use_id: id, text: 'synthetic file contents\n'.repeat(40) }
  ] }
];
const messages = [text('user', 'Fix the parser; keep the public API.'),
  ...pair('old', 'legacy.ts'), ...pair('current', 'parser.ts'),
  ...pair('test', 'parser.test.ts'), text('user', 'Continue the fix.')];
const probabilities = { call_t1: 0.1, result_t1: 0.1,
  call_t2: 0.9, result_t2: 0.1, call_t3: 0.1, result_t3: 0.9 };
const fakeJev = { async ask(state, questions) {
  return { answers: Object.fromEntries(Object.keys(questions).map(id =>
    [id, { type: 'noul', noul: probabilities[id] }])) };
} };
const result = await compact(messages, fakeJev, { preserveRecentMessages: 1 });
console.log(result.decisions.map(d => d.action).join(', '));
console.log(`${messages.length} -> ${result.messages.length} messages`);
JS
```

Expected: `drop_call, drop_result, keep`, then `8 -> 6 messages`. The legacy pair disappears, the parser result is shortened, and the test pair remains. No files are actually read: the filenames are synthetic transcript data.

## Adaptation tips

- Supply an explicit `goal` when the last three user prompts do not adequately describe the ongoing task; that is the default goal source.
- Protect irreplaceable evidence through application policy. Re-running a changed file read may return different content; re-running a side-effecting tool may be inappropriate.
- Treat shortened results as partial evidence. Character-based truncation can break JSON or other structured output; preserve the complete result through application policy when downstream code must parse it.
- Evaluate near-threshold cases before choosing a keep threshold. A lower threshold retains more; a custom policy can retain ambiguous cases. Upstream has no abstention interval.
- Use a custom `JevAsker` to capture raw responses, resolved model IDs, and actual token usage privately. Returned decisions preserve the two probabilities, but `stats` does not retain provider usage or model metadata.

These are adaptation suggestions; they are not all built-in options.

## Examples and demos

- [Unit tests](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/tests/fast-jev-compaction.test.ts): offline examples of state fitting, batching, truncation, and failure behavior. Run `npm test` offline after installation.
- [Parser-fix demo](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/examples/demo.ts): synthetic conversation with **live** TypeSafe judgments via `npm run demo`; requires a key and incurs usage charges.
- [Animated macOS demo](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/demo/JevDemo): scripted SwiftUI visualization, not recorded model behavior. It was inspected but not built during this review.

## Limits and data handling

The library sends fitted message text, tool inputs, and result metadata to TypeSafe on live calls. Omitting result bodies does not redact secrets from other fields. It returns data in memory without writing a transcript file; persistence belongs to your application. Consult [TypeSafe's legal terms](https://docs.typesafe.ai/legal) for provider retention conditions.

Defaults allow an estimated 25,000 state tokens and 30,000 total request tokens. These are library budgets; [current Jev limits](https://docs.typesafe.ai/models) distinguish 64k total tokens from 32k for state plus the longest question. Each batch resends the fitted state, so repeated input adds cost. Batches run concurrently without a request-count or concurrency cap. The built-in transport has no explicit timeout or retry policy.

Missing keys, HTTP failures, malformed or missing answers, and impossible budgets throw; callers must retain the original transcript or choose another fallback. Validation checks finite Noul numbers but does not reject values outside `[0, 1]`. A completed call can still make a wrong retention decision.

The optional [Claude Code adapter](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/hooks/README.md) documents an early-access function-hook API with generated types from Claude Code 2.1.274. It falls back to the host's built-in summary on errors or less than 25% character reduction by default, and logs decisions. Host installation, compatibility, and session persistence were not tested here.

## Review and maintenance

Reviewed on **2026-09-19** at [commit e3f262a](https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0): package version 0.2.0, plugin manifest 0.3.0. AI-assisted source review covered the library, plugin, license, and examples. On Node.js 22.19.0, all **29 offline tests**, `npm run typecheck`, and `npm run build` passed. The synthetic example above was also executed with assertions for retention, truncation, and pair integrity. No live inference, plugin installation, or model-quality evaluation was performed.

Related: [RAG triage](../../../examples/rag-triage/README.md) selects context before an answer; this library removes tool context from an existing conversation.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev use cases: nine patterns developers are building](../../knowledge-base/articles/jev-use-cases.md) — Mentioned in the source article. Pattern 2: drop tool calls that no longer matter instead of summarizing an agent's context.
- [10 Jev project ideas with practical starting points](../../knowledge-base/articles/jev-project-ideas.md) — Independently suggested by JevList; not an endorsement by rody. Build 5: prune stale agent tool call and result pairs.
- [Jev decision audits: validate the business case](../../knowledge-base/articles/jev-decision-audit.md) — Mentioned in the source article. Find a bounded, repeated agent step to replace.
<!-- knowledge:backlinks:end -->
