# Validation scope

This page distinguishes checks of the repository's code from claims about model quality. It contains no live response captures or private evaluation data.

## Offline checks

`npm run check` validates Markdown, local links and anchors, and the Python behavior tests for examples, Support Router, the evaluation runner, and the guide skill's example helper. CI performs these checks without a TypeSafe key. Tests cover request construction, answer validation, policy boundaries, replay behavior, error paths, and credential handling. The guide helper's tests use mocked transport to check its attempt bound and private key handling; they do not constitute live inference or an evaluation of an LLM following the skill.

The bundled inputs and responses are hand-authored synthetic fixtures. Mock mode is deterministic application testing; it is not local Jev inference. Follow [Contributing](../CONTRIBUTING.md#run-checks) to reproduce the checks.

The community directory check connects each README entry to a full page and one category in its own apps/tools index, verifies matching canonical sources, and requires a link back to that category. It also checks app tags, product/evidence links, and pricing/disclosure metadata. Tests cover missing pages, duplicates across both directories, incorrect app/tool placement, and commercial/closed-source metadata requirements. These checks verify structure, not licensing, prices, the truth of Jev claims, or a model's compliance with the guide skill.

## Live integration checks

On 2026-09-18, each of the original four [shared-runner recipes](../examples/README.md) completed an authenticated request using `jev-1.13.0`. The returned version was also `jev-1.13.0`; responses passed the same contract validation used by the examples and produced application decisions. This does not include the subsequently added computer-use example.

The [Support Router](../projects/support-router/README.md) also processed its six synthetic demo tickets through the live CLI with the same requested and returned version. The run exercised batch requests, contract validation, policy decisions, and output files. Its saved responses were replayed locally without further API calls and reproduced the decisions.

This confirms the exercised request and response paths worked at that time. It does not establish accuracy, calibration, repeatability, availability, latency, or compatibility with future model versions. No downstream ticket assignment, email, or external action was executed.

## Community project checks

The following upstream checks passed on 2026-09-18 using mocked responses. These checks apply to the linked commits, not subsequent releases. The Testimonial miner's maintainer also ran its 11 synthetic fixture emails through the project's live CLI on 2026-09-18 with `jev-1.13.0` (8 requests, 22,390 input tokens: 5 candidates, 3 rejected, 3 header skips); that confirms the request path at that version only. No other community project was tested with live inference, and none was evaluated for model quality.

| Project and reviewed commit | Executed checks |
| --- | --- |
| [Jev Review · 57690af](https://github.com/NiazMorshed2007/jev-review/tree/57690af54ef7d862c2483342c1e61c14dffcf727) | 13 tests, typecheck, and build on Node.js 22. |
| [llama-index-jev · 72c73dc](https://github.com/WiktorB2004/llama-index-jev/tree/72c73dc50bca4b7ea6928ef65ea09f1a7ee4a01e) | 52 reranker and selector tests on Python 3.12. |
| [Testimonial miner · 0852a28](https://github.com/AppitStudio/testimonial-miner/tree/0852a28f6961935afe440b1d698ce22412a4a7ec) | 26 offline tests on Python 3.12 and 3.14 with a fake IMAP source and a scripted model, locally and in the project's CI. |
| [TypeSafeAI.Net · 7f014c9](https://github.com/Hawxy/TypeSafeAI.Net/tree/7f014c92ec4d0cf89896989eb7cd20a0e033e621) | 89 core-client and adapter tests on .NET 10. |

### Tweet directory review on 2026-09-19

All 30 repositories linked in [StudioYebisu's roundup](https://x.com/studio_yebisu/status/2101065176069886152) received individual AI-agent source reviews. The catalog gained **21 detail pages**: four apps, thirteen Jev developer resources, and four explicitly separated [independent model research projects](../community/projects/tools/README.md#independent-model-research). Each addition has a category entry and a canonical upstream link in the root README. The research models are not official Jev weights or independently validated substitutes.

Nine resources were already listed. Seven retained their existing entries; [Jev Search](../community/projects/apps/jev-search.md#newer-provider-options) gained a dated update about optional provider chains, and [Jev for Home Assistant](../community/projects/tools/ha-jev.md#newer-question-editor) gained a dated update about the editor's live preview. Their earlier executed checks remain tied to the earlier revisions, not the newly inspected source.

Reviews covered public source, licensing or missing licensing, setup instructions, concrete decision integrations, data recipients, failure handling and representative test definitions. Each new guide records its exact commit and distinguishes inspected instructions from execution. Source-file paths and upstream Markdown anchors were checked against the reviewed clones; this does not verify published packages or hosted services. Open issue/PR checks found no overlapping proposals.

The new batch included only these candidate execution checks:

| Project | Executed check | Evidence boundary |
| --- | --- | --- |
| [Jev Voice Browser](../community/projects/tools/jev-voice-browser.md) | `node --test test/unit/policy.test.js test/unit/spans.test.js`: **24 passed**, with sanitized environment and network denied. | Mocked policy and text-span behavior; no browser, microphone or provider operation. |
| [jev-rules](../community/projects/tools/jev-rules.md) | **101 offline tests passed** on Node.js 24.11.1 with a sanitized environment and mocked requests. | Local rule selection, hooks and fallback behavior; no plugin installation or live classification. |
| [Jev Review (Dev Agrawal)](../community/projects/tools/jev-review-devagrawal.md) | `node --check src/dashboard/public/app.js` passed on Node.js 22.19.0. | JavaScript syntax only; the project's required Node.js 24 runtime, dependency checks and live review were not tested. |

The remaining new candidates were source-reviewed only. No live inference, desktop/device control, Discord moderation, wallet transactions, GPU deployments or model downloads were performed for this batch. No upstream speed, accuracy, profitability or safety claim was adopted as independently verified. Public source clones, review drafts and raw research remained outside the catalog; contributor affiliations and commercial relationships were not supplied, and human editorial approval is not claimed.

### Implementation guides reviewed on 2026-09-19

The [use-case tour](explore-use-cases.md) links complementary implementations selected through public X discovery and GitHub source review. Each guide records a fixed upstream revision and distinguishes actual execution from inspected instructions. Reviews were prepared with AI assistance; no live inference, browser automation, production database connection, or device action was performed for this batch. Upstream performance claims were not reproduced.

All nine guides received a second source review against their pinned revisions before draft publication. The checks below include preparation evidence; repeated tests are not additional coverage. The second pass corrected a path-intent example, clarified setup and configurable policy, and checked that suggested adaptations are identified as such. Home Assistant remains a source review with targeted extracted-code checks, rather than a tested installation.

| Project guide | Executed checks and limits |
| --- | --- |
| [fast-jev-compaction](../community/projects/tools/fast-jev-compaction.md) | 29 offline tests, typecheck, build, and the guide's synthetic keep/truncate/drop example with assertions. Claude Code plugin installation and live inference were not tested. |
| [Jev for Home Assistant](../community/projects/tools/ha-jev.md) | 28 Python files compiled, 15 YAML examples parsed, extracted usage-accounting code tested, and the pinned client exercised with a synthetic question/response. No full Home Assistant integration suite, installation, or device actions. |
| [Jev Logs](../community/projects/tools/jevlogs.md) | 32 tests passed and one live test was skipped; example typechecks, the fixed CLI demo, and an injected three-event scenario passed. No production delivery, live inference, or retention enforcement was tested. |
| [Jev Search](../community/projects/apps/jev-search.md) | 79 tests across 14 files passed; query-candidate output and hosted homepage reachability were checked. No live searches, production build, or deployment; the tested pnpm version differed from upstream's pin. |
| [Jev Ultrafast](../community/projects/tools/jev-ultrafast.md) | 31 mocked tests, Ruff, two JavaScript syntax checks, and package build. Real-browser connection and guard behavior were not tested. |
| [Laravel AI](../community/projects/tools/laravel-ai.md) | 26 upstream classification/HTTP-fake tests passed with 70 assertions, plus the guide's synthetic routing example. Reviewed development source on PHP 8.4 and Laravel 13; stable-package adoption, Laravel 12, and live inference remain untested. |
| [neo4jev](../community/projects/tools/neo4jev.md) | 161 offline unit tests passed, plus a synthetic edge-direction mapping probe. Remote Neo4j access, Streamlit rendering, and live inference were not tested. |
| [Notra](../community/projects/apps/notra.md) | The guide's composition example and 10 separate synthetic assertions ran against unmodified utilities. No monorepo dependency installation, upstream test suite, database bootstrap, or live scans. |
| [pg-jev](../community/projects/tools/pg-jev.md) | Three extracted PL/Python bodies compiled and five loopback mock requests passed. No PostgreSQL execution: tools were unavailable and Docker was not running. Full SQL regressions, example SQL, and permission isolation remain untested. |

## App directory review

The dedicated [app directory](../community/projects/apps/README.md) identifies user-facing applications and records their source/pricing tags, platforms, access paths, and Jev's specific role. Jev Search and Notra retain the implementation review evidence above; regrouping them does not establish new installation, hosted-access, or live-use results.

On **2026-09-19**, a read-only check of Notra's [product homepage](https://www.usenotra.com) and [official pricing](https://www.usenotra.com/pricing) confirmed published paid hosted plans, supporting its `Open source · Commercial · Paid` tags. Signup, trial eligibility, and checkout were not tested. Jev Search's homepage was fetched without submitting a query; no pricing terms were established there, so hosted pricing remains `Pricing unverified`. TipTour's `Free source build` tag applies to its inspected MIT source, with provider charges separate. No closed-source commercial app was added during this reorganization; the submission path is supported and tested with synthetic catalog fixtures.

[TipTour](../community/projects/apps/tiptour.md) was reviewed with AI assistance on **2026-09-19** at [d192c21](https://github.com/milind-soni/tiptour-macos/commit/d192c21f0fbefa578191e6c329a874142d11fa64). Source inspection covered licensing, build/setup, the Jev integration, stopping policy, data flow, and tests. `bash scripts/test-jev.sh` passed **8 isolated Swift Testing tests** using Apple Swift 6.2.3 and synthetic answers in a sanitized environment. There were no provider requests, app launches, permission changes, or desktop actions. Full app builds, packaged releases, pointer-loop behavior, live inference, and model quality remain untested. Source and test artifacts stayed outside the catalog.

[macbrow](../community/projects/apps/macbrow.md) was reviewed with AI assistance on **2026-09-19** at [a392a9c](https://github.com/timpratim/macbrow/commit/a392a9c56b8ff2978852c0fc911abbeb87b5c5b4). `uv sync --locked` succeeded with Python **3.14.4**; **26 upstream tests** passed with provider credentials removed, external pytest plugins disabled, a fixed test Chrome profile, and macOS `sandbox-exec` denying network access. Ruff lint and format checks passed, as did the credential-free policy listing. One flight-URL helper can attempt LLM compaction before falling back, so these results do not establish that the ordinary test command is offline when credentials are present. Source review covered Jev routing, code generation, policy, browser integration, costs, and data flow. No live inference, voice startup, desktop actions, permissions, or real Chrome connection was tested; upstream performance claims were not reproduced. Source and test artifacts stayed outside the catalog.

[Smart Paste](../community/projects/apps/smart-paste.md) was reviewed with AI assistance on **2026-09-19** at [e4adfc4](https://github.com/nomanjack/smart-paste/commit/e4adfc4e5741a0816674cf28d4d5628b96e32d1a), version **0.4.9**. `npm ci --ignore-scripts` installed its locked development dependencies; **56 upstream tests passed, none skipped**, using Node.js **24.19.0**, a sanitized environment, and macOS `sandbox-exec` denying network access. The tests mock provider answers, extension APIs, and browser DOM behavior. Source review covered MIT/font licensing, installation, the three-stage Jev pipeline, form writes and undo, settings, cancellation, and data handling. Chrome installation, actual website compatibility, live inference, and model quality remain untested. Source and test artifacts stayed outside the catalog.

## Evaluating an application

Use the [evaluation runner](../evaluations/README.md) with labels written before inspecting responses. Keep development and holdout cases separate, count service failures and review decisions, and report errors among automatic decisions alongside their coverage. A small synthetic dataset is useful for finding integration and policy mistakes; it is not representative production evidence.

Keep input datasets and response captures outside this repository. Run live mode only with an explicit request bound and a locally configured key. Re-evaluate questions and policy when changing a model, rubric, or workload. Preserve the requested and returned versions instead of silently treating an alias as fixed.

## Computer-use review

The [computer-use guide](computer-use.md), four new community pages, and expanded Jev Ultrafast page were prepared with AI assistance on **2026-09-19**, using X author posts, current TypeSafe docs, GitHub source/license inspection, and isolated checkouts. No live provider calls, personal desktop actions, Android/iOS control, or comparative performance measurements were performed. Initial browser/mobile checks used Node.js 22.19.0; the added browser form walkthrough used Node.js 24.19.0. Native Mac and Ultrafast tests used Python 3.14.4, and the Cua recipe used Python 3.12.11. See each project's declared runtime requirements before adopting it.

| Project and pinned revision | Checks executed here | Limits |
| --- | --- | --- |
| [Jev Browser (tontoko) · 92a318b](https://github.com/tontoko/jev-browser/tree/92a318b1f4215f064e9dd663172fb08534d2abdc) | `npm ci --ignore-scripts`, Chromium installation, `npm run check`: build and **270 tests passed, zero skipped**. | Real Chromium with local fixtures and injected/fake provider decisions. No live Jev, Firefox/WebKit, or published-artifact verification. |
| [typesafe-computer-use · cc7b506](https://github.com/awlevin/typesafe-computer-use/tree/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1) | `uv sync --frozen`; `uv run --frozen --offline pytest -q`: **144 tests passed**. | Mocked platform/provider boundaries; no screen capture, OS permissions, or desktop operation. |
| [Mobile Jev · 395fc22](https://github.com/droidrun/mobile-jev/tree/395fc222beac4f059f9a0beb337d114a2b066e99) | `npm test`: **55 tests passed**. | Synthetic/mock device and provider tests; no studio build or live device connection. |
| [Cua jev-use · 83f142c](https://github.com/trycua/cua/tree/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use) | Frozen Python install; Python suite initially **35 passed, one skipped**, then **36 passed** after `npm ci --ignore-scripts` enabled the parity test. `npm test`: **24 passed**; `npm run typecheck` passed. Both mock choosers returned valid selection envelopes. | Source subset included the required workflow fixture. No Driver, real UI loop, perception engine, Windows/PowerShell execution, or live provider test. |
| [Jev Ultrafast · 1231850](https://github.com/browser-use/jev-ultrafast/tree/1231850a0bf1a0c0341fe408ef1668dbbfdfac46) | Fresh `uv sync --frozen`; `uv run --frozen --offline pytest -q`: **31 passed**. The guide's exact synthetic chooser script returned `CLICK` mapped to `browser`. | No real browser connection, inspector task, text-helper call, or live Jev evaluation. |

The initial Cua test invocation lacked a repository workflow file used by its tests. Fetching that file at the same pinned revision resolved the setup error; no upstream source was modified. Source clones, logs, dependency caches, and browser downloads stayed outside this catalog. Test subprocesses received no provider credentials.

The expanded Jev Browser guide's exact `catalog-form.mjs` walkthrough ran in isolated headless Chromium with an injected synthetic decision and **zero provider requests**. Its exact field-value assertion passed. The extraction subset (`node --test test/structured.test.mjs`) was rerun: **7 passed**, already included in the 270-test suite above. The Mobile Jev CLI help and both browser walkthroughs were checked against their documented expected output. Native desktop, Android device, and Cua Driver setup commands were source-reviewed; those platform interactions were not executed.

The new [computer-use example](../examples/computer-use/README.md) passed its default synthetic run and **14 offline tests**. They cover selection mistakes, false completion, uncertainty/no-match, malformed responses, stale observations, caller permissions, source copying, non-UTF-8 locale handling, network avoidance, and failure before execution. `npm run check` includes these tests. The example's optional live mode and all real driver adaptations remain untested.

For iOS, the author's Jev + AXe posts were inspected and the public AXe tree was checked at [30f4bfa](https://github.com/cameroncooke/AXe/tree/30f4bfa9bc81817906a60fadedbc913d7314b7e1). No Jev implementation was found there; the guide presents the demonstration separately from adoptable integrations. Source search is not evidence that no private or unpublished implementation exists.
