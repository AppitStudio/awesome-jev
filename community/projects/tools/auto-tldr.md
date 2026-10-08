# Auto TLDR

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that follows a detailed answer with a self-contained TLDR request in the same conversation (handy with per-reply Read aloud); optional Jev filtering asks TypeSafe for the probability that a summary would materially help and submits only at 0.7 or higher, sending the completed answer only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gruckion/auto-tldr) |
| Maintainer | [gruckion](https://github.com/gruckion). Independently curated. |
| Format | Claude Code plugin (`claude plugin install auto-tldr@auto-tldr`) |
| Requirements | Claude Code 2.1.287+ (or Desktop Code 2.1.286+) with mods allowed; optional `.env` with `TYPESAFE_API_KEY` for Jev filtering. |
| License | [MIT](https://github.com/gruckion/auto-tldr/blob/02d2aed3cd37a637163a603f3c3a988f6b0b6a51/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Listen to a short summary instead of a long answer.
- Skip summaries for brief confirmations using a Jev probability gate.
- Mismatch: not for one-shot `claude -p` runs.

## How it works

[`hooks/register.js`](https://github.com/gruckion/auto-tldr/blob/02d2aed3cd37a637163a603f3c3a988f6b0b6a51/hooks/register.js) registers the mod; after each eligible answer it optionally asks Jev via `/v1/systemone` and then submits the TLDR prompt as a user message. Failures or >15 s skip the summary.

## Get started

Install (README *Install globally*):

```sh
claude plugin marketplace add gruckion/auto-tldr
claude plugin install auto-tldr@auto-tldr --scope user
```

With Jev filtering, one Jev request per eligible answer on your key; otherwise no network calls.

## Examples and demos

- Changelog: [`CHANGELOG.md`](https://github.com/gruckion/auto-tldr/blob/02d2aed3cd37a637163a603f3c3a988f6b0b6a51/CHANGELOG.md).

## Limits and data handling

With Jev on, the completed assistant answer goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 02d2aed3cd37](https://github.com/gruckion/auto-tldr/tree/02d2aed3cd37a637163a603f3c3a988f6b0b6a51). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
