# OpenCode Adaptive Fusion (self-learning model router plugin for OpenCode that can use Jev to classify tasks and pick an orchestration shape)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that turns the model picker into a learning router: it classifies each task, routes requests to the model with the best record for that task type and load tier, rescues sessions when a provider hits limits, and learns from HTTP outcomes plus human or shadow-model reviews. It starts observe-only. With a TypeSafe key, Jev does the task classification, load estimate and topology choice (single, router or sequential chain) probabilistically; without one it uses built-in heuristics.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Marble-GP/opencode-adaptive-fusion) |
| Maintainer | [Marble-GP](https://github.com/Marble-GP). Independently curated. |
| Format | OpenCode plugin (TypeScript, MIT, no build step) |
| Requirements | OpenCode 2.3.x (experimental hooks); optional `TYPESAFE_API_KEY` or `/fusion-jev-key` for Jev; your usual model providers. |
| License | [MIT](https://github.com/Marble-GP/opencode-adaptive-fusion/blob/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/scalar_subby/status/2121823368144101566)). |
| Jev evidence | [`plugins/adaptive-fusion/jev.ts`](https://github.com/Marble-GP/opencode-adaptive-fusion/blob/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e/plugins/adaptive-fusion/jev.ts) at the pinned commit. |

## When to use

- Let OpenCode learn which model to use per task type, with Jev as an optional classifier.
- Mismatch: stable OpenCode APIs; it relies on experimental hooks that may change.

## How it works

`plugins/adaptive-fusion/jev.ts` posts typed questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) using the key from the TUI command or `TYPESAFE_API_KEY`; `index.ts` uses the answers as a prior for classification and topology when `jevMode` is `auto` and a key is present. Integration evidence: [`plugins/adaptive-fusion/jev.ts`](https://github.com/Marble-GP/opencode-adaptive-fusion/blob/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e/plugins/adaptive-fusion/jev.ts).

## Get started

Clone the plugin and register its folder in OpenCode's global config.

```sh
git clone https://github.com/Marble-GP/opencode-adaptive-fusion.git
# add the plugins/adaptive-fusion folder to "plugins" in ~/.config/opencode/opencode.json
export TYPESAFE_API_KEY=...   # optional: Jev classification and topology
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Marble-GP/opencode-adaptive-fusion/blob/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e/README.md](https://github.com/Marble-GP/opencode-adaptive-fusion/blob/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e/README.md)

## Limits and data handling

With Jev on, task summaries are sent to TypeSafe on your key; routed requests go to your configured providers. Jev is optional: without a key the plugin routes on heuristics and statistics only. Docs and UI are bilingual (Japanese/English).

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 99225dd42e38](https://github.com/Marble-GP/opencode-adaptive-fusion/tree/99225dd42e38370d7c3f3a1df42c8c8ffc26e89e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
