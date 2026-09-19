# macbrow

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

An experimental voice assistant for macOS that uses Jev to route spoken requests to AppleScript tools or multi-step Chrome tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timpratim/macbrow) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [macbrow project homepage](https://github.com/timpratim/macbrow) — source-run access, with no separate product website listed. |
| Pricing and access | The [MIT source and setup](https://github.com/timpratim/macbrow#setup) have no app purchase fee, checked **2026-09-19**. TypeSafe and Gradium accounts/keys are required for voice use; the default LLM backend also needs LiveKit credentials. Provider usage can incur charges; service prices and free-tier eligibility were not verified. |
| Jev evidence | Inspected [router](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/macbrow/router.py), [agent](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/macbrow/agent.py), and [browser integration](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/macbrow/browser_task.py); live behavior was not tested. |
| Disclosure | Free source access does not include inference. AI-assisted, independently curated listing; no commercial relationship was declared. Not submitted on the creator's behalf, and inclusion is not endorsement. |
| Maintainer | [Pratim Bhosale / timpratim](https://github.com/timpratim). |
| Format | Python voice application with a local microphone/speaker console and a text CLI. |
| Platform and availability | macOS; experimental **0.1.0** source-run prototype. No packaged app or production readiness was verified. |
| Jev's role | Routes requests, selects arguments, and judges confirmations, browser follow-ups, missing details, and outcomes. Jev Ultrafast supplies browser action selection. Gradium handles speech; a separate LLM handles chat, script generation, and browser text preparation. |
| Requirements | Python **3.12+**, `uv`, macOS Automation permissions, and microphone access for voice. Browser tasks require Chrome remote debugging. Default keys: `TYPESAFE_API_KEY`, `GRADIUM_API_KEY`, `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET`. LM Studio is an optional local LLM backend, not a replacement for Jev or Gradium. |
| License | [MIT](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/LICENSE). |

## When to use

Explore voice control for opening apps and URLs, controlling media, or performing browser searches with follow-up instructions. The source also shows how an application can combine a typed tool router with a separate code-generation fallback.

This is a prototype for users comfortable inspecting Python and AppleScript, configuring provider keys, and supervising actions on their own Mac. It is not a standalone packaged assistant or an entirely local application.

## How it works

The [registry](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/macbrow/registry.py) offers tools according to the running apps and policy. A Jev Choice selects a tool while independent questions select its possible enum arguments. Only the chosen tool's argument answers are used. **Free-text arguments use a second request** to select spans from the utterance; the one-request routing path does not cover every command.

Application code renders escaped AppleScript arguments, checks policy, asks for clarification or confirmation where configured, and executes through `osascript`. Unknown actions can invoke an LLM to propose a new tool; compilation, policy, effect-pattern checks, and Jev review precede storage in `tools/learned.json`. A newly generated tool requires confirmation before its first execution.

Browser tasks use [Jev Ultrafast](../tools/jev-ultrafast.md) to select operations and observed targets. Macbrow adds Chrome profile selection, goal preparation, text helpers, follow-ups, and outcome judgments. GPT-5-mini through LiveKit Inference is the default generation backend; LM Studio is configurable.

The lockfile pins `typesafe-sdk` **0.7.0** and Jev Ultrafast at [1231850](https://github.com/browser-use/jev-ultrafast/tree/1231850a0bf1a0c0341fe408ef1668dbbfdfac46). Both default to the moving `jev-latest` alias and use `/v1/systemone`. The SDK route can override its model with `TYPESAFE_DEFAULT_MODEL`; the browser dependency uses `TYPESAFE_MODEL`. These are separate settings. Live API compatibility was not exercised.

## Get started

Start with dependency installation and the policy listing. Installation downloads packages; the policy listing makes no provider requests and executes no desktop actions. In a fresh checkout, leave provider keys unset for this first check.

```sh
git clone https://github.com/timpratim/macbrow.git
cd macbrow
git checkout a392a9c56b8ff2978852c0fc911abbeb87b5c5b4
uv sync --locked
uv run --frozen --offline python -m macbrow.cli --policy
```

Expect a strict-policy report marking the seed tools as allowed or blocked. Policy labels describe the code's checks, not a security guarantee. The registry can read Chrome's local profile metadata while rendering built-in placeholders.

**Optional live use:** commands below can send speech, requests, app context, or browser text to providers, incur charges, and perform real desktop actions.

1. Copy `.env.example` to `.env.local` and configure keys privately following the [upstream setup](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/README.md#setup). Keep the default strict policy enabled. Set `MACBROW_LEARN=0` to disable learning in voice mode. When changing optional backend or profile settings, export them before foreground launch: several modules read settings before the entrypoint loads dotenv files.
2. Grant microphone and per-app Automation access when prompted. Tools that simulate UI input may also need Accessibility access. For browser tasks, enable remote debugging at `chrome://inspect/#remote-debugging` and review the selected Chrome profile.
3. Run `uv run python agent.py console` for the foreground voice interface. A simple seed-tool request is “open Safari”; expect execution, a clarification, or a confirmation depending on the route. Voice startup and this live command were not exercised in review.

The upstream text example `uv run python -m macbrow.cli --dry "open github dot com"` still probes local app state and calls Jev. It suppresses action execution and learning; **it is not an offline demo**, and `uv --offline` would only disable dependency fetching.

## Examples and demos

- [Seed tools](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/tools/seed.json) provide real tool definitions, argument slots, and example requests.
- [Tests](https://github.com/timpratim/macbrow/tree/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/tests) cover policy rules, registry behavior, synthetic Chrome profiles, mocked YouTube parsing, and routing helpers.
- [Run instructions](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/README.md#run) describe the voice console and text interface. No separate interactive demo was verified.

The test suite's flight-URL helper attempts LLM query compaction and falls back when unavailable. Do not assume `uv run pytest -q` is provider-free in an environment containing credentials; the review run removed credentials and denied network access.

## Limits and data handling

Gradium receives voice input and speech-output text. TypeSafe receives utterances and app context, and browser tasks send page-derived text, targets, and recent actions. The configured LLM backend receives chat, generation requests, and relevant browser context. LM Studio can keep that generation path local, but Jev and Gradium remain remote services.

Browser automation attaches to real Chrome sessions, which can include signed-in accounts. The profile resolver falls back to the last-used profile if a requested email is not found; the browser attachment code also has a default-context fallback. Profile selection is not an isolation boundary.

The [console wrapper](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/console.sh) writes logs to `/tmp/macbrow-console.log` by default. Logs can contain transcripts, routed arguments, browser objectives, URLs, and entered text. Learned tools persist locally in `tools/learned.json`; keys are configured through environment variables or local dotenv files.

The [policy](https://github.com/timpratim/macbrow/blob/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4/macbrow/policy.py) uses pattern checks and restricted shell commands; browser restrictions also depend on model judgments and instructions. These are not a sandbox or proof against unintended actions. Confirmation is selective, not required for every state change. A Jev script-review error returns no judgment and can allow the compiled tool to proceed to confirmation; browser outcome verification can also be skipped on errors. The routing helpers' tests do not cover these full execution paths.

No latency, task-success, or safety claims were independently measured. Upstream timings are not adopted as catalog performance claims.

## Review and maintenance

Reviewed **2026-09-19** at [a392a9c](https://github.com/timpratim/macbrow/commit/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4). AI-assisted inspection covered the README, license, locked dependencies, voice entrypoint, router, registry, generator, execution/policy paths, browser integration, profile handling, logging, and tests. No duplicate catalog entry or open matching issue/PR was found.

In an isolated checkout outside this catalog, `uv sync --locked` succeeded with Python **3.14.4**. `python -m pytest -q` passed **26 tests** with a sanitized environment, external pytest plugins disabled, a fixed test Chrome profile, and macOS `sandbox-exec` denying network access. `ruff check .` and `ruff format --check .` passed. The credential-free policy listing was also checked; see [catalog validation](../../../docs/validation.md#app-directory-review).

No live provider requests, microphone capture, app-control actions, permission changes, or real Chrome connections were performed. Full voice startup, live routing, generated tools, browser completion, and model quality remain untested.

Related: [TipTour](tiptour.md) offers a different macOS app workflow centered on typed click requests; the [computer-use guide](../../../docs/computer-use.md) explains action selection and independent verification.
