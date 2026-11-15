# jev-pivot-lab (Jev-routed sub-executor that answers each prompt on the cheapest model and reasoning effort with a measured record good enough for it)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Two parts: `pivot run`, a sub-executor an agent can spawn (prompt in, answer out) that picks a model-and-effort slot from a fitted policy, with Jev as the router, falls back when a provider fails and always finishes inside its deadline; and a lab that measures every model and effort your Claude Code and Codex logins offer on exact-answer problems and replays routing policies. The maintainer's own result: on their 34 puzzles, per-turn Jev routing did not beat pinning the cheapest reliable slot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arthurcolle/jev-pivot-lab) |
| Maintainer | [arthurcolle](https://github.com/arthurcolle). Independently curated. |
| Format | Python CLI (stdlib only) with committed run data |
| Requirements | Python 3.10+ on macOS or Linux, the `claude` or `codex` CLI logged in, and a `TYPESAFE_API_KEY` for Jev routing (it falls back to the reference slot without Jev). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pivotlab/jev.py`](https://github.com/arthurcolle/jev-pivot-lab/blob/478baa165a6b2e28d36c5b4d922e28a130ffe60a/pivotlab/jev.py) at the pinned commit. |

## When to use

- Measure whether model routing pays for your own tasks before adopting it.
- Mismatch: tool use or coding in a repository; the shipped policy is fitted on reasoning puzzles.

## How it works

`pivotlab/jev.py` sends fan-out questions to `https://api.typesafe.ai/v1/systemone` (default `jev-1.14.0`) with strict answer validation and a run ledger; `--no-jev` never sends the prompt to Jev. Integration evidence: [`pivotlab/jev.py`](https://github.com/arthurcolle/jev-pivot-lab/blob/478baa165a6b2e28d36c5b4d922e28a130ffe60a/pivotlab/jev.py).

## Get started

Clone and run; there is nothing to install.

```sh
git clone https://github.com/arthurcolle/jev-pivot-lab && cd jev-pivot-lab
./pivot doctor
./pivot run "What is 17 + 26?"
python3 -m unittest discover -s tests   # offline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with measurements: [github.com/arthurcolle/jev-pivot-lab/blob/478baa165a6b2e28d36c5b4d922e28a130ffe60a/README.md](https://github.com/arthurcolle/jev-pivot-lab/blob/478baa165a6b2e28d36c5b4d922e28a130ffe60a/README.md)
- Run data: [github.com/arthurcolle/jev-pivot-lab/tree/478baa165a6b2e28d36c5b4d922e28a130ffe60a/runs](https://github.com/arthurcolle/jev-pivot-lab/tree/478baa165a6b2e28d36c5b4d922e28a130ffe60a/runs)

## Limits and data handling

Prompts go to TypeSafe (unless `--no-jev`) and to your Claude Code, Codex or opted-in metered gateways. Metered gateways need `--allow-billed` and are capped per run and per day. Results are one sample per cell. No license has been chosen, so default copyright applies.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 478baa165a6b](https://github.com/arthurcolle/jev-pivot-lab/tree/478baa165a6b2e28d36c5b4d922e28a130ffe60a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
