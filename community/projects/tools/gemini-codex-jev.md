# gemini-codex-jev by fl0AT (Google Antigravity plugin joining Gemini planning, Jev routing and patch gates, and Codex CLI execution)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Antigravity plugin: Gemini plans and accepts, Jev acts as a fast gate with built-in `task_route` and `patch_gate` templates (plus custom choice/noul/score/box questions), and Codex CLI executes in a sandbox with resume, fork and review. Exposes MCP tools (`jev_judge`, `codex_exec`, `codex_continue`, `codex_review`) and a subagent. Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Howardyh/gemini-codex-jev) |
| Maintainer | [fl0AT](https://github.com/Howardyh). Independently curated. |
| Format | Google Antigravity plugin with a Node.js MCP server |
| Requirements | Node.js 22+, Codex CLI signed in, and optionally a TypeSafe API key for Jev judging. |
| License | [MIT](https://github.com/Howardyh/gemini-codex-jev/blob/351c016ed61446c2c48634d90f9f264ff05c45e4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev-client.mjs`](https://github.com/Howardyh/gemini-codex-jev/blob/351c016ed61446c2c48634d90f9f264ff05c45e4/server/jev-client.mjs) at the pinned commit. |

## When to use

- Add Jev routing and patch-quality gates to a Gemini plus Codex workflow in Antigravity.
- Mismatch: other agent hosts; it targets Antigravity.

## How it works

`server/jev-client.mjs` posts questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) with a normalized SHA-256 cache and a per-task budget lock. Integration evidence: [`server/jev-client.mjs`](https://github.com/Howardyh/gemini-codex-jev/blob/351c016ed61446c2c48634d90f9f264ff05c45e4/server/jev-client.mjs).

## Get started

Clone into the Antigravity global plugins folder and start a new session.

```sh
git clone https://github.com/Howardyh/gemini-codex-jev.git ~/.gemini/config/plugins/gemini-codex-jev
export TYPESAFE_API_KEY=...   # optional
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/Howardyh/gemini-codex-jev/blob/351c016ed61446c2c48634d90f9f264ff05c45e4/README.md](https://github.com/Howardyh/gemini-codex-jev/blob/351c016ed61446c2c48634d90f9f264ff05c45e4/README.md)

## Limits and data handling

Task text and patches are sent to TypeSafe when Jev is enabled; Codex runs use your OpenAI account.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 351c016ed614](https://github.com/Howardyh/gemini-codex-jev/tree/351c016ed61446c2c48634d90f9f264ff05c45e4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
