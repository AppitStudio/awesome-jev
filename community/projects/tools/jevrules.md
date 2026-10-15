# jevrules

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Checks code against Cursor's `.cursor/rules` from Claude Code, Codex, a git hook or CI by asking Jev whether each applicable file follows each rule, with probabilities and next commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chrisDeFouRire/jevRules) |
| Maintainer | [chrisDeFouRire](https://github.com/chrisDeFouRire). Independently curated. |
| Format | Go CLI (macOS arm64 and Linux amd64 releases) |
| Requirements | TypeSafe API key; Cursor-style `.cursor/rules` files. |
| License | [MIT](https://github.com/chrisDeFouRire/jevRules/blob/b5e46efda703585bc0dd3c93241902ad7312fd10/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/validator/jev.go`](https://github.com/chrisDeFouRire/jevRules/blob/b5e46efda703585bc0dd3c93241902ad7312fd10/internal/validator/jev.go) at the pinned commit. |

## When to use

- Enforce Cursor rules for agents that never read them.
- Add a rule-conformance check to pre-commit or CI.
- Mismatch: findings are leads with probabilities, not verdicts.

## How it works

jevrules parses the rule files unchanged, works out which rules apply to which files, and sends each file-rule pair to Jev as a typed question; results list rule, file, probability and the next command for an agent. Integration evidence: [`internal/validator/jev.go`](https://github.com/chrisDeFouRire/jevRules/blob/b5e46efda703585bc0dd3c93241902ad7312fd10/internal/validator/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
curl -sL https://github.com/chrisDeFouRire/jevRules/releases/latest/download/jevrules_linux_amd64.tar.gz | tar xz jevrules
sudo mv jevrules /usr/local/bin/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example config: `examples/jevrules.yml`.

## Limits and data handling

File contents checked against rules are sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b5e46efda703](https://github.com/chrisDeFouRire/jevRules/tree/b5e46efda703585bc0dd3c93241902ad7312fd10). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
