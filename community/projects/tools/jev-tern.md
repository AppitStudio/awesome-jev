# jev-tern (single-file browser agent that drives a visible Tern picture-in-picture tab with one Jev judgment per step)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Single-file Node.js browser-agent engine for the OMP and Tern desktop setup. Each step makes one request to a Jev judge (which operation, which target, is the goal met) while page readiness, geometry and exact text matches run in code and are passed to the judge as `code_verified` facts. The README reports 1.6, 3.4 and 1.8 seconds on three live Wikipedia tasks against 28.9, 115.5 and 131.5 for browser-use (author's own measurement).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cyriusweng/jev-tern) |
| Maintainer | [cyriusweng](https://github.com/cyriusweng). Independently curated. |
| Format | Node.js ES module (`jevTern.mjs`, MIT) |
| Requirements | Node.js 18 or newer, a `TYPESAFE_KEY` for the Jev judge, any OpenAI-compatible chat endpoint for filling form fields (`TYPING_BASE_URL`, `TYPING_MODEL`, `TYPING_KEY`), and a browser bridge with six calls (`browser.open`, `tab.evaluate`, `tab.clickAt`, `tab.title`, `tab.allowedDomains`, `tab.run`); built for Tern's picture-in-picture WebKit tab. |
| License | [MIT](https://github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/CyriusWeng/status/2118350261110612379)). |
| Jev evidence | [`jevTern.mjs`](https://github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/jevTern.mjs) at the pinned commit. |

## When to use

- Run plain-language web tasks (click, type, select, close popups, jump to a section, click canvas controls) in a browser tab you can watch.
- Return a status (`done`, `blocked`, `stuck`, `budget`, `error`), a 0 to 1 goal probability and per-step evidence for each run.
- Mismatch: it was built for the OMP and Tern desktop setup, runs elsewhere only if you implement the six-call bridge, is logged-out by design and reads only the top frame (no iframes).

## How it works

`jevTern.mjs` posts typed questions to TypeSafe's `/v1/systemone` endpoint with model `jev-1.14.0` (Box questions and canvas mode need 1.14). A DONE needs the operation choice, a goal probability of at least 0.8 and the judge's own confidence of at least 0.6; an action picked below 0.55 attaches a viewport screenshot to the next judgment. Integration evidence: [`jevTern.mjs`](https://github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/jevTern.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
const jt = await import('/path/to/jevTern.mjs');
const r = await jt.run({
  task: "Open today's featured article",
  startUrl: 'https://en.wikipedia.org/wiki/Main_Page',
  maxSteps: 12,
  allowedDomains: ['en.wikipedia.org'],
});
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (how it works, bridge calls, limits): [github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/README.md](https://github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/README.md)
- Benchmark method, raw data and chart: [github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/BENCHMARK.md](https://github.com/cyriusweng/jev-tern/blob/5d8a0461a88946adb790808562f3ac0028ffee2e/BENCHMARK.md)

## Limits and data handling

Page text, element lists and (for canvas pages or low-confidence steps) viewport screenshots of the pages you drive are sent to TypeSafe on your key, at about 4k input tokens per screenshot. The benchmark is the author's own: three live Wikipedia tasks, three runs each. The LICENSE file is MIT with an extra notice that ported browser-use / jev-ultrafast code stays under its own notices, so GitHub reports the license as unrecognized.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 5d8a0461a889](https://github.com/cyriusweng/jev-tern/tree/5d8a0461a88946adb790808562f3ac0028ffee2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
