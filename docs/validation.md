# Validation scope

This page distinguishes checks of the repository's code from claims about model quality. It contains no live response captures or private evaluation data.

## Offline checks

`npm run check` validates Markdown, local links and anchors, and the Python behavior tests for examples, Support Router, the evaluation runner, and the guide skill's example helper. CI performs these checks without a TypeSafe key. Tests cover request construction, answer validation, policy boundaries, replay behavior, error paths, and credential handling. The guide helper's tests use mocked transport to check its attempt bound and private key handling; they do not constitute live inference or an evaluation of an LLM following the skill.

The bundled inputs and responses are hand-authored synthetic fixtures. Mock mode is deterministic application testing; it is not local Jev inference. Follow [Contributing](../CONTRIBUTING.md#run-checks) to reproduce the checks.

The community directory check connects each README entry to one project page and one category listing, verifies matching canonical sources, and requires a link back to the category. Its tests cover missing pages, duplicate entries, and mismatched navigation. These checks do not verify upstream installation instructions or project claims.

## Live integration checks

On 2026-09-18, each of the four [starter examples](../examples/README.md) completed an authenticated request using `jev-1.13.0`. The returned version was also `jev-1.13.0`; responses passed the same contract validation used by the examples and produced application decisions.

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

## Evaluating an application

Use the [evaluation runner](../evaluations/README.md) with labels written before inspecting responses. Keep development and holdout cases separate, count service failures and review decisions, and report errors among automatic decisions alongside their coverage. A small synthetic dataset is useful for finding integration and policy mistakes; it is not representative production evidence.

Keep input datasets and response captures outside this repository. Run live mode only with an explicit request bound and a locally configured key. Re-evaluate questions and policy when changing a model, rubric, or workload. Preserve the requested and returned versions instead of silently treating an alias as fixed.
