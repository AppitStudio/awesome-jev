# Jevstiller (proxy that distills repeated Jev classifications into a local model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in proxy for repeated Jev classification calls that trains a small local model on Jev's own answers and probability distributions, then answers most requests locally within an agreement budget you set, sending uncertain input and an audit sample on to Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tomerglick57/Jevstiller) |
| Maintainer | [tomerglick57](https://github.com/tomerglick57). Independently curated. |
| Format | Python package and Docker proxy (Apache-2.0) |
| Requirements | Python 3.10+ or Docker, and your existing `TYPESAFE_API_KEY` (the proxy forwards to Jev). |
| License | [Apache-2.0](https://github.com/tomerglick57/Jevstiller/blob/20008e73686b881d4b617a6e11bb1d915ababc6e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/tomer_glick/status/2120501596308312561)). |
| Jev evidence | [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/20008e73686b881d4b617a6e11bb1d915ababc6e/jevstiller/teachers/jev.py) at the pinned commit. |

## When to use

- Cut latency and calls for a high-volume, repeated Jev classification task.
- Measure how much of a task a small local model can take over from Jev.
- Mismatch: only helps repeated classification traffic; benchmarks are the maintainer's.

## How it works

`jevstiller/teachers/jev.py` wraps `typesafe-sdk` with one Choice question per state and uses the full distribution as the training target; your service points `TYPESAFE_BASE_URL` at the proxy, which serves the local student when it agrees with Jev and forwards the rest. Integration evidence: [`jevstiller/teachers/jev.py`](https://github.com/tomerglick57/Jevstiller/blob/20008e73686b881d4b617a6e11bb1d915ababc6e/jevstiller/teachers/jev.py).

## Get started

Run the container next to your service and point the SDK base URL at it; your service keeps its own key.

```sh
docker run -d -p 8080:8080 -v jevstiller-data:/data ghcr.io/tomerglick57/jevstiller
export TYPESAFE_BASE_URL=http://localhost:8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs site: [jevstiller.pages.dev](https://jevstiller.pages.dev)
- README: [github.com/tomerglick57/Jevstiller/blob/20008e73686b881d4b617a6e11bb1d915ababc6e/README.md](https://github.com/tomerglick57/Jevstiller/blob/20008e73686b881d4b617a6e11bb1d915ababc6e/README.md)

## Limits and data handling

Requests still reach TypeSafe until the local model qualifies, plus an ongoing audit sample; training data built from your traffic is stored in the proxy's data volume.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 20008e73686b](https://github.com/tomerglick57/Jevstiller/tree/20008e73686b881d4b617a6e11bb1d915ababc6e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
