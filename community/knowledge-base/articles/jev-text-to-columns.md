# Turn text into SQL decision columns with Jev

Jev can turn a text record into probabilities, categories and ordered scores that ordinary SQL can query. Save those judgments as versioned columns, retain uncertainty, and keep access checks and consequential actions in code. This guide builds a small SQLite decision table rather than assuming every ticket deserves a chatbot response.

**Based on:** [JEV TURNS TEXT INTO COLUMNS. THAT MAY MATTER MORE THAN 200× SPEED](https://x.com/fluixoo/article/2103123493567025321) by [Fluixo (@fluixoo)](https://x.com/fluixoo), published September 24, 2026. Appit Studio wrote this original guide with AI-assisted drafting and technical review; no human reviewer is recorded. Fluixo does not endorse our adaptation.

## Key takeaways

- A semantic judgment can be an input to another system. It need not become a final prediction or authorize an action.
- Ask independent questions about the same record together. Keep exact dates, counts, joins and permissions deterministic.
- Preserve the distribution as well as the selected value. A fractional Score is an expected rubric position; Noul is a yes-probability and has no separate confidence field.
- Pin the model and question versions. Recompute changed text and evaluate changed questions before reusing old thresholds.
- Test the complete workflow against a competent baseline. The article's speed headline is not an end-to-end promise.

## Why columns change the workflow

A support message can supply several useful signals: whether a charge is disputed, which queue fits, and how immediate the request sounds. A dashboard can inspect them; a reviewer can correct them; a downstream predictor can learn from them. None of those consumers needs the model to write an essay first.

Fluixo calls this a semantic feature compiler. It is a useful architectural analogy, not a claim that language has become deterministic. Allowed answers can still be wrong, including confidently wrong. Modern LLM structured outputs also constrain schemas, so compare actual error rates and total work rather than assuming typed output alone is unique.

The article points to TypeSafe's [feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery). Its vendor-run experiment uses 2,000 wine notes, with 800 reserved for final evaluation, and reports RMSE falling from 2.47 for word counts to 1.77 for discovered features. The final 29 Score questions supply means and standard deviations; nine Nouls add probabilities, giving 67 numeric columns. The notebook uses `jev-1.12`, not the current `jev-1.13.0`. We inspected that method but did not rerun it. These results establish a reported experiment, not an expected improvement for customer tickets.

An LLM can propose candidate features from development examples. Jev measures their meanings; a supervised model learns their relevance. Keep final test labels out of feature proposals, error feedback and threshold selection. Group related records or split chronologically when that matches deployment. A label embedded in the input is leakage, not predictive skill.

## Build a bounded SQLite decision table

### Project and prerequisites

Use [JevSQL](../../projects/tools/jevsql.md), **source-mentioned** in Fluixo's article, for the SQLite materialization step. We matched its identity and capabilities to EugeneBoondock's pinned [README](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/README.md) and implementation. It is a Node library/CLI, not a loadable SQLite extension or a trained CatBoost pipeline.

JevSQL 0.1.0 is MIT-licensed source and requires Node.js 22.16 or later. Live inference needs a TypeSafe account and key, sends selected row text and questions to TypeSafe, and may incur charges. Account provisioning and live inference were not tested. Protect cached answers, saved parameters and review history as application data.

Start in a scratch directory with synthetic tickets. Inspect the pinned source before running it, retain its license, and follow its setup instructions. Its engine/workflow tests use local mock responses. Avoid the live CLI demos until you intentionally enable paid calls.

### Select records before judgment

Create a separate analysis database with `tickets(id, status, body)` and a unique `id`. Import only records that the application is authorized to disclose. For the first trial, cap the source rows in code and use `rowMode: 'isolated'`, so questions for one record share its state while unrelated records remain separate.

JevSQL's [collection rewrite](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/src/engine.mjs) discovers the judgments before resolving them. Some mixed SQL clauses can be widened during collection. Use `strictCollect: true` and prefiltered input; don't treat a final result filter as a disclosure boundary. A tenant condition belongs in the authorized source selection, not in model policy.

### Define independent columns

The following is our adaptation of the article's ticket example, checked with scripted responses. Its thresholds are trial settings, not validated deployment policy. Save it as `features.sql`:

```sql
WITH eligible AS (
  SELECT id, body FROM tickets WHERE status = 'open'
)
SELECT id,
  jev_noul(body, 'Does the customer dispute a billed charge?') AS billing_p,
  jev_decide(body, 'Does the customer dispute a billed charge?', 0.1, 0.9) AS billing_band,
  jev_choice(body, 'Which queue best fits this request?',
    '{"billing":"Charges and invoices","technical":"Software faults","unknown":"Insufficient evidence or no matching queue"}', 0.8) AS owner,
  jev_choice_conf(body, 'Which queue best fits this request?',
    '{"billing":"Charges and invoices","technical":"Software faults","unknown":"Insufficient evidence or no matching queue"}') AS owner_confidence,
  jev_choice_probs(body, 'Which queue best fits this request?',
    '{"billing":"Charges and invoices","technical":"Software faults","unknown":"Insufficient evidence or no matching queue"}') AS owner_probabilities,
  jev_score(body, 'How time-sensitive is the request?',
    'Routine: no stated deadline|Soon: a stated near-term deadline|Immediate: work is blocked now') AS urgency,
  jev_score_probs(body, 'How time-sensitive is the request?',
    'Routine: no stated deadline|Soon: a stated near-term deadline|Immediate: work is blocked now') AS urgency_probabilities
FROM eligible ORDER BY id;
```

The probability, band, label and distribution projections reuse matching underlying questions; this query needs three distinct judgments per eligible row. JevSQL's [function implementation](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/src/functions.mjs) maps billing values strictly below 0.1 to `0`, strictly above 0.9 to `1`, and the intervening range, including both boundaries, to `NULL`. The owner's confidence gate can also return `NULL`; an explicit `unknown` choice remains a separate outcome. Route either to review.

A score such as 1.775 on this 0–2 rubric can reflect substantial probability at the immediate level. It is not a measured response deadline. Use exact timestamps and service-level calculations in code. [TypeSafe's confidence](https://docs.typesafe.ai/confidence) summarizes distribution concentration, not an independently established probability of correctness.

### Save, refresh and review

Construct the engine with a pinned model, a question/policy cache namespace, `strictCollect: true`, isolated rows, and explicit judgment and estimated-cost limits. If injecting a client for offline tests, its model must match the engine's model. Read the [engine source](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/src/engine.mjs) for these options.

Use `await engine.materialize('ticket_features_v1', sql, { dryRun: true })` to preview work, then materialize only after inspecting the source selection and estimate. Keep preview imports in memory: CLI `--csv` imports even during a dry run. Store decisions separately from operational tickets.

Read the saved table with ordinary SQL:

```sql
SELECT id, billing_p, owner, urgency
FROM ticket_features_v1
WHERE owner IS NULL OR owner = 'unknown' OR billing_band IS NULL
ORDER BY id;
```

Use `await engine.refresh('ticket_features_v1')` after source changes and inspect `engine.changes('ticket_features_v1')`. The [workflow implementation and tests](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/test/workflows.test.mjs) preserve the previous table when a refresh fails. Unchanged judgments can use the cache; a refresh still scans its source and can hold a transaction across inference. It is not automatic scheduling or change-data capture.

Retain the requested and returned model, question/rubric version, input hash, distribution, policy threshold, refresh status and human correction. A failed refresh leaves old values available, so display their age and failure status. A timeout, malformed answer or missing response is a service failure, never a negative billing verdict.

### Evaluate before changing operational behavior

Review disagreements on labeled development cases, then freeze questions and thresholds before testing untouched cases. Measure coverage, mistakes among accepted cases, review workload, refresh time and complete cost. Include inference, retries, stronger-model fallback, human review, storage and corrections. JevSQL's cost cap is based on an estimate; it is not a billing guarantee, and a late failure can follow already billed requests.

The [current model page](https://docs.typesafe.ai/models), checked October 3, lists `jev-1.13.0` at $0.042 per million input tokens with free output. It documents a 64k total request budget and a 32k state-plus-longest-question budget. JevSQL's byte-based planner estimate is not a substitute for checking those token limits. Price and limits can change.

This table supplies review signals. Refund permissions, amount limits, recipient checks and the actual refund remain a separate deterministic workflow with human approval where required. For the broader decision boundary, see [Build a Jev decision gate](jev-decision-gate.md); for learning from corrected outcomes, see [Audit Jev decisions against real outcomes](jev-decision-audit.md).

## Copyable build prompt

```text
Build a bounded ticket-text-to-columns prototype in my scratch project.

Inputs to edit:
- Project directory: <PATH OUTSIDE THE CATALOG>
- Input: <SYNTHETIC CSV OR AUTHORIZED SQLITE SNAPSHOT>
- Columns: <UNIQUE ID>, <STATUS>, <TEXT>
- Eligible rows and row cap: <DETERMINISTIC FILTER>, <MAX ROWS>
- Question/rubric version: <VERSION>
- Model: jev-1.13.0, confirmed against current docs
- Trial billing band: 0.1 / 0.9; trial owner confidence floor: 0.8
- Per-query judgment cap and estimated USD cap: <CAP>, <CAP>
- Live provider calls: disabled by default; <EXPLICIT ENABLE FLAG>

Use Node >=22.16 and JevSQL 0.1.0 pinned to
45f3862f679c064e371a800c2fcc0c5b8b90c6c6.
Read setup/license and implementation first:
https://github.com/EugeneBoondock/jevsql/tree/45f3862f679c064e371a800c2fcc0c5b8b90c6c6
https://docs.typesafe.ai/primitives
https://docs.typesafe.ai/confidence
https://docs.typesafe.ai/models
https://docs.typesafe.ai/model-jaggedness/jev-1.13

JevSQL implements the SQL judgment and saved-table step. Jev answers
bounded meaning questions. Code owns disclosure checks, arithmetic,
dates, review routing and writes. An LLM may propose question wording
from development examples; it must not see final-test labels. Do not
add a writer, CatBoost model or operational action to this prototype.

1. Create synthetic clear, ambiguous, unknown, missing-text and closed
   tickets. Preselect authorized rows before inference. Use a separate
   analysis database, strictCollect and isolated row state.
2. Adapt the guide's three questions: billing Noul, queue Choice with
   unknown, and ordered urgency Score. Preserve raw probabilities,
   confidence where present and a NULL review outcome. Complete question
   instructions belong in each question, not in its lookup ID.
3. Implement an injected mock client with no provider network access.
   Match its model to the engine. Preview without writes or calls, then
   materialize versioned columns and retain audit receipts.
4. Verify the source filter, distinct judgment count, shared projections,
   NULL/unknown routing, exact billing boundaries, unchanged refresh,
   changed-row refresh and rollback on failed refresh. Operational tables
   must not change. Mark stale results after an error.
5. Deliver runnable offline commands, fixtures, SQL, tests, a review query,
   question manifest and an honest validation report. Report synthetic
   checks separately from model accuracy, calibration and billed costs.
6. Live mode requires deliberate enablement, a key read from the
   environment and bounded requests. Explain exactly what leaves the
   machine. Handle HTTP failures, timeouts, invalid/missing responses,
   budget exhaustion and cancellation with visible pending/review work.
7. Before proposing real routing, freeze questions on development data,
   test untouched labeled rows, compare a competent baseline and include
   all review and failure costs. Stop if the prototype does not improve
   the intended workflow. Never authorize refunds from these columns.
```

## Validation and limits

**Source:** We read Fluixo's full ten-section article and code blocks through its final sign-off in logged-in Chrome on October 3, 2026. The body named projects and experiments but exposed no outbound technical links; we located the selected primary sources independently. An exact-title/author search did not establish a republished version. Source images were not reused; the diagram is original and CC0.

**Offline:** We inspected JevSQL's pinned README, license, client, engine, functions and workflow tests. On Node 24.14.0, 21 engine/workflow tests passed. Our exact SQL adaptation passed synthetic checks for the dry run, three judgments per open row, excluded closed records, uncertain owner/billing review, cached repeat refresh, changed-row work and failed-refresh rollback. The mock's probabilities and confidence were scripted software fixtures, not calibrated outputs. No provider request was made.

**Not verified:** TypeSafe signup, live SQL inference, production customer data, the wine benchmark, supervised training, model accuracy, threshold calibration, actual billing or workflow speed. The build prompt is a reviewed handoff, not proof an agent will produce a working deployment. TypeSafe's [known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) include numeric and date reasoning, indirect questions, distracting state and adversarial input. Treat state as untrusted evidence; typed answers do not establish injection resistance or truth.

## Adoption questions

### What does text to columns with Jev mean?

It means asking bounded questions about each text record and storing the returned probabilities, categories or scores as reusable fields. SQL or a supervised model can consume those fields while code keeps exact calculations and authorization separate.

### Is JevSQL a text-to-SQL model?

No. You supply SQL and the questions. JevSQL resolves semantic functions and can save their results as ordinary SQLite tables; it does not generate an arbitrary database query from a user's request.

### Does a Noul probability include confidence?

Noul returns a yes-probability with no separate confidence field. Choice and Score include distributions and confidence. Neither a high probability nor high confidence guarantees that the allowed answer is correct.

### Can I train CatBoost on Jev answers?

Yes, numeric encodings can be features for a supervised model. TypeSafe's wine cookbook demonstrates means and spreads for Scores and probabilities for Nouls. Keep test labels outside feature discovery and evaluate against simpler baselines on your own data.

### What happens when a JevSQL refresh fails?

The saved table and history remain at their previous successful revision. Record the failure and expose stale or pending status; do not interpret old data as a fresh verdict or a missing answer as permission to act.

## Sources, credits and corrections

- [Fluixo's original article](https://x.com/fluixoo/article/2103123493567025321), September 24, 2026: source thesis, examples and qualifications; read in full October 3.
- [TypeSafe feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery): vendor experiment, encodings and held-out evaluation; inspected, not rerun.
- [JevSQL pinned source](https://github.com/EugeneBoondock/jevsql/tree/45f3862f679c064e371a800c2fcc0c5b8b90c6c6): EugeneBoondock's MIT library and offline tests; implements the table step only.
- [Primitives](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [models](https://docs.typesafe.ai/models) and [known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13): current official API boundaries checked October 3.

The SQL, prompt and diagram are Appit Studio's adaptations. The guide credits Fluixo separately from its guide author. We have no recorded commercial relationship with the source author or JevSQL maintainer; JevList is independent of TypeSafe. AI assistance is disclosed, and no human review or source-author endorsement is implied. Propose corrections upstream in [Awesome Jev](https://github.com/AppitStudio/awesome-jev), the editorial source of truth.
