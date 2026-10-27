# voice-intent-pragmatics-bench (Korean voice-assistant intent benchmark with a Jev memory gate)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Measured benchmark of 30 Korean voice-assistant utterances across 37 conditions (3,330 responses) asking whether shared context and pragmatics cues let fast, low-effort models approach a stronger model's accuracy without adding latency; one family of conditions uses Jev as a relevance gate that passes only memories scoring above a threshold. Results page with animated charts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kimtami/voice-intent-pragmatics-bench) |
| Maintainer | [kimtami](https://github.com/kimtami). Independently curated. |
| Format | Python benchmark with results page |
| Requirements | Python 3.12 and uv; API keys for the providers you rerun, including TypeSafe for the gate. |
| License | [MIT](https://github.com/kimtami/voice-intent-pragmatics-bench/blob/1f1c5bbc293ac450ef9ce6b24709a14b9d5b7c18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`vib/gate.py`](https://github.com/kimtami/voice-intent-pragmatics-bench/blob/1f1c5bbc293ac450ef9ce6b24709a14b9d5b7c18/vib/gate.py) at the pinned commit. |

## When to use

- Compare latency and accuracy trade-offs for voice-assistant intent handling.
- See how a Jev relevance gate over memories performs against simply sharing context.
- Mismatch: 30 items in Korean; results are the author's.

## How it works

`vib/gate.py` uses the TypeSafe Python SDK with a Noul question per memory (`jev-1.14.0`) and passes only those above 0.4 or 0.5. Integration evidence: [`vib/gate.py`](https://github.com/kimtami/voice-intent-pragmatics-bench/blob/1f1c5bbc293ac450ef9ce6b24709a14b9d5b7c18/vib/gate.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/kimtami/voice-intent-pragmatics-bench && cd voice-intent-pragmatics-bench
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results page: [kimtami.github.io/voice-intent-pragmatics-bench/](https://kimtami.github.io/voice-intent-pragmatics-bench/)
- README (Korean): [github.com/kimtami/voice-intent-pragmatics-bench#readme](https://github.com/kimtami/voice-intent-pragmatics-bench#readme)

## Limits and data handling

Utterances and memories go to each provider when rerun. Grading used a blind LLM judge; numbers are the author's.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 1f1c5bbc293a](https://github.com/kimtami/voice-intent-pragmatics-bench/tree/1f1c5bbc293ac450ef9ce6b24709a14b9d5b7c18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
