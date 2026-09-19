# Jev Browser (tontoko)

[All projects](../README.md) · [Browser and computer use](../README.md#browser-and-computer-use)

Add semantic field selection and source-backed extraction to Playwright tests, browser scripts, a CLI session, or an MCP client. Start with a local form that needs no account.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tontoko/jev-browser) |
| Maintainer | [tontoko](https://github.com/tontoko). Independently curated; no upstream affiliation or sponsorship is asserted. |
| Format | TypeScript SDK, persistent CLI, and MCP server sharing one core. |
| Requirements | Git, Node.js 22.15+, npm, and Playwright Chromium for this guide. `JEV_API_KEY` or `TYPESAFE_API_KEY` is needed only for live semantic operations. |
| Reviewed package | `@tontoko/jev-browser` 0.5.0; Playwright 1.63.0; TypeSafe JavaScript SDK 0.6.0. |
| License | [Apache-2.0](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/LICENSE). Hosted inference is separate. |

## When to use

This is our strongest starting point **among the implementations inspected for browser forms, extraction, and application tests**. It accepts an existing Playwright `Page`, copies explicit input values, returns extraction evidence, and supports deterministic assertions. This is an assessment of integration fit, not a measured model-quality ranking.

| You want to… | Start with… | Verify independently… |
| --- | --- | --- |
| Fill a signup, contact, or internal admin form despite varying labels | `act()` for one operation; `run()` for a bounded multi-step goal | Exact values and the saved application record |
| Extract catalog items, invoices, or table rows | `extract()` with a Zod schema and `recordsScope` | Required fields, row identity, and attached source evidence |
| Test an application whose UI wording changes | Existing Playwright tests with `new JevBrowser({ page })` | Playwright assertions and backend state |
| Give a coding agent browser tools | The CLI or MCP adapter over the same core | Tool permissions and application-defined success |

Use ordinary locators when the target is already known. Native macOS and iOS app control are outside this package's scope; WebKit support does not make it an iOS app driver.

## How it works

The [decision adapter](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/src/decision.ts) sends observed DOM/ARIA candidates to Jev. Jev selects a candidate ID; Playwright performs the action. Caller-supplied `values` provide exact text, so a separate writing model is unnecessary. Extraction selects observed values and returns their source evidence.

| Responsibility | Owner |
| --- | --- |
| Interpret “the billing email field” among observed candidates | Jev |
| Supply the email, enforce allowed operations, and execute the selected action | Your code and Playwright |
| Establish that the intended record was saved exactly once | Your assertions or application API |

Caller-provided `expect` assertions or an `until` predicate define success. Automatic `ui-readback` combines selected result evidence with local value comparisons and lists unobserved fields; it is weaker than a backend assertion. [Semantic assertions](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/docs/semantic-verification.md) are separately labeled model judgments and can return inconclusive. A model's completion opinion is insufficient by itself.

## Get started

### 1. Install the reviewed source

Run in a directory outside Awesome Jev. Installation downloads packages and Chromium but makes no inference requests. Check `node --version` first; this package needs at least **22.15**.

```sh
git clone https://github.com/tontoko/jev-browser.git
cd jev-browser
git checkout 92a318b1f4215f064e9dd663172fb08534d2abdc
npm ci --ignore-scripts
npx playwright install chromium
npm run check
```

Expect a successful build and **270 passing tests**. They use local pages and injected decisions. Keep this shell in the `jev-browser` checkout for the following commands.

For an existing app, upstream also distributes compiled [GitHub release tarballs](https://github.com/tontoko/jev-browser/releases); follow the [pinned installation instructions](https://github.com/tontoko/jev-browser/tree/92a318b1f4215f064e9dd663172fb08534d2abdc#install). Registry publication and release tarball installation were not checked in this review.

### 2. Fill a local form without a key

Save this original walkthrough as **`catalog-form.mjs` in the upstream checkout root**. It launches a fresh headless Chromium instance, creates a synthetic form, injects an authored choice, fills the field, and checks the exact value. It never connects to your personal browser. Default execution makes **zero provider requests**, even if a key exists in your environment.

```js
import assert from 'node:assert/strict';
import { JevBrowser, JevDecisionEngine } from '@tontoko/jev-browser';

const live = process.argv.includes('--live');
const provider = live ? new JevDecisionEngine({ model: 'jev-1.13.0' }) : null;
let calls = 0;
let answers;
const engine = {
  async decide(request, options) {
    assert.equal(++calls, 1, 'This demo allows one decision only.');
    if (provider) {
      const result = await provider.decide(request, { ...options, maxRetries: 0 });
      answers = result.answers;
      return result;
    }
    // Authored test choice, not a Jev prediction.
    const match = Object.entries(request.questions.action.criteria).find(
      ([, item]) => item?.kind === 'fill' && item.target?.name === 'Email'
        && item.valueKey === 'email',
    );
    assert.ok(match, 'The synthetic Email field must be observed.');
    answers = { action: { choice: match[0], confidence: 1 } };
    return { model: 'synthetic-test-engine', answers };
  },
};
const browser = await JevBrowser.launch({
  engine,
  allowAction: plan => plan.action.kind === 'fill'
    && plan.action.target?.name === 'Email'
    && plan.action.valueKey === 'email',
});
try {
  await browser.page.setContent('<label>Email<input type="email"></label>');
  const result = await browser.act('Fill the Email field with the supplied email.', {
    values: { email: 'reader@example.invalid' },
  });
  assert.equal(await browser.page.getByRole('textbox').inputValue(), 'reader@example.invalid');
  console.log(JSON.stringify({
    mode: live ? 'live' : 'synthetic', status: result.status,
    email: 'reader@example.invalid', providerAttempts: live ? calls : 0,
    answers,
  }, null, 2));
} finally {
  await browser.close();
}
```

Run it:

```sh
node catalog-form.mjs
```

Expected output includes `"mode": "synthetic"`, `"status": "executed"`, `"email": "reader@example.invalid"`, and `"providerAttempts": 0`, followed by the authored choice and confidence. Candidate IDs are observation-specific. This proves observation, action execution, and the exact-value assertion with a fake decision; it does not test Jev's field-selection ability.

### 3. Configure a key privately

Create or obtain a key through [TypeSafe API keys](https://console.typesafe.ai/keys). In the upstream checkout, copy `.env.example` to `.env` **only if `.env` does not already exist**. The upstream ignore file excludes `.env`; keep permissions private and edit it locally:

```sh
cp -n .env.example .env
chmod 600 .env
```

Set `JEV_API_KEY` inside that file using a local editor. Do not put the value in chat, source code, shell command arguments, or an MCP configuration committed to Git. `TYPESAFE_API_KEY` is also supported; `JEV_API_KEY` takes precedence when both are present. The SDK does not automatically load `.env`; the next command explicitly asks Node to load it.

The walkthrough pins `jev-1.13.0`, listed by the [current model documentation](https://docs.typesafe.ai/models) when checked on 2026-09-19. Recheck model availability before changing it. Other upstream examples use their configured SDK default unless `JEV_MODEL` is set.

### 4. Optionally try one live decision

**Explicit live opt-in:** this sends the synthetic page and task to TypeSafe, may incur charges, and fills only the disposable Email field. It permits **one decision and at most one HTTP attempt**, with provider retries disabled. No form is submitted.

```sh
node --env-file=.env catalog-form.mjs --live
```

On success, expect `"mode": "live"`, `"status": "executed"`, and `"providerAttempts": 1`. The returned choice can differ from the fixture; a no-match, denied action, provider failure, or failed exact-value assertion stops the script. Inspect the result before another deliberate run. We verified the synthetic path, not this paid path.

## Examples and practical recipes

### Test an app with Playwright

Start with the [upstream Playwright example](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/examples/playwright.spec.ts). It fills a synthetic email field, clicks Save, and checks the heading and extraction evidence. Its semantic operations require live credentials.

For your own test, keep authentication, fixtures, and cleanup in Playwright. Pass its `page` to `new JevBrowser({ page })`, use Jev only for the ambiguous selection, then assert the exact result. For a create/update test, query a test-only application endpoint and compare the saved record and count; a success toast alone does not establish persistence. Closing a borrowed `JevBrowser` leaves Playwright responsible for its page.

### Fill a multi-step form

The [goal example](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/examples/goal.mjs) runs a synthetic contact server and independently checks that exactly one expected record was saved. Follow the [goal runtime guide](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/docs/goal-runtime.md) when adapting it.

Supply the values as named data, narrow the task, and configure `maxSteps`, `maxDecisions`, and `decisionRetries: 0`. Add a deterministic `until` or `expect` condition. These larger workflows are a separate opt-in from the one-call walkthrough; do not assume `npm run example:goal` has the same one-request budget. Count actual provider attempts when setting a cost limit.

### Extract rows with evidence

This **integration fragment** belongs inside a configured `JevBrowser` workflow; it is not a standalone offline script. Live extraction can make several decisions depending on the observed records and fields:

```js
import { z } from 'zod';

const result = await browser.extract(
  'Read each invoice row: its title and total amount.',
  z.array(z.object({ title: z.string(), amount: z.number() })),
  { recordsScope: 'tbody tr' },
);
console.log(result.data);
console.log(result.evidence);
```

Scope records so amounts stay attached to their own rows. Preserve evidence such as `0.amount` beside each exported record, validate locale-specific amounts/dates in code, and require review for missing fields. A schema validates shape; it does not prove the correct business record was selected. The [source-value selection pattern](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) explains why copying an observed value is useful.

Try the actual upstream extraction fixtures offline:

```sh
node --test test/structured.test.mjs
```

Expect **7 passing tests**, including two-row isolation, source links, nested objects, empty record lists, and rejection of invented defaults. Those tests use synthetic decisions.

### Connect the CLI or MCP server

The [CLI and MCP instructions](https://github.com/tontoko/jev-browser/tree/92a318b1f4215f064e9dd663172fb08534d2abdc#cli-persistent-browser-independent-commands) cover named sessions and client configuration. Native commands such as snapshot, selector-based fill, and assertions need no Jev key. Natural-language `act`, semantic assertions, and extraction can call TypeSafe. Start a dedicated test session, close it when finished, and scope permitted commands in code. Using an MCP client does not remove these distinctions or establish a request budget.

## Customize and troubleshoot

| Symptom or change | What to do |
| --- | --- |
| Chromium executable missing | Run `npx playwright install chromium` in the reviewed checkout. On Linux, follow Playwright's browser-system-dependency guidance if libraries are missing. |
| `CONFIG` / missing key | Check which variable is configured without printing it; use `node --env-file=.env …` for local scripts. Offline injected-engine mode needs no key. |
| `NO_MATCH` or `OBSERVATION_LIMIT` | Inspect `await browser.snapshot()`; narrow `scope`, improve labels, or deliberately adjust limits. Jev cannot select an omitted candidate. |
| `STALE_PLAN` or `STALE_TARGET` | Observe the current page again. Do not reuse a plan after navigation, another action, or a replaced node. |
| `ACTION_FAILED` or `ACTION_INTERRUPTED` | Inspect actual page/application state before retrying; the action may already have had an effect. |
| `EXTRACTION_MISSING` / schema failure | Inspect the source evidence and record scope. Make a field nullable only if missing data is acceptable; do not invent a fallback value. |
| A different label or form | Change the fixture, task, and assertions together. The offline picker deliberately knows only this fixture; it is not semantic inference. |
| Need several actions | Give the workflow an explicit attempt budget and independent success condition; raise the one-decision example's bound only deliberately. |

## Limits and data handling

The [security guide](https://github.com/tontoko/jev-browser/blob/92a318b1f4215f064e9dd663172fb08534d2abdc/SECURITY.md) documents `allowAction` and `allowCommand` hooks. They are application controls, not a network sandbox. The walkthrough's allowlist permits only one field fill. AI observation uses DOM/ARIA; arbitrary canvas interpretation needs another component. Browser events can still race with target checks.

Instructions, page text, URLs, labels, history, and expected semantic meanings can reach TypeSafe. Explicit `values` are withheld from decision payloads, but page echoes and quoted instructions can reveal them. Retain traces privately. Mutation failures are not automatically replayed; read-only decisions in a goal can retry, so a step limit is not a billing cap. Confidence thresholds require task-specific evaluation.

## Review and maintenance

AI-assisted review on **2026-09-19**, pinned to [92a318b](https://github.com/tontoko/jev-browser/tree/92a318b1f4215f064e9dd663172fb08534d2abdc), covered the license, package scripts, provider adapter, completion logic, policy boundaries, and tests. In a separate checkout with provider credentials absent, dependency installation, Chromium installation, and `npm run check` passed: **270 tests, zero skipped**. These used real Chromium with local fixtures and injected/fake decisions.

For this expanded guide, the exact `catalog-form.mjs` synthetic walkthrough passed on a supported Node runtime, including its independent value assertion; `node --test test/structured.test.mjs` passed all **7 tests** again. The current TypeSafe JavaScript SDK, model, and source-value extraction documentation were checked. Live inference, Firefox/WebKit, published artifacts, and workload quality were not tested. The walkthrough is original catalog teaching code using the upstream public API; its fixture responses are authored, not recorded Jev output.

Related: [computer-use guide](../../docs/computer-use.md) · [offline decision cycle](../../examples/computer-use/README.md) · [Jev Ultrafast](jev-ultrafast.md).
