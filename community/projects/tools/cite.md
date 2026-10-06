# Cite

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Elixir library that finds what you describe in a document — failures in a log, hallucinations in a transcript — by gathering candidate passages with fixed rules in code and having a decision model, via the bundled `Cite.Provider.TypeSafe` (Jev), judge each one; questions are written in a Spark DSL.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mdepolli/cite) |
| Maintainer | [mdepolli](https://github.com/mdepolli). Independently curated. |
| Format | Elixir library |
| Requirements | Elixir; `TYPESAFE_API_KEY` for the TypeSafe provider (tests can run without a key via `Req.Test`). |
| License | [MIT](https://github.com/mdepolli/cite/blob/a5969aceaee55ae16642f194b142886d7568b7f9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Scan logs, transcripts or chat histories for passages matching a description without writing regexes for every phrasing.
- Keep the gathering deterministic in code and use the model only for the per-passage judgment.
- Mismatch: Cite does not generate summaries or fixes; it only selects passages.

## How it works

Cite splits a source into passages, asks the provider each concern's question for every passage (e.g. "Does {passage} pose a riddle?" with yes/no descriptions), and gathers matches with fixed rules. `Cite.Provider.TypeSafe` calls Jev and documents its options and retries; it is the only shipped provider and stable through its documented options.

## Get started

Add the dependency (0.2.0 on Hex at review) and judge a source (live TypeSafe calls per passage batch):

```sh
# mix.exs
# {:cite, "~> 0.2.0"}
client = Cite.client(Cite.Provider.TypeSafe, api_key: System.fetch_env!("TYPESAFE_API_KEY"))
Cite.judge(client, Cite.source(["Why is a raven like a writing-desk?", "Take some more tea."]), Riddles)
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README Quick start: a `Riddles` policy judging three passages.
- [HexDocs](https://hexdocs.pm/cite) with options, errors and testing without a key.

## Limits and data handling

Passages are sent to TypeSafe. Early (0.2.x); the provider interface may change. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit a5969aceaee5](https://github.com/mdepolli/cite/tree/a5969aceaee55ae16642f194b142886d7568b7f9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
