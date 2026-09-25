# Truffler

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Rails intent search gem: TypeSafe Jev builds named-dimension labels at index time and encodes queries the same way, then ranks with SQL over labels, text similarity, and keywords—optional streamed Jev reranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kieranklaassen/truffler) |
| Maintainer | [kieranklaassen](https://github.com/kieranklaassen). Independently curated. |
| Format | Ruby gem for Rails 7.2/8.x (Active Record/Job/Support); no UI components. |
| Requirements | Ruby 3.2+; Rails 7.2 or 8.x; job backend; shared cache with `increment`; TypeSafe Jev via `ruby_llm-typesafe` or your own client; optional pgvector/`neighbor` for embeddings. |
| License | [MIT](https://github.com/kieranklaassen/truffler/blob/c8e41df0ef60d9e3b3d827fad45ca940989fab3c/LICENSE.txt). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Rails/TypeSafe paths not run on the review host. |

## When to use

Use when a **Rails app** needs semantic intent search over your own DB with typed Jev dimensions and tenant scoping. Prefer standalone CLI search tools when you are not on Rails.

## How it works

On save, Jev answers declared noul/choice/score labels into `truffler_labels`. Queries get the same treatment; ranking combines label dot products with text/keyword/exact signals. Optional smart search reranks streamed buckets.

## Get started

```sh
# Gemfile: gem "truffler"; gem "ruby_llm-typesafe"
bin/rails generate truffler:install
bin/rails db:migrate
# Reviewed tree:
git clone https://github.com/kieranklaassen/truffler.git
cd truffler
git checkout c8e41df0ef60d9e3b3d827fad45ca940989fab3c
```

## Examples and demos

- README model declaration sample; `docs/host-integration.md` for UI mapping.
- Upgrade generators for spend ledger tables.

## Limits and data handling

Record fields and queries declared in `reads`/`label` go to TypeSafe for Jev. Backfill spend caps and tenant ledgers need migrations per upstream notes. No bundled UI.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit c8e41df](https://github.com/kieranklaassen/truffler/tree/c8e41df0ef60d9e3b3d827fad45ca940989fab3c). AI-assisted README and LICENSE inspection; Rails install not executed.
