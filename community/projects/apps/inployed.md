# INployed

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows desktop app with a cloud pipeline that collects job postings, ranks them against your background, writes grounded one-page résumés, and fills and sends queued applications; Jev makes the yes-or-no calls in scoring and reads each application page when it is on.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yib7/INployed) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/yib7/INployed#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-19. |
| Jev evidence | [`local/jev.py`](https://github.com/yib7/INployed/blob/09321b7bfcce0031880c5645886cd7826bc5c1d8/local/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [yib7](https://github.com/yib7). Independently curated. |
| Format | Windows desktop app (Python) + cloud scrape pipeline |
| Platform and availability | Windows 11 (install from source per README). |
| Jev's role | Optional judge for scoring and for reading application pages before code fills them from your data. |
| Requirements | Windows 11, Git, Python 3.14; TypeSafe key to turn on Jev; other model keys for résumé writing. |
| License | [MIT](https://github.com/yib7/INployed/blob/09321b7bfcce0031880c5645886cd7826bc5c1d8/LICENSE) |

## When to use

- Run a grounded job search and auto-apply loop on your own machine.
- Mismatch: auto-apply sends real applications; review its gates before turning it on.

## How it works

`local/jev.py` wraps the System One API for the auto-apply loop; when on, Jev makes yes/no calls first in scoring and reads each page while code fills fields from your apply sheet. Integration evidence: [`local/jev.py`](https://github.com/yib7/INployed/blob/09321b7bfcce0031880c5645886cd7826bc5c1d8/local/jev.py).

## Get started

From the upstream README: install Git and Python 3.14 on Windows 11, clone, then follow the setup steps.

```sh
git clone https://github.com/yib7/INployed
# follow README setup on Windows 11
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README pipeline diagram

## Limits and data handling

Posting and page text go to TypeSafe; résumé generation uses other providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 09321b7bfcce](https://github.com/yib7/INployed/tree/09321b7bfcce0031880c5645886cd7826bc5c1d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
