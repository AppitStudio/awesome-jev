# Damocles

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code extension and desktop app embedding a multi-provider AI coding agent; with a TypeSafe (or OpenRouter) key, Jev runs its persistent-memory contradiction judge and memory reranking instead of a sub-call LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AizenvoltPrime/damocles) |
| Maintainer | [AizenvoltPrime](https://github.com/AizenvoltPrime). Independently curated. |
| Format | VS Code extension (build from source) and desktop app releases for Windows, macOS and Linux |
| Requirements | Model provider accounts/keys for chat (Claude, OpenAI, DeepSeek, etc.); `TYPESAFE_API_KEY` in Settings for the Jev memory judge, or an OpenRouter key. |
| License | [MIT](https://github.com/AizenvoltPrime/damocles/blob/11592d90d7f3c0ee7171fd0f7bdfa8d35dc37e7a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep an agent's long-lived memory consistent: let a typed judge decide whether a new fact replaces an older one.
- Rerank recalled memories cheaply instead of spending a chat-model sub-call.
- Mismatch: Jev does not power chat here; if you only want a chat agent, it adds nothing.

## How it works

Damocles stores memories and searches them with BM25. When a TypeSafe key is set (else an OpenRouter key), both memory reranks — `search_memories` and the optional injected-memory rerank under a ~2 s cap — and the contradiction judge run on TypeSafe's Jev classifier rather than the cheap sub-call model; the settings panel names the judge in use ([README: Persistent Memory](https://github.com/AizenvoltPrime/damocles/blob/11592d90d7f3c0ee7171fd0f7bdfa8d35dc37e7a/README.md)).

## Get started

Download a desktop release or build the extension, then add a TypeSafe key in Settings (live Jev calls on memory operations):

```sh
git clone https://github.com/AizenvoltPrime/damocles.git && cd damocles
npm install && npm run build
# press F5 in VS Code to launch the Extension Development Host
# Settings → TypeSafe → TYPESAFE_API_KEY
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README sections *Persistent Memory* and *TypeSafe* (provider list).
- Desktop releases with SHA-256 sums and GitHub build-provenance attestations.

## Limits and data handling

Memory text is sent to TypeSafe or OpenRouter when Jev is configured. The rest of the agent sends prompts/files to whichever chat providers you configure. No telemetry per upstream privacy statement. Extension and app were not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 11592d90d7f3](https://github.com/AizenvoltPrime/damocles/tree/11592d90d7f3c0ee7171fd0f7bdfa8d35dc37e7a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
