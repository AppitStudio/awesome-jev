# judge_rails

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rails gem that stores TypeSafe Jev Noul/Choice/Score answers as ordinary, indexable ActiveRecord attributes kept up to date, with SQL scopes such as `urgency_above(0.8)`; also a plain Ruby client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/just-the-v/judge_rails) |
| Maintainer | [just-the-v](https://github.com/just-the-v). Independently curated. |
| Format | Ruby gem with Rails generators and a no-key demo app |
| Requirements | Rails app; `JEV_API_KEY` or `TYPESAFE_API_KEY` (or Rails credentials). The `judge_rails_demo` seed runs without a key. |
| License | [MIT](https://github.com/just-the-v/judge_rails/blob/e6abbb585e90518c9d1a6b9a56513b65cab717b3/LICENSE.txt). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Sort and filter support tickets or reviews by Jev-judged urgency, intent, or sentiment in plain SQL.
- Keep judgments fresh automatically when source columns change.
- Mismatch: one-off scripts do not need persisted columns.

## How it works

`judge_source` names the text; each `judge_attribute` maps to a typed Jev question. Answers are stored in columns (plus a jsonb sidecar) and refreshed when the source changes, so queries need no API call ([README](https://github.com/just-the-v/judge_rails/blob/e6abbb585e90518c9d1a6b9a56513b65cab717b3/README.md)).

## Get started

Add the gem and generate attributes (live Jev calls when records are judged):

```sh
bundle add judge_rails
bin/rails generate judge:install
bin/rails generate judge:attribute Ticket urgency:noul intent:choice frustration:score
bin/rails db:migrate
export TYPESAFE_API_KEY=...
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `judge_rails_demo` boots with 250 pre-judged support tickets and needs no key.

## Limits and data handling

Record text is sent to TypeSafe and billed per judged record. Upstream notes Jev access may require the TypeSafe early-access waitlist, and a `json < 3` pin on activesupport 8.1.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit e6abbb585e90](https://github.com/just-the-v/judge_rails/tree/e6abbb585e90518c9d1a6b9a56513b65cab717b3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
