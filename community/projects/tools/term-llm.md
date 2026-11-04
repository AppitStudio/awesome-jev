# term-llm (terminal AI runtime with a `classify` command that asks typed Jev, OpenAI Decisions or Cloudflare Clef questions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal-first AI runtime for commands, chat, editing, tools, jobs and agents. Its `classify` command asks Choice, Score and Noul questions about text, structured state or images and returns decisions instead of prose, with TypeSafe System One (`jev-latest`) as the default provider and OpenAI Decisions and Cloudflare Clef as alternatives that share one question format. Chat features use separate LLM providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SamSaffron/term-llm) |
| Maintainer | [SamSaffron](https://github.com/SamSaffron). Independently curated. |
| Format | Go CLI with embedded web UI (release installer, Homebrew or source build) |
| Requirements | The release installer or Homebrew; a `TYPESAFE_API_KEY` for the default classify provider. |
| License | [MIT](https://github.com/SamSaffron/term-llm/blob/64c6061cf793c28b838f1f5e91b95123c595ec13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/classify/typesafe/client.go`](https://github.com/SamSaffron/term-llm/blob/64c6061cf793c28b838f1f5e91b95123c595ec13/internal/classify/typesafe/client.go) at the pinned commit. |

## When to use

- Script typed routing, safety checks or scoring from the shell with one provider-neutral question file.
- Mismatch: Jev is one classification backend of a much larger runtime; chat and editing do not use it unless you enable classification routing.

## How it works

`internal/classify/typesafe/client.go` posts the typed questions to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`) with bounded retries, and the other provider types translate the same questions to `/v1/decisions` or Cloudflare. Integration evidence: [`internal/classify/typesafe/client.go`](https://github.com/SamSaffron/term-llm/blob/64c6061cf793c28b838f1f5e91b95123c595ec13/internal/classify/typesafe/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/samsaffron/term-llm/main/install.sh | sh
term-llm classify "Production is down" --type noul --question "Is this urgent?"
term-llm classify models
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Classification guide: [term-llm.com/guides/classify/](https://term-llm.com/guides/classify/)
- README with install and quickstart: [github.com/SamSaffron/term-llm#readme](https://github.com/SamSaffron/term-llm#readme)

## Limits and data handling

Classify calls send your text or state to the chosen provider on your key. Environment key fallbacks go only to the provider's default endpoint. Chat and tool features send data to whichever LLM provider you configure. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 64c6061cf793](https://github.com/SamSaffron/term-llm/tree/64c6061cf793c28b838f1f5e91b95123c595ec13). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
