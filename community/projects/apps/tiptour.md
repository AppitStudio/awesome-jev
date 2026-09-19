# TipTour

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

A macOS menu bar app for interacting with desktop controls: type a click-based task for Jev, or use a separate Gemini mode for voice and writing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milind-soni/tiptour-macos) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [TipTour project homepage](https://github.com/milind-soni/tiptour-macos) — the reviewed source-build entry point. |
| Pricing and access | No app purchase fee for the MIT source build reviewed **2026-09-19**. Bring a TypeSafe key and optionally a Gemini key; provider usage can incur charges. Packaged-product pricing was not verified. |
| Jev evidence | [Jev client](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Jev/JevClient.swift) and the decision/loop implementation below were source-reviewed. |
| Disclosure | The free-source-build tag applies to source access, not inference or other distributed offerings. Independently curated; no commercial relationship was declared and inclusion is not endorsement. |
| Maintainer | [Milind Soni](https://github.com/milind-soni); independently curated here, not submitted on the maintainer's behalf. No commercial relationship was declared for this listing. |
| Format | Native Swift macOS application using a shared local perception and action engine. |
| Platform and availability | macOS **14.2+**. Reviewed access is a source build with Xcode; compatibility of packaged releases with this Jev mode was not checked. |
| Jev's role | Selects a detected control and click type, and judges completion or absence of a useful target. Gemini powers a separate voice/action mode. |
| Requirements and costs | Current Xcode and a signing team for an app build; a TypeSafe account/key for Jev mode. Optional Gemini mode needs its own key. Source is MIT licensed; provider usage can incur charges. |
| License | [MIT](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/LICENSE), including upstream Clicky attribution. |

## When to use

Use TipTour when you want a desktop interface for short requests such as clicking a visible button or opening a file with a double click. Its text panel shows candidate probabilities, completion and missing-target judgments, and request timing/token counts while the task runs.

The Jev mode supports single, double, and right clicks. It does not generate replacement text, type content, scroll, or interpret images directly. The separate Gemini mode handles voice, writing, and broader desktop actions; those capabilities should not be attributed to Jev.

## How it works

The reviewed [TypeSafe client](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Jev/JevClient.swift) posts to `/v1/systemone` using `jev-latest`, a moving alias. Its request shape matches the [HTTP API](https://docs.typesafe.ai/api) inspected for this review; live compatibility was not exercised.

1. Local perception produces target IDs, labels, sources, and locations. The [question builder](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Jev/JevGrounding.swift) deduplicates targets, keeps up to 200, and adds a no-match option.
2. One request sends the task, detected target descriptions, and action history. Two Choices select the target and click type; two Nouls judge task completion and whether the needed control is absent.
3. Code validates the decision, rejects unknown targets or unsupported click types, and applies its stopping thresholds. It stops when the no-match option wins, the absence probability reaches `0.50`, or the best target probability falls below `0.34`.
4. The [pointer loop](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Jev/JevPointerLoop.swift) checks desktop-action and auto-click settings, checks for app changes, and sends the selected target to the shared action engine with state-change validation requested. It stops on cancellation, a pause/failure, or its action budget.

The default budget is **12 actions**, with up to **13 Jev requests** because a final observation can judge the last action. These are code limits, not performance measurements. The model's completion threshold is `0.70`; it is not an independent guarantee that the user's task succeeded.

## Get started

**First check: isolated tests without provider keys or desktop actions.** Cloning requires network access; the test script creates a temporary Swift package with local source and synthetic responses. It does not install or launch the app.

```sh
git clone https://github.com/milind-soni/tiptour-macos.git
cd tiptour-macos
git checkout d192c21f0fbefa578191e6c329a874142d11fa64
bash scripts/test-jev.sh
```

At the reviewed revision, **8 Swift Testing tests pass**. The script needs a compatible Swift toolchain on macOS; review used Apple Swift **6.2.3**. These tests establish decision-code behavior, not model or desktop-control quality.

**Optional live app use:** Jev requests send task and screen-derived text to TypeSafe and can incur charges. Auto-click executes real desktop actions. Start with a non-sensitive app and a harmless visible control.

1. From the cloned repository, run `open tiptour-macos.xcodeproj`. Select the **TipTour** scheme, set your signing team, and build/run in Xcode. Xcode resolves package dependencies. Follow the pinned [build instructions](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/README.md#build); upstream asks users to avoid terminal app builds while preserving installed macOS permission state.
2. Open **Settings → Models** and add your own JEV/TypeSafe key. The app stores it in macOS Keychain. A Gemini key is only needed for the separate Gemini mode.
3. Grant Accessibility and Screen Recording / Screen Content permissions for inspection and local detection. Enable desktop actions and **Auto-click**. Microphone access is needed for Gemini voice.
4. Focus an app with a visible control, press **Ctrl+K**, and enter a specific click request. For example, “Click Cancel” is an illustrative first task when a harmless dialog has that button; it was not exercised during review. Expect the panel to show a decision and an action result or a stopping reason. Press **Escape** or **Stop** to cancel.

The app build, permissions flow, and live task above were source-reviewed, not executed for this listing.

## Examples and demos

- [Usage instructions](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/README.md#using-tiptour) explain shortcuts, supported actions, stopping, and mode differences.
- [Jev decision tests](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTourTests/JevTests.swift) demonstrate synthetic valid clicks, absent/uncertain targets, no-match selection, invalid responses, tied probabilities, bounded candidates, and missing credentials.
- [Decision panel implementation](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Jev/JevStepPanelView.swift) shows how the app presents judgments and the final status.

No separate credential-free interactive Jev app demo was verified. The test script is the verified offline starting point.

## Limits and data handling

Jev receives the typed task, detected labels/locations, and recent action descriptions. Pixels are not sent to Jev in this path, but screen-derived text can still contain private information. Gemini mode separately sends microphone audio and, when enabled, screenshots. Provider credentials are stored locally in [Keychain](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Utilities/KeychainStore.swift).

The app writes submitted text commands and action/status events to local JSONL files under the user's Application Support `TipTour/logs` directory; see the [command handler](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/App/CompanionManager.swift) and [log store](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/UI/TipTourSettingsWindowManager.swift). The app also configures [PostHog analytics](https://github.com/milind-soni/tiptour-macos/blob/d192c21f0fbefa578191e6c329a874142d11fa64/TipTour/Utilities/TipTourAnalytics.swift), with launch, permission, onboarding, and voice-control event call sites. Runtime telemetry and retention settings were not tested; this is not an entirely local application.

The Jev client surfaces HTTP/decoding failures without an application-level retry loop. Missing or invalid decision fields stop the task. The UI shows selected judgments and a shortlist, rather than an archive of full raw responses. Thresholds and upstream comments about model behavior were not validated on representative tasks.

The click-type question refers to “that element” in a batch where questions cannot consume one another's answers. The target and action may therefore need additional consistency checks in a future adaptation. Model-reported completion and the shared engine's state-change validation also need end-to-end testing before relying on task success. The isolated suite does not exercise the pointer loop, permission enforcement, detection, action execution, or recovery in real applications.

## Review and maintenance

Reviewed **2026-09-19** at [d192c21](https://github.com/milind-soni/tiptour-macos/commit/d192c21f0fbefa578191e6c329a874142d11fa64). AI-assisted inspection covered the README, MIT license, build settings, Jev client/question/decision code, pointer loop, decision panel, key storage, log and analytics paths, and isolated tests. Existing catalog entries and open issues/PRs were checked for duplicates.

Ran `bash scripts/test-jev.sh` in an isolated checkout outside this catalog with a sanitized process environment, using Apple Swift 6.2.3: **8 tests passed** with synthetic answers and no provider requests. The missing-key test injects a nil key provider; it does not read saved credentials. The full app, packaged releases, permissions, live inference, desktop actions, and model quality were not tested. See [catalog validation scope](../../../docs/validation.md#app-directory-review).

Related: [typesafe-computer-use](../tools/typesafe-computer-use.md) is a Python desktop-control implementation; the [computer-use guide](../../../docs/computer-use.md) discusses observation, action, and independent verification.
