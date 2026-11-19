# Centurion by Roberto Duré (Kafka log consumer that asks Jev to judge each log against your rules and runs actions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript service that consumes logs from Kafka one by one, pre-filters by rule scope in code, asks Jev to evaluate each log against your natural-language rules, records flags and runs actions through a Postgres outbox, with a React dashboard for rules and live events.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RobertoDure/centurion) |
| Maintainer | [RobertoDure](https://github.com/RobertoDure). Independently curated. |
| Format | TypeScript monorepo |
| Requirements | Node 20+, pnpm and Docker (Kafka, Postgres and a bundled jev-mock); a `TYPESAFE_API_KEY` only for live Jev. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/api/src/jev/gateway.ts`](https://github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/apps/api/src/jev/gateway.ts) at the pinned commit. |

## When to use

- Flag log lines that match plain-language rules without writing regexes, with an outbox for actions.
- Mismatch: high-volume log pipelines where one model call per log is too costly; there is no license file.

## How it works

`apps/api/src/jev/gateway.ts` sends each log's state and the matching rules' questions to `/v1/systemone` (or the deterministic `apps/jev-mock` in development); every Jev response is validated with zod and turned into verdicts by a pure rule engine before flags and actions are written in one transaction. Integration evidence: [`apps/api/src/jev/gateway.ts`](https://github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/apps/api/src/jev/gateway.ts).

## Get started

Start the local stack with the mock, then switch to live Jev.

```sh
git clone https://github.com/RobertoDure/centurion
cd centurion
pnpm install
pnpm infra:up      # Kafka, Postgres, jev-mock
cp .env.example .env
pnpm db:migrate
pnpm --filter @centurion/api dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/README.md](https://github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/README.md)
- Jev notes: [github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/docs/JEV_NOTES.md](https://github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/docs/JEV_NOTES.md)
- Rule authoring: [github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/docs/RULE_AUTHORING.md](https://github.com/RobertoDure/centurion/blob/accc9e64affc5cd2e3723ec364da42e1d45359df/docs/RULE_AUTHORING.md)

## Limits and data handling

Log contents are sent to TypeSafe in live mode; the size guard limits state size. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit accc9e64affc](https://github.com/RobertoDure/centurion/tree/accc9e64affc5cd2e3723ec364da42e1d45359df). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
