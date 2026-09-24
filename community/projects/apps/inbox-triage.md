# Inbox Triage

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Private-by-default Gmail labeler: local policy asks TypeSafe Jev (or OpenAI/Anthropic/rules) focused yes/no questions over trimmed excerpts, then adds triage labels only—never archive, send, delete, or mark read.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shimoverse/inbox-triage) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/shimoverse/inbox-triage#readme) — local CLI; no separate commercial site. |
| Pricing and access | MIT source; your Google OAuth desktop client + optional `TYPESAFE_API_KEY` (default `--provider jev`). No app purchase fee, checked **2026-09-24**. Google/TypeSafe billed separately. |
| Jev evidence | Inspected [`src/inbox_triage/providers/jev.py`](https://github.com/shimoverse/inbox-triage/blob/09a0f026609bc620ab2c7fe0005b08f1bab41910/src/inbox_triage/providers/jev.py): POST `{base}/v1/systemone` (default `https://api.typesafe.ai`) with model `jev-latest`. Policy in `policy.py` owns labels. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Gmail/Jev not run. |
| Maintainer | [shimoverse](https://github.com/shimoverse). Independently curated. |
| Format | Python CLI (`uv run inbox-triage`) with local OAuth tokens under `~/.config/inbox-triage/`. |
| Platform and availability | Source build on Python 3.11+ / uv; schedule via cron/launchd/systemd yourself. |
| Jev's role | Default classifier; optional `openai` (local Ollama), `anthropic`, or offline `rules`. Jev answers questions only—code decides labels. |
| Requirements | Python 3.11+; uv; Google Cloud OAuth desktop client with Gmail API; `TYPESAFE_API_KEY` for `--provider jev`. |
| License | [MIT](https://github.com/shimoverse/inbox-triage/blob/09a0f026609bc620ab2c7fe0005b08f1bab41910/LICENSE). |

## When to use

Use it when you want **local Gmail triage labels** with conservative policy and optional Jev. Prefer [Jevmail](jevmail.md) / [JevZero](jevzero.md) for different UX stacks; this tool never mutates beyond verified label adds.

## How it works

Auth stores tokens per account. Each run extracts short subject/excerpt + coarse flags (no full MIME/IDs to the model by design), asks the provider binary topic questions, then `policy.py` maps clear answers to `Triage/*` / `Topics/Shopping` labels and verifies the write.

## Get started

```sh
git clone https://github.com/shimoverse/inbox-triage.git
cd inbox-triage
git checkout 09a0f026609bc620ab2c7fe0005b08f1bab41910
uv sync
# place Google OAuth desktop JSON at ~/.config/inbox-triage/client_secret.json
uv run inbox-triage-auth
uv run inbox-triage --account you@example.com --provider rules --dry-run --max 5
# live Jev: TYPESAFE_API_KEY=... uv run inbox-triage --account you@example.com --provider jev
```

## Examples and demos

- README mermaid pipeline and provider table.
- CI badge; tests not executed on this review host.

## Limits and data handling

With `--provider jev`, trimmed mail excerpts leave the host to TypeSafe. Tokens stay local. Uncertain/suspicious mail is left unchanged. Google *Testing* OAuth refresh tokens expire after seven days unless you publish the app.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 09a0f02](https://github.com/shimoverse/inbox-triage/tree/09a0f026609bc620ab2c7fe0005b08f1bab41910). AI-assisted README + `providers/jev.py` / policy inspection. No live Gmail or TypeSafe spend.

Related: [Jevmail](jevmail.md), [JevZero](jevzero.md), [Jev Mail Classifier](jev-mail-classifier.md).
