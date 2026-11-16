# HS code lookup by cuongpham2107 (Vietnamese HS-code and import/export tariff lookup on Laravel and Filament, where Jev makes the classification steps)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted Laravel 13 + Filament 5 admin app for Vietnam's import/export tariff schedule. A chat at `/admin/tra-cuu` walks a goods description through Rule 1 and Rule 6 of the HS nomenclature (section, chapter, 4-digit heading, branch, 8-digit code), shows the legal basis, risks and a suggested customs description, charts the probabilities of candidate codes and lists MFN and FTA rates. If the description lacks a deciding criterion, it asks for that criterion instead of guessing. Yearly tariff schedules are loaded from Excel through a Python pipeline; lookups are logged with their confidence. Interface and docs in Vietnamese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cuongpham2107/hs_filament_jev_ai) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/cuongpham2107/hs_filament_jev_ai#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (no license file). You pay TypeSafe for your own calls and any hosting. Checked 2026-11-16. |
| Jev evidence | [`app/Ai/HsLookup/JevClient.php`](https://github.com/cuongpham2107/hs_filament_jev_ai/blob/8b04e90207af19c3d1cf69482d069dcb6697c815/app/Ai/HsLookup/JevClient.php) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [cuongpham2107](https://github.com/cuongpham2107). Independently curated. |
| Format | Laravel 13 + Filament 5 web app (PHP) with a Python tariff-import pipeline |
| Platform and availability | Self-hosted web app (Laravel + Filament admin panel); run on your own server |
| Jev's role | Jev answers each Rule 1/Rule 6 classification step (chapter, heading, branch, code) as typed questions with probabilities. |
| Requirements | PHP 8.3+, Composer, Node.js, uv for the Excel pipeline, a database, and `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Look up Vietnamese HS codes and tariff rates with a visible, step-by-step classification.
- Mismatch: binding customs rulings; results are guidance to check against the official schedule.

## How it works

`app/Ai/HsLookup/JevClient.php` sends each step's Choice and Noul questions through the Laravel AI SDK `classify()` call to the `typesafe` provider set in `config/ai.php` (key `TYPESAFE_API_KEY`); `config/hs.php` leaves the model empty, which means `jev-latest`. `HsLookup.php` builds the step-by-step reasoning from those answers. Integration evidence: [`app/Ai/HsLookup/JevClient.php`](https://github.com/cuongpham2107/hs_filament_jev_ai/blob/8b04e90207af19c3d1cf69482d069dcb6697c815/app/Ai/HsLookup/JevClient.php).

## Get started

Install the Laravel app, set the TypeSafe key, load a tariff schedule and open the lookup chat.

```sh
git clone https://github.com/cuongpham2107/hs_filament_jev_ai && cd hs_filament_jev_ai
composer install && npm install
cp .env.example .env && php artisan key:generate   # add TYPESAFE_API_KEY
php artisan migrate
composer run dev    # http://localhost:8000/admin/tra-cuu
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cuongpham2107/hs_filament_jev_ai/blob/8b04e90207af19c3d1cf69482d069dcb6697c815/README.md](https://github.com/cuongpham2107/hs_filament_jev_ai/blob/8b04e90207af19c3d1cf69482d069dcb6697c815/README.md)

## Limits and data handling

Goods descriptions go to TypeSafe on your key; the tariff data and lookup history stay in your database. Vietnamese-only interface. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 8b04e90207af](https://github.com/cuongpham2107/hs_filament_jev_ai/tree/8b04e90207af19c3d1cf69482d069dcb6697c815). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
