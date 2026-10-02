# IntentSQL

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local natural-language SQLite playground: inspectable semantic decisions, typed plans, deterministic SQL, and guarded writes via TypeSafe Jev / System One.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Amine-LG/IntentSQL) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Amine-LG/IntentSQL#readme) |
| Pricing and access | Free source build; no app purchase fee. Bring your own TypeSafe/compatible key; provider usage may incur charges. Checked 2026-10-02. |
| Jev evidence | [Upstream README](https://github.com/Amine-LG/IntentSQL/blob/f615d3c00a8b889ac769d30ce357414c5b4ac1c0/README.md) describes Jev/System One decisions for query plans and guarded writes. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/UI paths not run on the Linux review host. |
| Maintainer | [Amine-LG](https://github.com/Amine-LG). Independently curated. |
| Format | Python · local web playground (uvicorn, MIT) |
| Platform and availability | Local web (uvicorn) on Node/Python host |
| Jev's role | Jev answers typed plan/guard questions; the app owns SQL generation, review, and writes. |
| Requirements | Python venv; TypeSafe or compatible System One endpoint for live decisions. |
| License | [MIT](https://github.com/Amine-LG/IntentSQL/blob/f615d3c00a8b889ac769d30ce357414c5b4ac1c0/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Local natural-language SQLite playground: inspectable semantic decisions, typed plans, deterministic SQL, and guarded writes via TypeSafe Jev / System One. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/Amine-LG/IntentSQL.git
cd IntentSQL
git checkout f615d3c00a8b889ac769d30ce357414c5b4ac1c0
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit f615d3c00a8b](https://github.com/Amine-LG/IntentSQL/tree/f615d3c00a8b889ac769d30ce357414c5b4ac1c0). AI-assisted README and license inspection; live paths not executed.
