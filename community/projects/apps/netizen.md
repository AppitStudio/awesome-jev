# Netizen (simulate how Indonesian netizens react to a post before it goes live, judged by Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Simulator by Moddest Lab: retrieve similar past cases and their real comment mix, let Jev judge which personas (Bekasi mothers, ojol drivers, students, buzzers, news accounts and more) see the post, then run two rounds of reactions across niche, busy and viral reach scenarios. Text and image posts; a hosted demo where you bring your own key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Seheta/netizen) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://moddestlab.com/netizen/) |
| Pricing and access | Free hosted demo with your own TypeSafe key; free source build under MIT. Checked 2026-11-02. |
| Jev evidence | [`spike/rounds.py`](https://github.com/Seheta/netizen/blob/c20b572332c209f5997f95c1c7e4589eb50ce7fc/spike/rounds.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/seT_Troll/status/2117132355911778619)). |
| Maintainer | [Seheta](https://github.com/Seheta). Independently curated. |
| Format | Web app and CLI (Python, vanilla HTML/JS) |
| Platform and availability | Web demo; Python CLI and local web UI. |
| Jev's role | Judges each persona's reaction and stance. |
| Requirements | A browser and your own TypeSafe key for the demo; Python with uv to run locally. |
| License | [MIT](https://github.com/Seheta/netizen/blob/c20b572332c209f5997f95c1c7e4589eb50ce7fc/LICENSE) |

## When to use

- Pre-test how a post might land with different Indonesian audiences.
- Mismatch: weighted personas, not a sample of real people; Indonesian context.

## How it works

`spike/rounds.py` uses `typesafe_sdk` to ask Jev choice and score questions for each persona (take, stance, shift) across rounds; `spike/library_label.py` labels the case library's comments with Jev. Integration evidence: [`spike/rounds.py`](https://github.com/Seheta/netizen/blob/c20b572332c209f5997f95c1c7e4589eb50ce7fc/spike/rounds.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv run spike/run_issue.py --text "your draft post" --platforms X/Twitter,TikTok
uv run spike/server.py   # web UI on localhost:8798
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [moddestlab.com/netizen/](https://moddestlab.com/netizen/)

## Limits and data handling

Your post text or image is sent to TypeSafe with your key; the demo says the key is not stored. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit c20b572332c2](https://github.com/Seheta/netizen/tree/c20b572332c209f5997f95c1c7e4589eb50ce7fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
