# Condere (open-source spin-off analyst for a code repository, with Jev judging every run)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Developer preview that inspects a software repository, gathers outside evidence, compares commercialization routes, and returns a pursue-or-stop decision with linked reasoning and a build plan a coding agent can read. Jev and a second model judge published results on every run, with an optional paid Opus check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IntelIP/condere) |
| Maintainer | [IntelIP](https://github.com/IntelIP). Independently curated. |
| Format | Python service with an MCP server for Claude Code or Codex |
| Requirements | Python with uv; OpenAI plan sign-in or OpenRouter, Exa, and a key for Jev via OpenRouter. |
| License | [MIT](https://github.com/IntelIP/condere/blob/2c28ef6b9f8f5999a6ef81b1933c2889601e73ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/condere/runtime/judges.py`](https://github.com/IntelIP/condere/blob/2c28ef6b9f8f5999a6ef81b1933c2889601e73ad/src/condere/runtime/judges.py) at the pinned commit. |

## When to use

- Get a structured, evidence-linked view of whether a repo could become a product.
- Mismatch: developer preview; Jev is one of several judges.

## How it works

`src/condere/runtime/judges.py` asks `typesafe/jev-1.14` typed questions about each published spin-off result as probabilities, alongside a GPT judge; paid dispatches are bounded by a ledger in `src/condere/runtime/providers.py`. Integration evidence: [`src/condere/runtime/judges.py`](https://github.com/IntelIP/condere/blob/2c28ef6b9f8f5999a6ef81b1933c2889601e73ad/src/condere/runtime/judges.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync --locked --group dev
cp .env.example .env
uv run --env-file .env python scripts/run_local.py api
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Self-hosting guide: [github.com/IntelIP/condere/blob/main/docs/self-hosting.md](https://github.com/IntelIP/condere/blob/main/docs/self-hosting.md)

## Limits and data handling

Repository content and evidence are sent to the configured providers. Developer preview. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 2c28ef6b9f8f](https://github.com/IntelIP/condere/tree/2c28ef6b9f8f5999a6ef81b1933c2889601e73ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
