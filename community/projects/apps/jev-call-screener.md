# Jev Call Screener

[All projects](../README.md) · [Web apps](README.md#web-apps)

Open-source call-screening backend: ask why the caller is calling, classify the transcript with TypeSafe Jev, and forward or reject under a fail-open Go routing policy. Twilio adapter included; screening core is provider-independent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SuchintK/jev-call-screener) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/SuchintK/jev-call-screener#jev-call-screener) |
| Pricing and access | [Clone and run from source](https://github.com/SuchintK/jev-call-screener#quick-start); no app purchase fee. Bring `TYPESAFE_API_KEY`; Twilio (or another adapter) and telephony minutes are separate. Reviewed 2026-09-20. |
| Jev evidence | [`internal/adapters/jev/client.go`](https://github.com/SuchintK/jev-call-screener/blob/7f353add3909d0918b6d1c5757cd0bce461355aa/internal/adapters/jev/client.go) posts bounded Choice questions to `https://api.typesafe.ai/v1/systemone`; Go policy owns forward/reject/clarify. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live Twilio calls and live Jev were not tested. |
| Maintainer | [SuchintK](https://github.com/SuchintK). Independently curated. |
| Format | Go 1.27+ HTTP service (`cmd/server`) with Twilio and REST simulator adapters. |
| Platform and availability | Self-host Docker/`make run`; REST classify without telephony via `TELEPHONY_PROVIDER=none`. |
| Jev's role | Classifies caller transcripts into promotional/wanted/uncertain; does not generate dialogue or control the call. |
| Requirements | Go 1.27.1+; `TYPESAFE_API_KEY`; Twilio credentials when using that adapter; public HTTPS base URL for signature validation. |
| License | [MIT](https://github.com/SuchintK/jev-call-screener/blob/7f353add3909d0918b6d1c5757cd0bce461355aa/LICENSE). |

## When to use

Use it to screen inbound calls with calibrated reject/forward decisions and one clarification step. Prefer a hosted PBX feature when you need a managed product rather than a self-hosted backend. Defaults fail open so classifier errors forward rather than silently drop callers.

## How it works

1. Telephony (or REST) captures a transcript of why the caller is calling.
2. `ScreeningService` asks the Jev HTTP adapter a bounded Choice question.
3. Go `RoutingPolicy` rejects only high-confidence promotional calls, forwards high-confidence wanted calls, otherwise clarifies once, then forwards if still uncertain.
4. Jev timeouts/errors fail open by default (see threat model).

## Get started

```sh
git clone https://github.com/SuchintK/jev-call-screener.git
cd jev-call-screener
git checkout 7f353add3909d0918b6d1c5757cd0bce461355aa
cp .env.example .env   # TYPESAFE_API_KEY; TELEPHONY_PROVIDER=none for REST-only
make run
curl -X POST http://localhost:8080/api/v1/classify \
  -H 'Content-Type: application/json' \
  -d '{"transcript":"I am calling to offer you a lifetime free credit card"}'
```

Classify sends transcript text to TypeSafe and can incur charges. This listing did not run the server or live Jev/Twilio.

## Examples and demos

- README REST classify demo and architecture/threat-model docs.
- Adapter tests under `internal/adapters/jev/` (including opt-in live tests).

## Limits and data handling

Caller transcripts leave the host for TypeSafe. Twilio receives audio/signaling per its terms. Fail-open defaults may forward unwanted calls when uncertain—tune thresholds carefully. Upstream live-eval claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 7f353add](https://github.com/SuchintK/jev-call-screener/tree/7f353add3909d0918b6d1c5757cd0bce461355aa): MIT. AI-assisted source review of README, `internal/adapters/jev/client.go`, architecture/threat-model docs, and license. `go test`, Docker build, Twilio, and live TypeSafe calls were not executed on the review host.

Related: [Jevmail](jevmail.md), [Jev Mail Classifier](jev-mail-classifier.md), [Jev Anti-Spam Bot](jev-antispam-bot.md).
