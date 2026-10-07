# meeting-ledger

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Terminal app that keeps meetings on the record: Claude extracts decisions, action items, promises and open questions with cited transcript lines, a System One model (TypeSafe Jev or local Kev) checks proposed status changes across meetings, and anything the two disagree on waits for your review; stale promises are flagged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/owen-alderson/meeting-ledger) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/owen-alderson/meeting-ledger#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT source; the demo needs no key. Real use needs an Anthropic API key and a TypeSafe key (or a local Kev server), each billed by its provider. Checked 2026-10-08. |
| Jev evidence | [`meeting_ledger/decisions.py`](https://github.com/owen-alderson/meeting-ledger/blob/2608e75fd1a2155ca783052216bc42ec5bd207ca/meeting_ledger/decisions.py) asks the decision model to confirm each proposed change (applied only when both models agree at ≥ 70% confidence); source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [owen-alderson](https://github.com/owen-alderson). Independently curated. |
| Format | Python CLI/TUI (`meeting-ledger`) with an MCP server and Obsidian export |
| Platform and availability | Desktop terminal with Python (platform support beyond the README not verified); optional audio transcription runs on a Mac with Parakeet. |
| Jev's role | Checks Claude's proposed status changes and extracted items; Claude extracts and answers questions. |
| Requirements | Python, an `ANTHROPIC_API_KEY`, and a `TYPESAFE_API_KEY` (or `TYPESAFE_BASE_URL` for local Kev). |
| License | [MIT](https://github.com/owen-alderson/meeting-ledger/blob/2608e75fd1a2155ca783052216bc42ec5bd207ca/LICENSE). |

## When to use

- Track whether decisions and promises from meetings actually happened.
- Ask questions across meetings with cited answers.
- Mismatch: README's `pipx install meeting-ledger` did not resolve on PyPI at review time; install from GitHub.

## How it works

Transcripts (VTT/SRT, notes or local audio transcription) are numbered; Claude lists items citing lines, a literal-quote check flags unsupported items, and the decision model verifies status changes across later meetings; disagreements go to a review queue.

## Get started

Install from GitHub and open the demo (no key needed):

```sh
pipx install git+https://github.com/owen-alderson/meeting-ledger
meeting-ledger demo
```

Real meetings use Anthropic and TypeSafe requests, billed by each provider; the demo makes none.

## Examples and demos

- README *What it does* and demo GIF.
- [MCP server](https://github.com/owen-alderson/meeting-ledger/blob/2608e75fd1a2155ca783052216bc42ec5bd207ca/meeting_ledger/mcp_server.py).

## Limits and data handling

Transcript text goes to Anthropic and TypeSafe (or stays local with Kev); audio transcription runs on the Mac. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 2608e75fd1a2](https://github.com/owen-alderson/meeting-ledger/tree/2608e75fd1a2155ca783052216bc42ec5bd207ca). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
