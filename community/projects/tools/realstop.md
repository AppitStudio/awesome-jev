# RealStop (Claude Code Stop hook that catches agents handing work back, with Jev as an optional cloud judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Stop hook for Claude Code: when an agent tries to end with a question like "Want me to add the tests?", RealStop returns feedback so the turn continues, while approval stops still reach you. The default judge is a local model on Apple silicon, phrase rules are the fallback, and Jev is an opt-in cloud judge. Research preview; the README reports its own offline catch and false-intervention rates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/decision-tune/realstop) |
| Maintainer | [decision-tune](https://github.com/decision-tune). Independently curated. |
| Format | Python CLI and Claude Code hook (PyPI `realstop`) |
| Requirements | Claude Code; Python with uv or pipx; Apple silicon for the local judge, or a TypeSafe key for the Jev judge. |
| License | [Apache-2.0](https://github.com/decision-tune/realstop/blob/26520315539138515cc876b94c0ad891635c5fc2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/no-quit.py`](https://github.com/decision-tune/realstop/blob/26520315539138515cc876b94c0ad891635c5fc2/hooks/no-quit.py) at the pinned commit. |

## When to use

- Stop coding agents from ending turns early with unnecessary questions.
- Mismatch: Claude Code only; Jev is opt-in and paid per use.

## How it works

`hooks/no-quit.py` asks the configured judge about each stop; with `realstop judge jev` and a key, it sends the end of the request and reply to TypeSafe and reads the quit, gate and done answers. Integration evidence: [`hooks/no-quit.py`](https://github.com/decision-tune/realstop/blob/26520315539138515cc876b94c0ad891635c5fc2/hooks/no-quit.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install realstop
realstop setup --judge local
realstop judge jev   # opt-in cloud judge
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product page: [decisiontune.com/realstop/](https://decisiontune.com/realstop/)
- Model card: [huggingface.co/decision-tune/realstop](https://huggingface.co/decision-tune/realstop)

## Limits and data handling

With the Jev judge, excerpts of each stop are sent to TypeSafe. Research preview. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 265203155391](https://github.com/decision-tune/realstop/tree/26520315539138515cc876b94c0ad891635c5fc2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
