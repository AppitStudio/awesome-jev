# Jev as LLM

[All projects](../README.md) · [Web apps](README.md#web-apps)

Experimental Next.js web app that makes TypeSafe Jev “chat” one word at a time by asking repeated Choice questions over candidate continuations—with inspectable alternatives and step replay.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/damienen/jev-as-llm) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [jev-as-llm.vercel.app](https://jev-as-llm.vercel.app) |
| Pricing and access | Hosted examples need no key. Live mode uses your OpenRouter key in-browser (BYOK); replies usually cost less than a cent per upstream. No app fee. Checked 2026-09-24. |
| Jev evidence | Hosted demo [jev-as-llm.vercel.app](https://jev-as-llm.vercel.app) and [README](https://github.com/damienen/jev-as-llm/blob/882d6f64dcfca9fd7c56eab891bad00d6447a9be/README.md): browser calls OpenRouter Decisions (Jev) for next-word Choice; CSP limits connect-src to self + openrouter.ai. |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Live BYOK chat not run on the review host. |
| Maintainer | [damienen](https://github.com/damienen). Independently curated. |
| Format | Application |
| Platform and availability | Public web app (Vercel) + MIT source. Release stage: experimental demo. |
| Jev's role | Every generation step is a Jev multiple-choice over ~250 word options (plus lookup/stop). Code owns spacing/grammar caps; Jev never free-writes. |
| Requirements | Modern browser. Optional OpenRouter key for live mode. |
| License | [MIT](https://github.com/damienen/jev-as-llm/blob/882d6f64dcfca9fd7c56eab891bad00d6447a9be/LICENSE). |

## When to use

Use to **see** Jev Choice mechanics as a playful decoder. Prefer normal chat models for real assistants.

## How it works

Browser-side decoder asks Jev which continuation word wins; lookup fans out letter-prefix batches; stop ends the reply. Keys stay in the browser per CSP.

## Get started

1. Open [https://jev-as-llm.vercel.app](https://jev-as-llm.vercel.app).
2. Try recorded examples (no key).
3. For live mode, paste an OpenRouter key with a spend cap.

```sh
git clone https://github.com/damienen/jev-as-llm.git
cd jev-as-llm
git checkout 882d6f64dcfca9fd7c56eab891bad00d6447a9be
npm ci && npm run dev
```

## Examples and demos

- Hosted demo with six recorded example prompts.
- `EXPERIMENT_LOG.md` / `eval/` notes.

## Limits and data handling

Experimental quality—not a general LLM. Live mode spends OpenRouter/Jev budget. Telemetry endpoint receives counts only if enabled.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 882d6f6](https://github.com/damienen/jev-as-llm/tree/882d6f64dcfca9fd7c56eab891bad00d6447a9be). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [Preguntale a Jev](preguntale-a-jev.md), [Jev Asks Until Sure](jev-asks-until-sure.md).
