# Span selection

Extract email-shaped candidates with a small regular expression, then use Choice to select the one identified as the billing contact. Code returns the original substring and offsets; the model never generates an address.

```sh
python3 examples/run.py span-selection --mock
```

Run from the repository root with Python 3.10+. Expected decision: `status: selected`, `value: invoices@example.org`, `start: 76`, `end: 96`. Offsets use Python string indices and an exclusive end.

Adapt [input.json](input.json) and the `span-selection` branch in [recipes.py](../jev_examples/recipes.py). Candidate IDs link the model's selection to exact text. A `none` option means no candidate clearly matches; confidence below `0.8` results in `human_review` with no selected span.

The regex demonstrates candidate generation, not full email validation. Zero candidates stop locally because there is nothing to select; more than 254 candidates also stop, preserving space for `none` within Choice's 255-option limit. Prefilter a larger input. Python indices differ from byte offsets and JavaScript UTF-16 indices. Editing an input also requires a matching mock response, or use an explicitly opted-in live request. Follow the [shared live-mode instructions and limitations](../README.md#inspect-or-call-the-api).

References: [Choice](https://docs.typesafe.ai/primitives/choice) and [pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook).
