# Replace LLM decision calls with a Jev gate in Python

To stop paying a frontier LLM for yes-or-no decisions, find the agent steps that choose, score or approve rather than write. Compute the facts in code and send them to Jev as state. Ask typed questions in one call, then let reviewed thresholds in code act on the answers. The worked example below gates a code change as ship, return or escalate. Deterministic rules run first, and you run the gate in shadow mode before it blocks anything.

**Based on:** [“Jev Engineering: How to Stop Paying a Frontier Model to Make Yes-or-No Decisions (full course)”](https://x.com/hanakoxbt/article/2101709924828934222) by [Hanako](https://x.com/hanakoxbt), published 20 September 2026. This is an original Appit Studio guide, drafted with AI assistance. Hanako did not write or endorse this guide. No human reviewer is claimed.

Hanako's article argues that many model calls in an agent loop are decisions: which step runs next, whether a result is good enough, whether an action is risky. They produce a label that code immediately branches on. The article splits an agent into generation (an LLM), decision (Jev) and execution (code). It walks through a merge gate built with TypeSafe's Python SDK, then covers batching, dynamic option lists, guardrails, cost and a rollout sequence. It also promotes the author's paid course. We did not review that course, and this guide doesn't depend on it.

## Key takeaways

- **One rule decides where a call belongs.** If a step creates text, keep it with an LLM. If it picks from options you can list, rates something on a scale or answers yes or no, it is a candidate for Jev. If code can compute it exactly, keep it in code.
- **Build the state in code.** Changed files, planned paths, line counts, the test exit code and migration files are facts. Compute them deterministically and send a small, honest snapshot. TypeSafe documents that [irrelevant detail in a large state lowers accuracy](https://docs.typesafe.ai/model-jaggedness/jev-1.13), and that Jev is unreliable at counting, arithmetic and date comparison.
- **The distribution matters more than the label.** A Choice answer carries a probability for every option and a confidence value. A narrow win over the second option should not merge on its own, however confident a sentence-writing model would have sounded.
- **Thresholds and hard rules live in code, reviewed in pull requests.** An irreversible change escalates no matter what the model says. Confidence is not accuracy, so derive thresholds from your own labelled examples, not from an article.
- **Independent questions share one request.** TypeSafe evaluates [every question in a request against the same state](https://docs.typesafe.ai/patterns/fan-out). A question that depends on a fresh result needs a second request after your code updates the state.
- **Typed output is not correct output.** Jev cannot return an option you didn't define. It can still pick the wrong valid option with high confidence, which is why the rollout below starts in shadow mode.

## Build a merge gate with typed answers

The primary path uses the official [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python) (`typesafe-sdk`, version 0.7.1 when we checked). Our example input is a change summary: files touched, the plan's allowed paths and summary, and the test result. The output is one of three decisions: `ship`, `return` (send back to the author) or `escalate` (a person decides).

1. **Pick one bounded decision.** Write down the three outcomes and what belongs in each before calling any model. Keep the actions that follow (merging, commenting, paging someone) in ordinary code you already trust.
2. **Set up access.** You need a TypeSafe account and an API key from the [console](https://console.typesafe.ai/). Access was in early access at the time of writing. Create a Python 3.12 virtual environment, install `typesafe-sdk` and set `TYPESAFE_API_KEY` in the environment, not in source. Try one question in the [Playground](https://console.typesafe.ai/playground) first. Change one field, such as `migrations`, and watch the probabilities move.
3. **Compute the snapshot.** A function takes the diff, the plan and the test exit code and returns plain fields: `files_touched`, `outside_plan` (touched minus planned paths), line counts, `tests`, `migrations` and the plan summary. Nothing in it needs a model.
4. **Apply hard rules before Jev.** Failed tests return the change without a model call. A migration or other irreversible file escalates without a model call. This is our editorial addition. In the article, migrations were a state field Jev saw, and a high blast-radius score triggered escalation.
5. **Ask three questions in one request.** Question IDs are keys for your code and are [not sent to the model](https://docs.typesafe.ai/primitives), so write the complete question in `instructions` and describe each option.

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient, TypeSafeError

QUESTIONS = {
    "verdict": Choice(
        instructions="Given the change summary in the state, what should happen to this code change?",
        criteria={
            "ship": "Tests passed and every touched file is inside the planned paths.",
            "return": "The diff goes beyond what the plan described but is reversible.",
            "escalate": "The change is irreversible or touches something the plan never mentioned.",
        },
    ),
    "blast_radius": Score(
        instructions="How hard would this change be to undo?",
        criteria=[
            "One file; a plain revert undoes it.",
            "Several files; a revert needs care.",
            "Data or schema; it cannot be reverted cleanly.",
        ],
    ),
    "needs_human": Noul(instructions="Should a person read this change before it merges?"),
}


def gate(state: dict) -> str:
    if state["tests"] != "passed":
        return "return"
    if state["migrations"]:
        return "escalate"
    try:
        with TypeSafeClient(model="jev-1.13.0") as client:
            response = client.system_one(state, QUESTIONS)
    except TypeSafeError:
        return "escalate"
    verdict = response.choices["verdict"]
    if response.scores["blast_radius"].score >= 1.5 or response.nouls["needs_human"].noul >= 0.70:
        return "escalate"
    if verdict.choice == "ship" and verdict.confidence >= 0.88:
        return "ship"
    return "return"
```

**Keep the policy order.** Hard rules come first, then the wide-blast-radius or needs-a-person check, then the confident ship path. Everything else returns. The thresholds `1.5`, `0.70` and `0.88` come from the article and are placeholders until you have your own labelled data. A service error escalates instead of shipping, so an outage never merges a change.

**Log everything separately.** Record the snapshot, the model ID from the response, every raw probability and confidence, the policy decision and what a person later decided. Pin a model version (as above) once you tune thresholds, because the `jev-latest` alias [moves when a new release ships](https://docs.typesafe.ai/models).

**Two corrections to the article's code.** SDK 0.6.0 changed `Score` to take an ordered `criteria` list. The article's `Score(legend=…)` form fails validation in 0.7.1. The Noul answer field is `.noul`, not `.p`. The article's sample response also shows a confidence of 0.18 for a 0.52 / 0.46 / 0.02 split. TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) gives a Choice formula that yields 0.28 for that split, so treat the sample as illustrative.

**Expected result:** clean, in-plan changes with confident verdicts ship. Close calls and out-of-plan changes go back to the author. Irreversible, wide or unclear changes, and any call that fails, reach a person. This is a design target checked with fake responses (see below), not a measured accuracy.

### Batch questions and rebuild the options

Adding a question to the same request adds that question's input tokens, not another round trip. The article suggests extra checks for the same gate: whether a change touches authentication, adds a dependency or has a commit message that matches the diff. Answers cannot read each other, so a decision that needs a new search result belongs in a second request.

Build options from what exists now. Offer only reviewers who are available, or only passages you currently hold. Filter obvious mismatches in code before a large Choice. [Jev Ultrafast](../../projects/tools/jev-ultrafast.md) from Browser Use is the article's example of this design. The article names Browser Use's flight-search demo but does not link the repository. The agent builds a fresh table of the controls on the page for each step, and Jev picks an operation and a target from it. A separate text model writes only when a field needs typing, and the example checks the route, date and results independently after Jev reports it is done. It is a **source-mentioned teaching example**, not a merge gate. Its MIT source needs a TypeSafe key, a separate text-model key and Chrome through Browser Harness for live runs, and it finds flights without booking them.

### Roll out in shadow mode

Run the gate next to your current process and let it change nothing. Collect real changes with the decision a person actually made, including ambiguous and adversarial ones. Then plot accuracy against confidence and choose thresholds from that curve. Automate the safest branch first and keep a person on uncertain ones. Version the questions, criteria and thresholds with the code, and rerun the evaluation when the model or rubric changes.

[jevlens](../../projects/tools/jevlens.md) fits this step. It is **independently suggested by JevList**; Hanako doesn't mention it. It uses the same Python SDK to run labelled Choice, Noul and Score cases and stores every probability as JSONL. That lets you change thresholds and replay them without another API call, and it can store unlabelled shadow records. Its MIT source was catalog-reviewed at commit `cd21fce`, where the offline tests passed. Live evaluation sends your cases to TypeSafe and can incur charges. Its suggested thresholds are starting points, not policy.

If you would rather have risk signals in CI than write your own gate, [jev-pr-profiler](../../projects/tools/jev-pr-profiler.md) is an **alternative independently suggested by JevList**. The GitHub Action sets a deterministic risk floor that Jev cannot lower, sends compact pull-request metadata rather than patch hunks, and exposes review-depth outputs. It never approves, merges or blocks on its own. It is MIT-licensed and was catalog-reviewed at commit `482b916` without a live run. It needs a TypeSafe or AI Gateway key, and provider usage can incur charges.

### What it costs

TypeSafe lists `jev-1.13.0` at $0.042 per million input tokens with free output (checked 25 September 2026). At about 1,000 input tokens per decision, 10,000 decisions cost about $0.42 in inference. That is arithmetic, not a benchmark. The article's comparison with frontier models, TypeSafe's speed and cost multiples, and the builders' results it cites (a flight search, paper and email classification, a tool-call relevance filter, a feed filter, an SEO agency's audits) are claims by their authors. We did not reproduce them. Measure cost per completed task: a cheap wrong decision that costs a human round trip is not cheap.

## Copyable build prompt

Copy the following into your coding agent and fill the bracketed inputs. Review the proposed rules and thresholds before any live call.

```text
Build a small Python decision gate for [YOUR DECISION, e.g. whether a code change ships, returns to the author or escalates to a person] in [YOUR PROJECT]. Use the official TypeSafe Python SDK (typesafe-sdk) and read the current docs before writing calls: https://docs.typesafe.ai/sdk/python, https://docs.typesafe.ai/primitives, https://docs.typesafe.ai/confidence and https://docs.typesafe.ai/models. Check the installed SDK version and use its actual field names (for example Score takes an ordered criteria list and a Noul answer exposes .noul).

Inputs I will supply: [THE RAW INPUT, e.g. diff file list, plan paths and summary, test exit code], the allowed outcomes [OUTCOME NAMES AND DEFINITIONS], and hard rules [DETERMINISTIC RULES, e.g. failed tests return; migrations escalate].

Steps:
1. Write a pure function that turns the raw input into a small JSON state with only computed facts. No model call.
2. Apply the hard rules in code before any model call.
3. Define Choice, Score and Noul questions with complete instructions and a description for every option; question IDs are not seen by the model. Ask all independent questions in one system_one request and pin the model version.
4. Map answers to outcomes with named thresholds in code, in this order: hard rules, escalation checks, the confident automatic path, then the safe default. Treat thresholds as placeholders.
5. On any SDK error, timeout or missing answer, choose the outcome that needs a person. Never default to the automatic action.
6. Log the state, model ID, raw probabilities and confidence, the policy decision and the final human decision as separate fields.

Deliver: the module, a pinned dependency list, and tests that use fake SystemOneResponse objects for a confident automatic case, a close race, each escalation trigger, each hard rule and a service failure. Default commands must make no network calls. Add an opt-in shadow-mode script that runs the gate over [N] labelled examples I provide, stores every raw answer, and prints accuracy by confidence band so I can set thresholds; explain that it sends those examples to TypeSafe and costs money. State clearly that the tests prove policy wiring, not model accuracy.
```

## Validation and limits

On 25 September 2026 we read the full article body, its code blocks and the two posts it embeds. We checked the code against the current TypeSafe documentation and inspected the pinned upstream sources behind the three linked catalog pages. We also installed `typesafe-sdk` 0.7.1 in a scratch environment and ran the gate above with **fake responses**, making no API call. A confident ship, a close race, a wide blast radius, a needs-a-person answer, each hard rule and a service error produced the intended decisions. The article's `Score(legend=…)` form was rejected by the SDK. This exercise checks the policy code and SDK types only. We did **not** call TypeSafe, measure latency, cost or accuracy, run Jev Ultrafast, jevlens or jev-pr-profiler, or evaluate the gate on real changes. The article's figures and the builder results it reports are unverified. No edit indicator was visible on the article when we read it. The guide image is an original Appit Studio diagram (CC0), not the article's cover. Recheck SDK field names and pricing before implementing.

## Adoption questions

### When should I use Jev instead of an LLM in an agent?

Use Jev when the answer space is known before you ask: pick an option, score on a scale you define, or answer yes or no. Keep an LLM for writing, planning and explanation, and keep code for anything it can compute exactly.

### How do I choose confidence thresholds for a Jev gate?

Run the gate in shadow mode on real, labelled cases, plot accuracy against confidence and set each threshold from that curve and the cost of being wrong. The numbers in examples are placeholders, and confidence is not an accuracy percentage.

### Can Jev hallucinate or return an invalid answer?

Jev cannot return an option outside the schema you define. It can still choose the wrong valid option with high confidence, so keep hard rules in code and route uncertain answers to a person.

### How much does a Jev decision cost?

TypeSafe lists Jev 1.13 at $0.042 per million input tokens with free output. A decision with about 1,000 input tokens costs about $0.000042 in inference. Retries, human reviews and wrong decisions cost more, so measure cost per completed task.

### Must I install all the linked projects?

No. The primary recipe needs only the TypeSafe Python SDK. Jev Ultrafast is a source-mentioned teaching example of rebuilding options each turn; jevlens is a suggested tool for shadow-mode calibration; jev-pr-profiler is a suggested CI alternative.

## Sources, credits and corrections

Original article: [Hanako, “Jev Engineering: How to Stop Paying a Frontier Model to Make Yes-or-No Decisions (full course)”](https://x.com/hanakoxbt/article/2101709924828934222). It embeds posts by [Rob Hallam](https://x.com/robj3d3/status/2101074194260000982) (a feed filter) and [Ira Bodnar](https://x.com/irabukht/status/2101090579127951694) (an SEO audit pipeline); their figures are their own claims. The article promotes the author's paid course at jev-engineering.site; we found no other republished version. Technical references: [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python) and [changelog](https://docs.typesafe.ai/sdk/python/changelog), [question types](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [models and pricing](https://docs.typesafe.ai/models), [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), and the linked project pages. The guide was written by Appit Studio with AI assistance; no paid placement, affiliate link or human review is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) for a stale API, mismatched project or attribution error.
