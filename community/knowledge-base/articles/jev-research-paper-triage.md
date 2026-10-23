# Triage research papers with Jev: tune thresholds on labelled splits

A research library grows faster than anyone can read it. Deciding which papers belong in a curated reading collection is a yes-or-no judgment per collection, made from the title and abstract. This guide turns that judgment into Jev Noul questions and spends most of its effort on the part that decides whether the result is usable: labels written before predictions, one threshold per question chosen on a development split, and a frozen test on papers the threshold has never seen.

**Based on:** [“Decision Models for Research Triage”](https://x.com/omarsar0/article/2113296402289676594) by [elvis (@omarsar0)](https://x.com/omarsar0), published **22 October 2026** and read in full on **23 October 2026**. The article benchmarks Jev 1.14 against Drex Max, a competing decision model to which the author had early access, and thanks Nace, its maker, for credits and partnership. Guide by **Appit Studio**, with AI-assisted research, drafting and offline checks; no human reviewer is recorded.

## Key takeaways

- **Define yes before tuning.** The source found that a clear definition of what counts as a member mattered before any threshold work.
- **Label first, predict second.** The 250 papers were labelled before any model predictions were seen.
- **One threshold per model and per question.** Thresholds were chosen on 101 papers and kept fixed for the other 149.
- **Pick thresholds by the cost of each mistake.** The source used F1 for its benchmark but advises weighing which mistakes matter more in your own application.
- **The comparison is small and exploratory.** The author says so, and Jev's competitor was provided with credits and early access.

## What the source measured

elvis built the benchmark around a real problem at DAIR.AI: deciding which papers from a library of thousands belong in reading collections such as *Harness Engineering* and *Self-Improving Agents*. Each of 250 pre-labelled papers was shown to the model as title and abstract only, with two yes-or-no questions, one per collection. The first asks whether the paper is mainly about the harness around a model: prompts, context, memory, tools, agent loops or multi-agent setup. The second asks whether it is mainly about an agent that improves itself through a loop that makes lasting changes to its weights, prompts, memory, skills or code.

Both models received the same instructions. On the 149 test papers, Drex Max got both labels right 76.5% of the time and Jev 1.14 74.5%. Averaged over five repeated runs, the figures were 78.1% and 74.9%. For ranking *Harness Engineering* papers, AUROC was 0.924 for Drex Max and 0.907 for Jev. The author calls this an exploratory comparison, notes the small number of labels and that some papers were used during earlier development, and says freshly labelled papers would give a stronger test.

The article does not publish the papers, labels, instructions or evaluation code, so its numbers cannot be checked. It does not report per-collection precision and recall, the chosen thresholds, or cost. Read the headline gap as two points on 149 papers, not as a ranking of the models.

## Build a paper-triage evaluation with Jev

### 1. Write the definition of yes, then label

For each collection, write a one-paragraph definition with what is in, what is out, and two or three borderline examples. “Mainly about” does a lot of work in the source's questions. A paper that uses an agent loop to study something else is a borderline case your definition should settle. Then label at least a few hundred papers against those definitions without looking at any model output. Include deliberately borderline papers, as the source recommends; they are where thresholds are decided.

Split the labelled set before any model call: a development split for choosing instructions and thresholds, and a test split you touch once. The source used 101 and 149. If one author or one project contributes several papers, keep them in the same split.

### 2. Ask one Noul per collection in one request

Both questions read the same title and abstract, so they belong in one request. In Jev each is a [Noul](https://docs.typesafe.ai/primitives/noul), which returns `noul`, the probability that its statement is true. It has no separate `confidence` field, so the threshold applies directly to that probability.

```python
from typesafe_sdk import Noul

QUESTIONS = {
    "harness_engineering": Noul(instructions=(
        "Is this paper mainly about the harness around a model: its prompts, context, memory, "
        "tools, agent loops or multi-agent setup? Answer yes only if that is the paper's main subject.")),
    "self_improving_agents": Noul(instructions=(
        "Is this paper mainly about an agent that improves itself through a loop that makes lasting "
        "changes to its weights, prompts, memory, skills or code?")),
}
state = {"title": paper["title"], "abstract": paper["abstract"]}
# client.system_one(state=state, questions=QUESTIONS, model="jev-1.14.0")
```

Pin `jev-1.14.0` or `jev-1.13.0`. The [models page](https://docs.typesafe.ai/models) says the `jev-latest` alias moves with new releases, and a threshold tuned on one version is not evidence for another. Store the raw probabilities, the returned model ID and the instructions version for every paper, so thresholds can be re-chosen later without new calls.

### 3. Choose one threshold per question on the dev split

TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) suggests 0.7 for yes and 0.3 for no as Noul starting points. On a labelled dev split you can do better by choosing the cut that minimises the cost of your mistakes:

```python
def pick_threshold(dev, cost_fp=1.0, cost_fn=1.0):
    """dev: list of (p_yes, is_member). Returns the cut with the lowest dev cost."""
    cuts = sorted({p for p, _ in dev}) + [1.01]          # 1.01 = never say yes
    def cost(t):
        fp = sum(1 for p, y in dev if p >= t and not y)
        fn = sum(1 for p, y in dev if p < t and y)
        return cost_fp * fp + cost_fn * fn
    return min(cuts, key=lambda t: (cost(t), -t))      # ties: prefer the stricter cut
```

With equal costs this behaves much like the source's F1 choice. If a missed paper costs a curator more than an extra paper in a review queue, raise `cost_fn`. If a wrong inclusion damages a published collection, raise `cost_fp`. Run it separately for each question. Iterate on instructions only with dev results, never test results.

A middle band can be more useful than one cut. Accept above a high threshold, reject below a low one, and send the band between to a person. Choose both ends on the dev split, and report how many papers land in the band.

### 4. Freeze, then score the held-out split once

Write the thresholds and instruction text to a versioned file before scoring the test split. Report per question: true and false positives and negatives, precision and recall with counts, papers in any review band, and the share with both labels right, which is the source's headline metric. AUROC is a useful check on ranking quality, as the source shows, but it does not tell you how a fixed threshold will behave.

Re-run part of the test split. The source averaged five runs; [jev-paired-replay](../../projects/tools/jev-paired-replay.md), an **independent JevList suggestion**, shows that repeated Jev 1.13 calls on items near a threshold can flip decisions. If papers flip between runs, widen the review band rather than trusting one run.

### 5. Run it daily, and keep checking

[Paper Radar](../../projects/apps/paper-radar.md) is an **independent JevList suggestion**, not named by elvis, that runs this pattern on new arXiv papers. Interests are written in plain English, Jev returns one probability per interest, thresholds sit in config, and every decision and model version is committed to the repository. Its `label` and `calibrate` commands report Brier score, calibration error and a precision/recall table on your labels and suggest thresholds. Those suggestions are fitted and reported on the same labels, so keep separate held-out papers for the final check. Its TypeSafe default model is the `jev-latest` alias; pin a version in `radar.toml`.

Once the collection is live, label a sample of new decisions every few weeks. Papers drift: new terminology, new kinds of agents. A threshold that was right in October may not be in March.

## Copyable build prompt

```text
Build a two-collection paper-triage evaluation with Jev.

Inputs:
- Labelled papers: [CSV OF id, title, abstract, in_collection_a, in_collection_b]
  (labels written before any model output; borderline papers included)
- Collection definitions: [ONE PARAGRAPH EACH, WITH IN/OUT EXAMPLES]
- Mistake costs per collection: [COST OF A FALSE YES, COST OF A MISSED PAPER]
- Pinned model: jev-1.14.0

Read first:
- https://x.com/omarsar0/article/2113296402289676594 (source method)
- https://docs.typesafe.ai/primitives/noul
- https://docs.typesafe.ai/confidence and https://docs.typesafe.ai/models

Steps:
1. Split into dev (about 40%) and test before any model call; keep papers
   from the same project in one split. Save the split.
2. One request per paper: state = title and abstract; one Noul per
   collection. Store raw probabilities, model ID and instruction version.
3. On dev only, pick one threshold per collection by minimising the
   weighted cost of mistakes; optionally a review band with two cuts.
4. Freeze thresholds and instructions in a versioned file.
5. Score test once: per-collection TP/FP/FN/TN, precision and recall with
   counts, review-band size, share with both labels right, AUROC.
6. Re-run 30 test papers twice more; report decisions that flip.
7. Errors and missing answers are counted and reported, never scored as no.
8. Offline tests with recorded fixture probabilities for the threshold
   picker and report, including a collection with no positives in dev.

Do not tune on test results. Report all numbers with counts and state
that the result is limited to this labelled set and model version.
```

## Validation and limits

- **Source inspected:** the complete article through the X API on 23 October 2026. It is short, links only to the competing product's documentation and console, and discloses credits and partnership with its maker. The dataset, labels, instructions and code are not published.
- **Offline example tested:** the threshold picker above on a seeded synthetic dev/test set. Raising the cost of missed papers lowered the cut and raising the cost of false yeses did not lower it; a dev set with no members returned the never-yes cut. This checks the code, not Jev. Paper Radar's offline suite passed 68 of 68 at the pinned commit.
- **Not tested:** any Jev or Drex Max call, real papers, labels, thresholds, AUROC, repeat-run stability or cost. The source's figures are reported as the author's.
- **Design limits:** title and abstract may not settle “mainly about”; a few hundred labels give wide intervals; thresholds need re-checking when the model version, instructions or paper mix changes.

## Adoption questions

### Which Jev question type fits a collection-membership decision?

A Noul, one per collection, asked in the same request against the paper's title and abstract. A Noul returns the probability that its statement is true and has no separate confidence field, so the threshold is applied to that probability.

### Why tune a separate threshold for each question?

Each collection has its own definition, base rate and cost of a mistake, so the same probability can mean different things for two questions. The source tuned one threshold per model and per collection and kept each fixed when scoring the test papers.

### Why label papers before seeing any predictions?

Labels written after reading the model's answers drift toward agreeing with them, which inflates every metric. Write the labels and the definition of yes first, including borderline papers, then run the model.

### Is F1 the right way to pick a threshold?

It is a reasonable default when both mistakes cost about the same. The source notes that your own application should weigh which mistakes cost more. A missed paper in a curated collection and a wrong inclusion rarely cost the same.

### Does the source show that Jev is worse than Drex Max?

It shows a small exploratory gap on one benchmark: 74.5 against 76.5 percent of test papers with both labels right. The author had early access and credits from Drex Max's maker, and some papers had been used during earlier development.

### How many labelled papers do I need?

The source used 101 for tuning and 149 for testing and still called it exploratory. With a few dozen positives per collection, one or two papers can move precision or recall by several points, so report counts with every percentage.

## Sources, credits and corrections

- **Main source:** [elvis's X article](https://x.com/omarsar0/article/2113296402289676594), 22 October 2026. The two collection questions, the label-first 101/149 split, per-model and per-collection thresholds chosen by F1, the repeated runs and the cost-of-mistakes advice are the author's. The cost-weighted picker, review band, flip check and drift sampling are Appit Studio's editorial additions. The source's comparison was supported with credits and early access by a competing vendor; this guide does not evaluate that product.
- **API references:** [Noul](https://docs.typesafe.ai/primitives/noul), [confidence](https://docs.typesafe.ai/confidence) and [models](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connections:** [Paper Radar](https://github.com/Eliot5566/JEV-Paper-Radar/tree/d55299b911ea4ada60912648158bf5258d99ccfa) and [jev-replay](https://github.com/poisson-labs/jev-replay/tree/aeaba514ec54e69fd6c6ba847623172614cfee80), both MIT, suggested by JevList; neither is named by the source, and no affiliation with their maintainers is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The article's images are not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
