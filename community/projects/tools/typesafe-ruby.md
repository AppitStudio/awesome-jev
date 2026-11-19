# typesafe (Ruby) by Robert Evans (dependency-free Ruby client for the full System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ruby 3.2+ gem covering `POST /v1/systemone` and `GET /v1/models` with all four question types (Noul, Choice, Score, Box), images, compression, retries with `Retry-After`, typed errors, response validation and Rails credentials support, using only `Net::HTTP`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/revans/typesafe-ruby) |
| Maintainer | [revans](https://github.com/revans). Independently curated. |
| Format | Ruby gem |
| Requirements | Ruby 3.2+ and a `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/typesafe/client.rb`](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/lib/typesafe/client.rb) at the pinned commit. |

## When to use

- Call Jev from Ruby or Rails with typed questions and calibrated answers, without adding an HTTP dependency.
- Mismatch: if you need an OpenRouter route too, see the other Ruby clients in this catalog.

## How it works

`lib/typesafe/client.rb` builds the request body from typed question objects, posts it to `/v1/systemone` with retries and backoff, and wraps the answer in a `SystemOneResponse` with helpers such as `yes?(0.9)`, `choice`, `confidence` and `score`. Integration evidence: [`lib/typesafe/client.rb`](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/lib/typesafe/client.rb).

## Get started

Add the gem from Git or a local path and ask a question.

```sh
# Gemfile
gem "typesafe", git: "https://github.com/revans/typesafe-ruby"
# then
TYPESAFE_API_KEY=... ruby -Ilib examples/triage.rb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/README.md](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/README.md)
- Triage example: [github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/examples/triage.rb](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/examples/triage.rb)
- Changelog: [github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/CHANGELOG.md](https://github.com/revans/typesafe-ruby/blob/e65f67acb632713b55014b7817993e6c70a37196/CHANGELOG.md)

## Limits and data handling

Not published to RubyGems at the reviewed commit (install from Git or path). Unofficial client; check it against TypeSafe's current API docs.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit e65f67acb632](https://github.com/revans/typesafe-ruby/tree/e65f67acb632713b55014b7817993e6c70a37196). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
