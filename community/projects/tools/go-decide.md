# go-decide

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI that puts a choice or ordered rubric to a System One model — TypeSafe Jev by default, Cloudflare Clef opt-in — and prints a JSON outcome whose exit code tells your script to act, ask a person or escalate; it gates and labels decisions but never approves them. Early development, no tagged release yet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rshade/go-decide) |
| Maintainer | [rshade](https://github.com/rshade). Independently curated. |
| Format | Go CLI installed with `go install` (pseudo-version until v0.1.0) |
| Requirements | Go toolchain, a `TYPESAFE_API_KEY` (Cloudflare credentials for the Clef backend). |
| License | [Apache-2.0](https://github.com/rshade/go-decide/blob/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let a script fast-path only decisions that are clear enough and send the rest to a human.
- Tune floor/confident thresholds against your own labelled decisions with `go-decide eval`.
- Mismatch: upstream says thresholds are placeholders and confidence is not calibrated; in its 40-decision probe 2 of Jev's 20 `decided` outcomes were not safe to fast-path.

## How it works

[`jevclient/jevclient.go`](https://github.com/rshade/go-decide/blob/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/jevclient/jevclient.go) calls Jev and [`clefclient/`](https://github.com/rshade/go-decide/tree/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/clefclient) calls Clef; the [`decision/`](https://github.com/rshade/go-decide/tree/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/decision) package applies thresholds and builds the envelope. CLI reference: [`docs/jev-decide-cli.md`](https://github.com/rshade/go-decide/blob/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/docs/jev-decide-cli.md); probe write-up: [`docs/probe-2026-09-28.md`](https://github.com/rshade/go-decide/blob/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35/docs/probe-2026-09-28.md).

## Get started

Install and make a first decision (README):

```sh
go install github.com/rshade/go-decide/cmd/go-decide@latest
export TYPESAFE_API_KEY=...
go-decide ask --state "All 412 tests passed and the security scan is clean." \
  --instructions "Is this build ready to release?" \
  --option ship="safe to release" --option hold="needs more work"
```

Each `ask`/`score` is one request to Jev (or Clef), billed to your key.

## Examples and demos

- README *Make your first decision*, scripting with exit codes, and *Know the limits*.

## Limits and data handling

State and options go to TypeSafe (or Cloudflare). Pre-release; boundaries in CONTEXT.md and plans in ROADMAP.md. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit d0afbdd1201c](https://github.com/rshade/go-decide/tree/d0afbdd1201c74c9b7ccc7b5fb2845aa09afeb35). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
