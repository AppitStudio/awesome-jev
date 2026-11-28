# Guardrail Proxy by royharden (OpenAI-compatible proxy that screens every prompt and response with Jev in one batched call)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in OpenAI-compatible proxy with a review dashboard: each user prompt and model response is screened by Jev in one batched request for PII, prompt injection, jailbreaks, toxicity, exfiltration intent, credential leaks, prompt leakage and off-policy replies, and a pure policy function passes, redacts, flags or blocks it with adjustable thresholds. Fails closed when Jev is unavailable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royharden/guardrail-proxy-bolt) |
| Maintainer | [royharden](https://github.com/royharden). Independently curated. |
| Format | Supabase Edge Functions proxy + React dashboard |
| Requirements | Node.js; a Supabase project, a TypeSafe key and an OpenAI key for the live path. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`supabase/functions/_shared/jev.ts`](https://github.com/royharden/guardrail-proxy-bolt/blob/1ff66658dafc3e331498dae6312569d30e37b0d9/supabase/functions/_shared/jev.ts) at the pinned commit. |

## When to use

- Developers who want a calibrated input/output screen in front of an OpenAI-compatible model.
- Mismatch: a hardened security product; the hosted path was not exercised by the author.

## How it works

`supabase/functions/_shared/jev.ts` posts the batched screening questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`); the proxy and screen functions apply `decide()` to the probabilities and log events. Integration evidence: [`supabase/functions/_shared/jev.ts`](https://github.com/royharden/guardrail-proxy-bolt/blob/1ff66658dafc3e331498dae6312569d30e37b0d9/supabase/functions/_shared/jev.ts).

## Get started

Run the local journey test, which uses the same decision function without live Jev or OpenAI.

```sh
git clone https://github.com/royharden/guardrail-proxy-bolt && cd guardrail-proxy-bolt && npm install
npm run test:journey
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Local journey: [github.com/royharden/guardrail-proxy-bolt#local-journey-no-live-jev-or-openai](https://github.com/royharden/guardrail-proxy-bolt#local-journey-no-live-jev-or-openai)

## Limits and data handling

Prompts and responses go to TypeSafe for screening and to OpenAI for answers. The README says the hosted Supabase path was not exercised. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 1ff66658dafc](https://github.com/royharden/guardrail-proxy-bolt/tree/1ff66658dafc3e331498dae6312569d30e37b0d9). Inspected the README and the proxy, screen and shared Jev modules at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
