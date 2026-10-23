# Gate an n8n news brief with Jev: three questions, one filter, visible failures

A daily digest is only useful if it stays quiet when nothing happened. The pattern here puts a cheap Jev judgment between a wide search and an expensive summary: three bounded questions per article, combined in an ordinary n8n filter, with the thresholds in one Config node. This guide explains the template's gate, how to tune it, and changes we recommend before trusting its silence.

**Based on:** [“Build a morning AI news brief with You.com, Jev, and n8n”](https://blog.n8n.io/spotlight-you-com/), a Verified Node Spotlight guest post by **Tyler Eastman** of You.com, published by the [n8n team](https://blog.n8n.io/author/marketing/) on **13 October 2026** and read on **23 October 2026**, together with its [public workflow template](https://n8n.io/workflows/20558-send-weekday-ai-news-briefs-to-slack-with-youcom-and-typesafe-jev/). **Disclosure:** the post is a vendor guest post promoting You.com's own n8n node on n8n's blog. Guide by **Appit Studio**, with AI-assisted research, drafting and an offline simulation; no human reviewer is recorded.

## Key takeaways

- **Filter before the expensive step.** Search wide, judge every result cheaply, and run the writing model only on what survives.
- **Ask atomic questions.** The template asks three separate questions in one Jev request and combines them in the workflow, so each threshold can be tuned on its own.
- **Keep the dials in config.** Topics, the team description, priorities and the materiality threshold live in one node.
- **Silence must mean "nothing material", not "the judge failed".** In the published template, a failed Jev call is filtered out like noise.
- **Tune from logged answers.** Save all three values for every article, not just the survivors, and label a week of mornings.

For the same gate in Python, see [the decision-gate guide](jev-decision-gate.md); for choosing a threshold from labelled data, see [the decision-model evals guide](jev-decision-model-evals.md).

## How the template's gate works

Every weekday at 8am, the workflow searches each Config topic with the You.com node, 15 results from the past day per topic. A Set node normalises each article, and a Remove Duplicates node drops URLs seen in earlier runs. An HTTP Request node then posts one request per article to TypeSafe's `/v1/systemone` endpoint with `model: "jev-latest"`. The `state` holds the watch context from Config (topic, team, what it cares about) and the article's title, description, URL and publication time. It asks three questions:

**Check which export you import.** On 23 October 2026, the n8n template library still exported the HTTP Request version described here. Its page also links Tyler Eastman's [MIT-licensed companion repository](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/tree/2359416d502a5e732df74a6e9be42c38b1d4b81d), whose `workflow.json` already uses TypeSafe's official Evaluate node. Both keep the same three filter fields, `jev-latest`, early deduplication and `continueRegularOutput` error setting. Apply HTTP-body edits to the library export and node-field edits to the companion; they are different snapshots of the same workflow. The repository also documents the author's threshold evaluation; its results are not a measurement of your team's feed.

| Question | Type | What counts | Template filter |
| --- | --- | --- | --- |
| `reports_new_development` | Noul, with true and false criteria and examples | One recent release, launch, law or ruling, not a tracker, roundup, explainer, ranking or opinion | probability ≥ 0.8 |
| `about_topic` | Noul | The topic is the subject, not a passing mention | probability ≥ 0.8 |
| `materiality` | Score, three levels: noise (0), minor (1), material (2) | Whether it changes what the team can build or must do | score ≥ `materialityThreshold`, 1.3 |

A Filter node combines the three with AND. Survivors are grouped by topic, and You.com Research writes one cited brief per topic for Slack. A topic with no survivors gets no post. Note that the grouping is by topic: several outlets covering one launch become one brief together, and merging them into one story is left to the research step.

The source estimates about $0.00004 per article and $0.01 to $0.04 for a whole morning including search and research. At the $0.042 per million input tokens listed on TypeSafe's [models page](https://docs.typesafe.ai/models), $0.00004 corresponds to roughly a thousand input tokens per call, which is plausible given that the question definitions alone run to about 2,000 characters. We did not measure it. The post also says Jev returns "calibrated confidence". TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) is more specific: a [Noul](https://docs.typesafe.ai/primitives/noul) returns a probability of yes without a separate confidence field, and a [Score](https://docs.typesafe.ai/primitives/score) returns a probability-weighted level. Whether those numbers are calibrated on your news feed is something to measure.

## Before you rely on it

### 1. Make Jev failures visible

The template's Jev node is set to continue on error, and the filter reads each answer with a default of 0. When the call fails, the item carries an error instead of answers, scores 0 on all three checks, and is dropped exactly like noise. Because deduplication runs before the Jev call, that article is already marked seen and will not be judged on the next run. A TypeSafe outage, an expired key or a rate limit therefore produces the same Slack channel as a quiet morning.

Our offline simulation of the filter and node order shows both effects. Change the failure path and the point at which an item is marked seen:

- **Use the error output and validate answers.** Set the Jev node's error handling to continue using the error output, and connect that branch to an alert or review queue. On the regular output, require both Noul values to be finite numbers from 0 to 1 and the materiality score to be a finite number from 0 to 2. Missing or invalid answers also go to review; an HTTP success alone is insufficient.
- **Mark seen after a valid judgment.** Move Remove Duplicates after answer validation and before the materiality filter. Use the normalised key `{{ $('Prepare article').item.json.urlKey }}` from the linked input item; the HTTP response does not retain `$json.urlKey`. Keep errored and malformed items out of that node. They remain eligible next time if search still returns them. Because the seen check now runs later, repeated articles can incur another Jev request before they are discarded; measure that cost.

This repairs judgment-stage loss only. An item marked seen can still miss the brief if You.com Research or Slack fails later. Keep a durable retry queue for accepted articles and undelivered briefs if delivery matters. Do not clear all seen history as a delivery retry mechanism.

We simulated this order offline; it has not been run in n8n, so test both branches with a forced error, such as a deliberately invalid key, before switching it on.

### 2. Pin the model

`jev-latest` is an alias that moves to new versions, per TypeSafe's [models page](https://docs.typesafe.ai/models). Replace it with a dated version such as `jev-1.13.0` in the request body, so that a threshold tuned this month still means the same thing next month.

### 3. Log every answer, then tune

Before the filter, append each article's title, URL, topic, the two Noul probabilities and the materiality score to a sheet or table. After a week, mark each row "should have been in the brief" or not, and choose each threshold against the cost of a missed story and a noisy one. The source suggests adjusting `materialityThreshold` after a week. With logged answers you can also see when the 0.8 Noul thresholds, not materiality, are what drop good articles. The [evals guide](jev-decision-model-evals.md) shows how to choose a threshold without fitting it to the same week you measure on.

### 4. Remember the testing trap

The template's sticky note warns that test runs mark articles as seen. Before the first real morning, clear the deduplication history once, as the note describes, or your first brief will skip everything you tested with.

TypeSafe's own [n8n-nodes-typesafe-ai](../../projects/tools/n8n-nodes-typesafe-ai.md) package is an **independent JevList suggestion for the library export**: the blog does not name it, while the linked companion already uses it. Install `@typesafe-ai/n8n-nodes-typesafe-ai`, including the scope. Its Evaluate operation attaches answers to each item; Route branches on one question. Preserve the three-question Evaluate path for this brief and re-check the error branch and field names rather than replacing it with a single route question. You.com search/research, n8n hosting and Slack access have their own requirements and costs; free source code does not include those services or TypeSafe inference.

## Copyable build prompt

```text
Adapt n8n template 20558 (weekday AI news brief with You.com and Jev) for
production.

Inputs:
- Topics: [LIST]; team description: [1-2 SENTENCES]; cares about: [LIST]
- Alert destination for failures: [SLACK CHANNEL OR EMAIL]
- Pinned model: jev-1.13.0 (or the dated version you deploy)

Read first:
- https://blog.n8n.io/spotlight-you-com/
- https://n8n.io/workflows/20558-send-weekday-ai-news-briefs-to-slack-with-youcom-and-typesafe-jev/
- https://docs.typesafe.ai/primitives/noul, https://docs.typesafe.ai/primitives/score,
  https://docs.typesafe.ai/confidence
- https://github.com/youdotcom-oss/n8n-ai-brief-workflow/tree/2359416d502a5e732df74a6e9be42c38b1d4b81d
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/

Changes:
1. Identify the export: template library uses HTTP Request; the linked
   companion uses TypeSafe Evaluate. Pin the model in the corresponding
   request body or node field.
2. Set the Jev node to continue using the error output; send that branch to
   the alert destination with the count and first error message.
3. Validate that both Nouls are finite numbers in [0,1] and materiality is
   a finite number in [0,2]; send missing/invalid answers to review.
   Then move "Skip articles already seen" before the materiality filter,
   using {{ $('Prepare article').item.json.urlKey }} as the key.
4. Before the filter, append topic, title, URL, both Noul values and the
   materiality score to a log table.
5. Keep the three filter conditions; read their thresholds from Config.

Tests before going live:
- One run with an invalid TypeSafe key: expect an alert, no brief, and the
  articles still unseen afterwards.
- One normal run: expect logged rows for every article and briefs only for
  topics with survivors.
- A 200 response with missing answers: expect review and no seen marker.
- A repeated valid article: expect no second brief; another judgment may
  still be billed. Keep the original item linked so the key resolves.
- A Research or Slack failure: retain accepted work in a retry queue;
  seen history alone cannot recover delivery.
- Clear deduplication history after testing in the test workflow only.

Do not add credentials to the workflow JSON. Do not change thresholds until
a week of rows has been labelled.
```

## Validation and limits

- **Source inspected:** the complete post in logged-in Chrome, the template page and its public API export, and the linked companion repository at `2359416`. The library export uses HTTP Request; the companion uses TypeSafe Evaluate. Both were inspected for Config, filters, deduplication order and error settings. Neither was imported into n8n.
- **Offline simulation:** a Node.js 22 script reproduced the template's filter expressions and node order. Three passing answers keep an article; a minor score or a low development probability drops it; an error item is dropped too. With deduplication before judging, an article seen during an outage is not judged the next day. With the fixed order it is judged and posted, if search still returns it.
- **Not tested:** importing or running the workflow in n8n, the You.com node, any Jev or Slack call, the error-output behaviour inside n8n, or the cost figures, which are the source's.
- **Audit replay:** seven additional offline assertions checked a valid item, a low score, an error item, a missing answer, a nonnumeric answer, an out-of-range answer and a valid repeated item. The proposed validation leaves invalid/error items unseen. These authored cases test policy and bookkeeping, not n8n node execution, item linking, persistent history or successful delivery.
- **Disclosure of the source:** a vendor guest post on a vendor blog; it describes You.com's verified node favourably and is not an independent evaluation.

## Adoption questions

### Why ask Jev three questions instead of one?

Each question judges one thing, so you can see which one drifted and tune its threshold separately. The template asks whether an article reports a new development, whether it is about the topic, and how material it is to your team, in one request.

### How much does the Jev filter cost per morning?

The source estimates about $0.00004 per article and $0.01 to $0.04 for a whole morning, including You.com search and research. Check TypeSafe's current pricing and your own token counts before relying on that figure.

### What does materialityThreshold 1.3 mean?

The template's materiality Score has three levels numbered 0 to 2: noise, minor and material. The returned score is probability-weighted, so 1.3 keeps articles that lean towards material. Tune it from a week of logged scores.

### Is Jev's answer here a calibrated confidence?

Not by default. A Noul returns a probability of yes and has no separate confidence field, and a Score returns a weighted level. Whether 0.8 means 80 percent on your news feed is something to check against your own labels.

### What happens if the Jev call fails?

In the template as published, the Jev node continues on error and the filter treats missing answers as 0, so the article is dropped like noise and has already been marked as seen. Route errors to an alert so an outage does not look like a quiet day.

### Do I need You.com to use this pattern?

No. The gate works on any list of items with a title and description. You.com supplies search and the written brief in the template; any search source and any summariser can take those places.

## Sources, credits and corrections

- **Main source:** [“Build a morning AI news brief with You.com, Jev, and n8n”](https://blog.n8n.io/spotlight-you-com/), guest post by Tyler Eastman (You.com), published by the n8n team, 13 October 2026, and its [public template](https://n8n.io/workflows/20558-send-weekday-ai-news-briefs-to-slack-with-youcom-and-typesafe-jev/). The filter-first design, the three atomic questions, the Config dial and the cost estimates are the author's. The question table, the failure-handling analysis and simulation, the logging and pinning advice are Appit Studio's additions.
- **API references:** TypeSafe [Noul](https://docs.typesafe.ai/primitives/noul), [Score](https://docs.typesafe.ai/primitives/score), [confidence](https://docs.typesafe.ai/confidence) and [models and pricing](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Companion and execution reference:** Tyler Eastman's [workflow repository](https://github.com/youdotcom-oss/n8n-ai-brief-workflow/tree/2359416d502a5e732df74a6e9be42c38b1d4b81d) (MIT) and n8n's [Remove Duplicates documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/). The node migration in the companion is distinct from the library export; it preserves the failure settings analysed above.
- **Editorial connection:** [n8n-nodes-typesafe-ai](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/tree/c12537bbd9ed7159b7bbe23678ca128c7b2fb52b), MIT, suggested by JevList; no affiliation with TypeSafe, You.com or n8n is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author, You.com or n8n endorsement, or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
