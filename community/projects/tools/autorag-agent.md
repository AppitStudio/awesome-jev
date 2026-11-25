# AutoRAG Agent by Markr.AI and NomaDamas (personal librarian agent that searches and cites your local files, chats and mail, with Jev making every routing and evidence judgment)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local librarian agent (CLI, terminal UI, MCP server, messengers and TypeScript API) that indexes documents, chats and mail in place and answers with citations. Jev is a required component: it routes each query, checks decomposition and follow-ups, judges whether cited excerpts are relevant and supported, gates `auto` permissions, and labels evidence for an opt-in learning-to-rank reranker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Marker-Inc-Korea/AutoRAG) |
| Maintainer | [Markr.AI / NomaDamas](https://github.com/Marker-Inc-Korea) (lead: Jeffrey Kim). Independently curated. |
| Format | TypeScript package and CLI (`@autorag/librarian`) |
| Requirements | Node.js or Bun; a decision-model credential (TypeSafe, OpenRouter, Vercel AI Gateway, Cloudflare Workers AI, OpenCode, or a Dazzi Models sign-in); local MinSync embedding engine. |
| License | [Apache-2.0](https://github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/jeffreykim0711/status/2125539725067076057)). |
| Jev evidence | [`src/agent/decision-backends.ts`](https://github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/src/agent/decision-backends.ts) at the pinned commit. |

## When to use

- Ask questions across local files, chats and mail and get cited answers without uploading the files to a remote embedder.
- Give Claude Code or Codex retrieval over your files through the AutoRAG Lite MCP server.
- Mismatch: if you need it to run without any hosted decision model; Jev (or a configured fallback) is required and there is no opt-out.

## How it works

`src/agent/decision-backends.ts` maps each backend to a default Jev model: `jev-latest` on TypeSafe, `typesafe/jev-1.13` on OpenRouter, `typesafe-ai/jev-1.13.0` on Vercel AI Gateway, `typesafe/jev` on Cloudflare Workers AI and `jev-1.13` on OpenCode. `docs/retrieval/jev.md` documents every Jev question and the session probe that stops the run when no decision model answers. Integration evidence: [`src/agent/decision-backends.ts`](https://github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/src/agent/decision-backends.ts).

## Get started

Install the CLI globally, then follow the installation guide to index folders and connect a decision model.

```sh
npm install -g @autorag/librarian
# or: bun install -g @autorag/librarian
# then follow docs/guide/installation.md (autorag init, then autorag tui)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev decisions: [github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/docs/retrieval/jev.md](https://github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/docs/retrieval/jev.md)
- Learning to rank: [github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/docs/retrieval/learning-to-rank.md](https://github.com/Marker-Inc-Korea/AutoRAG/blob/42368a32d16fd714addcba69adeb48b7ab3cefd9/docs/retrieval/learning-to-rank.md)

## Limits and data handling

Jev receives the question text and, for citation and evidence judgment, the cited excerpts. Signed in, the default backend is the maintainers' own hosted Dazzi Models service; signed out it is OpenRouter (a third-party host), and direct TypeSafe is one option among several. The `openai` backend and the small-chat-model fallback use non-Jev models. Embeddings run locally by default.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 42368a32d16f](https://github.com/Marker-Inc-Korea/AutoRAG/tree/42368a32d16fd714addcba69adeb48b7ab3cefd9). Inspected the README, `docs/retrieval/jev.md`, the learning-to-rank docs and the decision-backend code at the pinned commit; the agent was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
