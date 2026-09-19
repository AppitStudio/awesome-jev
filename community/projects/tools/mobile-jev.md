# Mobile Jev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Use Jev to navigate an Android app and enter supplied text through Mobilerun. Start with offline tests, preview one decision, then try the included dark-theme task with a separate result check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/droidrun/mobile-jev) |
| Maintainer | [Droidrun](https://github.com/droidrun); integrates the Mobilerun service. Independently curated, not a maintainer submission or sponsored placement. |
| Format | JavaScript agent and Next.js/React studio. |
| Requirements | Git and Node.js 22.16+ (upstream recommends 24). Live CLI: curl 7.70+, a ready Mobilerun Android device and API keys. Optional studio: pnpm 10.30.1 and its installed dependencies. |
| License | [MIT](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/LICENSE). Service/device charges are separate. |

## When to use

Choose it when you want to explore Android settings, fill fields with known test values, or build a smoke-test harness around an app you own. The included dark-theme demo has a visible result and an independent switch-state check. No ADB connection is required; device control goes through the Mobilerun service.

This is an **Android** integration. It does not implement iOS automation, generate missing form values, or provide ready-made assertions for every app. See [iOS evidence and adaptation guidance](../../../docs/computer-use.md#ios-simulator-evidence) for the separate Simulator work.

## How it works

The [policy](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/policy.mjs) builds operation and target choices from the observed UI and installed apps. It uses the TypeSafe v1 HTTP API, defaults to `jev-latest`, and supports `TYPESAFE_MODEL` for pinning. Text values come from exact goal spans or explicit `--text` values, not a second generative model.

The [device adapter](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/device.mjs) checks device/app/target freshness. The [loop](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/agent.mjs) records a mutation before observing again, verifies eligible text replacements, and refuses to replay uncertain mutations. Used choices are validated; uncertainty on unrelated speculative targets is ignored.

In plain terms: Mobilerun reads the screen → code lists available actions → Jev selects an action and target → code checks and executes it → Mobilerun reads the result. A final Jev `done` means the model proposes stopping; your app test still needs its own success check.

## Get started

### 1. Get a first result without keys or a phone

Run these commands in a terminal, in a directory outside your Awesome Jev checkout. If you already have this version of Mobile Jev, use that checkout. The pinned revision makes these instructions reproducible; it is not a promise that the upstream default branch has the same behavior.

```sh
git clone https://github.com/droidrun/mobile-jev.git
cd mobile-jev
git checkout 395fc222beac4f059f9a0beb337d114a2b066e99
npm test
node scripts/run.mjs --help
```

Expect **55 passing tests**, then help text listing `observe`, `run`, `--text`, `--steps`, and `--execute`. The tests use synthetic data, mocked providers, and local transport checks. They do not control a phone or call Jev. Neither this test path nor the CLI needs studio dependencies installed.

For a smaller walkthrough of why action selection and verification differ, run the catalog's [offline decision cycle](../../../examples/computer-use/README.md). That example uses synthetic browser fields; it is not an Android driver.

### 2. Configure a private key and one test device

You need a Mobilerun account with a ready Android device and a TypeSafe account with API access. Use an English-language test device for the included theme verifier. Live use sends screen state and your goal to services and may incur **both Mobilerun/device charges and TypeSafe inference charges**. Check your account plans and [current TypeSafe models and pricing](https://docs.typesafe.ai/models).

From the Mobile Jev directory, create a local configuration file only if one does not already exist:

```sh
test -e .env.local || cp .env.example .env.local
chmod 600 .env.local
```

Open `.env.local` in your editor and fill these fields privately:

| Variable | Where it comes from |
| --- | --- |
| `MOBILERUN_API_KEY` | [Mobilerun API keys](https://cloud.mobilerun.ai/api-keys). |
| `TYPESAFE_API_KEY` | [TypeSafe API keys](https://console.typesafe.ai/keys). |
| `MOBILERUN_DEVICE_ID` | The ID of your own ready test device, selected from the command below. |
| `TYPESAFE_MODEL` | Leave `jev-latest` for exploration, or set a supported fixed model when comparing runs. |

The file is ignored by upstream Git. Never put keys in prompts, command arguments, screenshots, or committed files. The loader reads exported environment variables first, then `.env.local`, then `.env`; an old exported value can override a file change.

These commands **contact Mobilerun**. They list devices, check readiness/accessibility, and read UI state; the doctor checks for the presence of the TypeSafe key but does not perform inference:

```sh
node scripts/run.mjs devices
# Set MOBILERUN_DEVICE_ID in .env.local before continuing.
node scripts/doctor.mjs
```

Choose the exact device from the listing. Expect doctor checks for Node, curl, keys, device connection, Accessibility, and UI observation to pass. Stop at a failed check and use the troubleshooting table below.

### 3. Preview one live decision

This command reads the remote phone and makes **at most one Jev request**, with no automatic model retry. It does not execute the selected action. It is a live preview, not an offline dry run:

```sh
node scripts/run.mjs run 'Turn on dark theme in Android Settings.'
```

The output includes a `decision` event with the selected operation, target, confidence, and requested/returned model, followed by a status and timings. On a screen where an action is needed, expect `status: "preview"` and `steps: 0`. It may instead report `done`, `blocked`, or another stop condition; a particular action or confidence is not guaranteed.

### 4. Execute one bounded step and inspect it

Once you have confirmed the target device and are ready to change its UI, run:

```sh
node scripts/run.mjs run 'Turn on dark theme in Android Settings.' \
  --execute --steps 1 --trace artifacts/theme-first-step.jsonl
node scripts/run.mjs observe
```

This permits at most **one executed action**, which could open Settings or change its switch. `step_limit` is an expected stop when the full task needs more actions; it is not a successful app test. The observation command reads the current phone without calling Jev. Trace files include raw model requests/responses and actions; use a new filename for a new attempt because the CLI refuses to overwrite an existing trace.

Action limits and request limits differ. At this revision, an executing loop permits at most `2 × steps + 4` Jev decisions, including stale-state retries and checks after the action budget is spent. Thus `--steps 1` allows up to **6 Jev requests**; each model request has a 30-second timeout and no transport retry. Mobilerun readiness, observations, and verification add separate service requests. Step limits are not a total-cost cap.

### 5. Open the optional visual studio

For a live device stream and action timeline, install the studio dependencies using **pnpm 10.30.1** and run:

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Open `http://127.0.0.1:3040`. Starting the studio connects its device view; pressing **Run task** executes a live task. Use the CLI above when you want an explicit one-step limit. Stop cancels the active task; Clear removes finished runs from the studio display, not changes on the device. Stop the local server with Ctrl+C when finished. See [upstream studio instructions](https://github.com/droidrun/mobile-jev/tree/395fc222beac4f059f9a0beb337d114a2b066e99#the-studio).

## Practical use cases

### Verify an Android setting changed

This is the shipped end-to-end demo. On an English-language Android test device with a labeled **Dark theme** switch, run:

```sh
node scripts/demo.mjs dark-theme --reset
```

The reset phase uses Jev to turn the switch off and verifies that baseline. The task then turns it on and reads a fresh switch state. The report should contain `verified: true`, `baselineVerifiedOff: true`, and `stateChangeVerified: true` when both phases succeed. These are expected success conditions, not recorded results from this review.

This command **changes the phone** and permits up to 16 actions and 36 Jev decisions in each of two phases: at most **72 Jev requests** for one reset-and-task attempt, plus Mobilerun reads/actions. It saves reports and traces under `artifacts/demos/`. Without `--reset`, a verified final on-state does not prove a change occurred. The demo leaves dark theme **on**; manually restore your original setting after inspecting the result. `--reset` prepares the next run rather than cleaning up afterward.

### Enter an exact search term

On a test device whose Settings app has a search field, preview:

```sh
node scripts/run.mjs run \
  'In Android Settings, open Search and enter exactly Wi-Fi. Leave the search field visible.' \
  --text 'Wi-Fi'
```

The supplied text takes precedence over goal-span candidates, so the only supplied value is `Wi-Fi`. After inspecting the preview, append `--execute --steps 4` to permit up to four actions and twelve Jev decisions. This is an adaptation recipe; Settings search layouts differ and it was not run on a phone for this review. Read the field afterward and confirm the full value equals `Wi-Fi`; opening the search screen alone is not success. Clear the test query manually before another run.

### Fill a field in your own QA app

Prepare your own disposable app screen with a visible **Display name** field. This fixture is not bundled with Mobile Jev. Preview a goal with one exact synthetic value:

```sh
node scripts/run.mjs run \
  'In the current QA app, fill Display name with the supplied value Avery Example. Leave the form open without submitting it.' \
  --text 'Avery Example'
```

For a controlled execution, append `--execute --steps 3` (at most ten Jev decisions). Assert the final field value equals `Avery Example`, the intended app is still foreground, and the app's test backend has received no submission. Reset fixture state between trials. The words “without submitting” are a model instruction, not an executor permission boundary: enforce allowed actions in a custom policy before using a real account or consequential form.

### Turn an exploratory flow into an app test

Use the theme demo's [verifier](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/demo-verifiers.mjs) as the pattern: define the final state before running, read fresh app state afterward, and fail if evidence is absent or ambiguous. For a saved profile, check the persisted test record as well as the text field. Keep numeric/date parsing and expected values in code. A `done` response and a successful input acknowledgment are insufficient assertions.

This integration supplies navigation and input; a general structured-data exporter is additional work. For extracting records from Android screens, build candidates from observed text, preserve the source element and observation, select with Jev, and copy/parse in code. See the [source-value selection pattern](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) and the catalog's [offline extraction example](../../../examples/span-selection/README.md).

## Examples and demos

- [Dark-theme demo](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/docs/DEMO.md): the full setup, reset, measurement, and verification boundaries, including reported failed exploratory tasks.
- [Uber recording](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/docs/media/uber-demo.mp4): upstream demonstration ending at payment selection; it does not demonstrate a completed booking. Timing was not reproduced here.
- [Input-verification tests](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/input-verification.test.mjs): examples of verified and unverified field entry.

## Limits and data handling

The generic loop's `done` is a model judgment; the dark-theme verifier is task-specific. Add independent assertions for every app-test requirement. Confidence gating defaults to **0** (disabled). The CLI accepts `--confidence` between 0 and 1; choose a threshold from representative tasks rather than treating confidence as proof of correctness. Only the selected operation and its used target affect that cutoff. The [current Choice contract](https://docs.typesafe.ai/primitives/choice) and [HTTP API](https://docs.typesafe.ai/api) explain the returned answers.

Device state and commands pass through Mobilerun. TypeSafe receives the goal, visible text, selected app inventory, field state, and history. Keys stay server-side; the studio receives device-scoped streaming credentials. Traces can contain UI content and typed values. Use synthetic device data and keep artifacts private. The localhost studio supports one operator and one active task per configured device; public hosting needs additional authentication and authorization.

## Troubleshooting

| Symptom | What to check next |
| --- | --- |
| Node or curl check fails | Use Node 22.16+ and curl 7.70+. Node 24 is the upstream recommendation. |
| Device missing or not ready | Run `devices`, confirm the selected ID and readiness in Mobilerun, then rerun doctor. Do not select a different device blindly. |
| Changed `.env.local` has no effect | An exported variable takes precedence. Check variable names and your terminal configuration without printing key values. |
| HTTP 401 or other API failure | Confirm the relevant provider account/key privately. Doctor does not validate TypeSafe authentication through an inference call. Stop repeated attempts until configuration is fixed. |
| `needs_input` or wrong text candidate | Supply the complete intended value with `--text`. The model cannot choose an omitted value. |
| `input_unverified` or transport failure after typing | Inspect the phone before retrying. Text may already have been entered; the loop deliberately avoids automatic replay. |
| `stuck`, `unstable_screen`, `loading_timeout`, or `decision_limit` | Inspect current state and trace, then reset the test screen. Increasing the budget does not fix a missing control or unsupported action. |
| `step_limit` after a one-step run | The action budget was reached. Inspect that step before deciding whether to run a larger task. |
| Theme verification fails | Confirm English locale, `com.android.settings`, and one readable checkable control labeled Dark theme. A label without a switch is not enough. |
| Trace path already exists | Choose a new filename; the CLI refuses to overwrite an existing trace. |

## Review and maintenance

AI-assisted review on **2026-09-19** at [395fc22](https://github.com/droidrun/mobile-jev/tree/395fc222beac4f059f9a0beb337d114a2b066e99) covered README, MIT license, configuration loader, CLI, demo verifier, policy, loop, transports, freshness and input checks, and tests. `npm test` passed **55 tests** with provider credentials absent in a separate checkout; CLI help also worked without credentials. Request bounds above were derived from the loop and demo source. Current TypeSafe API, Choice, models, and source-value cookbook pages were read for this guide.

Studio dependency installation/build, Mobilerun connectivity, phone control, live Jev behavior, and demonstration measurements were not reproduced. Search and QA-form recipes are supplied adaptation examples, not measured successes. No paid inference or device change was performed for this review.

Related: [computer-use guide](../../../docs/computer-use.md) · [offline decision cycle](../../../examples/computer-use/README.md).
