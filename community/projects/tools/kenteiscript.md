# KenteiScript

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small JSON quiz/test DSL (“DSL as harness”) where an LLM authors items and TypeSafe Jev grades free-text answers; includes MulmoKentei, a sample Cloudflare Worker runtime.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/receptron/kenteiscript) |
| Maintainer | [receptron](https://github.com/receptron). Independently curated. |
| Format | JS/TS scripts + Cloudflare Worker sample |
| Requirements | Node/yarn or Wrangler; JEV_URL / TypeSafe credentials for live grading. |
| License | [MIT](https://github.com/receptron/kenteiscript/blob/f155a6e0bfd815f9e63ab4a08decf7e46bbb722e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/mock-jev.mjs`](https://github.com/receptron/kenteiscript/blob/f155a6e0bfd815f9e63ab4a08decf7e46bbb722e/scripts/mock-jev.mjs) at the pinned commit. |

## When to use

- Author quizzes as JSON and grade open answers with a decision model.
- Want a mock `/v1/systemone` for local Worker development.
- Mismatch: DSL + sample runtime; not a full LMS.

## How it works

Workers call a configurable `JEV_URL` System One endpoint. `scripts/mock-jev.mjs` implements a local `POST /v1/systemone` stub for offline development; production points at TypeSafe Jev. Integration evidence: [`scripts/mock-jev.mjs`](https://github.com/receptron/kenteiscript/blob/f155a6e0bfd815f9e63ab4a08decf7e46bbb722e/scripts/mock-jev.mjs).

## Get started

Clone, run the mock Jev stub, and start MulmoKentei with Wrangler as documented.

```sh
git clone https://github.com/receptron/kenteiscript && cd kenteiscript
# yarn + wrangler per README; optional mock-jev.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README KenteiScript overview
- scripts/mock-jev.mjs

## Limits and data handling

Grading quality depends on question design and Jev. Cloudflare sample is illustrative.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit f155a6e0bfd8](https://github.com/receptron/kenteiscript/tree/f155a6e0bfd815f9e63ab4a08decf7e46bbb722e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
