# Jev Content Moderation

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Content moderation demo with asymmetric approve / shadow / remove thresholds on Jev probabilities, so irreversible removal needs more certainty than approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kallurayaankit/jev-content-mod) |
| Maintainer | [kallurayaankit](https://github.com/kallurayaankit). Independently curated. |
| Format | Python demo (uv) |
| Requirements | Python 3.12, uv, TypeSafe API key in `.env`. |
| License | [MIT](https://github.com/kallurayaankit/jev-content-mod/blob/90f644b1ebad873aebe31c432972b148ef6623fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/uhnkitcalorieya/status/2110277172124614787)). |
| Jev evidence | [`moderate.jev`](https://github.com/kallurayaankit/jev-content-mod/blob/90f644b1ebad873aebe31c432972b148ef6623fd/moderate.jev) at the pinned commit. |

## When to use

- Prototype a moderation queue where removal is gated by a higher threshold than approval.
- Teach threshold asymmetry with a runnable example.
- Mismatch: demo-scale; no labeled evaluation set published.

## How it works

Jev scores content; code applies three bands with unequal thresholds (approve at 0.5, remove only at 0.85) and a reversible shadow band in between. Integration evidence: [`moderate.jev`](https://github.com/kallurayaankit/jev-content-mod/blob/90f644b1ebad873aebe31c432972b148ef6623fd/moderate.jev).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
cp .env.example .env   # add your TypeSafe key
uv run python demo.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample content in `content.py`; policy in `policy.py`.
- Creator thread on X (linked in Disclosure).

## Limits and data handling

Moderated text is sent to TypeSafe when run live.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 90f644b1ebad](https://github.com/kallurayaankit/jev-content-mod/tree/90f644b1ebad873aebe31c432972b148ef6623fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
