# Cua jev-use

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Run a synthetic Jev chooser first, then use the same pattern to fill and verify a local browser form through Cua Driver.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) |
| Maintainer | [Cua](https://github.com/trycua), a computer-use tooling vendor. Independently curated; no sponsorship or endorsement is asserted. |
| Format | Public-preview Python/TypeScript integration recipe and chooser CLI. |
| Requirements | Python 3.10+ and uv (documented setup uses 3.12); Node.js 22+ for TypeScript. Real UI proof also needs Cua Driver 0.23.2+, an accessible desktop, and supported Chromium. `TYPESAFE_API_KEY` only for live Jev. |
| License | Repository [MIT](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/LICENSE.md); optional perception components have separate terms. |

## When to use

Start here when building your own observer → candidate builder → chooser → executor → verifier integration. The standalone chooser can serve an existing harness; it does not drive the desktop itself. The complete checked-in task is a small **browser form fixture**, not proof of arbitrary native app control across operating systems.

| Common workflow | Starting point | What still needs building |
| --- | --- | --- |
| Fill a form and prove it was submitted | The included loopback form and managed setup verifier. | Your form-specific candidates and independent result check. |
| Add Jev to an existing desktop harness | The JSON chooser CLI. | Observation, candidate construction, execution, and verification remain yours. |
| Compare Python and TypeScript implementations | Matching runners and mock providers in both languages. | Evaluation on your own tasks and deployment environment. |
| Prototype native-app smoke tests | Candidate IDs, fresh observations, and refusal behavior as a design reference. | A native-app adapter, test fixtures, and assertions; the checked-in proof covers a browser form. |

For a ready-made browser extraction API, see [Jev Browser](jev-browser-tontoko.md). Cua's fixture does not implement a general scraper or an iOS testing harness.

## How it works

The [Python core](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/python/core.py) constructs immutable action candidates. Jev selects a candidate ID, including `reobserve` and `abstain`; the runner maps that ID back to the original action. A persistent MCP connection owns the Driver session and fresh browser references. A separate fixture `/state` read confirms the submitted value.

The chooser CLI accepts up to 32 candidates and returns a selection, confidence, probabilities, and available model identity. Its schema excludes arbitrary tool names, arguments, environment data, and screenshot bytes. The [provider adapter](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/python/jev_adapter.py) uses the official SDK; it is separate from the Driver binary.

## Get started

### 1. Install the example

Install **Git and [uv](https://docs.astral.sh/uv/getting-started/installation/)**. Python 3.10+ is supported; the commands below select Python 3.12. This first path needs neither Cua Driver, a browser, Node.js, nor an API account. Use your own projects directory outside Awesome Jev:

```sh
git clone https://github.com/trycua/cua.git
cd cua
git checkout 83f142c4290a0f7d9ed545ae8532858c6e4f8145
cd libs/cua-driver/examples/jev-use
uv sync --frozen --python 3.12
```

This downloads dependencies. Run later commands from **`cua/libs/cua-driver/examples/jev-use`**, not the repository root.

### 2. Get a visible offline result

For macOS/Linux shells:

```sh
uv run --frozen --offline python python/choose_action.py --mock < fixtures/jev-choice-request-v1.json
```

In Windows PowerShell, use its pipe syntax instead of `<`:

```powershell
Get-Content -Raw fixtures/jev-choice-request-v1.json | uv run --frozen --offline python python/choose_action.py --mock
```

Expected output, reformatted for readability:

```json
{
  "schema": "cua.jev_choice_v1",
  "selected_id": "submit-form",
  "model": "mock",
  "confidence": 1.0,
  "probabilities": {"submit-form": 1.0, "reobserve": 0.0, "abstain": 0.0}
}
```

The mock chooses the first ordinary candidate. Its `1.0` confidence is scripted, not a Jev quality measurement. No provider is called and no UI action is performed. You can also run the credential-free Python suite:

```sh
uv run --frozen --offline python -m unittest discover -s python/tests
```

The reviewed version ran **36 tests: 35 passed and one skipped** before installing TypeScript dependencies. After the optional TypeScript setup below, **all 36 passed**, including the cross-language parity check. Tests include local fixture-server checks; they do not launch Driver or contact TypeSafe.

### 3. Connect a real browser with mocked decisions

This checkpoint **opens and operates a real browser** on a local test page. Install **Cua Driver 0.23.2 or later** using the upstream [platform installation instructions](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/docs/content/docs/how-to-guides/driver/install.mdx), and complete daemon/permission setup for your OS. Driver is a separate installation from the Python dependencies.

| Platform | Browser and session prerequisites |
| --- | --- |
| macOS | macOS 14+, an unlocked desktop, Google Chrome in `/Applications`, and Cua Driver's Accessibility and Screen Recording grants. |
| Windows | A logged-in desktop and a system-installed Chrome or Edge. Run the terminal and Driver without administrator elevation. |
| Linux | Start with an X11 desktop and a system-installed Chrome/Chromium, with the Driver daemon running as the same user. Follow upstream instructions for AT-SPI and any Wayland-specific limits. |

Confirm installation before trying the form:

```sh
cua-driver --version
cua-driver status
cua-driver doctor
```

On macOS, if the CLI is not on `PATH`, point the recipe directly to the app and check permissions:

```sh
export CUA_DRIVER_BIN="/Applications/CuaDriver.app/Contents/MacOS/cua-driver"
"$CUA_DRIVER_BIN" permissions status --json
```

The permission report should show both `accessibility` and `screen_recording` as `true`. Then, from the example directory:

```sh
uv run --frozen python verify_setup.py --max-steps 4 --output-dir proof-mock
uv run --frozen python -m json.tool proof-mock/summary.json
```

The verifier creates an isolated Chromium profile, fills the loopback form with `jev-guide-mock`, submits it, and reads the fixture's `/state` endpoint independently. It manages and closes its own test server. Success prints:

```json
{"event": "setup_complete", "checks": 1, "fixture_closed": true}
```

The summary must contain `"complete": true` and `"observed": {"submitted": "jev-guide-mock"}`. The personal browser profile is not used. Keep `proof-mock/` private; choose a new output directory for every attempt. Driver may use its own telemetry settings, so “mock provider” here does not mean an entirely offline process.

### 4. Opt in to Jev decisions

Create a key in the [TypeSafe console](https://console.typesafe.ai/keys), and check [models and pricing](https://docs.typesafe.ai/models). The managed verifier securely prompts for a key in an interactive terminal, without displaying or saving it. If `TYPESAFE_API_KEY` is already set in the process environment, it uses that value. An unattended run without the variable stops before starting; this recipe does not load `.env` automatically.

**Optional live step:** the following command sends the synthetic form's compact goal, observations, candidate descriptions, and history to TypeSafe. It repeats the mock browser check, then runs the Python agent with live Jev decisions. It may incur provider charges and performs real interactions with the isolated test browser.

```sh
uv run --frozen python verify_setup.py --live --max-steps 4 --output-dir proof-live
uv run --frozen python -m json.tool proof-live/summary.json
```

The live runner is limited to **four decisions and 180 seconds**. With the locked Python SDK's default two retries, that permits **at most 12 TypeSafe HTTP attempts**, rather than four guaranteed billable requests. It uses `jev-latest` unless `TYPESAFE_DEFAULT_MODEL` selects a supported model. Record the model when comparing runs, because the alias can move.

Success prints `"checks": 2`; inspect the summary for `"complete": true`, a `"provider": "live"` check, and `"observed": {"submitted": "jev-guide-live"}`. This value comes from the test server after submission, not from a model's declaration of success. `proof-live/python-live.jsonl` retains the selected candidates, distributions, actions, and outcome. A failed or incomplete check is not evidence that nothing happened; inspect the log before starting a new attempt.

## Worked example: reuse the chooser in your own harness

The included [request fixture](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/fixtures/jev-choice-request-v1.json) describes a Submit control from `capture-fixture-1` and offers `submit-form`, `reobserve`, and `abstain`. The mock returns only `submit-form`; it never invents a tool call.

To adapt that shape to a customer-form test:

1. Your harness observes the test page and builds an immutable table of allowed actions, such as typing a synthetic customer name into a specific fresh field reference.
2. Send only the goal, compact observation, history, and candidate IDs/descriptions to the chooser. Keep tool arguments in your own action table.
3. Resolve the returned ID to that original action. If the page changed, discard the choice and reobserve. `reobserve` performs no Driver action; `abstain` stops.
4. Execute the permitted action, then check the saved record through the test application's API or database fixture. Compare exact values in code.

Changing the fixture's goal text alone does not create a new automation. Update these three parts together:

| Part to customize | Where | Example change |
| --- | --- | --- |
| Candidate builder | `python/core.py` or `typescript/core.ts` | Offer only valid next actions for your test fields and current page state. |
| Jev state and judgment | `python/jev_adapter.py` or `typescript/jev_adapter.ts` | Explain the task and provide the relevant fresh observations. Keep `reobserve` and `abstain`. |
| Completion and failure checks | `python/run.py` or `typescript/run.ts` | Replace the fixture-specific `/state` oracle with your own independent assertion. |

The supplied runners intentionally target their loopback fixture; `--fixture-url` is not a general arbitrary-site switch. For extracting a displayed price or date, parse candidate source values in code and let Jev select the intended candidate, then return the exact source value. That is an adaptation idea; the Cua recipe does not ship a general extraction method. The [offline computer-use example](../../../examples/computer-use/README.md) demonstrates this pattern locally.

## Optional TypeScript setup

Python is enough for every checkpoint above. If you want the parallel TypeScript implementation, install **Node.js 22+ and npm**, then run from the same example directory:

```sh
npm ci --ignore-scripts
npm run choose:mock -- < fixtures/jev-choice-request-v1.json
npm test
npm run typecheck
```

On Windows use `npm.cmd ci --ignore-scripts`, and pipe the fixture with `Get-Content -Raw fixtures/jev-choice-request-v1.json | npm.cmd run choose:mock`. To exercise both languages against the real browser with mocked decisions, run `uv run --frozen python verify_setup.py --typescript --max-steps 4 --output-dir proof-both-mock`. This starts two browser checks and should report `"checks": 2`; it does not call Jev.

## Troubleshooting

| Symptom | Next check |
| --- | --- |
| `uv` or Python is unavailable | Complete uv installation and rerun `uv sync --frozen --python 3.12`; keep the pinned lockfile. |
| `cua-driver` cannot be found | Reopen the terminal after Driver installation, or set `CUA_DRIVER_BIN` to its absolute executable path. |
| Browser cannot launch or attach | Check `cua-driver doctor`, the system browser installation, and the interactive desktop. Avoid elevation on Windows. |
| Permission errors on macOS | Grant the installed Driver app Screen Recording and Accessibility; check its permission report. |
| `browser_prepare` asks for a `pid` | The upstream guide identifies this as an older Driver contract; update Driver before running this recipe. |
| Mock passes but live fails | Check key access, quota, and the selected TypeSafe model. The browser check does not establish API access. |
| Output directory already exists | Pick a new `--output-dir`; previous evidence is intentionally preserved. |
| `complete: false`, `unknown`, or `budget_exhausted` | Read the retained JSONL log and fixture result before retrying; increasing the budget does not fix an invalid candidate or assertion. |

## Examples and demos

- [Request fixture](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/fixtures/jev-choice-request-v1.json): the smallest reusable chooser input.
- [Python runner](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/python/run.py): complete form loop and independent verification.
- [Upstream validation record](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/docs/jev-use-validation.md): distinguish upstream platform evidence from this catalog's narrower checks.

## Limits and data handling

The [X announcement](https://x.com/trycua/status/2100649543079502213) linked development work. The standalone recipe subsequently [merged in PR #3916](https://github.com/trycua/cua/pull/3916). **Optional visual perception remains separate:** [PR #3943](https://github.com/trycua/cua/pull/3943) was still a draft at review time. Do not assume its OCR/icon extension ships with normal Driver installation; its detector also has separate AGPL terms.

Live decisions send compact goal, observation, candidate, and optional typed-region data to TypeSafe. Screenshot bytes are not Jev input. Logs contain decision evidence; retain it privately. Capture-bound visual refusal must not fall back to an unbound coordinate click. Ambiguous mutations stop rather than replay. General step limits are not currency budgets; the request-attempt bound above is specific to the pinned Python-only setup. The standalone runner's `--dry-run` still resets the fixture and prepares/navigates the browser. The fixed fixture is an integration proof, not an evaluation of general computer-use quality.

## Review and maintenance

AI-assisted source review on **2026-09-19**, pinned to [83f142c](https://github.com/trycua/cua/tree/83f142c4290a0f7d9ed545ae8532858c6e4f8145), covered license, setup, core/adapter/runner, chooser schema, fixtures, and tests. Checks ran from an isolated source subset with the required workflow fixture and provider credentials absent:

- Frozen Python setup; `uv run --frozen --offline python -m unittest discover -s python/tests`: **35 passed, one skipped** initially; **36 passed** after TypeScript dependencies were installed for the parity test.
- Python mock chooser: returned `submit-form` with `model: mock`.
- `npm ci --ignore-scripts`, `npm test`, and `npm run typecheck`: **24 TypeScript tests passed**, typecheck passed.
- TypeScript mock chooser: returned the corresponding `submit-form` envelope.

The locked Python `typesafe-sdk==0.6.0` retry/model defaults were checked against installed source and the [current SDK reference](https://docs.typesafe.ai/sdk/python/api/clients/sync). Browser setup and live commands were checked against upstream source but not executed. Driver installation, desktop/browser execution, optional perception, Windows/PowerShell execution, and live inference remain untested here. See [catalog validation](../../../docs/validation.md#computer-use-review) for the shared record.

Related: [computer-use guide](../../../docs/computer-use.md) · [native macOS reference](typesafe-computer-use.md).
