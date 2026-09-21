# jev-feels

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ruby gem that turns TypeSafe Jev into ordinary Ruby: `feels?`, `decide`, `score`, Rails/ActiveModel validations, and optional String refinements—without writing prompt strings at the call site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Qew7/jev-feels) |
| Maintainer | [Qew7](https://github.com/Qew7). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Ruby gem **jev-feels** **1.1.0** (`gem "jev-feels"`); stdlib `Net::HTTP` client. |
| Requirements | Ruby **≥ 3.2**; live calls need `JEV_API_KEY` (or configured `api_key`) for `https://api.typesafe.ai/v1/systemone`. |
| License | [MIT](https://github.com/Qew7/jev-feels/blob/7a1b34c594da02c7b1c1efd0d4fb73f2bfff14ea/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, `lib/jev/transport.rb`, `lib/jev/client.rb`, ActiveModel helpers). `bundle exec rspec` was not run in this environment (Bundler could not install gems). No live TypeSafe calls. Distinct from [feelings](feelings.md) (BAML) and [ruby_decision_model](ruby-decision-model.md) (generic Ruby client). |

## When to use

Use it when you want named semantic checks as methods on models or strings in Ruby/Rails (`email.feels?(:urgent)`, `validates_feeling`). Prefer [feelings](feelings.md) inside BAML, or [ruby_decision_model](ruby-decision-model.md) for a thinner client without the ActiveModel DSL.

## How it works

[`lib/jev/transport.rb`](https://github.com/Qew7/jev-feels/blob/7a1b34c594da02c7b1c1efd0d4fb73f2bfff14ea/lib/jev/transport.rb) posts JSON to `v1/systemone` under `https://api.typesafe.ai`. [`lib/jev/client.rb`](https://github.com/Qew7/jev-feels/blob/7a1b34c594da02c7b1c1efd0d4fb73f2bfff14ea/lib/jev/client.rb) uses model `jev-latest`. `Jev.define` registers named Noul/Choice/Score questions; `Jev::Model` / `feels` / `decide` / `validates_feeling` bind fields to those definitions. Validation skips (e.g. `allow_blank`) avoid HTTP. Upstream documents that judged text is sent to TypeSafe.

## Get started

```sh
# Gemfile
gem "jev-feels"
```

```ruby
# config/initializers/jev.rb
Jev.configure { |c| c.api_key = ENV.fetch("JEV_API_KEY") }
Jev.define :urgent, "Requires immediate attention or action"
```

From the reviewed tip:

```sh
git clone https://github.com/Qew7/jev-feels.git
cd jev-feels
git checkout 7a1b34c594da02c7b1c1efd0d4fb73f2bfff14ea
# bundle install && bundle exec rspec   # not run in this listing environment
```

Live calls need a TypeSafe-compatible key and can incur charges.

## Examples and demos

- README Rails `SupportEmail` / PORO / String refinement examples.
- Specs under `spec/` (not executed here).

## Limits and data handling

Field text leaves the host on live Jev checks. Thresholds and routing belong in your code. Confirm TypeSafe billing separately. Upstream demo narratives were not independently measured.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 7a1b34c](https://github.com/Qew7/jev-feels/tree/7a1b34c594da02c7b1c1efd0d4fb73f2bfff14ea): **1.1.0**, MIT. AI-assisted source review of README, LICENSE, client/transport, and model helpers. No live provider calls; RSpec not run here.

Related: [feelings](feelings.md), [ruby_decision_model](ruby-decision-model.md).
