# HookMeter

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (plus optional FastAPI / Cloudflare Worker backend) that scores social-post drafts as you type with TypeSafe Jev—curiosity, emotional arousal, hook pattern, and clickbait risk—then shows a short rewrite hint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ehui1226/hookmeter-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/ehui1226/hookmeter-jev) |
| Pricing and access | [Load unpacked](https://github.com/ehui1226/hookmeter-jev#1-%E5%AE%89%E8%A3%85-chrome-%E6%89%A9%E5%B1%95) from `extension/`; optional local FastAPI or deploy [`cloudflare_worker.js`](https://github.com/ehui1226/hookmeter-jev/blob/0f495b9bf21dfb6ca0c14489dce288c1346f5178/cloudflare_worker.js). No app purchase fee. Bring a TypeSafe (or OpenRouter) key. Inference can incur charges. Reviewed 2026-09-21. |
| Jev evidence | [`hookmeter_engine.py`](https://github.com/ehui1226/hookmeter-jev/blob/0f495b9bf21dfb6ca0c14489dce288c1346f5178/hookmeter_engine.py) and [`cloudflare_worker.js`](https://github.com/ehui1226/hookmeter-jev/blob/0f495b9bf21dfb6ca0c14489dce288c1346f5178/cloudflare_worker.js) POST Score/Choice/Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or OpenRouter Decisions (`typesafe/jev-1.13`). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; Chrome install and live TypeSafe calls were **not** run. Bundled `test_hookmeter_engine.py` failed without a live/mocked Jev response shape on the review host (4 failures). Distinct from [jevx](jevx.md) / [Vibe Check for X](vibecheck.md) draft scorers. |
| Maintainer | [ehui1226](https://github.com/ehui1226). Independently curated. |
| Format | Manifest V3 Chromium extension **1.0.0** + Python engine + optional Cloudflare Worker. |
| Platform and availability | Chrome: Developer mode → Load unpacked on `extension/`. Content scripts match X/Twitter and generic pages; host permissions include `api.typesafe.ai` and X domains. |
| Jev's role | Judges draft hook quality (curiosity gap, emotional arousal, psychology pattern, clickbait noul) and returns a short Chinese/English rewrite hint. Local heuristics/cache can show instant estimates before the Jev round trip. |
| Requirements | Chromium; `TYPESAFE_API_KEY` (or OpenRouter) for live scoring; optional local Python server. |
| License | [MIT](https://github.com/ehui1226/hookmeter-jev/blob/0f495b9bf21dfb6ca0c14489dce288c1346f5178/LICENSE). |

## When to use

Use it when you want keystroke-level viral-hook telemetry on social drafts with typed Jev dimensions and a tachometer-style UI. Prefer [jevx](jevx.md) for X post discovery plus draft scoring without a backend; prefer [Vibe Check for X](vibecheck.md) for a simpler draft vibe meter. Do not treat scores as audited engagement predictions.

## How it works

A content script watches the compose box (IME-aware debounce). Draft text goes to the local FastAPI server or Cloudflare Worker, which builds typed Score/Choice/Noul questions in `hookmeter_engine.py` / `cloudflare_worker.js` and calls TypeSafe Jev. Results render in a Shadow DOM badge. Draft text leaves the browser when you score live.

## Get started

```sh
git clone https://github.com/ehui1226/hookmeter-jev.git
cd hookmeter-jev
git checkout 0f495b9bf21dfb6ca0c14489dce288c1346f5178
# Chrome → chrome://extensions → Load unpacked → select extension/
# Optional local API: set TYPESAFE_API_KEY and run the upstream FastAPI entry
```

Live scoring sends draft text to TypeSafe (or OpenRouter) and can incur charges.

## Examples and demos

- Upstream README architecture diagram and dual UI themes (Cyber Tachometer / Nordic Zen).
- `test_jev.py` is a live TypeSafe connectivity script (needs a key; not run here).
- Offline engine unit tests were **not** green on the review host without a working mock response.

## Limits and data handling

Draft text reaches TypeSafe/OpenRouter through your configured backend. Extension host permissions are broad (`http://*/*`, `https://*/*` content scripts)—review before loading. Upstream “0 ms / viral” marketing language is author framing, not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 0f495b9](https://github.com/ehui1226/hookmeter-jev/tree/0f495b9bf21dfb6ca0c14489dce288c1346f5178): MIT. AI-assisted source review of README, LICENSE, `extension/manifest.json`, `hookmeter_engine.py`, and `cloudflare_worker.js`. No Chrome load; no live TypeSafe calls. Engine unit tests failed (KeyError/`metrics`) without live mocks—disclosed evidence gap.

Related: [jevx](jevx.md), [Vibe Check for X](vibecheck.md), [PageGrade](pagegrade.md).
