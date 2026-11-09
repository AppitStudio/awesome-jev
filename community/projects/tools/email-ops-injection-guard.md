# email-ops (Claude Code inbox-triage skill with a TypeSafe Jev prompt-injection guard)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill plus two Python scripts that triage your inbox mail by mail and never send; every mail text first passes a Jev prompt-injection guard whose verdict is shown above it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kevintheo-ai/email-ops) |
| Maintainer | [kevintheo-ai](https://github.com/kevintheo-ai). Independently curated. |
| Format | Claude Code skill + Python scripts (MIT) |
| Requirements | Claude Code, Python, IMAP accounts, and a `TYPESAFE_API_KEY` for the guard. |
| License | [MIT](https://github.com/kevintheo-ai/email-ops/blob/7e68862a3abd88b2d0d1bd532cc308129dd58442/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/injection_guard.py`](https://github.com/kevintheo-ai/email-ops/blob/7e68862a3abd88b2d0d1bd532cc308129dd58442/scripts/injection_guard.py) at the pinned commit. |

## When to use

- Triage mail with an agent while flagging injected instructions.
- Reuse the guard alone via `--check-file` or `--check-stdin`.
- Mismatch: the guard is a second line; numbers were measured on jev-1.13.0.

## How it works

`injection_guard.py` asks Jev seven Noul questions per text (one overall injection question plus hazard checks) and prints one verdict line; the README reports 82.6% recall and 0.7% false alarms on 1,102 texts with `jev-1.13.0`. Integration evidence: [`scripts/injection_guard.py`](https://github.com/kevintheo-ai/email-ops/blob/7e68862a3abd88b2d0d1bd532cc308129dd58442/scripts/injection_guard.py).

## Get started

Clone, create the venv, copy `config/email-ops.example.toml`, set `TYPESAFE_API_KEY` and run `scripts/injection_guard.py --dry-run`.

```sh
git clone https://github.com/kevintheo-ai/email-ops.git && cd email-ops
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kevintheo-ai/email-ops/blob/7e68862a3abd88b2d0d1bd532cc308129dd58442/README.md](https://github.com/kevintheo-ai/email-ops/blob/7e68862a3abd88b2d0d1bd532cc308129dd58442/README.md)

## Limits and data handling

Mail headers and text are sent to TypeSafe for the guard check; no code can send mail.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 7e68862a3abd](https://github.com/kevintheo-ai/email-ops/tree/7e68862a3abd88b2d0d1bd532cc308129dd58442). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
