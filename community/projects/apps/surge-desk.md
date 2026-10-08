# Surge Desk

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hackathon demo for 911 surges: each call transcript (multilingual, with location) gets six typed TypeSafe Jev questions in one request — same emergency as an open incident?, what the call adds, severity, life threat — so code can merge duplicates, keep new life-safety facts, split hidden emergencies and rank P1–P4, asking the supervisor when Jev is under 70% sure; nothing is dispatched without human approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/valensangui8/surge-desk) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Live demo](https://rapid-response-command.vercel.app/911) · [replay mode](https://rapid-response-command.vercel.app/911?demo=replay) (reachable 2026-10-08). |
| Pricing and access | Free public demo; self-hosting needs Vercel AI Gateway auth and an optional `TYPESAFE_API_KEY` (billed by TypeSafe; without it judgments fall back to keyword rules). Checked 2026-10-08. |
| Jev evidence | [`src/lib/surgeAi.ts`](https://github.com/valensangui8/surge-desk/blob/7236011025b9cf70411ecd6facb2020b7507840d/src/lib/surgeAi.ts) asks all questions per call in one `@typesafe-ai/sdk` request; [`src/lib/surge.ts`](https://github.com/valensangui8/surge-desk/blob/7236011025b9cf70411ecd6facb2020b7507840d/src/lib/surge.ts) holds the option sets and priority policy. Source inspected at the pinned commit; whether the live demo uses Jev or replays recorded responses was not verified. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [valensangui8](https://github.com/valensangui8). Independently curated. |
| Format | Next.js web app (hackathon prototype) |
| Platform and availability | Web browser (hosted demo on Vercel; self-host with Node). |
| Jev's role | Classifies duplicate vs new emergency, new intel, severity and life threat per call and verifies drafted broadcast messages; code sets priorities and humans approve. |
| Requirements | Node/npm; Vercel AI Gateway credentials (`vercel env pull`); optional `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Demo calibrated triage with a human-approval gate on a realistic surge scenario.
- Study how one multi-question Jev request feeds a code policy.
- Mismatch: a 45-minute hackathon prototype with fictional data — not for real dispatch.

## How it works

Calls are judged against open incidents; code policy marks P1 if life threat ≥ 60% or severity ≥ 3.4, merges same-emergency calls, and an LLM writes short dispatch lines and multilingual known-incident messages that Jev checks against the facts.

## Get started

Run locally (README *Run it*):

```sh
git clone https://github.com/valensangui8/surge-desk.git && cd surge-desk
npm install
vercel env pull .env.local                 # AI Gateway auth
echo "TYPESAFE_API_KEY=..." >> .env.local  # optional
npm run dev                                # http://localhost:3000/911
```

Self-hosted runs bill TypeSafe (Jev) and the AI Gateway models.

## Examples and demos

- [Demo video](https://youtu.be/DwR1v5WSwdY) (1:53).
- Replay mode on the live demo.

## Limits and data handling

Demo transcripts are fictional; self-hosted runs send call text to TypeSafe and the gateway. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 7236011025b9](https://github.com/valensangui8/surge-desk/tree/7236011025b9cf70411ecd6facb2020b7507840d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
