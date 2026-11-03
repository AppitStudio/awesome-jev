# alert-router (Alertmanager webhook receiver where Jev decides whether a warning pages, waits for an hourly digest or is suppressed)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Homelab Alertmanager webhook receiver that decides for each warning whether to page, add it to an hourly digest or suppress it, and fails open: anything short of a confident, well-formed, non-urgent verdict pages. Critical alerts and the dead-man's switch never pass through it. The README explains why it gates on a calibrated confidence and lists the bugs found while moving it into its own repository.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/michaelrubi/alert-router) |
| Maintainer | [michaelrubi](https://github.com/michaelrubi). Independently curated. |
| Format | Python service (Docker image, Kubernetes manifests, Prometheus rules) |
| Requirements | Alertmanager, an ntfy topic and a `JEV_API_KEY`; Python and uv to develop. |
| License | [MIT](https://github.com/michaelrubi/alert-router/blob/44a06fcdfb2d35b0b063b89a630bb298c3ac394d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/alert_router/classifier.py`](https://github.com/michaelrubi/alert-router/blob/44a06fcdfb2d35b0b063b89a630bb298c3ac394d/src/alert_router/classifier.py) at the pinned commit. |

## When to use

- Cut alert noise without losing real pages by letting a confident classifier quiet only the clearly unimportant warnings.
- Mismatch: built for one author's homelab, and the GitHub repository is a push mirror of a self-hosted canonical repo.

## How it works

`src/alert_router/classifier.py` posts the alert description to the configured Jev URL (model `jev-latest`) as a typed choice question (`page_now`, `digest`, `suppress`); a missing key, HTTP error, timeout, malformed or non-finite confidence, or unknown choice all page. Integration evidence: [`src/alert_router/classifier.py`](https://github.com/michaelrubi/alert-router/blob/44a06fcdfb2d35b0b063b89a630bb298c3ac394d/src/alert_router/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/michaelrubi/alert-router.git
cd alert-router
uv sync && uv run pytest   # 62 tests, no network
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the fail-open table, calibration notes and observability: [github.com/michaelrubi/alert-router#readme](https://github.com/michaelrubi/alert-router#readme)

## Limits and data handling

Alert text goes to TypeSafe on your key. The author benchmarked calibration for their own alerts; the repository is a push mirror (canonical repo: git.rubiconetic.com), so check which copy you follow. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 44a06fcdfb2d](https://github.com/michaelrubi/alert-router/tree/44a06fcdfb2d35b0b063b89a630bb298c3ac394d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
