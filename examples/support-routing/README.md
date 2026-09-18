# Support routing

Classify a synthetic support request into a department using Choice. Ask a separate Noul question about explicitly stated urgency. Code combines the answers; neither question depends on the other's result.

```sh
python3 examples/run.py support-routing --mock
```

Run from the repository root with Python 3.10+. Expected decision: `route: technical`, `urgency: high`. The fixture describes a broken CSV export and a deadline today.

Adapt [input.json](input.json) and the `support-routing` branch in [recipes.py](../jev_examples/recipes.py). The `other` option catches requests outside the available departments. Choice confidence below `0.8` or a selection of `other` routes to `human_review`. Noul urgency values between `0.15` and `0.85` produce `review` rather than a forced yes/no priority. These thresholds are illustrative.

This prints a proposed route; it does not send, assign, or escalate a real ticket. Multi-intent and ambiguous requests need evaluation against your own examples. Follow the [shared live-mode instructions and limitations](../README.md#inspect-or-call-the-api) to opt into API calls.

References: [Choice](https://docs.typesafe.ai/primitives/choice), [Noul](https://docs.typesafe.ai/primitives/noul), and [confidence](https://docs.typesafe.ai/confidence).
