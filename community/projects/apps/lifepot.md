# LifePot

[All projects](../README.md) · [Web apps](README.md#web-apps)

Replayable artificial-life game where Jev proposes species roles, relationships and bounded rule changes from your three answers, and validated rules (not code) drive a deterministic ecosystem.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tugrulguner/lifepot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://lifepot.modepot.io) |
| Pricing and access | Free to play on the hosted site; free source build with your own TypeSafe key. Checked 2026-10-15. |
| Jev evidence | [`src/app/api/judge/setup-intent.ts`](https://github.com/tugrulguner/lifepot/blob/accf99d7907f2dcadfc5b8c83473ef40486d9625/src/app/api/judge/setup-intent.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tugrulguner](https://github.com/tugrulguner). Independently curated. |
| Format | Web app (Next.js, TypeScript) |
| Platform and availability | Web (hosted at lifepot.modepot.io or self-hosted) |
| Jev's role | Jev proposes ecosystem rules; code validates and executes them. |
| Requirements | Node.js to self-host; TypeSafe key optional (labeled deterministic fallback without one). |
| License | [MIT](https://github.com/tugrulguner/lifepot/blob/accf99d7907f2dcadfc5b8c83473ef40486d9625/LICENSE) |

## When to use

- Play with an ecosystem whose rules come from typed model decisions and can be replayed exactly.
- Study a contract that rejects incomplete or unviable model proposals before execution.
- Mismatch: an experimental game, not a biological forecast.

## How it works

Jev answers typed Choice and Score questions; LifePot accepts only enumerated roles, interactions and settings, validates them with Zod schemas and graph invariants, and records decisions in a ledger so runs replay without calling Jev. Integration evidence: [`src/app/api/judge/setup-intent.ts`](https://github.com/tugrulguner/lifepot/blob/accf99d7907f2dcadfc5b8c83473ef40486d9625/src/app/api/judge/setup-intent.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tugrulguner/lifepot.git && cd lifepot
npm ci
cp .env.example .env.local   # optional: TYPESAFE_API_KEY
npm run dev -- --hostname 127.0.0.1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Play online: [lifepot.modepot.io/play](https://lifepot.modepot.io/play)

## Limits and data handling

Your setup answers go to TypeSafe from the server; on the hosted site the operator's key and limits apply.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit accf99d7907f](https://github.com/tugrulguner/lifepot/tree/accf99d7907f2dcadfc5b8c83473ef40486d9625). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
