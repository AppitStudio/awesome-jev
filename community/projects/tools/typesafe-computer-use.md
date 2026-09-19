# typesafe-computer-use

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Use this experimental macOS CLI to study how local screen reading and Jev decisions can select the next click, scroll, or text-entry action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/awlevin/typesafe-computer-use) |
| Maintainer | [Aaron Levin](https://github.com/awlevin). Independently curated; no upstream affiliation or sponsorship is asserted. |
| Format | Experimental Python macOS CLI with saved observations and judgments. |
| Requirements | macOS 14+, Python 3.12+, uv; Screen Recording and Accessibility permissions for desktop use. `TYPESAFE_API_KEY`; optional `ANTHROPIC_API_KEY` for writing and final answers. |
| License | [MIT](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/LICENSE). |

## When to use

Choose this as a compact native-Mac reference when the workflow spans app windows or lacks a useful DOM. Its inspectable OCR/Accessibility merge makes it useful for understanding why the agent selected a control. It is an experimental operator, not a ready-made macOS regression-test framework.

| Common workflow | What this project supplies | What you add |
| --- | --- | --- |
| Navigate a native app or locate a labeled control | OCR, Accessibility labels, bounded action choices, and local execution. | An allowed app/window scope and checks before each action. |
| Fill a test form | Focused-field context, optional text writer, and field readback. | Synthetic values, permitted fields, and an exact expected value. |
| Investigate a failed interaction | Numbered screenshots, submitted state, raw judgments, and timing logs. | A reproducible test state and your application's expected result. |
| Prototype a macOS smoke test | A perception and action loop to adapt. | Test setup/reset, assertions, and a failure report; these are not an included testing harness. |

For structured browser forms and source-backed extraction, start with [Jev Browser](jev-browser-tontoko.md). This macOS project is useful when native controls matter; it does not implement an iOS Simulator integration or a general table-extraction API.

## How it works

[Perception](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/typesafe_computer_use/perception.py) combines Apple Vision OCR with native Accessibility labels. [Decision questions](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/typesafe_computer_use/decide.py) select an operation and speculative targets; code uses only the selected branch. Accessibility presses and coordinate fallbacks execute locally. Date parsing and other exact preparation remain in code.

An optional Anthropic model supplies free text or an uncatalogued URL. Text entry also receives a Jev check. The loop stops on low confidence, repeated no-ops, or its step limit. These heuristics do not establish permission or task correctness.

## Get started

### 1. Install and get an offline success

Use a Mac with **macOS 14+, Git, Python 3.12+, and [uv](https://docs.astral.sh/uv/getting-started/installation/)**. No API account or desktop permissions are needed for the mocked tests. Clone into your own projects directory, outside the Awesome Jev checkout:

```sh
git clone https://github.com/awlevin/typesafe-computer-use.git
cd typesafe-computer-use
git checkout cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1
uv sync --frozen
uv run --frozen --offline pytest -q
```

Installation downloads dependencies; the test command runs offline afterward. The reviewed version printed **`144 passed`**. This is your first checkpoint: Python dependencies and mocked program behavior work, without capturing the screen, using a provider, or driving the Mac.

### 2. Inspect what the computer sees

For this step, grant your terminal **Screen Recording** and **Accessibility** in **System Settings → Privacy & Security**, then restart the terminal if macOS requests it. Use a disposable desktop/test account and a Finder window containing synthetic files. Close private windows and the key editor before capturing anything.

From the cloned project directory:

```sh
uv run --frozen clicker-inspect "Focus the search field in Finder." \
  --no-open --out inspections/finder-first
```

During the three-second countdown, bring Finder to the front. This command reads the desktop locally and writes `raw.png`, `annotated.png`, and `state.txt` under `inspections/finder-first/`. It makes **no Jev request** and performs no click or typing. `--no-open` keeps it from opening the output files automatically.

Open the annotated image and state file yourself. Find the intended field in the numbered items and check that the active app, labels, and focused-field information are plausible. Missing controls here are an observation problem; adding an API key will not repair them.

### 3. Configure a private key

Create a key in the [TypeSafe console](https://console.typesafe.ai/keys). Live requests use your account and may incur charges; check [models and pricing](https://docs.typesafe.ai/models). In the cloned project's directory, create a private environment file without overwriting an existing one:

```sh
cp -n .env.example .env
chmod 600 .env
```

Edit `.env` privately, setting `TYPESAFE_API_KEY`. Leave `ANTHROPIC_API_KEY` and `CLICKER_EMAIL` empty for this first exercise. The CLI loads `.env` from its **current working directory**; the upstream repository ignores this file. Keep its contents out of source control, screenshots, terminal output, and chat. An existing exported `TYPESAFE_API_KEY` takes precedence over the file.

### 4. Ask Jev for one proposed action

**Optional live step:** the next command re-reads your saved image locally, sends derived text/state to TypeSafe, and writes a decision. It never acts on the desktop. The explicit empty environment values keep the optional Anthropic writer and email filling disabled, including when `.env` contains values for them.

```sh
ANTHROPIC_API_KEY= CLICKER_EMAIL= uv run --frozen clicker \
  "Focus the search field in Finder." \
  --image inspections/finder-first/raw.png --app Finder \
  --steps 1 --out runs/finder-preview
```

This is **one decision request, with up to three HTTP attempts** under the locked SDK's default two retries. It may return a proposed action, `done`, `none`, or a low-confidence stop; no particular action is guaranteed. Look for the selected action and confidence in the terminal, then inspect `runs/finder-preview/step-001-answers.json` and `run.json`. A `dry run` outcome means it proposed an action without executing it.

Image replay rebuilds OCR from pixels; it does not restore the original live Accessibility tree or focused field. To compare with current live observations, omit `--image` and `--app`, retaining `--steps 1` and the disabled writer. That captures the current desktop and still calls Jev. Adding **`--act`** to a current-screen run enables real UI changes; keep the first action bounded to one step on the disposable test desktop. Stop an acting run with Ctrl-C while the terminal has focus, or move the pointer to the top-left corner.

Both a preview and `--image` use live inference. The `--offline` in the earlier `uv` test command controls package resolution; it is not a provider-network guard.

## Worked example: turn a Preferences action into a test

This is a suggested adaptation for **your own test app**, not a checked-in native-app demo:

1. Reset a disposable app profile and launch its Preferences window with a test value such as `Sample Workspace`.
2. Use inspection output to locate the labeled workspace-name field. Restrict candidates to that app and window before execution.
3. Let Jev select the field; have code type the predetermined replacement `QA Workspace`. Known test values do not need a writing model.
4. Read the value through the app's test API, exported configuration, or an XCTest assertion, and compare it exactly with `QA Workspace`.
5. Save the observation, raw answers, action, and assertion result together. Reset the profile before another attempt.

A Jev `done` decision or the optional model's final answer does not replace step 4. Likewise, a confidence threshold cannot tell you that the correct app was modified. See the [offline computer-use example](../../../examples/computer-use/README.md) for a runnable demonstration of candidate identity, freshness checks, and independent assertions before building the real adapter.

## Customize and troubleshoot

| Change | Where to start |
| --- | --- |
| Use a different browser | Set `CLICKER_BROWSER` to its app name; verify that the platform adapter supports its URL and automation behavior. Default: `Google Chrome`. |
| Use known websites | Review `SITES` in `typesafe_computer_use/config.py`; uncatalogued URLs require the optional writer. |
| Limit a task | Set `--steps`, inspect `--min-confidence`, and add app/window restrictions in your adapter. The default confidence floor is illustrative. |
| Enable free-form text | Supply `ANTHROPIC_API_KEY` privately and deliberately choose `CLICKER_WRITER_MODEL` / `CLICKER_ANSWER_MODEL`; this adds provider calls and the final-answer screenshot transfer described below. |
| Make tests reproducible | Pin a supported Jev model using `TYPESAFE_DEFAULT_MODEL`, keep a fixed app fixture, and record the requested model alongside the saved run. Default SDK model: moving alias `jev-latest`. |

| Symptom | Next check |
| --- | --- |
| `uv` is missing or Python cannot resolve | Complete uv installation, reopen the terminal, and confirm Python 3.12+ is available. Dependencies use macOS frameworks. |
| Capture shows wallpaper or misses the intended app | Check Screen Recording permission and which app was frontmost at capture time. Only the main display is captured. |
| `--act` refuses to start or clicks do nothing | Check Accessibility permission for the terminal that launched the process. |
| `TYPESAFE_API_KEY is not set` | Run from the project directory containing `.env`, or set the process environment privately. |
| No text is written or no final answer appears | The optional Anthropic writer is disabled in the starter exercise; that is expected. |
| Wrong or missing candidate | Inspect `state.txt` / `step-001-payload.txt`; improve labels and observations before increasing the step budget. |
| Authentication, quota, or repeated timeout errors | Check the provider account and selected model; stop and inspect the failure instead of automatically restarting the run. |

## Examples and demos

- The author's [X demonstration](https://x.com/awlevin/status/2100262612428894676) motivated this review. Its cost and speed comparisons were not independently reproduced.
- [`clicker-inspect`](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/typesafe_computer_use/cli.py) captures and writes the observed state without calling Jev; it still reads the desktop. `--no-open` suppresses opening the output files.
- [Action tests](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/tests/test_actions.py) and [decision tests](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/tests/test_decide.py) are the reproducible offline examples.

## Limits and data handling

OCR may miss icons; Accessibility coverage varies by app. Coordinate fallback can be affected by movement or occlusion. Add application/window restrictions, fresh identity checks, and exact readback before using this pattern in tests. The defaults allow 100 steps and a 0.4 confidence floor; neither is a recommended production setting. SDK retries and supplementary writing/field-check/final-answer calls mean general step limits are not billing caps. The three-attempt bound above applies to the one-step, non-acting, writer-disabled preview only.

TypeSafe receives screen text, app/URL context, field state, the goal, and recent actions. **The optional final-answer model receives a screenshot** in [writer.py](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/typesafe_computer_use/writer.py), even though the Jev decision loop uses text. Anthropic also receives writing context when enabled. Run folders retain raw/annotated screenshots, request state, judgments, and typed content; keep them private. The tool is not a permission boundary for arbitrary desktop tasks.

## Review and maintenance

AI-assisted source review on **2026-09-19** at [cc7b506](https://github.com/awlevin/typesafe-computer-use/tree/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1) covered license, setup, questions, loop, executor, writer data flow, and tests. Frozen installation and `uv run --frozen --offline pytest -q` passed in a separate checkout with provider credentials absent: **144 tests**, rerun when expanding this guide. CLI flags, environment precedence, and the locked `typesafe-sdk==0.6.0` retry/model defaults were checked against source and the [current SDK reference](https://docs.typesafe.ai/sdk/python/api/clients/sync). Desktop inspection and live commands above were source-checked only. No screen capture, Accessibility interaction, live inference, or native app task was run.

Related: [macOS test adaptation](../../../docs/computer-use.md#macos-and-ios-app-tests) · [Cua recipe](cua-jev-use.md).
