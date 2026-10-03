# enigma-jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Software Enigma/Bombe pipeline where TypeSafe Jev ranks cribs and judges whether a trial decryption is German—Bletchley Park’s human analyst steps as typed decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agodoy21/enigma-jev) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Hosted app](https://enigma-jev.vercel.app) — 3D Enigma, research pages, and live break path. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-30**. Hosted machine unlock needs a TypeSafe key (session cookie; key not written to disk per upstream). CLI/local use needs `TYPESAFE_API_KEY`. TypeSafe usage may incur charges. Hosted unlock and live breaks not run on the review host. |
| Jev evidence | Inspected [`src/jev/judge.ts`](https://github.com/agodoy21/enigma-jev/blob/2a6e4e8f32b409906517b7721e0f334b7ff29570/src/jev/judge.ts) and [`src/jev/client.ts`](https://github.com/agodoy21/enigma-jev/blob/2a6e4e8f32b409906517b7721e0f334b7ff29570/src/jev/client.ts): crib ranking and German-plaintext judgment via TypeSafe Jev. Live breaks not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Also noted on HN Show HN. Live TypeSafe paths not run on the review host. |
| Maintainer | [agodoy21](https://github.com/agodoy21). Independently curated. |
| Format | Bun/TypeScript Enigma I/M3/M4 + Bombe + web/CLI; MIT. |
| Platform and availability | Browser (Vercel) or local Bun ≥ 1.3. |
| Jev's role | Crib ranking and plaintext-is-German judgment; code owns Enigma crypto, Bombe search, hill-climb, and UI. |
| Requirements | Bun ≥ 1.3; TypeSafe key for Jev steps. |
| License | [MIT](https://github.com/agodoy21/enigma-jev/blob/2a6e4e8f32b409906517b7721e0f334b7ff29570/LICENSE). |

## When to use

Use it to study typed System One judgments inside a historically grounded crypto pipeline with measurable backtests. Prefer simpler demos when you only want a toy Choice UI.

## How it works

Code implements Enigma machines, crib dragging, Welchman Bombe, and ciphertext-only hill-climb. Jev replaces two analyst calls: which crib to try and whether a candidate plaintext is German. Research and `/jev` pages document discrimination, calibration, and cost without requiring a key.

## Get started

```sh
git clone https://github.com/agodoy21/enigma-jev.git
cd enigma-jev
git checkout 2a6e4e8f32b409906517b7721e0f334b7ff29570
bun install
bun run web
# Open http://localhost:5199 — or https://enigma-jev.vercel.app
```

## Examples and demos

- Hosted: [enigma-jev.vercel.app](https://enigma-jev.vercel.app).
- CLI break of the 1930 Enigma I manual test message (see upstream README).
- Upstream reports 52 tests passing; not re-run on the review host.

## Limits and data handling

Live Jev sends crib/plaintext candidates to TypeSafe and may incur charges. Session key handling is documented upstream; catalog checks did not unlock the hosted machine or run live breaks.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 2a6e4e8](https://github.com/agodoy21/enigma-jev/tree/2a6e4e8f32b409906517b7721e0f334b7ff29570). AI-assisted README and license inspection; install/live paths not executed.
