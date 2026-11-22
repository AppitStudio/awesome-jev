# is_even_ai by Chayut Orapinpatipat (parody Ruby gem that asks Jev whether an integer is even)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A deadpan, zero-dependency Ruby gem that answers whether an integer is even by asking TypeSafe Jev (or OpenAI, Claude, Gemini or any OpenAI-compatible endpoint), complete with a migration prompt for your coding agent, caching and refinements. The README is clear that `n.even?` is faster, free, offline and correct; it is a joke and a compact, readable example of a Jev `noul`, `choice` and `score` client in Ruby.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chayuto/is_even_ai) |
| Maintainer | [chayuto](https://github.com/chayuto). Independently curated. |
| Format | Ruby gem (published on RubyGems) |
| Requirements | Ruby 3.2+; `TYPESAFE_API_KEY` for the Jev provider. |
| License | [MIT](https://github.com/chayuto/is_even_ai/blob/56c8b8976940adcc1e104d6ec060390a2205f9ef/LICENSE.txt) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/is_even_ai/providers/jev.rb`](https://github.com/chayuto/is_even_ai/blob/56c8b8976940adcc1e104d6ec060390a2205f9ef/lib/is_even_ai/providers/jev.rb) at the pinned commit. |

## When to use

- A light-hearted demo of typed decisions, or a short reference for calling the System One API from Ruby.
- Mismatch: actually checking parity; use `Integer#even?`.

## How it works

`lib/is_even_ai/providers/jev.rb` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and can ask the question as a `noul`, a `choice` (parity) or a five-level `score` (evenness); `RESEARCH.md` documents the wire schemas and models the cost per million checks. Integration evidence: [`lib/is_even_ai/providers/jev.rb`](https://github.com/chayuto/is_even_ai/blob/56c8b8976940adcc1e104d6ec060390a2205f9ef/lib/is_even_ai/providers/jev.rb).

## Get started

Install the gem, configure the Jev provider once and ask.

```sh
gem install is_even_ai
export TYPESAFE_API_KEY=...
ruby -e 'require "is_even_ai"; IsEvenAI.configure { |c| c.provider = :jev; c.cache = true }; p IsEvenAI.even?(42)'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Cost and wire-format research: [github.com/chayuto/is_even_ai/blob/56c8b8976940adcc1e104d6ec060390a2205f9ef/RESEARCH.md](https://github.com/chayuto/is_even_ai/blob/56c8b8976940adcc1e104d6ec060390a2205f9ef/RESEARCH.md)
- RubyGems: [rubygems.org/gems/is_even_ai](https://rubygems.org/gems/is_even_ai)

## Limits and data handling

Every uncached check sends the integer to the provider and costs money (modelled at $4.20 per million checks for Jev in RESEARCH.md). A parody and educational project by the author's own description.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 56c8b8976940](https://github.com/chayuto/is_even_ai/tree/56c8b8976940adcc1e104d6ec060390a2205f9ef). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
