# Call Coach

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local live sales-call assistant: it listens (or accepts typed turns), asks TypeSafe Jev after each sentence what the rep should do next, and shows a confidence-aware coaching cue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZeroGold/call-coach-ai) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [Project homepage](https://github.com/ZeroGold/call-coach-ai#readme) |
| Pricing and access | Clone the MIT source and run locally (Node.js ≥ 18). No app purchase fee. Bring a TypeSafe API key via `TYPESAFE_API_KEY`. Optional Electron overlay (`npm run overlay`) pulls heavier native deps. TypeSafe usage can incur charges. Checked 2026-09-21. |
| Jev evidence | [`server.mjs`](https://github.com/ZeroGold/call-coach-ai/blob/0d657db522966d5b7663c1f1d5a0cdfc36172337/server.mjs) posts transcript turns to `https://api.typesafe.ai/v1/systemone` (model `jev-latest` by default) using the typed questions in [`schema.json`](https://github.com/ZeroGold/call-coach-ai/blob/0d657db522966d5b7663c1f1d5a0cdfc36172337/schema.json). Client-side [`public/decide.js`](https://github.com/ZeroGold/call-coach-ai/blob/0d657db522966d5b7663c1f1d5a0cdfc36172337/public/decide.js) maps Choice/Score/Noul answers into act-or-listen UI. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; `node --check server.mjs` clean. Live microphone/TypeSafe calls and Electron overlay were not run. Distinct from [Jev Call Screener](jev-call-screener.md) (inbound call gate vs live sales coaching). |
| Maintainer | [ZeroGold](https://github.com/ZeroGold). Independently curated. |
| Format | Node HTTP demo **1.0.0** (`call-coach`) plus optional Electron shell; static UI under `public/`. |
| Platform and availability | Localhost web UI at `http://localhost:3000`; Chrome/Edge preferred for voice. Work-in-progress demo per upstream README. |
| Jev's role | Judges next-best sales action (Choice), buying stage (Score), and signal Nouls over a capped transcript window. Browser ASR (optional Transformers.js) and UI code own capture and presentation. |
| Requirements | Node.js ≥ 18; `TYPESAFE_API_KEY`. No npm packages required for the basic `node server.mjs` path. |
| License | [MIT](https://github.com/ZeroGold/call-coach-ai/blob/0d657db522966d5b7663c1f1d5a0cdfc36172337/LICENSE). |

## When to use

Use it to explore **sentence-by-sentence sales coaching** with calibrated Jev decisions and a playbook UI. Prefer [Jev Call Screener](jev-call-screener.md) when you need to accept or reject inbound callers. Not a hosted CRM product—local demo only.

## How it works

Each `/analyze` request sends recent turns as `sales_call_transcript` state plus the `schema.json` question set. Jev returns structured answers; `decide.js` applies hysteresis and minimum-score rules so the UI can “keep listening” instead of forcing an action. A **Play sample call** path feeds scripted lines through the same live API without a microphone.

## Get started

```sh
git clone https://github.com/ZeroGold/call-coach-ai.git
cd call-coach-ai
git checkout 0d657db522966d5b7663c1f1d5a0cdfc36172337
TYPESAFE_API_KEY=... node server.mjs
```

Open `http://localhost:3000`, allow the mic if prompted, or use **Play sample call**. Live runs send transcript text to TypeSafe and can incur charges.

## Examples and demos

- Upstream README screenshots and sample-call path.
- This listing: `node --check server.mjs` succeeded; no live TypeSafe or Electron run.

## Limits and data handling

Call transcript text leaves the host on each analyze request. Upstream labels the project a WIP demo. Optional ASR downloads Whisper ONNX models locally. Confirm TypeSafe terms separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 0d657db](https://github.com/ZeroGold/call-coach-ai/tree/0d657db522966d5b7663c1f1d5a0cdfc36172337): **1.0.0**, MIT. AI-assisted source review of README, LICENSE, `server.mjs`, `schema.json`, and `public/decide.js`. No live provider or Microphone tests.

Related: [Jev Call Screener](jev-call-screener.md), [Crush Monitor](crush-monitor.md).
