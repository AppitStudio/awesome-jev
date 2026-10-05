# Sedum

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pre-alpha browser-testing framework: write Playwright tests in TypeScript with plain-English `ai(...)` steps, where TypeSafe Jev (default) resolves which element a sentence means and judges whether a claim holds on the page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sedum-dev/sedum) |
| Product homepage | [sedum.dev](https://sedum.dev) |
| Maintainer | [sedum-dev](https://github.com/sedum-dev). Independently curated. |
| Format | Test framework and CLI (pre-alpha) |
| Requirements | Node.js 20.19+, Git, a Playwright Chromium install; `TYPESAFE_API_KEY` (default provider), a compatible endpoint via `TYPESAFE_BASE_URL`, or Cloudflare Clef. Linux and macOS verified; Windows experimental. |
| License | [MIT](https://github.com/sedum-dev/sedum/blob/c7b97540694d3633743e46fa522fa4056caa379d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Write end-to-end tests without maintaining selectors, while keeping assertions in Playwright where you need exactness.
- Run a PR suite with a decision model instead of a per-step LLM agent platform.
- Mismatch: pre-alpha; the test format may change before 1.0.

## How it works

For each `ai(...)` step Sedum sends the sentence and a bounded page description (visible text, element names and roles; not cookies, raw HTML, hidden text or form values; env secrets replaced by placeholders) to the provider's Resolver/Judge interfaces. Results are cached locally in Git metadata to skip repeat lookups ([provider privacy](https://github.com/sedum-dev/sedum/blob/c7b97540694d3633743e46fa522fa4056caa379d/docs/provider-typesafe.md)).

## Get started

Scaffold a project and run the example test headed (live Jev calls):

```sh
mkdir my-sedum-tests && cd my-sedum-tests
npm init -y && git init
npm install -D sedum-cli
npx sedum init
npx sedum browsers install chromium
cp .env.example .env   # set TYPESAFE_API_KEY
npx sedum run tests/example.test.ts --headed
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README checkout example against saucedemo.com; maintainer cost/speed comparison (team PR suite and a 17-step checkout) with method on [sedum.dev](https://sedum.dev). Upstream-reported, not reproduced here.

## Limits and data handling

Visible page text goes to TypeSafe and is billed; experimental `run --affected` also sends the Git diff and test sources. Use `--sensitive-origin` to keep page details and screenshots out of saved results.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit c7b97540694d](https://github.com/sedum-dev/sedum/tree/c7b97540694d3633743e46fa522fa4056caa379d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
