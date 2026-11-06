# Jev Doom (watch TypeSafe Jev play Freedoom with inspectable decisions)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local dashboard that lets TypeSafe Jev (direct or via Vercel AI Gateway) make structured decisions inside Freedoom/ViZDoom while you inspect choices, probabilities, latency and cost. Distinct from System1Doom.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/olivier-motium/jev-doom) |
| Maintainer | [olivier-motium](https://github.com/olivier-motium). Independently curated. |
| Format | Python + Node local dashboard (MIT) |
| Requirements | macOS or Linux, Python 3.10–3.13, Node.js 22+, and a TypeSafe or AI Gateway key for live play. |
| License | [MIT](https://github.com/olivier-motium/jev-doom/blob/0f7729d110e5c5a9fb733d55cebb728c043e4d75/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevdoom/adapters/gateway.py`](https://github.com/olivier-motium/jev-doom/blob/0f7729d110e5c5a9fb733d55cebb728c043e4d75/jevdoom/adapters/gateway.py) at the pinned commit. |

## When to use

- Watch a decision model play Freedoom with a live dashboard.
- Compare TypeSafe direct vs Vercel AI Gateway backends.
- Mismatch: experiment/demo, not a production agent; Windows not validated.

## How it works

`jevdoom/adapters/gateway.py` launches a Node gateway that forwards typed questions with `TYPESAFE_API_KEY` or `AI_GATEWAY_API_KEY`; deciders turn engine state into finite choices. Integration evidence: [`jevdoom/adapters/gateway.py`](https://github.com/olivier-motium/jev-doom/blob/0f7729d110e5c5a9fb733d55cebb728c043e4d75/jevdoom/adapters/gateway.py).

## Get started

Clone, install per README, set a TypeSafe or AI Gateway key, and start the local dashboard.

```sh
git clone https://github.com/olivier-motium/jev-doom.git && cd jev-doom
export TYPESAFE_API_KEY=...
# follow README quick start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/olivier-motium/jev-doom/blob/0f7729d110e5c5a9fb733d55cebb728c043e4d75/README.md](https://github.com/olivier-motium/jev-doom/blob/0f7729d110e5c5a9fb733d55cebb728c043e4d75/README.md)

## Limits and data handling

Game state summaries used as Jev questions are sent to TypeSafe or the gateway on your key. Independent experiment; not an official TypeSafe, Vercel or Doom product.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 0f7729d110e5](https://github.com/olivier-motium/jev-doom/tree/0f7729d110e5c5a9fb733d55cebb728c043e4d75). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
