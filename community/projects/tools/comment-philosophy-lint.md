# comment-philosophy-lint by coucha (jev-lint rule set that flags code comments restating the code, run on a local or hosted Jev-compatible model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Japanese-documented rule set for jev-lint: comments should explain constraints and rejected alternatives, not restate code or names. Rules such as `comment-restates-code` and `jsdoc-restates-declaration` are judged by a decision model, by default LiquidAI's d1-3B served locally on llama.cpp's `/v1/systemone`, or any Jev-compatible endpoint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cou723/comment-philosophy-lint) |
| Maintainer | [cou723](https://github.com/cou723). Independently curated. |
| Format | jev-lint rule package (TypeScript tests, pnpm) |
| Requirements | jev-lint, pnpm, and a `/v1/systemone` endpoint: a local llama.cpp `llama-server` with d1-3B (as documented), or TypeSafe Jev via `TYPESAFE_BASE_URL` and a key. |
| License | [MIT](https://github.com/cou723/comment-philosophy-lint/blob/ca273bdc7ec38d43a22aa58029a573ec71d75fd4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`README.md`](https://github.com/cou723/comment-philosophy-lint/blob/ca273bdc7ec38d43a22aa58029a573ec71d75fd4/README.md) at the pinned commit. |

## When to use

- Enforce a "comments say why, not what" policy in TypeScript projects with jev-lint.
- Mismatch: if you expect it tuned for hosted Jev; it is documented and calibrated for a local d1-3B.

## How it works

The README configures `.jev-lint.yaml` with the rules under `rules/` and points jev-lint at `TYPESAFE_BASE_URL`; `test/accuracy.test.ts` checks rule verdicts against a labelled corpus. Integration evidence: [`README.md`](https://github.com/cou723/comment-philosophy-lint/blob/ca273bdc7ec38d43a22aa58029a573ec71d75fd4/README.md).

## Get started

Add jev-lint and this package as dev dependencies, start a Jev-compatible server, and run the comments lint script.

```sh
pnpm add -D jev-lint github:cou723/comment-philosophy-lint
llama-server -hf LiquidAI/d1-3B-GGUF:Q8_0 --port 8090
TYPESAFE_BASE_URL=http://127.0.0.1:8090 TYPESAFE_API_KEY=local pnpm lint:comments
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/cou723/comment-philosophy-lint/blob/ca273bdc7ec38d43a22aa58029a573ec71d75fd4/README.md](https://github.com/cou723/comment-philosophy-lint/blob/ca273bdc7ec38d43a22aa58029a573ec71d75fd4/README.md)
- jev-lint: [jevlist.ai/projects/jev-lint](https://jevlist.ai/projects/jev-lint)

## Limits and data handling

With the documented local setup, code stays on your machine; pointing it at TypeSafe sends comments and code to TypeSafe. Accuracy notes and known limits are in the README (Japanese).

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ca273bdc7ec3](https://github.com/cou723/comment-philosophy-lint/tree/ca273bdc7ec38d43a22aa58029a573ec71d75fd4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
