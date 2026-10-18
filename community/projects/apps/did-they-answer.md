# Did They Answer?

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app that scores how thoroughly the UK government engages with the petitions it answers: Jev rates each response against a published rubric, with a hand-labelled gold set split into tune and holdout to keep prompt changes honest.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TheGoatedDev/Did-They-Answer) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://petitions.thegoated.dev/) |
| Pricing and access | Free public site; MIT source if you self-host with your own OpenRouter key. Checked 2026-10-18. |
| Jev evidence | [`src/lib/judge.ts`](https://github.com/TheGoatedDev/Did-They-Answer/blob/f37ff19df35e9fab126b4e84fa6a2693651faf72/src/lib/judge.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TheGoatedDev](https://github.com/TheGoatedDev). Independently curated. |
| Format | Next.js web app with Postgres (Drizzle), hosted at petitions.thegoated.dev |
| Platform and availability | Web (hosted site; self-hostable) |
| Jev's role | Jev rates each government response against the rubric; the app stores and displays the scores. |
| Requirements | To self-host: Node 24, pnpm, Docker for Postgres, and an OpenRouter key for `typesafe/jev-1.14`. |
| License | [MIT](https://github.com/TheGoatedDev/Did-They-Answer/blob/f37ff19df35e9fab126b4e84fa6a2693651faf72/LICENSE) |

## When to use

- Browse how directly government responses address what UK petitions asked.
- Copy the evaluation loop: two independent labellers, an adjudicator, and a holdout split used only to confirm changes.
- Mismatch: UK Parliament petitions only; scores reflect the author's rubric.

## How it works

Petitions come from the UK Parliament petitions API; `judge.ts` holds the rubric and sends each government response to `typesafe/jev-1.14` through OpenRouter. The author reports about 2,600 calls for roughly $0.20 to judge every response, and averages several eval runs because answers vary by a few points. Integration evidence: [`src/lib/judge.ts`](https://github.com/TheGoatedDev/Did-They-Answer/blob/f37ff19df35e9fab126b4e84fa6a2693651faf72/src/lib/judge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
docker compose up -d db
cp .env.example .env.local   # add OPENROUTER_API_KEY
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [petitions.thegoated.dev/](https://petitions.thegoated.dev/)
- Design notes: `docs/PLAN.md`.

## Limits and data handling

Petition text and government responses are public; self-hosting sends them to OpenRouter on your key.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit f37ff19df35e](https://github.com/TheGoatedDev/Did-They-Answer/tree/f37ff19df35e9fab126b4e84fa6a2693651faf72). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
