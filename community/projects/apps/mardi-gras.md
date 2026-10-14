# Mardi Gras

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Terminal UI for Beads agent issues that can use Jev as an optional fast judge for duplicate checks, focus order, formula choice and Codex approval risk advice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/quietpublish/mardi-gras) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/quietpublish/mardi-gras#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/quietpublish/mardi-gras/blob/c897fbbae931d33294cd67780ef164cc93ca73ca/internal/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [quietpublish](https://github.com/quietpublish). Independently curated. |
| Format | Terminal UI (Go, single binary) |
| Platform and availability | macOS / Linux terminal (Homebrew or source) |
| Jev's role | Jev judges duplicates, ordering and risk; code and the user decide. |
| Requirements | Beads project; optional `MG_JEV_API_KEY` for Jev features. |
| License | [MIT](https://github.com/quietpublish/mardi-gras/blob/c897fbbae931d33294cd67780ef164cc93ca73ca/LICENSE) |

## When to use

- Watch coding-agent issues as a live 'parade' in the terminal.
- Get Jev duplicate warnings and risk readings without letting it auto-approve anything.
- Mismatch: Jev features are optional; the TUI works without them.

## How it works

With a key set, mg sends a redacted issue snapshot (title, type, status, priority, labels, ages, start of description) to Jev for yes/no, choice and score judgments, caches verdicts per snapshot, and degrades to plain behavior when Jev is off or slow. Integration evidence: [`internal/jev/client.go`](https://github.com/quietpublish/mardi-gras/blob/c897fbbae931d33294cd67780ef164cc93ca73ca/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
brew install matt-wright86/homebrew-tap/mardi-gras
mg
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev guide: `docs/jev.md`.

## Limits and data handling

Redacted issue snapshots are sent to TypeSafe (or `MG_JEV_URL`) and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit c897fbbae931](https://github.com/quietpublish/mardi-gras/tree/c897fbbae931d33294cd67780ef164cc93ca73ca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
