# ruby_decision_model

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Call decision models (Noul, Choice, Score) from Ruby through one stdlib-lean client, with Typesafe's native API and OpenRouter as providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/obie/ruby_decision_model) |
| Maintainer | [obie](https://github.com/obie) / Obie Fernandez. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Ruby gem `ruby_decision_model` (0.1.0 at review); no runtime gems beyond the standard library. |
| Requirements | Ruby **≥ 3.2**. Live calls need `TYPESAFE_API_KEY` (Typesafe provider) or `OPENROUTER_API_KEY` (default OpenRouter provider). |
| License | [MIT](https://github.com/obie/ruby_decision_model/blob/f79a890ce4eaa8f83d8220727319ee7b11416e01/LICENSE.txt). |

## When to use

Use it when a Ruby or Rails-adjacent application needs typed judgments without pulling a large HTTP stack, and you want the same client shape for OpenRouter's decisions endpoint or Typesafe `POST /v1/systemone`. Prefer language-native SDKs if you are not on Ruby.

## How it works

`Client#ask` builds question objects and posts them with a state. The [Typesafe provider](https://github.com/obie/ruby_decision_model/blob/f79a890ce4eaa8f83d8220727319ee7b11416e01/lib/ruby_decision_model/providers/typesafe.rb) uses `https://api.typesafe.ai` + `/v1/systemone` and maps aliases such as `typesafe/jev-1.13` → `jev-latest`. OpenRouter defaults to `typesafe/jev-1.13` on `https://openrouter.ai/api/alpha/decisions`. Retries follow patterns documented alongside the official Typesafe SDKs. Application code still owns thresholds and downstream actions.

## Get started

```ruby
gem "ruby_decision_model"
```

```ruby
require "ruby_decision_model"

client = RubyDecisionModel::Client.new(provider: :typesafe)
response = client.ask(
  state: { title: "Server returns 500 on checkout", reporter: "support" },
  questions: {
    "urgent" => RubyDecisionModel::Questions.noul("Is this urgent?"),
    "severity" => RubyDecisionModel::Questions.score(
      "How severe is this issue?",
      criteria: ["cosmetic", "minor", "major", "critical"]
    )
  }
)
```

`Client.new` with no arguments selects Typesafe when `TYPESAFE_API_KEY` is set, otherwise OpenRouter. Live calls incur provider charges.

Pinned checkout for inspection:

```sh
git clone https://github.com/obie/ruby_decision_model.git
cd ruby_decision_model
git checkout f79a890ce4eaa8f83d8220727319ee7b11416e01
```

Upstream ships unit tests under `test/` (`client_test.rb`, `providers_test.rb`, and others). This review machine had no Ruby runtime, so those tests were not executed here.

## Examples and demos

README quick-start and provider sections. No separate live demo was run.

## Limits and data handling

Request state and questions go to the selected provider. OpenRouter's decisions endpoint is described upstream as alpha and may move. No model-quality claims are made by this listing.

## Review and maintenance

Reviewed on **2026-09-19** at [commit f79a890](https://github.com/obie/ruby_decision_model/tree/f79a890ce4eaa8f83d8220727319ee7b11416e01): gem **0.1.0**, MIT, Ruby ≥ 3.2. AI-assisted source review of the client, Typesafe/OpenRouter providers, question helpers, and README. Unit tests were inspected by path but **not run** (no Ruby on the review host). No live provider calls.

Related: [Advocaat](advocaat.md) is the TypeScript batched-ask client; [Laravel AI](laravel-ai.md) covers PHP/Laravel TypeSafe classification.
