# brojev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Go browser agent for Claude Code with its own CDP engine, where Jev (via OpenRouter) picks each action and target during a delegated browser sub-task.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/barockok/brojev) |
| Maintainer | [barockok](https://github.com/barockok). Independently curated. |
| Format | Claude Code plugin + Go binary |
| Requirements | Chrome/Chromium on macOS or Linux, OpenRouter API key for `run`. |
| License | [MIT](https://github.com/barockok/brojev/blob/aded1e3bdbfd8dad55349250afe6a20bbf26a154/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/jev.go`](https://github.com/barockok/brojev/blob/aded1e3bdbfd8dad55349250afe6a20bbf26a154/internal/jev/jev.go) at the pinned commit. |

## When to use

- Delegate a browser sub-task from Claude Code with fewer agent turns.
- Mismatch: hook downloads a release binary at session start; review before installing.

## How it works

For `run`, Jev chooses the next operation and target from a page snapshot in one request; the Go daemon executes CDP primitives and hands back when stuck. Integration evidence: [`internal/jev/jev.go`](https://github.com/barockok/brojev/blob/aded1e3bdbfd8dad55349250afe6a20bbf26a154/internal/jev/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add barockok/brojev
claude plugin install brojev@brojev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup command `/brojev:setup` runs a smoke test (per README).
- Eval folder: `eval/`.

## Limits and data handling

Page snapshots go to OpenRouter/TypeSafe. Third-party licenses in `THIRD_PARTY_LICENSES`.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit aded1e3bdbfd](https://github.com/barockok/brojev/tree/aded1e3bdbfd8dad55349250afe6a20bbf26a154). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
