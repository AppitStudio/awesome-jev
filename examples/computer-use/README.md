# Computer-use decision cycle

[Computer-use guide](../../docs/computer-use.md) · [All examples](../README.md)

Fill the accounts-payable field with an exact supplied email, preserve the delivery contact, and extract the invoice amount due. This small Python example separates semantic selection from permissions, execution, and assertions.

**The page, answers, and executor are synthetic.** No browser, Mac app, Simulator, or phone is controlled. The default runs offline using the Python 3.10+ standard library.

## Run it

If you have not downloaded the catalog yet:

```sh
git clone https://github.com/AppitStudio/awesome-jev.git
cd awesome-jev
```

From the repository root, run:

```sh
python3 examples/computer-use/run.py
```

The JSON output retains `raw_response` with all choices, probabilities, confidence values, model identity, and synthetic zero usage. Its proposal fills `e2` using the local `billing_contact` value and extracts `€120.00` verbatim from `t2`. The final result is:

```json
{
  "status": "simulated_verified",
  "checks": {
    "billing_value": true,
    "delivery_unchanged": true,
    "not_submitted": true,
    "amount_source": true,
    "amount_value": true
  }
}
```

This is a standalone example; the shared `examples/run.py` and guide helper still run the original four recipes.

## Find your way around

| File | Purpose | What to change first |
| --- | --- | --- |
| [input.json](input.json) | Synthetic goal, UI observation, exact local input value, and independent expected result | Rename a visible field to try another label for the same concept. |
| [mock-response.json](mock-response.json) | Hand-authored model-shaped answers | Inspect the selected IDs and distributions; changing the prompt does not change these scripted answers. |
| [Request and policy](../jev_examples/computer_use.py) | Typed questions, review rules, fixture executor, and assertions | Read `build_request`, then `prepare`, then `verify_fixture`. |
| [Runner](run.py) | Offline/live selection, one-attempt bound, raw output, and exit status | Use `--show-request` to inspect what would leave the process. |
| [Tests](../tests/test_computer_use.py) | Examples of correct and incorrect choices | Start with the wrong-field, wrong-amount, and premature-`done` tests. |

Try the failure cases without editing JSON:

```sh
python3 -m unittest discover -s examples/tests -p test_computer_use.py -v
```

The tests intentionally feed plausible but wrong decisions to the code. They pass when the oracle catches those mistakes. To adapt the fixture, update observations and expected results independently; keep your expected answer out of the model request. A changed mock only tests your application branch, not how Jev responds to the changed wording.

## What Jev would decide

[Request and policy code](../jev_examples/computer_use.py) asks three independent **Choice** questions over one observation:

| Question | Meaning | Code behavior |
| --- | --- | --- |
| `operation` | Fill a field, finish, wait, or report blocked? | Only fill can change the fixture; no submit operation exists. |
| `field` | Assuming a fill is needed, which textbox means accounts payable? | Use only on the fill branch; copy the caller's exact value. |
| `amount` | Which observed text represents the amount due? | Copy the selected source text; do no model arithmetic. |

Question instructions contain their meaning; IDs are only lookup keys. Both target questions include `none`. Relevant confidence below the illustrative **0.8** floor causes review. Uncertainty on the unused field question does not block a `done` result; malformed response envelopes are still rejected.

The request includes an observation fingerprint captured **before** inference. The fixture executor compares current state to that fingerprint, checks the caller's surface/field scope, then changes at most one editable field. It cannot navigate, click, submit, execute scripts, or generate text. Waiting, uncertainty, and missing evidence stop this one-cycle demo rather than retrying automatically.

Afterward, a separate oracle compares exact values and checks that nothing was submitted. A premature `done`, a confidently selected delivery field, or a subtotal mistaken for the amount due fails the oracle. Expected IDs and values are withheld from Jev. The supplied email is also withheld from the initial request; ordinary page text can still contain private values in a real integration.

## Optional live judgments

Review the exact outgoing payload without contacting TypeSafe:

```sh
python3 examples/computer-use/run.py --show-request
```

Get a key from the [TypeSafe console](https://console.typesafe.ai/keys); the [guided setup](../../skills/awesome-jev-guide/references/setup.md#2-obtain-and-configure-a-key-when-live-access-is-wanted) explains accounts and private key storage. After configuring `TYPESAFE_API_KEY` privately in the environment, explicitly opt in:

```sh
python3 examples/computer-use/run.py --live
```

This makes **at most one HTTP attempt**, with no retries and a 30-second network timeout, to `POST https://api.typesafe.ai/v1/systemone` using `jev-1.13.0`. Calls may incur charges. Only this checked-in synthetic task/observation is sent; execution remains in memory. This mode was **not run during this contribution**. `--show-request` takes precedence even when combined with `--live`.

Exit codes: **0** means the synthetic oracle passed; **2** means review, blocked/waiting, or a failed assertion; **1** means a provider, response, or execution error. Provider failure cannot reach the executor. One attempted request does not guarantee the provider received or completed it.

## Adapt it to an actual driver

Replace the synthetic observation/executor with the appropriate [reviewed implementation](../../docs/computer-use.md#choose-a-starting-point), while retaining the independent oracle. Bind references to the specific page/frame or app/window/device. After typing, capture fresh UI state and read the value back; after saving, verify the resulting test record independently.

The fixture fingerprint is conservative: any change stops execution. Real drivers need their own identity/freshness strategy and must account for the race between a check and a UI event. This example does not supply a live driver, vision/OCR, durable trace store, general input schema, or prompt-injection defense. Its input schema is a fixed authored fixture. For known fields and exact selectors, direct automation can be simpler than adding Jev.

## Troubleshooting

| What you see | What to do |
| --- | --- |
| `python3` is not found | Install Python 3.10+; on Windows, try `py -3` in place of `python3`. |
| The runner path cannot be found | Run from the `awesome-jev` checkout root. Keep the shared `examples/jev_examples` directory with the example. |
| `TYPESAFE_API_KEY` is required | Remove `--live` for the offline demo, or configure the key privately in the process environment. The runner does not automatically load `.env`. |
| Exit 2, `human_review`, `wait`, or `blocked` | Inspect raw answers and the proposal's reason. This is a deliberate stop; the demo does not retry or lower its threshold automatically. |
| Exit 2 and `failed` | Inspect which exact check is false. A valid choice can still select the wrong field or amount. |
| A stale-observation error | Build a new request from fresh state; do not reuse the old decision or rewrite its fingerprint. |
| A response-validation or provider error | Compare `--show-request` with the linked API contract. Correct the setup or payload before an explicit retry. |

## Validation and provenance

```sh
python3 -m unittest discover -s examples/tests -p test_computer_use.py -v
```

The offline tests cover wrong semantic selections, false completion, missing/uncertain and malformed answers, stale state, denied actions, disabled controls, preserved fields, source copying, default network avoidance, and service failure. They test code behavior, not Jev accuracy, browser correctness, speed, or cost.

Original AI-assisted example and hand-authored synthetic fixtures; code is covered by this repository's MIT license. API/model/state guidance and the [Choice primitive](https://docs.typesafe.ai/primitives/choice), [function-calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling), and [building guide](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) were checked on **2026-09-19**. Also see the [HTTP contract](https://docs.typesafe.ai/api) and [model reference](https://docs.typesafe.ai/models). The cookbook's example model differs; this example uses the repository's existing `jev-1.13.0` pin.
