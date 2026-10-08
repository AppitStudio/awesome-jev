# Jev content grader: review and revise drafts with Claude

Use Jev to judge a draft against explicit criteria, then give Claude only the passages that need revision. Preserve both versions and compare them under the same rubric before a person chooses what to publish. This guide starts with a small prose-linting path rather than promising a measured productivity gain.

Based on [AI Edge’s complete article, “Opus 5.5 + Jev: The Complete Setup (10x Your Output)”](https://x.com/aiedge_/article/2107835983735787568), published by [AI Edge (@aiedge_)](https://x.com/aiedge_) on **7 October 2026**, read in logged-in Chrome on **8 October 2026**. Guide by **Appit Studio**, with AI-assisted research, drafting and source review; no human reviewer is recorded.

## Key takeaways

- The article separates repeated judgments, deeper writing/reasoning and executable actions. Its examples cover inbox triage, research filtering and grading existing content.
- For content, it proposes clarity and specificity scores, genericness/curiosity checks, rewriting weaker drafts and a second Jev pass. These are suggested workflows, not published evaluation results.
- A concrete first step is [riff](../../projects/tools/riff.md): local static checks plus optional Jev prose findings. It is a **JevList suggestion**, not named or endorsed by AI Edge.
- Keep a fixed brief, stable draft IDs and a bounded revision pass. Confidence is a model statistic, not permission to publish or evidence that a claim is true.

For a broader architecture, read [Building a Jev agent harness](building-a-jev-agent-harness.md). For selecting incoming posts before drafting, use [the content triage guide](jev-content-triage.md). Here the input is an existing draft and the output is a reviewable revision.

## Set up the two roles

The official [TypeSafe agent-skill instructions](https://docs.typesafe.ai/agent-skill) confirm the article’s Claude Code installation sequence:

```sh
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Load the plugin after installation and keep `TYPESAFE_API_KEY` in the environment that launches your worker; never put a real key into a draft or prompt. This guide did not install a plugin into the reader’s account or provision a key.

In Claude Code, `/model` selects the writing model. Current [Claude Code model configuration](https://code.claude.com/docs/en/model-config) identifies `claude-opus-5-5` and requires version 2.1.280 or later for Opus 5.5. Check provider and account availability; the article also says other writing models can fill this role. A Jev skill does not make every agent turn use Jev automatically.

The source links [jevplayground.com](https://jevplayground.com/), which labels itself an **independent third-party playground**. It is distinct from the official [TypeSafe console Playground](https://console.typesafe.ai/playground). Neither playground was run for this guide. Real calls send state to the chosen service; account access and inference charges are separate from source-code licensing.

## A small draft-review path with riff

[Riff’s catalog page](../../projects/tools/riff.md) describes the reviewed **0.1.0** source at commit `70f203e5d356148970e9e1900af3969320b8088d`. It is MIT, requires Python 3.11 or later, and has no source purchase fee. The repository is publicly accessible as checked on 8 October, although that pinned README still calls it private. Install from source; the reviewed README does not establish a PyPI release.

Start with a synthetic Markdown draft that you can inspect in full. From a scratch checkout outside your application:

```sh
git clone https://github.com/scale-venture-partners/riff.git
cd riff
git checkout 70f203e5d356148970e9e1900af3969320b8088d
uv sync --frozen
uv run riff samples/sloppy.md --no-jev --type social_post --format json
```

The final command runs static checks without inference. In this guide’s offline run it reported five findings and exited **1**, meaning findings exist. Exit **0** means no findings, **1** means findings, and **2** means an error; save both the JSON report and stderr rather than treating every nonzero exit as the same failure.

For an explicitly authorized live pilot, fix the document type, select a few relevant rules and use a copied synthetic draft. Riff’s `--type social_post` avoids its separate model-based document classification. Semantic rules send prose blocks to TypeSafe and may incur charges; the pinned backend retries calls. Bound the input and rule list and account for retry attempts, not just successful-call totals.

Useful inspected rules include `JEV001` (preamble), `JEV202` (superficial analysis), `JEV301` (filler vocabulary) and `JEV502` (vague abstraction). These are style checks. They do not establish authorship, detect every factual error or directly reproduce the article’s clarity/specificity ranking.

Hand Claude a saved draft, its brief and the relevant findings. Ask for one revision that addresses those findings while retaining supported facts. Save it under a new version; rerun the same selected checks, then inspect the diff. A lower finding count can conceal a worse draft, so keep the original and let a person accept or reject the revision.

## If you need the article’s full grading rubric

Design clarity and specificity as separate [Score questions](https://docs.typesafe.ai/primitives/score), with concrete ordered descriptions for each level. A three-level Score is a probability-weighted position from 0 to 2, including fractional values; it is not automatically a 1–10 rating. Use [Noul](https://docs.typesafe.ai/primitives/noul) for a single yes/no proposition, such as whether the draft names a concrete action for its audience.

Supply the audience, goal, allowed facts, voice and fixed draft text as state. Each question must contain its full judgment instructions; IDs identify answers and do not supply context. Ask independent questions together, then grade a rewritten draft only after its text exists. Keep ranking weights and tie handling in code.

The article’s statement that Jev only gives yes/no answers conflicts with its own Choice and Score examples. The current docs support all three types. Its blanket “confidence scores” wording also needs narrowing: Noul has only a yes probability; Choice and Score have separate confidence fields. The [confidence documentation](https://docs.typesafe.ai/confidence) defines those statistics from distributions, so copying one universal threshold is inappropriate. Keep ambiguous or incomplete evaluations in review and tune a policy on representative labeled examples, then assess it on untouched drafts.

This rubric adapter is proposed work. The build prompt below specifies what to produce; a completed live integration is not claimed.

## Validation and limits

Read the full X article through “Closing” and inspected the linked setup resources. The author’s earlier newsletter, [“Opus 5.5 + Jev: BEST AI Combo Possible”](https://newsletter.aiedgehq.co/p/opus-5-5-jev-best-ai-combo-possible), lists **AI Edge Team**, **30 September 2026**. It shares the setup theme but covers leads, citation verification and inbox management instead of the X article’s content grader. Treat it as related material, not an identical republication. Its claim that verification eliminates hallucinations is not established by a bounded answer format.

Riff’s pinned source, license, request construction, error handling and reporting were inspected. Its locked environment uses `typesafe-sdk` **0.6.0**; **105 offline tests passed**, with **7 live tests deselected**. The static sample produced five findings. No TypeSafe call, Claude rewrite, installed connector, billing measurement or end-to-end content grader was run.

Riff records provider errors, but its finding helper skips missing/non-Noul answers. It also omits short blocks and link lists and skips oversized text. Therefore a clean report does not prove complete semantic coverage. An adapter should separately track expected versus observed answers and eligible versus skipped passages before marking a review complete.

The article’s “10x,” faster and cheaper framing is promotional, not a benchmark reproduced here. Include grading, writing, retries, hosting and human review when comparing against your actual workflow. A second automated grade may reward superficial changes; independently check facts and editorial quality.

## Copyable build prompt

```text
Build a bounded draft-review tool from the following inputs:
- Working directory: [MY PRIVATE SCRATCH PROJECT]
- Audience, goal and voice: [BRIEF]
- Facts and citations the writer may use: [APPROVED EVIDENCE]
- Input: [AT MOST 3 SYNTHETIC MARKDOWN DRAFTS, 200 WORDS EACH]
- Writing model: [AVAILABLE CLAUDE MODEL; RECORD ITS EXACT ID]
- Mode: offline first; no live calls until I explicitly authorize them.

Use Python 3.11+, uv, and riff 0.1.0 from pinned commit
70f203e5d356148970e9e1900af3969320b8088d:
https://github.com/scale-venture-partners/riff/tree/70f203e5d356148970e9e1900af3969320b8088d
Riff implements local lint and optional Jev paragraph findings. It does not
rank drafts, rewrite them or approve publication. It is a JevList suggestion;
AI Edge did not name it. MIT source; live text goes to TypeSafe and may be billed.

Read current official docs before writing requests:
https://docs.typesafe.ai/agent-skill
https://docs.typesafe.ai/primitives/score
https://docs.typesafe.ai/primitives/noul
https://docs.typesafe.ai/confidence
https://docs.typesafe.ai/sdk/python/api/exceptions
https://code.claude.com/docs/en/model-config
Use the TypeSafe skill if available; say if it is missing.

1. Show the draft IDs, brief, data recipients and proposed rubric first.
2. Run riff with --no-jev --type social_post --format json. Preserve the JSON,
   stderr and exit status. Expected findings exit 1; errors exit 2.
3. Save immutable originals, reports and revision IDs. Keep question/rule
   versions, model IDs, weights and any thresholds in one reviewable config.
4. For offline replay use authored fixtures for findings and failures.
   Keep incomplete coverage, skipped text, missing answers and errors visible.
5. Propose separate clarity/specificity Scores and atomic Noul questions if
   batch ranking is needed. Implement that adapter separately from riff.
   Use full instructions per question, current SDK fields and code-owned math.
6. Only after authorization, run a bounded live pilot. Limit total attempts
   including retries and document separate Jev and writer costs. Pin Jev's
   versioned model; do not expose a key in logs or prompts.
7. Claude revises at most once using the approved facts and observed findings.
   Save the diff and regrade with the identical rubric. No repeat-until-pass loop.
8. Produce a review table of before/after findings, raw typed answers when
   available, coverage status, errors and the exact revision. No publishing.
9. Check synthetic clean/problem drafts, expected findings exit 1, provider
   timeout, missing answer, skipped short block and a rewrite that alters a fact.
   Retain every original and mark failures incomplete. Human review chooses final.

Deliver config, input drafts, reports, revision files, meaningful offline tests
and run instructions. State what was tested versus merely proposed. Do not
claim accuracy, virality, savings or a completed live integration from fixtures.
```

## Adoption questions

### How do I use Jev as a content grader with Claude?

Give Jev a fixed draft and a specific editorial rubric. Keep its typed judgments separate from Claude’s rewrite, then compare the original and revised text under the same rubric. A person checks facts and chooses the final draft.

### Can Jev write or rewrite my content?

No. Jev returns Choice, Score and Noul answers about supplied text. Claude or another text model writes the revision; code preserves draft versions, identifies findings and limits the number of passes.

### Does a high Jev score mean a post will perform well?

No. A rubric measures the supplied text against your criteria. It does not establish audience response, factual accuracy or future reach. Compare rubric judgments with independent human labels and later outcomes before relying on them.

### Does every Jev answer include confidence?

No. Choice and Score return confidence alongside their distributions. Noul returns the probability of yes in noul, with no separate confidence field. Missing answers and service failures require review rather than an inferred pass.

### Can riff replace the article’s complete content grader?

Riff implements static prose checks and optional Jev semantic findings. It does not rank a batch by clarity and specificity, run Claude rewrites or approve publication. Those steps need a separate adapter and human review.

### What happens when a grading call fails?

Keep the original draft and mark its review incomplete. Record errors, skipped text and missing answers separately from findings. Do not treat an empty findings list as proof that every passage was checked.

## Sources, credits and corrections

- **Main source:** [AI Edge’s X article](https://x.com/aiedge_/article/2107835983735787568), 7 October 2026. All three workflow examples and its closing were read in logged-in Chrome.
- **Related earlier version:** [AI Edge Team’s newsletter](https://newsletter.aiedgehq.co/p/opus-5-5-jev-best-ai-combo-possible), 30 September 2026; different examples and promotional claims, separately credited.
- **API corrections:** [Score](https://docs.typesafe.ai/primitives/score), [Noul](https://docs.typesafe.ai/primitives/noul), [confidence](https://docs.typesafe.ai/confidence), [models](https://docs.typesafe.ai/models) and [official skill](https://docs.typesafe.ai/agent-skill), checked 8 October 2026. The TypeSafe skill was not installed in this authoring environment; official docs were used instead.
- **Editorial connection:** [riff’s pinned source](https://github.com/scale-venture-partners/riff/tree/70f203e5d356148970e9e1900af3969320b8088d), MIT. Its static and semantic paths have different data flow. No source-author endorsement or affiliation is claimed.
- **Image:** Appit Studio’s original workflow diagram, dedicated to CC0 1.0. No source image or private browser capture is republished.
