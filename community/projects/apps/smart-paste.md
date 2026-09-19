# Smart Paste

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

An experimental Chrome extension for distributing pasted text across relevant web form fields, with exact source copying and undo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nomanjack/smart-paste) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/nomanjack/smart-paste#readme); no separate product website is listed. |
| Pricing and access | [Unpacked installation](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/README.md#install) from MIT source, with no app purchase step. Requires a TypeSafe account/key; inference can incur separate charges. Checked 2026-09-19. No hosted service or paid distribution was verified. |
| Jev evidence | Inspected [question and extraction pipeline](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/core.js) and [API worker](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/worker.js). Tests mock provider answers; live inference was not tested. |
| Disclosure | Independently curated with AI assistance, not submitted on the creator's behalf. The contributor reports no affiliation or commercial relationship with the project or creator. Source was inspected; inclusion is not endorsement. |
| Maintainer | [Noman Ijaz / nomanjack](https://github.com/nomanjack). |
| Format | JavaScript Chrome Manifest V3 extension. No compilation or npm installation is required to load it. |
| Platform and availability | Version **0.4.9**, experimental, distributed as an unpacked Chrome extension. Upstream documents shortcuts for macOS, Windows, and Linux; cross-platform operation and store distribution were not tested. No GitHub releases were listed at review. |
| Jev's role | Choice questions select passages and token boundaries; Noul questions judge relevance and proposed values. Matching requires explicit enablement and a key. No second model provider was found in the inspected runtime. |
| Requirements | Chrome Developer mode and a TypeSafe API key entered in extension settings. Development tests require Node.js; the locked dependencies require **22.22.2+ within 22.x, 24.15.0+ within 24.x, or 26+**, more specific than the README's Node 22+ guidance. |
| License | [MIT](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/LICENSE); bundled Inter font uses the [SIL Open Font License](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/assets/OFL.txt). |

## When to use

Try it for moving a contact block into name, email, and message fields, or extracting a title and description from issue notes. Developers can also study how model-selected boundaries become exact source slices before an application writes to a form.

It fits supported text controls in an existing Chrome page. It does not navigate a workflow, submit forms, or support every kind of input.

## How it works

The [content script](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/content.js) intercepts a paste when matching is configured and the focused control is supported. The [adapters](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/adapters.js) collect up to eight controls from the focused form, dialog, or fieldset. They exclude populated neighboring fields, but retain the focused field even when it already contains text.

The worker calls `POST https://api.typesafe.ai/v1/systemone` with `jev-latest`, Bearer authentication, state, and typed questions. Its wire format matches the [current HTTP API reference](https://docs.typesafe.ai/api) inspected during review; live compatibility remains untested and the alias can change.

1. JavaScript constructs bounded passages with original offsets. Jev selects a passage per field and judges whether the text is relevant to the form. Code requires a passage probability of at least `0.65`, a `0.15` lead, and a relevance Noul of at least `0.65`.
2. For accepted passages, Jev selects start and end tokens. Code requires each boundary probability to reach `0.60` with a `0.15` lead, checks ordering, slices the original text, and validates email, URL, and telephone shapes.
3. Jev judges each proposed value. Code requires a verification Noul of at least `0.85`, rejects identical values assigned to differently labeled fields, and returns accepted rows.

The client checks that the form and focus are still current before inserting. It reads values back twice after blur and reports retention failures; undo restores prior values only where later edits have not changed the inserted text. These thresholds and heuristics are application policy, not demonstrated accuracy guarantees. Full raw answers are processed in the worker but are not retained as an inspection log.

## Get started

Retrieve the reviewed source; these commands do not make inference requests:

```sh
git clone https://github.com/nomanjack/smart-paste.git
cd smart-paste
git checkout e4adfc4e5741a0816674cf28d4d5628b96e32d1a
```

Follow the pinned [installation instructions](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/README.md#install). The following browser steps were source-reviewed, not executed:

1. Open `chrome://extensions`, enable **Developer mode**, select **Load unpacked**, and choose the repository folder.
2. In Smart Paste settings, enter your TypeSafe key, enable matching, and save. Reload existing web tabs.
3. On a non-sensitive test form with Name, Email, and Message controls, focus the empty Name field and paste this synthetic text once:

```text
Name: Alex Morgan
Email: alex@example.com
Message: Please send the workshop schedule.
```

**That paste sends the text and form metadata to TypeSafe and can make up to three billable requests.** Expect matched values or a visible no-match/error result; no live result is claimed for this sample. Review the fields before submitting. Use the toolbar's **Undo** to restore eligible changes; the extension button or `⌘J` / `Ctrl+J` opens the toolbar.

## Examples and demos

- [Matching pipeline tests](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/tests/pipeline.test.js) exercise source offsets, names and companies, invalid boundaries, and rejected verification using supplied answers.
- [Form-flow tests](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/tests/flow.test.js) run the content script against jsdom forms with mocked extension messages, including paste, cancellation, and undo.
- [Upstream sample text](https://github.com/nomanjack/smart-paste/blob/e4adfc4e5741a0816674cf28d4d5628b96e32d1a/sample.txt) provides issue and other destination notes; its presence does not establish support for date/time input controls.

No separate hosted demo or video was found. To run the mocked suite from the checkout with a supported Node version:

```sh
npm ci --ignore-scripts
npm test
```

Dependency installation contacts the package registry; the tests use mocked network transport and model responses, without a TypeSafe key.

## Limits and data handling

The manifest injects content scripts into HTTP and HTTPS pages. Supported controls are visible text, email, telephone, URL, textarea, and basic contenteditable fields in the top-level document. Password and credential/payment-labeled controls are filtered heuristically. Selects, checkboxes, date/number inputs, iframes, shadow DOM fields, and some rich editors are unsupported. Chrome internal pages and its built-in PDF viewer cannot load these content scripts.

The full pasted text goes to TypeSafe with the form heading, field labels/types, and focused/occupied flags. Existing field values are omitted. Filtering destination fields does **not** redact arbitrary secrets from the source text; the specific configured API key is rejected if present. The destination website can observe inserted text and dispatched input/change events before submission.

Settings and the key use `chrome.storage.local`, restricted to trusted extension contexts, rather than Chrome sync storage or an OS credential vault. The separate capture path stores text in `chrome.storage.session`; direct paste passes its current text without replacing that stored capture. The inspected code does not continuously read the system clipboard. Bundled fonts avoid a remote font request.

Inputs are limited to 12,000 characters and 120 passages, with at most 250 tokens considered per boundary-selection passage. One paste makes one to three sequential HTTP calls, with a ten-second overall timeout and no automatic HTTP retry. Settings changes, stale context, or cancellation stop pending results. Unknown, missing, or insufficiently supported answers leave affected fields unfilled.

When matching is enabled, a failed or uncertain match does not automatically perform the original native paste. Disable matching in settings to return to native paste behavior. The focused field may be replaced wholesale; existing neighboring values are excluded. A partial insertion failure requires reviewing the form and using undo where appropriate. Model verification and heuristic field exclusions do not guarantee correctness or prompt-injection resistance.

## Review and maintenance

Reviewed **2026-09-19** at [e4adfc4](https://github.com/nomanjack/smart-paste/commit/e4adfc4e5741a0816674cf28d4d5628b96e32d1a), version **0.4.9**. AI-assisted inspection covered the README, licensing, manifest, package lock, Jev pipeline, worker, adapters, paste handling, settings, and test suite. Existing catalog entries and open issues/PRs were searched; no duplicate was found.

The source checkout and test artifacts stayed outside this catalog. Dependency installation used `npm ci --ignore-scripts`; verification used Node.js **24.19.0**, a sanitized environment, and macOS `sandbox-exec` denying network access. All **56 upstream mocked tests passed**, with none skipped; see the [catalog validation record](../../../docs/validation.md#app-directory-review). Chrome installation, browser permissions, real website compatibility, live inference, and model quality were not tested. No user clipboard or provider credentials were accessed.

Related: [Span selection](../../../examples/span-selection/README.md) teaches exact source copying offline; [Jev Browser](../tools/jev-browser-tontoko.md) provides a developer-oriented Playwright integration.
