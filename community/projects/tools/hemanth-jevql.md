# jevql (hemanth)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

npm `jev-ql` tagged-template and cognitive syntax for calibrated semantic SQL over unstructured rows using TypeSafe Jev System One—distinct from [kylemclaren/jevql](jevql.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hemanth/jevql) |
| Maintainer | [hemanth](https://github.com/hemanth). Independently curated. |
| Format | JavaScript npm package (`jev-ql`). |
| Requirements | Node.js; TypeSafe Jev access for live asks. |
| License | [MIT](https://github.com/hemanth/jevql/blob/64bfad85c3c6137357cf04f32f63796afacccc0a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live queries not run. Distinct from kylemclaren/jevql (Postgres client). |

## When to use

Use for **in-process** semantic SQL/cognitive queries over JS data. Prefer [jevql](jevql.md) (kylemclaren) for a psql-style client against unmodified PostgreSQL.

## How it works

`jevql` templates compile relational filters plus Jev noul/choice/score primitives with pushdown-style planning (per README). Docs site: [hemanth.github.io/jevql](https://hemanth.github.io/jevql/).

## Get started

```sh
npm install jev-ql
# see README tagged-template examples; pin tip 64bfad85c3c6137357cf04f32f63796afacccc0a
```

## Examples and demos

- README cognitive syntax and GROUP BY CHOICE examples.
- Project pages site.

## Limits and data handling

Row text in asks reaches TypeSafe. Not a Postgres server extension.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 64bfad8](https://github.com/hemanth/jevql/tree/64bfad85c3c6137357cf04f32f63796afacccc0a). AI-assisted README inspection; live Jev not run.

Related: [jevql](jevql.md), [JevSQL](jevsql.md), [duckdb-jev](duckdb-jev.md).
