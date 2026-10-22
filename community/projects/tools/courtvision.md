# CourtVision (basketball computer vision with a Jev decision layer)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Real-time basketball pipeline that turns single-camera video into verified stats, then uses Jev to classify play type and moment stakes, rank coach cards and guard Claude's narration lines, with an operator dashboard over WebSockets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aiden-guan/courtvision) |
| Maintainer | [aiden-guan](https://github.com/aiden-guan). Independently curated. |
| Format | Python library and CLI |
| Requirements | Python 3.10 to 3.12; `TYPESAFE_API_KEY` for live Jev (stub, replay and off modes need none); an Anthropic key for narration. |
| License | [MIT](https://github.com/aiden-guan/courtvision/blob/ed2667be7ce779705011c9dbede8f26fe0031874/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`courtvision/decision/client.py`](https://github.com/aiden-guan/courtvision/blob/ed2667be7ce779705011c9dbede8f26fe0031874/courtvision/decision/client.py) at the pinned commit. |

## When to use

- Add typed judgments to live sports analytics without an LLM in the hot path.
- Study a decision client with deadlines, circuit breakers and replay modes.
- Mismatch: perception accuracy depends on camera setup; see the README's limitations.

## How it works

`courtvision/decision/client.py` wraps the TypeSafe SDK with live, stub, replay and off modes, hard deadlines and per-bundle breakers; it never raises into callers and returns a fallback result on any failure. Integration evidence: [`courtvision/decision/client.py`](https://github.com/aiden-guan/courtvision/blob/ed2667be7ce779705011c9dbede8f26fe0031874/courtvision/decision/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture and benchmark sections in the README: [github.com/aiden-guan/courtvision#readme](https://github.com/aiden-guan/courtvision#readme)

## Limits and data handling

In live mode, sanitized game state is sent to TypeSafe and narration prompts to Anthropic. Accuracy figures are the author's.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit ed2667be7ce7](https://github.com/aiden-guan/courtvision/tree/ed2667be7ce779705011c9dbede8f26fe0031874). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
