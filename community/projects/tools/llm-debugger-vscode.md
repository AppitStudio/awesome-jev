# LLM Debugger (VS Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code extension that finds bugs by driving the real debugger — breakpoints, stepping, live values — with Jev answering each step's 'what next?' and a generation model only for hypotheses and fixes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mohsen1/llm-debugger-vscode-extension) |
| Maintainer | [mohsen1](https://github.com/mohsen1). Independently curated. |
| Format | VS Code extension (TypeScript) |
| Requirements | VS Code; TypeSafe API key plus a generation-model key. |
| License | [MIT](https://github.com/mohsen1/llm-debugger-vscode-extension/blob/17522a386e16bbe21952345c9fc1bc1ba84ad418/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ai/jev.ts`](https://github.com/mohsen1/llm-debugger-vscode-extension/blob/17522a386e16bbe21952345c9fc1bc1ba84ad418/src/ai/jev.ts) at the pinned commit. |

## When to use

- Hunt a failing check or a named symptom with `@debugger` in the chat sidebar.
- Compare the `jev` routing strategy against an `llm` baseline (benchmark included).
- Mismatch: supported runtimes are limited to what the extension can debug.

## How it works

At each step the extension sends the current line, program output and what has been tried to Jev as a choice of next debugger action; the generation model is woken only for the opening hypothesis, breakpoint locations, expressions and the final fix. Integration evidence: [`src/ai/jev.ts`](https://github.com/mohsen1/llm-debugger-vscode-extension/blob/17522a386e16bbe21952345c9fc1bc1ba84ad418/src/ai/jev.ts).

## Get started

After installing the extension, in the chat sidebar (not run on the review host):

```sh
@debugger the async order total comes out NaN
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark: `benchmark/run.js`.

## Limits and data handling

Debugger state and code context are sent to TypeSafe and the generation provider, billed to your keys.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 17522a386e16](https://github.com/mohsen1/llm-debugger-vscode-extension/tree/17522a386e16bbe21952345c9fc1bc1ba84ad418). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
