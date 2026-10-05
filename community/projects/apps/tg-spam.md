# TG-Spam

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

Self-hosted Telegram anti-spam bot and Go library (maintained since 2023); its optional Jev provider asks one typed spam question (plus an optional gibberish question) and thresholds the returned probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/umputun/tg-spam) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [tg-spam.umputun.dev](https://tg-spam.umputun.dev) |
| Pricing and access | Free MIT source build (binary, Homebrew, or Docker per upstream). The Jev provider is off by default and requires your own TypeSafe API key; TypeSafe usage is billed separately. Checked 2026-10-05. |
| Jev evidence | [README: Jev integration](https://github.com/umputun/tg-spam/blob/e159ba4fde9b1b2eab1b924260212ed0164b6e1c/README.md) documents `--jev.token`, the pinned `jev-1.13.0` default, the spam/ham criteria, threshold (default 0.30), veto mode, and the optional gibberish question; source not executed. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [umputun](https://github.com/umputun). Independently curated. |
| Format | Self-hosted Go bot / server and Go library |
| Platform and availability | Any host that runs the Go binary or Docker image; operates on Telegram groups via a bot token. |
| Jev's role | Optional LLM-style checker: Jev returns a spam probability that can flip or confirm (veto mode) the base detector's decision, alongside or instead of the OpenAI/Gemini checks. |
| Requirements | Telegram bot token with privacy mode disabled; for Jev, `--jev.token` / `JEV_TOKEN` with a TypeSafe key (setting only `--jev.apibase` does not enable it). |
| License | [MIT](https://github.com/umputun/tg-spam/blob/e159ba4fde9b1b2eab1b924260212ed0164b6e1c/LICENSE). |

## When to use

- Moderate a public Telegram group with layered detectors (samples, heuristics, CAS) and an optional typed Jev spam check.
- Use veto mode so Jev only confirms already-detected spam, reducing false positives.
- Mismatch: if you need a fully local stack with no third-party inference, leave the LLM/Jev providers disabled.

## How it works

When `--jev.token` is set, TG-Spam sends the message (bounded by `--jev.max-symbols-request`) with a spam question and spam/ham criteria to Jev and compares the probability with `--jev.threshold`. `--jev.gibberish-threshold` adds a second question in the same call. Provider results combine with OpenAI/Gemini under the shared `any` / `all` consensus and timeout rules.

## Get started

Install and run the bot with a Telegram token; add the Jev flags to enable the provider (live TypeSafe calls):

```sh
brew tap umputun/apps && brew install umputun/apps/tg-spam
tg-spam --telegram.token=<bot-token> --telegram.group=<group> \
  --jev.token=$TYPESAFE_API_KEY --jev.model=jev-1.13.0 --jev.veto
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README: full `jev:` option list and threshold-tuning guidance (raise toward 0.35 for false positives, lower toward 0.25 for misses).

## Limits and data handling

With Jev enabled, message text leaves your host for TypeSafe and each check is billed. Pin a model version (not an alias) so a tuned threshold keeps its meaning. Spam accuracy was not measured in this review.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit e159ba4fde9b](https://github.com/umputun/tg-spam/tree/e159ba4fde9b1b2eab1b924260212ed0164b6e1c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
