# Quality rubric

Evaluate a synthetic support reply along two independent dimensions: usefulness with three ordered levels, and clarity with four. Normalize each score to 0–1 before applying 60% usefulness and 40% clarity weights in code.

```sh
python3 examples/run.py quality-rubric --mock
```

Run from the repository root with Python 3.10+. Expected decision: `status: scored`, normalized usefulness `0.9`, normalized clarity approximately `0.8667`, and `weighted_score: 0.8867`.

Adapt [input.json](input.json) and the `quality-rubric` branch in [recipes.py](../jev_examples/recipes.py). A Score is a probability-weighted position in its ordered rubric, so divide by `number_of_levels - 1` before combining differently sized scales. Do not treat the raw score as a probability.

When either dimension has confidence below `0.8`, the example returns `human_review` and withholds the composite. The example assesses wording and usefulness relative to supplied text; it does not verify undocumented product facts. Weights and thresholds have not been calibrated. Follow the [shared live-mode instructions and limitations](../README.md#inspect-or-call-the-api) to opt into API calls.

References: [Score](https://docs.typesafe.ai/primitives/score) and [composite scoring](https://docs.typesafe.ai/patterns/composite-scoring).
