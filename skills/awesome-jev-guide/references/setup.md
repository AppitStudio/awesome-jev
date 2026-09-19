# Guided setup

Read this when helping someone run a selected resource. Adapt commands to their OS, shell, directory, and chosen stack. Commands below run from an Awesome Jev checkout and use `python3`; on Windows, use an installed Python 3.10+ command such as `py -3` after checking its version.

## 1. Get a working offline example

For the repository's Python demos, check `git --version` and `python3 --version`. No API account, SDK package, or Node.js installation is needed for these demos. Node.js 22+ is only needed for this repository's development checks or installing skills through the CLI.

Use an existing checkout when available. Otherwise clone into a suitable directory without overwriting existing work:

```sh
git clone https://github.com/AppitStudio/awesome-jev.git
cd awesome-jev
python3 skills/awesome-jev-guide/scripts/try_example.py support-routing
```

Select the matching recipe: `support-routing`, `quality-rubric`, `span-selection`, or `rag-triage`. Output identifies synthetic mode and a computed decision. The values are authored examples, not local Jev inference or accuracy measurements. If no coding setup is wanted, the official [quick start](https://docs.typesafe.ai/introduction/quickstart) also describes the browser Playground; that uses the provider, not the offline fixtures.

For the full batch tool, use its [README](https://github.com/AppitStudio/awesome-jev/blob/main/projects/support-router/README.md) and start with `python3 projects/support-router/run.py`. A community integration needs its own installation path, not these commands.

For UI workflows, use the standalone [computer-use example](https://github.com/AppitStudio/awesome-jev/blob/main/examples/computer-use/README.md): `python3 examples/computer-use/run.py`. It is not a `try_example.py` recipe. Expect `simulated_verified` with five passing checks; both the decisions and UI are synthetic. Its `--live` option still simulates the UI, requires an already configured environment key, and permits at most one HTTP attempt. Continue through the [computer-use implementation guides](https://github.com/AppitStudio/awesome-jev/blob/main/docs/computer-use.md) for actual browser, Mac, or Android setup; do not offer an unverified iOS Jev adapter as installable.

The helper can also be run from an installed skill: use its actual `scripts/try_example.py` path and pass `--repo PATH_TO_AWESOME_JEV`. It reuses the checkout's request builder, validator, and policy; installing the skill alone does not install the repository or an SDK. It does not load `.env` files.

## 2. Obtain and configure a key when live access is wanted

The official quick start points to [TypeSafe API keys](https://console.typesafe.ai/keys). Have the user sign in or create an account through the official console, then create/copy a key in its keys settings. Explain what to find without inventing unobserved button labels. Account access, limits, and billing can vary; check the current [models and pricing](https://docs.typesafe.ai/models) and console rather than promising free credits or a fixed price.

The user enters the key privately. Never ask them to paste it into chat, source code, a command argument, or a screenshot. Do not create keys, accept terms, or change payment settings merely to explain setup.

For a one-time first call, the helper below uses `TYPESAFE_API_KEY` if already set. Otherwise it asks for the key without echo in an interactive terminal. It does not write the entered key to a file or shell history, and it does not persist it for later commands. In a noninteractive agent terminal, it stops with setup guidance if no key is configured.

For an application, use its existing private environment or secret manager. Confirm that the chosen client actually reads the configured variable. The official clients use `TYPESAFE_API_KEY`; community clients can differ. A `.env` file works only if the application explicitly loads it. Use an ignored private file and its framework's loader when appropriate, keep real values out of `.env.example`, and keep keys on the server rather than in browser/mobile bundles. Do not change shell profiles globally as a setup shortcut.

## 3. Inspect, then make a bounded first call

First show what will be sent:

```sh
python3 skills/awesome-jev-guide/scripts/try_example.py support-routing --show-request
```

This prints the fixture-based request without network access or a key. The helper's `--show-request` also suppresses live execution if both flags are present.

For an authorized first live check, run:

```sh
python3 skills/awesome-jev-guide/scripts/try_example.py support-routing --live
```

Explain that it sends the selected fixture state and questions to TypeSafe and may incur charges. Inspect fixtures first if this is a modified checkout; use synthetic data for the first check. This helper permits **one HTTP attempt**, with a 30-second timeout and no retries or downstream actions. It reports requested/returned model IDs, usage, and the policy decision. A live answer can differ from the mock.

The helper takes its default pinned model from the checkout's example client. Check current model support before running; use `--model MODEL_ID` deliberately for a live request or request preview. Re-evaluate policy before changing a tuned version. An alias can move and does not pin an experiment.

Other CLIs and SDKs have their own retry policies. The ordinary `examples/run.py --live` path allows up to three attempts; do not call it a one-attempt check. Configure attempt count, timeouts, request count, and data scope for custom integrations before live execution.

## 4. Continue in the user's stack

For a custom Python app, follow the current [Python SDK setup](https://docs.typesafe.ai/sdk/python) in a project environment. For JavaScript/TypeScript, follow the current [JavaScript SDK setup](https://docs.typesafe.ai/sdk/javascript) in the existing project with its package manager. Verify names and runtime requirements before executing commands. Record installed versions and use the project's lockfile; do not copy illustrative package versions into unrelated projects.

Use the actual exported SDK types to build and read questions. Follow [building a starter](building.md) for fixtures, policy, errors, and evaluation. Support Router datasets and output captures belong outside the public checkout; follow the selected runner's documented path and replay rules.

## When a step fails

| Symptom | Useful next step |
| --- | --- |
| Python, Git, or the selected runtime is missing | Identify the OS and guide installation through the runtime's official instructions, then recheck the version. |
| Missing key or no interactive prompt | Let the user run the helper in their terminal or configure the private process environment; do not request the value in chat. |
| Authentication or permission failure | Check the configured variable, selected account, and key status in the console without printing the key; stop repeated requests. |
| Invalid request/model or SDK mismatch | Compare the exact request shape and installed SDK types with the current API/model docs; do not guess new fields. |
| Rate limit or temporary service failure | Honor current retry guidance within the agreed attempt budget; stop this one-attempt smoke check instead of looping. |
| Network/timeout failure | Check connectivity and report that the outcome may be uncertain; avoid automatically repeating consequential actions. |
| Unexpected decision | Inspect state, questions, candidates, raw answers, and code policy. A working connection does not establish correctness. |

End with the successful checkpoint, the next command, and any remaining blocker. Key creation is not proof of API access, a successful call is not an accuracy evaluation, and an offline demo proves only the demonstrated program path.
