# agrouter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI that asks Jev which coding-agent CLI, model and reasoning effort (Claude Code, Codex or any configured CLI) a prompt needs, then prints the choice as JSON or launches that CLI with it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SvetlovA/agrouter) |
| Maintainer | [SvetlovA](https://github.com/SvetlovA). Independently curated. |
| Format | Go CLI |
| Requirements | Go 1.27+ (or a release build); `claude`/`codex` on PATH for exec mode; TypeSafe API key. |
| License | [MIT](https://github.com/SvetlovA/agrouter/blob/8e3fe6af3d8557eeb317d9ed2e227748bdf9ae06/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pkg/jev/client.go`](https://github.com/SvetlovA/agrouter/blob/8e3fe6af3d8557eeb317d9ed2e227748bdf9ae06/pkg/jev/client.go) at the pinned commit. |

## When to use

- Send trivial prompts to cheap models and hard ones to strong models without editing each call.
- Wrap agent launches in scripts with a JSON decision and per-stage confidence.
- Mismatch: one of several Jev model routers in the catalog; savings depend on your prompts.

## How it works

Decision mode builds typed questions over the configured catalog of CLIs/models/efforts, posts them to TypeSafe through `pkg/jev`, and prints the pick with project complexity and confidence; exec mode adds the chosen model and effort to the CLI's own arguments and runs it. Integration evidence: [`pkg/jev/client.go`](https://github.com/SvetlovA/agrouter/blob/8e3fe6af3d8557eeb317d9ed2e227748bdf9ae06/pkg/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
go install github.com/SvetlovA/agrouter/cmd/agrouter@latest
export TYPESAFE_API_KEY=...
agrouter "rename cnt to count in utils.py"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration template written to `~/.config/agrouter/config` on first routing call.

## Limits and data handling

Prompt text goes to TypeSafe on your key; the chosen agent CLI then receives it under its own terms.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 8e3fe6af3d85](https://github.com/SvetlovA/agrouter/tree/8e3fe6af3d8557eeb317d9ed2e227748bdf9ae06). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
