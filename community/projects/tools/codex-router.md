# codex-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex CLI model router that picks the model and reasoning effort for each turn (optionally via a System One classifier such as Jev) and shows the choice in Codex's footer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexei-led/codex-router) |
| Maintainer | [alexei-led](https://github.com/alexei-led). Independently curated. |
| Format | Go CLI/proxy with TUI panel |
| Requirements | Codex CLI; macOS/Linux binary or Go; TypeSafe key for the Jev classifier. |
| License | [MIT](https://github.com/alexei-led/codex-router/blob/5521c74637e6c0d222a34b30307a5cd2f00d96e6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/classifier/systemone.go`](https://github.com/alexei-led/codex-router/blob/5521c74637e6c0d222a34b30307a5cd2f00d96e6/internal/classifier/systemone.go) at the pinned commit. |

## When to use

- Send reading and small edits to a light model and repeated failures to the strongest one.
- See the routing choice live in Codex's footer and a TUI panel.
- Mismatch: classifier backends are configurable; Jev is one of them.

## How it works

A local proxy builds a System One route request from the current request and recent dialogue; the classifier's choice selects model and effort before Codex sends the turn. Integration evidence: [`internal/classifier/systemone.go`](https://github.com/alexei-led/codex-router/blob/5521c74637e6c0d222a34b30307a5cd2f00d96e6/internal/classifier/systemone.go).

## Get started

Download a release binary per the upstream README, then (not run on the review host):

```sh
codex-router tui
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- User guide: `docs/user-guide.md`.

## Limits and data handling

Recent dialogue snippets are sent to the configured classifier (TypeSafe when using Jev) and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 5521c74637e6](https://github.com/alexei-led/codex-router/tree/5521c74637e6c0d222a34b30307a5cd2f00d96e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
