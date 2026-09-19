# Jev-cu

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Study a Codex computer-use loop that asks Jev to select targets and actions from macOS Accessibility text, with action previews and optional independent result verification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sac-Y/Jev-cu) |
| Maintainer | [Sac-Y](https://github.com/Sac-Y). Contributor affiliation and commercial relationships were not supplied for this catalog review. |
| Format | Experimental JavaScript runtime and installable Codex skill; package version `0.1.0`. |
| Platform | macOS apps through Codex desktop's `cua_repl` runtime. No browser DOM/tab adapter is implemented. |
| Requirements | Node.js and npm for offline tests; compatible Codex computer-use access and `TYPESAFE_API_KEY` for live decisions. Upstream does not declare a minimum Node.js version. |
| Jev's role | Chooses an observed target and action type, and judges completion and risk using the TypeSafe HTTP API. |
| License | [Package metadata](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/package.json) declares ISC; no standalone license file was present at the reviewed commit. |
| Access and costs | Source checkout; live TypeSafe calls require an account/key and may incur charges. Codex access is separate. No hosted service or bundled inference is established by this listing. |

## When to use

- Explore short, text-rich native-app workflows such as selecting a Calendar view or locating a Calculator button.
- Inspect how a coding agent can supply goals and exact input while Jev selects from observed controls.
- Study candidate filtering, action previews, confidence thresholds, and independent result checks using a replaceable driver.

This is an experimental developer resource. The execution-policy gaps below need addressing before unattended use. Canvas design, browser DOM automation, and general-purpose desktop reliability are outside the verified scope. The similarly named [Cua jev-use](cua-jev-use.md) is a separate project using Cua Driver.

## How it works

The [loop](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/loop.mjs) reads Accessibility text, filters supported roles, and ranks up to 40 candidates by default. It sends candidate descriptions, a small context excerpt, the goal, constraints, and recent actions to TypeSafe. It does not send screenshots to Jev.

The [request builder](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/jev-decide.mjs) submits two Choice questions for target/action and two Noul questions for completion/risk to `POST /v1/systemone`, using `jev-latest` by default. This request shape matches the [TypeSafe API documentation](https://docs.typesafe.ai/api) inspected during review; live compatibility was not tested. The alias can change over time.

Code applies an app allowlist, label patterns, probability thresholds, and a step budget before dispatching an action. Codex supplies input text, keys, and coordinates; Jev does not generate those values. The loop observes again after an action. A caller-supplied `verify(ax)` can check the actual result before steps and after the final step. Without it, `done` can mean only that Jev judged the goal complete.

The four questions run independently. In particular, the risk question cannot see the target/action answers from the same request, and the request does not include the executor's complete `resources` parameters. Its risk score does not verify the exact action ultimately executed. See TypeSafe's [question composition guidance](https://docs.typesafe.ai/concepts/how-to-build-with-system-one).

## Get started

### Inspect the source and run offline tests

Clone outside the Awesome Jev checkout and keep the following commands in the new directory:

```sh
git clone https://github.com/Sac-Y/Jev-cu.git
cd Jev-cu
git checkout 38fb31de7dfe6209bbe6e04057c00c6e885ba577
npm test
```

The reviewed package has no third-party dependencies, so dependency installation is unnecessary for this test command. Expect **18 passing tests**, covering parsing, candidate selection, policy branches, mocked execution, and result verification. The suite uses synthetic test inputs and mock drivers; it needs no key, provider request, or real desktop action. The catalog review ran it on Node.js 21.6.1; that records the observed environment, not a recommended or minimum runtime version.

### Optional skill installation and live preview

Read the upstream [skill](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/skill/jev-use/SKILL.md) and [runtime example](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/skill/jev-use/references/runtime.md) before installation. From the external checkout:

```sh
npm run install-skill
```

The [installer](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/install-skill.mjs) replaces `~/.codex/skills/jev-use`, copies the skill, and substitutes the checkout's absolute path. Preserve any existing skill with that name first. Keep the source checkout available; the installed skill references its scripts. Start a new Codex session after installation. Installation was source-reviewed but not executed for this listing.

For live use, configure `TYPESAFE_API_KEY` privately in the runtime environment or the external checkout's ignored `.env.local`. Do not commit or print it. Follow the linked runtime example in `cua_repl`, reading the current tool documentation before importing the loop; this is not a standalone terminal desktop agent. Use a test app state containing no unrelated private content.

The upstream example requests a Calendar view change with `dryRun: true` and an independent view-state verifier. **This preview still makes a live TypeSafe request when a decision is needed**, sends UI-derived text, and may incur charges. It previews one proposed action rather than simulating the whole task. A successful existing-state verifier can finish without a request. A decision permits up to three HTTP attempts for retryable server responses. Read the returned target, action, and policy result before considering execution; the reviewed execution limitations still apply.

## Examples and demos

- [Runtime example](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/skill/jev-use/references/runtime.md): a Calendar Week-view preview with a state verifier; requires a compatible runtime and live key when a decision is needed.
- [Calendar navigation plan](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/skill/jev-use/references/calendar-demo.md): a proposed sequence and verification criteria, explicitly documented as awaiting execution, not a recorded successful demo.
- [Unit tests](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/tests/core.test.mjs): the verified offline starting point.
- [P0 cases](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/fixtures/p0/cases.json): 12 target-selection cases over saved Calendar, Calculator, and NetEaseMusic snapshots. Despite the upstream “offline evaluation” wording, `npm run p0` calls the live API. It tests snapshot target selection, not complete task success, and was not run during this review.

## Limits and data handling

Two implementation defects were reproduced with synthetic inputs and a mock driver:

- **Approved target and executed target can diverge.** After policy approves a selected element, `click_element` uses `resources.at` instead of that element when coordinates are supplied. The review approved element `1` but observed the mock driver receive `[999, 999]`. Coordinate clicks, drags, and focus-based keyboard/text actions need validation of the actual operation and arguments, not just the selected label. See the [executor](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/loop.mjs#L328).
- **Completion is checked before response validation.** An invalid synthetic `done: 2` produced `verdict: "done"` even with missing risk/confidence. Validate completion values before using them, and independently verify the task outcome. See the [policy](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/policy.mjs#L69).

The label filters and model risk judgment are heuristics. An allowed app is not authorization for every operation inside it. The code also relaxes confidence thresholds for several apps, including Calendar, TextEdit, and Figma; this does not establish that their actions have no side effects. The skill instructs the agent to stop repeated ineffective actions, but the runtime only records unchanged observations and otherwise continues within its step limit.

TypeSafe receives the goal, selected UI context and candidate descriptions, recent-action summaries, and supplied constraints/plan. URL removal and truncation are not privacy redaction. Window titles, ordinary field values, or Calendar text may contain private information. Local JSONL traces under `runs/` retain goals, normalized decisions, and execution summaries; keep them private. Per-step trace records strip the raw response, so they do not preserve every typed answer for later diagnosis. No provider-retention assessment was performed.

The license declaration needs an accompanying license text or clarification from upstream before treating reuse terms as fully documented. This listing is not an endorsement or a claim of measured safety, accuracy, or speed.

## Review and maintenance

AI-assisted source review on **2026-09-19** covered [commit 38fb31d](https://github.com/Sac-Y/Jev-cu/tree/38fb31de7dfe6209bbe6e04057c00c6e885ba577), including README, package/license metadata, installer, skill instructions, request construction, policy, executor, evaluation script, and tests. The upstream default branch still pointed to that commit when this listing was prepared.

`npm test` passed **18/18 tests** in a sanitized environment without provider credentials. Two additional synthetic probes reproduced the target-coordinate substitution and invalid-completion behavior described above. Those probes executed no real UI actions and made no provider requests. No performance or model-quality claim follows from these checks.

Skill installation, current Codex driver compatibility, real desktop operation, live inference, and P0 evaluation remain untested. Contributor affiliation was not supplied; no human review is claimed by this AI-assisted evidence record. No duplicate catalog entry or matching open issue/PR was found during review.

Related: [computer-use guide](../../../docs/computer-use.md) · [typesafe-computer-use](typesafe-computer-use.md) · [offline computer-use example](../../../examples/computer-use/README.md).
