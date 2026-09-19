# Jev Voice Browser

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

A voice-controlled Playwright reference project for studying decisions over partial speech, page elements, and candidate text spans.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/moritzkremb/jev-voice-browser) |
| Maintainer | [Moritz Kremb](https://github.com/moritzkremb). |
| Format | Node.js browser-control reference implementation with a local voice/text dashboard. |
| Jev's role | Select intent, element, site, and text/URL candidates; judge command completeness and potential destructive actions. |
| Requirements | Node.js 20+, npm, Playwright Chromium, TypeSafe account and `TYPESAFE_API_KEY` (legacy `JEV_API_KEY` accepted). Chrome/Edge and microphone permission for the upstream speech workflow. |
| Model and SDK | `jev-1.13.0`; `@typesafe-ai/sdk` declared as `^0.6.0`. |
| License | [MIT](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/LICENSE). Provider usage can incur charges. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this to explore when a streaming voice command is complete enough to execute,
how to expose typed decisions in an inspector, or how to choose among page elements
without generating scripts. The microphone and controlled browser are separate
windows; typed commands also work through the dashboard.

Treat it as an experimental browser-control example. Its confirmation and failure
handling need further work before use with consequential account actions.

## How it works

The [controller](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/src/controller.js)
debounces transcripts, snapshots the page, and allows up to two overlapping requests.
The [Jev client](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/src/jev.js)
sends transcript, page URL/title, and compact element labels through the SDK's
`systemOne` method. It retains raw answers and request/usage metadata for the UI.

[Questions and thresholds](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/src/constants.js)
are centralized. Choice answers select actions, targets, destinations, and spans;
Noul answers gate command detection, completeness, and destruction; a Score selects
scroll amount. [Application policy](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/src/policy.js)
waits, ignores, offers numbered targets, requests confirmation, or executes through
Playwright. Text candidates are extracted and normalized in code, including filler
removal; the selected text is not necessarily an exact substring of the original
speech. Jev does not generate the payload.

## Get started

The [upstream setup](https://github.com/moritzkremb/jev-voice-browser#run-it) installs
dependencies and Chromium locally:

```sh
git clone https://github.com/moritzkremb/jev-voice-browser.git
cd jev-voice-browser
npm install --ignore-scripts
npx playwright install chromium
cp .env.example .env
```

Set `TYPESAFE_API_KEY` privately in `.env`. Launching and issuing commands is a live
workflow: transcripts and page context go to TypeSafe, visited sites receive browser
traffic, and speech recognition may send audio to the browser vendor's service.
Upstream specifically describes Google processing. API requests can incur charges.

```sh
./run.sh
```

Open `http://localhost:8787` in Chrome. Type `go to example dot com`, or start the
microphone and grant permission. The separate Chromium window should navigate;
the dashboard shows decisions, thresholds, and estimated usage. This launch path
was inspected, not executed during the catalog review.

## Examples and demos

- [Supported phrases](https://github.com/moritzkremb/jev-voice-browser#what-you-can-say) cover navigation, search, typing, scrolling, and tabs.
- [Demo script](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/scripts/demo.js) replays commands against real sites and Jev. `npm run demo` and `npm run demo:ci` are live workflows, even without a microphone.
- [Unit tests](https://github.com/moritzkremb/jev-voice-browser/tree/054db0f3dbf537af63a8117632d3f941ccd520e1/test/unit) use mocked decisions. `npm test` is the upstream offline suite; `npm run test:integration` makes real provider calls when a key is present.
- [Recording walkthrough](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/DEMO.md) is a scripted presentation, not independently reproduced performance evidence.

## Limits and data handling

- Observation is capped at 100 elements with truncated labels; iframe content is not collected. Recognition is configured for `en-US`.
- Low-confidence text selection can fall back to the first heuristic candidate; uncertain typing targets can fall back to a detected search box. These paths can still act.
- Confirmation covers selected click, Enter, and select actions. Numbered disambiguation executes directly without reapplying the destructive-action gate; search-field submission is outside that gate. Missing destruction scores default to zero. These judgments are not an authorization boundary.
- Wait/disambiguation responses can schedule repeated provider calls without a fixed total request cap. The displayed cost uses a hard-coded token rate, not a billing record.
- The SDK uses an eight-second timeout and one retry. On provider failure the controller emits an `error` event, but the server registers no listener for it; this can terminate the process. Browser-action exceptions are logged and followed by a fresh snapshot.
- The server binds to loopback by default, with no application authentication or WebSocket origin validation in the inspected code. Do not expose the control port. `.browser-profile/` persists browser state; attaching through `--cdp` gives access to that browser's existing session.
- The dashboard receives transcripts, page snapshots, and action history. The key remains server-side. “Undo” only navigates back; it cannot reverse a submitted form or other external action.

## Review and maintenance

Reviewed **2026-09-19** at
[`054db0f3dbf537af63a8117632d3f941ccd520e1`](https://github.com/moritzkremb/jev-voice-browser/commit/054db0f3dbf537af63a8117632d3f941ccd520e1).
Inspected README, license, package manifest, launcher, Jev client, questions,
controller, policy, executor, browser/snapshot collection, dashboard speech handling,
unit tests, and live-test/demo entry points.

Executed `node --test test/unit/policy.test.js test/unit/spans.test.js` with an empty
environment except `PATH` and network access denied: **24 tests passed**. These
checks establish mocked policy and parsing behavior only. Dependencies were not
installed; the remaining unit suite, microphone, Chromium workflow, integration
tests, and live model quality were not tested. Upstream timing, accuracy, and cost
claims were not reproduced.

Related: [Jev Browser](jev-browser-tontoko.md) · [Offline computer-use example](../../../examples/computer-use/README.md).
