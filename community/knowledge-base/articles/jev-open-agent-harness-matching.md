# Match client requests to GitHub issues with Jev in an agent harness

An account team logs client requests in one tool; engineering tracks work as GitHub issues. Each week someone has to say which requests are already tracked, where each stands, and which are new. This guide builds that run as three separate steps: code shortlists candidate issues, Jev picks one issue or none, and uncertain answers go to review before any write is approved.

**Based on:** [“I put Jev inside an Open Agent Harness”](https://x.com/akshay_pachaar/article/2109678653974155459) by [Akshay (@akshay_pachaar)](https://x.com/akshay_pachaar), published **12 October 2026** and read in full on **23 October 2026**. The article thanks TrueFoundry, which maintains the harness it uses, for working with the author on it. Guide by **Appit Studio**, with AI-assisted research, drafting and offline checks; no human reviewer is recorded. For Akshay's earlier conceptual comparison, see [Jev vs LLMs](jev-vs-llms.md).

## Key takeaways

- **This is a decision over candidates.** The output is one issue ID or “none”, not prose, so it fits a Choice question.
- **Shortlisting is its own failure point.** The source keeps the top 10 of 300 issues by shared words. A match that does not reach the shortlist cannot be chosen.
- **Equal accuracy, different review.** In the author's 40-request test, both the Jev and the Opus-only versions got 37 right. Jev's low-confidence answers sent more cases to review, and review caught 5 errors.
- **Confidence still lets errors through.** One of Jev's three misses was confident and skipped review.
- **The harness owns credentials and writes.** Generated scripts should not see API keys, and nothing changes in Notion or GitHub until the team approves.

## What the source tested

Akshay's scenario has 40 client requests and 300 GitHub issues, 200 open and 100 closed. At his estimate of about 230 tokens per issue, the backlog is about 69,000 tokens. He identifies three cost levers: context, number of model calls, and which model makes each decision. TrueForge, the harness, addresses the first two with deferred tool loading, offloading large tool results to sandbox files, a code mode and subagents. Jev addresses the third.

The weekly run he describes: a script ranks issues by shared words and keeps ten per request; Jev chooses one of them or “none”; Claude Opus 5.5 drafts new issues for “none” answers and re-checks matches below 0.80 confidence, or 0.90 for closed issues; a script maps the chosen issue to *in progress*, *tracked, not started*, or *fixed or declined*; the account team approves every proposed link and new issue.

Both versions he ran, one with a Jev connector and one where Opus picks from the same shortlists, scored 37 of 40 against known answers. With Jev, 16 answers went to review and 5 errors were caught. Without Jev, 5 went to review and none were caught. His cost comparison estimates Opus at 150 to 250 times Jev's decision cost from list prices and token counts. That is an estimate for the 40 decisions, not a measured bill for the whole run. The test set and agent definitions were not found in the TrueForge repository. An [AI Engineering Hub adaptation](https://github.com/patchy631/ai-engineering-hub/blob/6e39877e2e59d8365ca002fb251ccbb095571282/run-jev-inside-agent-harness/README.md), added by **Sitam Meur (@sitammeur)** on **12 October 2026**, repeats the workflow and results and supplies screenshots and a video, but its directory contains only the README and media assets. Neither inspected repository supplies a machine-readable evaluation set or the two agent definitions, so the results are not independently reproducible from those materials.

Two of the article's descriptions need tightening against current docs. The [models page](https://docs.typesafe.ai/models) lists default limits of 64k tokens per request and 32k per question. Its explicit long-context opt-in raises both, with accuracy and latency tradeoffs; this guide stays within the defaults. The article mentions only the 32k figure. The [Choice page](https://docs.typesafe.ai/primitives/choice) confirms the 255-option limit. The article also says Jev's confidence is calibrated, so 0.88 confidence should be right about 88% of the time, and adds “if that holds for our workflow.” Keep that caveat: the [confidence documentation](https://docs.typesafe.ai/confidence) defines `confidence` as a statistic of the probability spread, not a correctness rate on your data.

## Build the weekly matching run

### Prerequisites

- Read access to the request log and to GitHub issues, with titles, labels, assignees, state and how each closed issue was closed.
- A TypeSafe key for Jev, a generation model for drafting and review, and a harness that keeps credentials outside generated code and supports approval before writes.
- A labelled set: for 40 or more past requests, the issue that actually tracks each one, or “none”. Include near-duplicates, regressions and requests with no issue.

### 1. Shortlist in code and measure shortlist recall

Start with the source's ten candidates from shared words. Before you test Jev, check how often the labelled issue appears in the shortlist. The author notes that clients and engineers describe the same problem in different words. If the right issue is missing for a meaningful share of requests, improve retrieval first, for example with labels, components or embeddings. A better decision step cannot recover a candidate that was never offered.

### 2. Ask one Choice plus a companion Noul

Use issue numbers as option keys and a short title and summary as each description, so code can map the answer back. TypeSafe's Choice page suggests that a “none of the above” option may not work well in many cases and recommends a companion Noul asking whether anything fits. We keep both:

```python
from typesafe_sdk import Choice, Noul, TypeSafeError

ACCEPT = {"open": 0.80, "closed": 0.90}   # the source's starting floors; re-tune on your labels

def match_questions(candidates):
    criteria = {f"#{c['number']}": f"{c['title']}: {c['summary']}" for c in candidates}
    criteria["none"] = "No listed issue tracks the same underlying problem or request"
    return {
        "match": Choice(
            instructions="Which listed GitHub issue tracks the same underlying problem or request as the client request in the state?",
            criteria=criteria),
        "any_match": Noul(
            instructions="Does any listed GitHub issue track the same underlying problem or request as the client request in the state?"),
    }

def decide(response, candidates):
    m, any_match = response.choices["match"], response.nouls["any_match"].noul
    if m.choice == "none":
        return {"issue": None, "route": "review", "proposal": "draft_new_issue" if any_match < 0.3 else "unclear"}
    issue = next((c for c in candidates if f"#{c['number']}" == m.choice), None)
    if issue is None or issue.get("state") not in ACCEPT:
        return {"issue": None, "route": "review", "error": "unknown_issue_or_state"}
    floor = ACCEPT[issue["state"]]
    accepted = m.confidence >= floor and any_match >= 0.7
    return {"issue": m.choice, "route": "accept" if accepted else "review", "confidence": m.confidence}

def match_request(client, client_request, candidates):
    if not candidates:
        return {"issue": None, "route": "review", "error": "empty_shortlist"}
    try:
        response = client.system_one(
            state={"client_request": client_request, "candidates": candidates},
            questions=match_questions(candidates), model="jev-1.14.0")
        return {**decide(response, candidates), "raw": response.model_dump(mode="json")}
    except (TypeSafeError, KeyError) as error:
        return {"issue": None, "route": "review", "error": type(error).__name__}
```

The wrapper sends the client request and candidate metadata as `state`, pins `jev-1.14.0`, preserves the raw response on success and routes failures to review. An empty shortlist is a retrieval failure to inspect, not proof that no issue exists. Unknown issue IDs or states also stay in review. Add independent questions, such as urgency, to the same request if you need them. The 0.7 and 0.3 Noul cut-offs are the starting points suggested in TypeSafe's confidence documentation; the 0.80 and 0.90 Choice floors are the source's. All four are starting values to tune on your labelled set.

The article says all 40 requests went in one batched call but does not show the request. Each question is evaluated against the whole `state`. Stay within both default limits: state plus the largest question at 32k tokens, and state plus all questions combined at 64k. One request per client request is the simplest layout. If batching, put each request's identity and complete matching instruction in its question; response keys alone are not visible to the model. Check both budgets and request isolation before comparing batching performance.

### 3. Map the match to a status in code

Once an issue is chosen, its status is a lookup, not a judgment. Open with an assignee or an in-progress label means *in progress*. Open with neither means *tracked, not started*. Closed means *fixed* or *declined*, depending on how GitHub records the closure. Keep that mapping in code so a reviewer can check it.

### 4. Review what is uncertain, and sample what is not

Send every `review` result to the generation model or a person, with the shortlist and Jev's probabilities. The article's REQ-004 example shows why. A request about search “spinning and then giving up” after a company-wide rollout looked like an existing timeout issue but had a different cause. Jev gave it low confidence and review marked it new. REQ-001 shows the other side: a confident wrong match went straight through. Sample some accepted matches for review each week, especially before a summary reaches a client.

### 5. Keep credentials and writes in the harness

Generated scripts that can read the Notion, GitHub and Jev keys can leak them, and issue text retrieved into a script can steer what it does. The source relies on two TrueForge guards: credentials are applied by the harness, outside the sandbox, and writes need approval. The [TrueForge README](https://github.com/truefoundry/trueforge/tree/109088036870e7839e9f86811e09fb3f4ada3d68) describes sandboxing with secrets kept in the harness, tool approval, and two modes. Local mode is one process on SQLite with no login by default, intended for localhost only. Hosted mode uses Postgres and Redis for shared use. The README requires Node 22.14 or newer; the article says 22.13. Use the README.

TrueForge is MIT-licensed and is the harness the source uses. Model, sandbox and connector usage are billed separately by their providers. It is not in the JevList catalog, so it is linked here as a source-mentioned tool rather than a catalog connection.

### 6. Evaluate before you schedule it

Split labelled requests into tuning and untouched evaluation sets before choosing floors. Use tuning data to choose the floors and report performance on the untouched set; 40 rows are an example starting set, not proof of enough coverage. Run the full pipeline and report, separately: shortlist recall; matches accepted without review and how many were wrong; matches sent to review and how many review corrected; “none” answers and how many were correct. Choose the floors from those counts and the cost of each mistake. Telling a client their bug is being fixed when it is not costs more than an extra review. Then schedule the run, as the source does, to leave proposals waiting for approval.

[jev-issue-radar](../../projects/tools/jev-issue-radar.md) is an **independent JevList suggestion**, not named by Akshay, that shows a small read-only version of this split for GitHub duplicates. It uses lexical candidates, a Jev decision per pair, evidence line IDs checked in code, and no writes. It compares one pair at a time rather than choosing among a shortlist, and calls Jev through OpenRouter. **MIT source, Node 22+; live runs need an OpenRouter key and may incur provider charges.** Issue text leaves the host for OpenRouter/Jev; no live comparison was run for this guide.

## Copyable build prompt

```text
Build a weekly request-to-issue matching run.

Inputs:
- Request log export (read-only): [SOURCE AND FIELDS]
- GitHub repository (read-only token): [OWNER/REPO]
- Labelled evaluation set: [CSV OF request_id, true_issue_or_none]
- Harness: [TRUEFORGE OR OTHER], with credentials outside generated code
- Python environment with typesafe-sdk (0.7.5 checked offline)
- Pinned Jev model: jev-1.14.0

Read first:
- https://x.com/akshay_pachaar/article/2109678653974155459 (source workflow)
- https://docs.typesafe.ai/primitives/choice
- https://docs.typesafe.ai/primitives/noul
- https://docs.typesafe.ai/confidence and https://docs.typesafe.ai/models
- https://github.com/truefoundry/trueforge (if using TrueForge; MIT)

Steps:
1. Shortlist up to 10 issues per request in code. Report shortlist recall
   on the labelled set before any Jev call.
2. One request per client request: Choice over issue numbers plus "none",
   and a Noul asking whether any listed issue matches.
3. Accept only when Choice confidence clears a per-state floor (start at
   0.80 open, 0.90 closed) and the Noul is at least 0.7. Everything else,
   including every "none", goes to review.
4. Map the chosen issue to a status in code from state, assignee, labels
   and how it was closed.
5. Review step gets the request, shortlist and probabilities, and may
   propose a link or draft a new issue. It never writes.
6. All writes to the request log or GitHub wait for my approval.
7. Errors, timeouts, missing answers, unknown issue IDs or states, and
   empty shortlists go to review with the reason kept. Empty retrieval
   does not prove there is no matching issue.
8. Offline tests with a mocked transport and fixture issues: confident
   match, low confidence, closed issue, none, ambiguous none, provider
   error, timeout, connection failure, missing Choice or Noul, unknown
   issue, unknown state and empty shortlist without a network call.
9. Choose floors on tuning rows and evaluate on untouched rows. Report
   shortlist recall, accepted and wrong, reviewed and corrected, none
   and correct, Jev and generation token usage.

Do not claim accuracy or savings beyond the labelled set. Do not schedule
the run until I approve the floors.
```

## Validation and limits

- **Source inspected:** the complete X article and its three code blocks in logged-in Chrome on 23 October 2026; its linked earlier post; the AI Engineering Hub adaptation and its commit credit; and the TrueForge README at a pinned commit. The article thanks TrueFoundry for working with the author. The 40-request test set and both agent definitions were not found in the public repository.
- **Offline example tested:** the question builder and policy above ran against a mocked HTTP transport with `typesafe-sdk` 0.7.5. Thirteen cases passed during this audit: confident open match accepted, low-confidence match reviewed, closed issue below its higher floor reviewed, low-probability “none” proposed as new, ambiguous “none” marked unclear, unknown issue and unknown state reviewed, missing Choice and missing Noul reviewed, HTTP 500, timeout and connection failures reviewed, and an empty shortlist reviewed without a request. The earlier catalog check recorded jev-issue-radar's 48 passing offline tests; this audit re-inspected its pinned source rather than repeating the suite.
- **Not tested:** TrueForge, MCP connectors, Notion or GitHub data, Jev or Opus inference, review yield, cost. The source's 37 of 40 and its cost multiple are the author's results on 40 cases and were not reproduced.
- **Design limits:** lexical shortlists miss differently worded matches; 40 labelled requests give wide uncertainty; floors tuned on one backlog and model version need re-checking when either changes.

## Adoption questions

### Why not give Jev the whole GitHub backlog?

A Choice question accepts up to 255 options and a request has context limits, so a 300-issue backlog with discussions will not fit as one question. Shortlist candidates in code first, and measure how often the right issue survives the shortlist.

### Did Jev make the matching more accurate than Opus?

Not in the source's test. Both versions got 37 of 40 requests right. The difference the author reports is in review: low Jev confidence sent 16 answers for a second look and caught 5 errors, while the version without Jev reviewed 5 and caught none.

### Is Jev's confidence a probability that the match is correct?

No. TypeSafe defines Choice confidence as a statistic of how the probabilities are spread. Whether 0.8 confidence means about 80 percent correct on your backlog has to be checked against labelled requests before it controls what skips review.

### What should happen when no issue matches?

Treat none as a proposal, not a write. Pair the Choice with a Noul asking whether any listed issue matches, and send every none answer to review, where a person or the generation model drafts a new issue for approval.

### Can a confident match still be wrong?

Yes. In the source's test one of Jev's three misses had the highest confidence on the wrong issue and went straight through. Sample accepted matches for review as well, especially when the summary will be sent to a client.

### Is TrueForge required for this workflow?

No. The source uses TrueForge, an MIT-licensed harness, for scheduling, approvals and credential isolation. Any harness that keeps credentials outside generated code and requires approval before writes can run the same shortlist, decide and review steps.

## Sources, credits and corrections

- **Main source:** [Akshay's X article](https://x.com/akshay_pachaar/article/2109678653974155459), 12 October 2026, written with TrueFoundry's involvement as the article states. The scenario, shortlist-decide-review pipeline, floors, status mapping and results are the author's. The companion Noul, shortlist-recall check, accepted-match sampling and evaluation report are Appit Studio's editorial additions.
- **Related publication:** [AI Engineering Hub adaptation](https://github.com/patchy631/ai-engineering-hub/blob/6e39877e2e59d8365ca002fb251ccbb095571282/run-jev-inside-agent-harness/README.md), added by [Sitam Meur](https://github.com/sitammeur) on 12 October 2026. It repeats the source workflow and results with media, adds an explicit shortlist-miss caveat, and is not a published evaluation dataset. The X author and TrueFoundry disclosure remain the primary attribution.
- **Source-mentioned tool:** [TrueForge](https://github.com/truefoundry/trueforge), MIT, maintained by TrueFoundry.
- **API references:** [Choice](https://docs.typesafe.ai/primitives/choice), [Noul](https://docs.typesafe.ai/primitives/noul), [confidence](https://docs.typesafe.ai/confidence) and [models](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connection:** [jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar/tree/5878ba97d70d8aed10a2a628f224a8612d4e870b), MIT, suggested by JevList; not named by the source, and no affiliation with its maintainer is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The article's images are not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement, TrueFoundry relationship or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
