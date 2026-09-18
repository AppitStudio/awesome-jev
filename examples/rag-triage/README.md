# RAG passage triage

Evaluate one query and one retrieved passage using three independent Noul questions: relevance, answer evidence, and contradiction. Code decides whether the passage is a candidate for a later answer-generation step.

```sh
python3 examples/run.py rag-triage --mock
```

Run from the repository root with Python 3.10+. Expected decision: `status: candidate_evidence`, `passage_id: guide-export-01`. No answer is generated or fact-checked.

Adapt [input.json](input.json) and the `rag-triage` branch in [recipes.py](../jev_examples/recipes.py). Noul values at or above `0.85` count as a strong positive signal; values at or below `0.15` count as a strong negative. A strong contradiction gets `conflict_review`; a strong negative relevance/evidence signal gets `exclude`; ambiguous combinations get `human_review`.

These cutoffs demonstrate abstention and require evaluation on your own corpus. Textual support does not establish that a passage is true, current, or authoritative. User-controlled passages can influence model decisions. This example does not implement an injection detector or security boundary. Apply it to each query/passage pair rather than assuming a question can use another question's answer. Follow the [shared live-mode instructions and limitations](../README.md#inspect-or-call-the-api).

References: [Noul](https://docs.typesafe.ai/primitives/noul) and [classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages).
