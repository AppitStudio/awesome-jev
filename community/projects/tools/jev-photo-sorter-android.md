# jev-photo-sorter (separates family photos from WhatsApp junk on an Android phone with Jev, deleting nothing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command-line workflow that pulls photos from an Android phone over adb, has Jev look at each non-camera photo (category, real people, circulating chain, document value, sentimental value), shows a review page where you flip mistakes, and moves junk into a `JEV_Quarantine` album you clean up yourself; camera photos with EXIF are kept without asking, and moves can be undone.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/renrai/jev-photo-remover-android) |
| Maintainer | [renrai](https://github.com/renrai). Independently curated. |
| Format | Node.js CLI over adb (TypeScript; no license file) |
| Requirements | Node.js 22.18+, Android platform-tools (`adb`) with USB debugging, and a TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classify.ts`](https://github.com/renrai/jev-photo-remover-android/blob/18a87239121348d610b422ae2b76ef2923b5350e/src/classify.ts) at the pinned commit. |

## When to use

- Clear years of forwarded memes and screenshots from a family phone without losing real photos.
- Mismatch: if you cannot send photo thumbnails to an API; text-only mode is much less accurate.

## How it works

`src/classify.ts` uses the official `@typesafe-ai/sdk` `systemOne` call with the questions in `src/questions.ts` and opts in to experimental image input; `src/policy.ts` maps answers to keep, document, junk or review, with protection always winning. Identical forwarded files reuse the first answer. Integration evidence: [`src/classify.ts`](https://github.com/renrai/jev-photo-remover-android/blob/18a87239121348d610b422ae2b76ef2923b5350e/src/classify.ts).

## Get started

Install, add your key, pull photos, run a 200-photo calibration and review before quarantining.

```sh
npm install
cp .env.example .env   # add TYPESAFE_API_KEY
npm run pull && npm run classify -- --limit 200 && npm run review
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/renrai/jev-photo-remover-android/blob/18a87239121348d610b422ae2b76ef2923b5350e/README.md](https://github.com/renrai/jev-photo-remover-android/blob/18a87239121348d610b422ae2b76ef2923b5350e/README.md)

## Limits and data handling

With `sendImages` on (default), a 768 px copy of each non-camera photo plus file metadata goes to TypeSafe on your key; camera photos never leave the computer.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 18a872391213](https://github.com/renrai/jev-photo-remover-android/tree/18a87239121348d610b422ae2b76ef2923b5350e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
