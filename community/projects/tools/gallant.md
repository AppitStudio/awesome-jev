# Gallant (decision-model linter for code and docs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-binary Go linter that checks code, documents and other text files against fuzzy rules you write (for example, comments that repeat the code), answered by decision models: Jev through OpenCode Zen by default, or Cloudflare Clef and others.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/madxmike/gallant) |
| Maintainer | [madxmike](https://github.com/madxmike). Independently curated. |
| Format | Go CLI |
| Requirements | Go (or a release binary); an OpenCode API key for jev-1.13 (jev-1.13-free needs none), or another provider's key. |
| License | [MIT](https://github.com/madxmike/gallant/blob/706f7d531100c5ea8515a519e746891cd1db7d46/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`eval/opencode/opencode.go`](https://github.com/madxmike/gallant/blob/706f7d531100c5ea8515a519e746891cd1db7d46/eval/opencode/opencode.go) at the pinned commit. |

## When to use

- Lint for rules that deterministic linters can't express.
- Run rule checks in CI with no Python or Node runtime.
- Mismatch: large files can exceed decision-model input limits; chunk them yourself.

## How it works

`eval/opencode/opencode.go` sends each file and rule to OpenCode Zen's System One gateway serving Jev (`jev-1.13` or `jev-1.13-free`); rules live in `.agents/gallant` by default. Integration evidence: [`eval/opencode/opencode.go`](https://github.com/madxmike/gallant/blob/706f7d531100c5ea8515a519e746891cd1db7d46/eval/opencode/opencode.go).

## Get started

From the upstream README (not run on the review host):

```sh
go install github.com/madxmike/gallant/cmd/gallant@latest
gallant .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Providers and rules help: `gallant --help providers`, `gallant --help rules`

## Limits and data handling

Linted file content is sent to the chosen provider.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 706f7d531100](https://github.com/madxmike/gallant/tree/706f7d531100c5ea8515a519e746891cd1db7d46). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
