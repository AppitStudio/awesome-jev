# Watermelon

[All projects](../README.md) · [Web apps](README.md#web-apps)

Status-update honesty auditor: paste a weekly program update; TypeSafe Jev judges language while local code parses dates/slippage; the app returns whether the stated health matches the facts and whether escalation is warranted.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shashwatc12/watermelon) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [https://watermelon.shashwatchavan.com](https://watermelon.shashwatchavan.com) (live demo) |
| Pricing and access | MIT source and public demo; no app purchase. Self-host / CLI needs `TYPESAFE_API_KEY`. Demo and live calls use the operator's TypeSafe budget. Checked 2026-09-21. |
| Jev evidence | [`src/jev.js`](https://github.com/shashwatc12/watermelon/blob/b960cbaebb4e9ab9e7bb3177c71d450cbce96bd0/src/jev.js) posts one multi-question System One call to `https://api.typesafe.ai/v1/systemone` (`jev-latest`). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline tests inspected; live TypeSafe calls were not run on the review host. Upstream eval accuracy figures were not independently reproduced. |
| Maintainer | [shashwatc12](https://github.com/shashwatc12). Independently curated. |
| Format | Portable `Request→Response` core with Node server and Cloudflare Worker hosts (`watermelon` **0.1.0**). |
| Platform and availability | Public web demo; `npm start` local Node; Cloudflare Worker deploy configs included. |
| Jev's role | Six typed questions (health choice, blocked/slipped/escalate noul, spin score, dominant risk choice). Code extracts numeric slip signals and applies `POLICY` thresholds; Jev does not rewrite the update. |
| Requirements | Node.js for local server/CLI; `TYPESAFE_API_KEY` for live assessments (mock mode without a key). |
| License | [MIT](https://github.com/shashwatc12/watermelon/blob/b960cbaebb4e9ab9e7bb3177c71d450cbce96bd0/LICENSE). |

## When to use

Use it when program status prose may overstate health and you want a receipted, thresholded “watermelon?” signal plus escalation cue. Prefer general text classifiers when you do not need date/arithmetic overrides or the portable core. Do not treat demo votes or author-labelled evals as catalog-measured accuracy guarantees.

## How it works

`extract.js` pulls claimed labels and “N weeks late” style facts. `jev.js` sends bounded update text to TypeSafe once. `verdict.js` combines Jev answers with extracted facts and policy floors (for example escalate at `noul >= 0.2`). Optional signed receipts and reviewer votes close the loop on the live demo.

## Get started

```sh
git clone https://github.com/shashwatc12/watermelon.git
cd watermelon
git checkout b960cbaebb4e9ab9e7bb3177c71d450cbce96bd0
npm start                      # http://127.0.0.1:8787 — MOCK without a key
# Live (TypeSafe charges): export TYPESAFE_API_KEY=… && npm start
# Or open https://watermelon.shashwatchavan.com
```

## Examples and demos

- Live demo: [watermelon.shashwatchavan.com](https://watermelon.shashwatchavan.com).
- Offline **`npm test`**: **22 passed** on the review host (core, portable, node server mock paths).
- Upstream `evals/` reports and failure-mode probes (author-run; not re-executed here).

## Limits and data handling

Update text goes to `api.typesafe.ai` on live runs; the API key stays in the host environment. Upstream error bodies are not forwarded. Mock mode never claims live Jev numbers. Thresholds were tuned on author-written labels; the demo collects reviewer votes to retune.

## Review and maintenance

Reviewed on **2026-09-21** at [commit b960cba](https://github.com/shashwatc12/watermelon/tree/b960cbaebb4e9ab9e7bb3177c71d450cbce96bd0): **0.1.0**, MIT. AI-assisted source review of README, `src/jev.js`, `src/verdict.js`, and tests. **`npm test`**: **22 passed**. No live TypeSafe calls.

Related: [Hx](hx.md), [JevEye](jeveye.md).
