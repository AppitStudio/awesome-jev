# Calendar Curator (Home Assistant)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Home Assistant custom integration that reads events from your calendars, asks Jev whether each one matches a criteria prompt, and mirrors the matches into a target calendar, with caching, reconciliation and a deletion cap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/poesterlin/calendar-curator) |
| Maintainer | [poesterlin](https://github.com/poesterlin). Independently curated. |
| Format | Home Assistant custom integration (Python, HACS) |
| Requirements | Home Assistant; a System One endpoint and key (default endpoint is OpenCode's System One inference URL; TypeSafe also works). |
| License | [MIT](https://github.com/poesterlin/calendar-curator/blob/bba8875d8682b5d5d260a38544b7d21e89fc463b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`custom_components/calendar_curator/jev_client.py`](https://github.com/poesterlin/calendar-curator/blob/bba8875d8682b5d5d260a38544b7d21e89fc463b/custom_components/calendar_curator/jev_client.py) at the pinned commit. |

## When to use

- Copy only the events you care about (for example, kids' activities) from busy calendars into one family calendar.
- Run the filter on a schedule or on demand with a button or service.
- Mismatch: the review-band notifications and pause switch are not built yet.

## How it works

On each sync the integration fetches events, removes duplicates and sends each event's text with your criteria to the configured endpoint through `jev_client.py`; matches above the threshold are mirrored with markers, and stale mirrors are removed (at most 20% per scheduled run). Integration evidence: [`custom_components/calendar_curator/jev_client.py`](https://github.com/poesterlin/calendar-curator/blob/bba8875d8682b5d5d260a38544b7d21e89fc463b/custom_components/calendar_curator/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
# HACS > Custom repositories > add https://github.com/poesterlin/calendar-curator (Integration)
# install Calendar Curator, restart Home Assistant, then add the integration
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Status and setup in the README: [github.com/poesterlin/calendar-curator#readme](https://github.com/poesterlin/calendar-curator#readme)

## Limits and data handling

Event titles and descriptions are sent to the configured System One endpoint. The default endpoint is OpenCode's, not TypeSafe's; check which one you configure.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit bba8875d8682](https://github.com/poesterlin/calendar-curator/tree/bba8875d8682b5d5d260a38544b7d21e89fc463b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
