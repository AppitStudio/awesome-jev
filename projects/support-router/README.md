# Support router

Turn a batch of support messages into department suggestions and a human-review
queue. Jev answers two questions about each message; Python applies your routing
policy. The tool writes local files and does not change tickets or contact customers.

## Try the offline demo

Requires Python 3.10 or later and this repository. No packages or API key are needed.
Run from the repository root:

```bash
python3 projects/support-router/run.py
```

The six synthetic tickets exercise billing, technical support, account help,
overlapping requests, uncertain urgency, and uncertain department selection. The
bundled responses are authored fixtures, **not measured Jev results**. Default
policy produces three department suggestions and three human-review entries.

To save a review queue, choose a new output directory:

```bash
python3 projects/support-router/run.py \
  --output-dir /tmp/jev-support-router-demo-001
```

The command prints one JSON object per ticket to stdout and a summary to stderr.
With `--output-dir`, it also writes:

| File | Contents |
| --- | --- |
| `decisions.jsonl` | Every ticket, exact request, response, policy, and decision. |
| `review-queue.jsonl` | Complete records requiring a person to review them. |
| `summary.json` | Counts, token usage, question version, and requested/returned models. |

An existing output directory is refused. Choose another name for a new run. Every
mode requires output paths outside this repository, including symlinked paths.
Output files retain the input messages, so choose a private location for real data.

## Route your own tickets

Create a UTF-8 JSONL file with one object per line. Ticket IDs must be unique:

```json
{"id":"ticket-101","message":"Please send a copy of my invoice."}
{"id":"ticket-102","message":"Our export API is failing and all shipments are blocked."}
```

The router sends only the message to the model. IDs and additional input fields
(including evaluation labels) stay out of model state. Empty messages are allowed
and should resolve to `other`; messages above 20,000 characters are rejected locally.

Inspect the exact requests before a live run:

```bash
python3 projects/support-router/run.py --input tickets.jsonl --dry-run
```

Make `TYPESAFE_API_KEY` available in your shell environment, then opt into API calls:

```bash
python3 projects/support-router/run.py \
  --live \
  --input tickets.jsonl \
  --limit 10 \
  --output-dir /tmp/jev-routing-run-001
```

`--live` sends the selected messages to TypeSafe and may incur charges. The runner
does not load `.env` files automatically. Omitting `--limit` processes the whole
validated input within the live budget. The default budget is 50 requests; larger
batches stop before any call. Use `--max-tickets N` to explicitly raise that budget.
The default model is pinned to `jev-1.13.0`; use `--model` to
explicitly evaluate another version. Each ticket makes one request containing both
questions. Input and configuration are validated before any request.

The CLI makes at most one attempt per ticket and does not retry automatically.
On a service or
response-contract error, the batch stops making requests. The
failed ticket and every remaining ticket enter the review queue with `error` or
`not_processed` status; the process exits with code 1. Token totals include only
successful responses and may omit usage incurred by failed attempts.

## Change departments and review policy

Copy [config.json](config.json) and pass `--config your-config.json`. Use a complete
configuration; unknown settings are rejected to catch spelling mistakes. Department
keys are lowercase identifiers. Provide 2–255 options, including `other`, with
descriptions that distinguish their responsibilities. `human_review` is reserved.

The default department boundaries are:

| Department | Responsibility |
| --- | --- |
| `billing` | Charges, invoices, refunds, payment methods, subscription billing/cancellation. |
| `technical` | Product failures, outages, integration bugs; account-access-only issues excluded. |
| `account` | Login, MFA recovery, access, profile, and nonbilling account lifecycle. |
| `other` | No clear request, no matching team, or equally primary requests for different teams. |

Two independent judgments share the same state:

1. A **Choice** selects the department from your definitions.
2. A **Noul** estimates whether the message states a deadline or current work
   blockage. Frustration and a polite “ASAP” alone do not meet this definition.

Questions tell the model to distinguish current requests from quoted or resolved
background. They also tell it to ignore text attempting to control the classifier.
This guidance still needs evaluation on your messages.

Default policy is explicit, with inclusive acceptance boundaries:

| Setting | Default | Effect |
| --- | --- | --- |
| `department_confidence_min` | `0.8` | Confidence below this value requires review. |
| `urgency_low_max` | `0.15` | Noul at or below this value means `ordinary`. |
| `urgency_high_min` | `0.85` | Noul at or above this value means `high`. |
| `review_uncertain_urgency` | `true` | A Noul between the two boundaries requires review. |

`other` always requires review. With `review_uncertain_urgency: false`, a confident
department may proceed while urgency remains `review`; use that setting only when
the downstream workflow can handle unknown urgency. A high urgency value by itself
does not force review or trigger an external escalation.

Thresholds are illustrative. Choice confidence describes the distribution's
concentration, not the probability that the whole workflow is correct. A Noul near
0.5 expresses uncertainty about “yes,” not medium severity. Tune policy on labeled
development cases and check it on held-out messages before relying on automatic
suggestions. The [evaluation runner](../../evaluations/README.md) uses this same
request builder and policy.

## Inspect and replay a decision

Each output preserves the model's probabilities and the application reason codes:

```json
{
  "department": "technical",
  "route": "human_review",
  "urgency": "review",
  "needs_review": true,
  "review_reasons": ["urgency_uncertain"],
  "department_confidence": 0.92,
  "urgency_noul": 0.5
}
```

`department` preserves the raw selected option; `route` is the application decision.
Other review codes are `department_uncertain` and `department_out_of_scope`. Service
failures use `service_or_contract_error`; tickets skipped after that failure use
`batch_stopped_after_error`. These are explanations of code policy, not generated
model reasoning.

Replay a completed capture without a key or new API calls:

```bash
python3 projects/support-router/run.py \
  --input tickets.jsonl \
  --replay /tmp/jev-routing-run-001/decisions.jsonl
```

Use the same input selection and `--model` as the original run. Each replay is bound
to its full request, so changed text, model, or question definitions are rejected.
You can supply a configuration with changed policy thresholds to see their effects
without rerunning inference. Changing department descriptions requires new answers.
Failed or incomplete captures cannot supply missing responses for replay.
Records and summaries retain `quality_evidence: false` for synthetic fixtures
through subsequent replays. Replay records preserve their source mode/provenance.
`quality_evidence: true` identifies live-origin data; it does not claim a representative benchmark or
acceptable accuracy.

## Embed or extend it

[support_router.py](support_router.py) exposes:

```python
config = load_config()  # Or load_config("your-config.json").
request = build_request({"id": "ticket-101", "message": "Please send my invoice."}, config)
# Obtain and validate a TypeSafe response with the shared client.
decision = decide(request, response["answers"], config)
```

Pass the same configuration to request building and decision-making. Keep any
ticket-system integration outside this module so a suggestion can be inspected
before it changes a workflow. A queue consumer should record the reviewer's chosen
department and urgency alongside the original record for later evaluation.

The question version is `support-router-v1`. Bump it when question meaning changes,
recapture fixtures, and rerun evaluation. Keep the requested model pinned when
comparing results. Both the workflow and CLI use the repository's
[small HTTP teaching client](../../examples/jev_examples/client.py); copy that
dependency too if extracting this project. For broader integrations, use an
[official TypeSafe SDK](https://docs.typesafe.ai/sdk).

Run focused offline tests from the repository root:

```bash
python3 -m unittest discover -s projects/support-router/tests -v
```

The design follows TypeSafe's [Choice](https://docs.typesafe.ai/primitives/choice),
[Noul](https://docs.typesafe.ai/primitives/noul),
[confidence](https://docs.typesafe.ai/confidence), and
[intent-routing](https://docs.typesafe.ai/patterns/intent-routing) documentation.

Code and synthetic fixtures are covered by the repository's
[MIT license](../../LICENSE-CODE).
