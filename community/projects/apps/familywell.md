# FamilyWell (self-hostable family organizer whose optional TypeSafe key lets Jev sort shopping items and expenses filed under Other)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Family organizer with shared shopping lists, tasks, calendar, spending, projects and recipes, built as a small core plus modules you switch on per family. With a TypeSafe key, items added to a shop's catch-all Other aisle are sorted into the best-fit aisle and expenses saved as Other get a category, with a one-tap backlog sort. The source is PolyForm Noncommercial: free for personal use, not for commercial use or resale.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bvdr/familywell) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://familywell.co) |
| Pricing and access | Self-hosting is free for personal, noncommercial use under PolyForm Noncommercial 1.0.0; commercial use is not allowed. The hosted version's pricing was not verified. TypeSafe calls use your own key. Checked 2026-11-04. |
| Jev evidence | [`app/Support/TypeSafe.php`](https://github.com/bvdr/familywell/blob/5e178dbc58990fba9dbe310b9fe79f7baa78e6b8/app/Support/TypeSafe.php) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [bvdr](https://github.com/bvdr). Independently curated. |
| Format | Laravel (PHP 8.2) and React app with Docker Compose self-hosting |
| Platform and availability | Self-hosted web app (installable PWA); a hosted version exists at familywell.co. |
| Jev's role | Optionally sorts shopping items and expenses filed under Other into the best-fit aisle or category. |
| Requirements | PHP 8.2+, Composer and Node 22+ (or Docker); a `TYPESAFE_API_KEY` for the optional categorisation. |
| License | [PolyForm Noncommercial 1.0.0](https://github.com/bvdr/familywell/blob/5e178dbc58990fba9dbe310b9fe79f7baa78e6b8/LICENSE) |

## When to use

- Self-host a family organizer and see a small, optional Jev call that never blocks saving.
- Mismatch: Jev is one optional nicety, and the PolyForm Noncommercial license forbids commercial use.

## How it works

`app/Support/TypeSafe.php` posts the item or expense text and typed questions to `https://api.typesafe.ai/v1/systemone`; each caller checks that a key is configured and treats failures as no result, so saved data is never lost. Integration evidence: [`app/Support/TypeSafe.php`](https://github.com/bvdr/familywell/blob/5e178dbc58990fba9dbe310b9fe79f7baa78e6b8/app/Support/TypeSafe.php).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bvdr/familywell.git
composer install && npm install
composer dev   # or: docker compose up -d with the published compose file
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with module list, self-hosting and AI categorisation: [github.com/bvdr/familywell#readme](https://github.com/bvdr/familywell#readme)
- Hosted version and live demo: [familywell.co](https://familywell.co)

## Limits and data handling

With a key, shopping item and expense text go to TypeSafe on your key; nothing is sent without it. License is PolyForm Noncommercial 1.0.0 (source available, not open source). The hosted familywell.co service and its pricing were not reviewed. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 5e178dbc5899](https://github.com/bvdr/familywell/tree/5e178dbc58990fba9dbe310b9fe79f7baa78e6b8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
