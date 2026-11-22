# DSPy Jev decision types and ReAnchor (run DSPy Predict programs on Jev and calibrate their thresholds)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DSPy's experimental System One support: `Predict` runs any Signature whose outputs are all decisions (`bool`, `Literal`, or the new `Noul`, `Score` and `Choice` types) on Jev through `dspy.LM("typesafe:jev-latest")`, keeps the returned probabilities, and the `ReAnchor` optimizer fits thresholds, score cuts and choice weights from cached probabilities with no extra LLM or Jev calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stanfordnlp/dspy) |
| Maintainer | [stanfordnlp](https://github.com/stanfordnlp). Independently curated. |
| Format | Python library (part of DSPy 3.5, experimental API) |
| Requirements | Python with DSPy 3.5+ (`pip install -U dspy`); `TYPESAFE_API_KEY` for the Jev backend. Signatures need decision-only output fields, each with a question-style `desc`. |
| License | [MIT](https://github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/bradwmorris/status/2124349757552480322)). |
| Jev evidence | [`dspy/adapters/decision.py`](https://github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/dspy/adapters/decision.py) at the pinned commit. |

## When to use

- Move existing DSPy classification and triage programs onto Jev, then tune the decision thresholds on your own labelled data with ReAnchor.
- Mismatch: Signatures with free-text outputs; DSPy raises an error naming any field that is not a decision type.

## How it works

`dspy/adapters/decision.py` turns decision-typed output fields into one System One request and reads the answers back from TypeSafe's provider data; the vendored `dspy/_vendor/lm15/providers/typesafe.py` posts to `https://api.typesafe.ai/v1/systemone`. The same decision types also work with ordinary LLMs, so a program can switch between an LM and Jev without changing its Signature. Integration evidence: [`dspy/adapters/decision.py`](https://github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/dspy/adapters/decision.py).

## Get started

Install DSPy, point an `LM` at Jev and run a decision-only Signature; the tutorial walks through `Noul`, `Score`, `Choice` and `ReAnchor`.

```sh
pip install -U dspy
export TYPESAFE_API_KEY=...
python - <<'EOF'
import dspy
dspy.configure(lm=dspy.LM("typesafe:jev-latest"))
class Triage(dspy.Signature):
    """Triage an email."""
    body: str = dspy.InputField()
    needs_response: bool = dspy.OutputField(desc="Do I need to reply?")
print(dspy.Predict(Triage)(body="Can you send the invoice today?").needs_response)
EOF
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tutorial: [github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/docs/docs/tutorials/jev_decisions/index.md](https://github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/docs/docs/tutorials/jev_decisions/index.md)
- ReAnchor API: [github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/docs/docs/api/experimental/ReAnchor.md](https://github.com/stanfordnlp/dspy/blob/226d534da38ab8a39e4d6383e01e121dab50da51/docs/docs/api/experimental/ReAnchor.md)
- Launch post by Drew Breunig and Isaac Miller: [www.cmpnd.ai/blog/building-jev-programs-with-dspy.html](https://www.cmpnd.ai/blog/building-jev-programs-with-dspy.html)
- Mentioned on X: [x.com/bradwmorris/status/2124349757552480322](https://x.com/bradwmorris/status/2124349757552480322)

## Limits and data handling

Experimental API that may change without warning. Inputs of each Predict call are sent to TypeSafe when Jev is the configured LM. The blog's results (for example 90% fewer missed emails after ReAnchor) are the authors' own measurements on their email history.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 226d534da38a](https://github.com/stanfordnlp/dspy/tree/226d534da38ab8a39e4d6383e01e121dab50da51). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
