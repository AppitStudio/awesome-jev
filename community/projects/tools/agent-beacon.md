# Beacon (shared, self-improving memory for coding agents, with Jev evaluation)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Memory layer that records sessions across Claude Code, Codex, Cursor and OpenCode and turns useful corrections into shared memory; Jev is the default evaluator that decides whether a session holds a lesson worth keeping.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Asymptote-Labs/agent-beacon) |
| Maintainer | [Asymptote-Labs](https://github.com/Asymptote-Labs). Independently curated. |
| Format | Go CLI with agent integrations |
| Requirements | macOS or Linux; Homebrew or the install script; a TypeSafe API key for Jev evaluation. |
| License | [MIT](https://github.com/Asymptote-Labs/agent-beacon/blob/b2fe72bc06954b99d949cda0b4c35833eecd6baa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cli/beacon/internal/learning/evaluator.go`](https://github.com/Asymptote-Labs/agent-beacon/blob/b2fe72bc06954b99d949cda0b4c35833eecd6baa/cli/beacon/internal/learning/evaluator.go) at the pinned commit. |

## When to use

- Stop repeating the same correction to different coding agents.
- Review memory candidates before they become shared skills.
- Mismatch: the evaluator step needs a key (Jev, or SubQ as an alternative).

## How it works

`evaluator.go` sends a bounded, redacted projection of each trace with rubric questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default); candidates that pass become memory you can approve. Integration evidence: [`cli/beacon/internal/learning/evaluator.go`](https://github.com/Asymptote-Labs/agent-beacon/blob/b2fe72bc06954b99d949cda0b4c35833eecd6baa/cli/beacon/internal/learning/evaluator.go).

## Get started

From the upstream README (not run on the review host):

```sh
brew tap asymptote-labs/tap
brew install beacon
TYPESAFE_API_KEY=... beacon memory evaluations run --limit 10
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [docs.beacon.sh](https://docs.beacon.sh)
- Memory evaluation docs: [docs.beacon.sh/cli/memory](https://docs.beacon.sh/cli/memory)

## Limits and data handling

Redacted trace projections are sent to TypeSafe during evaluation.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b2fe72bc0695](https://github.com/Asymptote-Labs/agent-beacon/tree/b2fe72bc06954b99d949cda0b4c35833eecd6baa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
