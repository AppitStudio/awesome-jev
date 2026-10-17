# Dernier Abri (Last Shelter)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

French student 3D browser defence game where Jev estimates from a text description whether a night silhouette is a zombie or a survivor, and deterministic, tested code decides whether to fire, using Bayesian evidence fusion and a sequential test.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Pablositoo/dernier-abri) |
| Maintainer | [Pablositoo](https://github.com/Pablositoo). Independently curated. |
| Format | Python server and browser 3D game |
| Requirements | Python 3.10+, a modern browser; a TypeSafe key for real Jev (a simulated mode needs none). |
| License | [MIT](https://github.com/Pablositoo/dernier-abri/blob/3426f198be9b7502701a83efc530f1387ba79c73/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev_client.py`](https://github.com/Pablositoo/dernier-abri/blob/3426f198be9b7502701a83efc530f1387ba79c73/server/jev_client.py) at the pinned commit. |

## When to use

- See "the model classifies, the code decides" applied to a high-stakes toy decision.
- Reuse the headless simulator and calibration analysis to study decisions under uncertainty.
- Mismatch: a course project (aivancity L3); README mainly in French.

## How it works

The server sends only a text description of each silhouette to `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`) and gets a probability; explicit versioned rules combine it with whether the silhouette stops when ordered, and doubt always means another warning rather than a shot. Integration evidence: [`server/jev_client.py`](https://github.com/Pablositoo/dernier-abri/blob/3426f198be9b7502701a83efc530f1387ba79c73/server/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Pablositoo/dernier-abri.git && cd dernier-abri
python3 server.py --fake   # simulated Jev, no key; open http://localhost:8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshot: `docs/capture_jeu.png`.

## Limits and data handling

With a real key, silhouette descriptions go to TypeSafe on your key, server-side only.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 3426f198be9b](https://github.com/Pablositoo/dernier-abri/tree/3426f198be9b7502701a83efc530f1387ba79c73). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
