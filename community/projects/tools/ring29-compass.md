# Compass (ring29 labs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

zsh helper that keeps your native completions and adds a plain-English request: type a CLI prefix plus what you want (e.g. `aws ec2` and 'list all instances in table format') and Compass gathers candidates from completions, shell history and local help, then asks TypeSafe Jev to rank them; the chosen command is inserted for review, never executed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ring29-labs/compass) |
| Maintainer | [ring29-labs](https://github.com/ring29-labs). Independently curated. |
| Format | Python 3.10+ package with zsh (tested) and Bash 4+ widgets; no runtime dependencies |
| Requirements | Python 3.10+, zsh on macOS or Linux, and a `TYPESAFE_API_KEY` (`COMPASS_OFFLINE=1` uses keyword ranking without Jev). |
| License | [MIT](https://github.com/ring29-labs/compass/blob/5675cb6bf2220e7c80be2bd5ce7cc96226398983/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Recall the exact flags for a large CLI such as the AWS CLI from a plain-English description.
- Mismatch: requests must start with a CLI prefix; blank-prompt requests and Fish/PowerShell widgets are not supported yet.

## How it works

[`compass/completion.py`](https://github.com/ring29-labs/compass/blob/5675cb6bf2220e7c80be2bd5ce7cc96226398983/compass/completion.py) collects native completions and [`compass/core.py`](https://github.com/ring29-labs/compass/blob/5675cb6bf2220e7c80be2bd5ce7cc96226398983/compass/core.py) merges history and help, deduplicates, and sends up to 254 candidates plus a no-match option to `api.typesafe.ai/v1/systemone` for ranking; [`shell/compass.zsh`](https://github.com/ring29-labs/compass/blob/5675cb6bf2220e7c80be2bd5ce7cc96226398983/shell/compass.zsh) binds the widget.

## Get started

Install into zsh (README *Get started*):

```sh
git clone https://github.com/ring29-labs/compass.git ~/.local/share/compass
export TYPESAFE_API_KEY=...
source ~/.local/share/compass/shell/compass.zsh
```

Each plain-English request is one Jev ranking call billed to your TypeSafe key.

## Examples and demos

- README demo recorded in a real zsh session with the AWS CLI completer and live Jev.
- README *Examples* (offline standalone suggestions).

## Limits and data handling

Your request text and candidate commands (including matching shell-history entries) go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 5675cb6bf222](https://github.com/ring29-labs/compass/tree/5675cb6bf2220e7c80be2bd5ce7cc96226398983). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
