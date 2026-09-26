# AskJev (openconstruct)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Static single-file web app that asks TypeSafe Jev yes/no questions (Noul) through OpenRouter and shows YES/NO plus the raw probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/openconstruct/askjev) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/openconstruct/askjev#readme) — static `index.html`; no separate commercial site. |
| Pricing and access | Host or open the MIT file locally; bring an OpenRouter API key (localStorage). No app fee; provider usage separate. Checked **2026-09-26**. |
| Jev evidence | [`index.html`](https://github.com/openconstruct/askjev/blob/d2854b108e6c39b0c4686db1e1230bf3877bf8a7/index.html) posts Noul questions to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live install/provider paths not run on the review host. Distinct from the pZacca askjev MCP server. |
| Maintainer | [openconstruct](https://github.com/openconstruct). Independently curated. |
| Format | Single static HTML page (no framework). |
| Platform and availability | Any static host or local file/server. No hosted demo URL verified. |
| Jev's role | One Noul question per submit; UI maps ≥0.5 → YES else NO and shows percentage. |
| Requirements | Modern browser; OpenRouter key with Jev/Decisions access. |
| License | [MIT](https://github.com/openconstruct/askjev/blob/d2854b108e6c39b0c4686db1e1230bf3877bf8a7/LICENSE). |

## When to use

Use for a **minimal browser yes/no** demo of Jev Noul. Prefer MCP/CLI tools for agent integration. Distinct from [askjev MCP (pZacca)](https://github.com/pZacca/askjev).

## How it works

The page builds a Decisions API request with `state.question` and a Noul `answer` question; no server stores the key beyond localStorage.

## Get started

```sh
git clone https://github.com/openconstruct/askjev.git
cd askjev
git checkout d2854b108e6c39b0c4686db1e1230bf3877bf8a7
# open index.html in a browser (or serve statically); paste OpenRouter API key
```

## Examples and demos

- Upstream README request/response examples.
- No analytics backend.

## Limits and data handling

Question text goes to OpenRouter→Jev. 50% thresholding is a UI choice. Thin surface by design.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit d2854b1](https://github.com/openconstruct/askjev/tree/d2854b108e6c39b0c4686db1e1230bf3877bf8a7). AI-assisted source inspection; live paths not executed.
