# jev-hook-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standard-library Python module and example hook implementing the checks a Claude Code hook should run before sending session text to TypeSafe Jev or another HTTP judge: kill switch, exclusion words with session pins, refusal of secret dumps, masking of keys and personal data, length cut, leftover re-check, pending log line and an https-only, no-redirect POST.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tsetse012/jev-hook-guard) |
| Maintainer | [tsetse012](https://github.com/tsetse012). Independently curated. |
| Format | Single module `jev_hook_guard.py`, example `UserPromptSubmit` hook and settings snippet, unit tests |
| Requirements | Python 3 and Claude Code; a `TYPESAFE_API_KEY` for the example hook (without it the hook sends nothing). |
| License | [MIT](https://github.com/tsetse012/jev-hook-guard/blob/4882a2ff1025ec39ce555055b60f003f5ed219f5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Build a Claude Code hook that calls Jev without leaking secrets or personal data.
- Reuse the masking and refusal rules in other judgment-API integrations.
- Mismatch: masking is pattern-based; it reduces but cannot eliminate leakage risk.

## How it works

[`jev_hook_guard.py`](https://github.com/tsetse012/jev-hook-guard/blob/4882a2ff1025ec39ce555055b60f003f5ed219f5/jev_hook_guard.py) provides `refuse()`, `mask()`, `leftover()`, `append_jsonl()` and `post_json()`; [`hooks/example_prompt_hook.py`](https://github.com/tsetse012/jev-hook-guard/blob/4882a2ff1025ec39ce555055b60f003f5ed219f5/hooks/example_prompt_hook.py) asks Jev whether a prompt requests something hard to undo. The README table lists what leaves the machine and what never does.

## Get started

Run the tests, then register the example hook via `hooks/settings.snippet.json` (README):

```sh
git clone https://github.com/tsetse012/jev-hook-guard && cd jev-hook-guard
python3 -m unittest discover -s tests -v
```

The example hook makes one Jev request per prompt when a key is set, billed by TypeSafe.

## Examples and demos

- [Settings snippet](https://github.com/tsetse012/jev-hook-guard/blob/4882a2ff1025ec39ce555055b60f003f5ed219f5/hooks/settings.snippet.json).
- README *What leaves the machine, what never does*.

## Limits and data handling

Only masked text (600 characters by default) goes to the configured endpoint. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 4882a2ff1025](https://github.com/tsetse012/jev-hook-guard/tree/4882a2ff1025ec39ce555055b60f003f5ed219f5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
