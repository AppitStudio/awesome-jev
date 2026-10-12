# jev-apply

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Fills job applications page by page from your own JSON profile and résumé: rules answer known fields, and a decision model picks which of your facts or options answers each question. Laya (local) is the default; TypeSafe Jev is a one-line backend switch. It stops before the final Submit by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Noface07/SystemOne-Apply) |
| Maintainer | [Noface07](https://github.com/Noface07). Independently curated. |
| Format | Python CLI + local web UI (Playwright) |
| Requirements | Python 3.12+, uv, Playwright; for Jev `DECISION_BACKEND=typesafe` and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Noface07/SystemOne-Apply/blob/c8d36de8c8f07ad8899eb2719edd43790df85cb7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Speed up repetitive job-application forms while keeping every value from your own data.
- Compare decision backends (Laya, Clef, Jev, chat model) on real form wording.
- Mismatch: Jev is optional (Laya default). Automating applications may break site terms; review before submitting.

## How it works

The agent observes each page, applies rules, then asks the selected backend which fact/option fits; long lists are shortlisted to TypeSafe's 255-option limit; safety checks run before acting. Jev integration: [`jev_apply/model.py`](https://github.com/Noface07/SystemOne-Apply/blob/c8d36de8c8f07ad8899eb2719edd43790df85cb7/jev_apply/model.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Noface07/SystemOne-Apply.git
cd SystemOne-Apply
uv sync --extra playwright --extra laya
# set DECISION_BACKEND=typesafe and TYPESAFE_API_KEY in .env to use Jev
```

## Limits and data handling

With Jev, field wording and candidate facts go to TypeSafe (paid API); Laya runs locally. Derived from Browser Use's jev-ultrafast (MIT). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit c8d36de8c8f0](https://github.com/Noface07/SystemOne-Apply/tree/c8d36de8c8f07ad8899eb2719edd43790df85cb7). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
