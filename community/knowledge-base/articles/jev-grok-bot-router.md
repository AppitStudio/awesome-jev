# Wire Jev into Grok Bot: a shadow-first router skill

A Grok Bot agent can waste most of its budget on predictable mistakes: reopening a browser for a file it already has, reading more sources than the question needs, or repeating an approach that already failed the same way. This guide adds one Jev router in front of those steps, logs its advice for a week, and then lets it skip work only where code-owned thresholds and the log support it.

**Based on:** [“How To Wire Jev Into Grok Bot: The Best Agent I've Built”](https://x.com/0x_rody/article/2112558839589417355) by [rody (@0x_rody)](https://x.com/0x_rody), published **20 October 2026** and read in full on **23 October 2026**. Guide by **Appit Studio**, with AI-assisted research, drafting and offline checks; no human reviewer is recorded. rody also wrote the source of our [project ideas guide](jev-project-ideas.md); this is a different article.

## Key takeaways

- **One question, few fields.** The article's router asks a single Choice question over four short fields: goal, task type, last error and repeat count. Jev never sees the conversation or repository.
- **Shadow before active.** Log the router's choice beside what the agent actually did, review the disagreements, then let it act.
- **Code owns side effects and thresholds.** Approval for sending, publishing, paying or deleting should not depend on a model answer. A skip should require a confidence floor that you set from the shadow log.
- **The state must contain the evidence.** Jev cannot know an artifact exists or how many sources were read unless code puts that fact in the state.
- **A shared computer means a shared key.** Every bot on the account can read the environment variable that holds the key.

For general placement of decisions in agent loops, see [agent-loop patterns](jev-agent-loops.md); for routing a task to a worker, see [the worker router](jev-agent-worker-router.md). This guide covers the hosted-agent install and rollout path.

## What the article proposes

rody's seven steps, summarised: create a TypeSafe key; deliver it to the Grok Bot computer through a masked secret request rather than chat; install `typesafe-sdk` and smoke-test one Choice call; build a `route()` function with five actions (`proceed`, `reuse_cache`, `stop_retry`, `research_capped`, `ask_human`); install it as a `jev-usage-router` skill that fires before browser sessions, research passes, retries and extra bots; run it in shadow mode for a week with a daily report; then switch to active mode with two kill switches (a `bypass jev` phrase and `{"enabled": false}`).

The article includes copyable instructions for each step. Its advice to measure on your own traffic “rather than taking anyone's number, including mine” is sound, and it gives no cost or accuracy figures of its own. It names two platform limits: one computer per account, which the [Grok Bot overview](https://cursor.com/docs/grok-bot) confirms, and 20 retained run records per routine, which we could not confirm in public documentation. Treat the second as the author's report and export your logs regardless.

## Build the router

### Prerequisites

- A TypeSafe account and API key; calls are billed per input token, as listed on the [models page](https://docs.typesafe.ai/models).
- Python with `typesafe-sdk` (we checked **0.7.5**) on the Grok Bot computer.
- A private repository for the router code and skill, so the authoritative copy lives outside the agent's computer.

### 1. Deliver the key, then limit what it can cost

Follow the article's approach: ask the bot to request the key through a masked secret prompt, set it as `TYPESAFE_API_KEY`, and confirm only that it is readable. Then add what the article implies but does not spell out. Because every bot on the computer can read that variable, use a dedicated key, set a spending limit in the TypeSafe console if your plan offers one, and rotate the key if any bot processes untrusted web content that could instruct it to reveal environment variables.

### 2. Smoke-test with a pinned model

The article opens the client with `model="jev-latest"`. That alias currently points to `jev-1.13.0`, while `jev-preview` points to `jev-1.14.0`, according to the [models page](https://docs.typesafe.ai/models). An alias can move without a code change, so pin a versioned ID before you collect a shadow week. A threshold tuned on one version is not evidence for the next. Record `response.model` with every decision.

The article's checklist for the smoke test is useful: the answer should be one of your own options, with a full probability spread and a `confidence` value. In SDK 0.7.5, `response.choices["action"]` is a typed view over `response.answers`; a missing answer raises `KeyError`, which the router must catch.

### 3. Give Jev the facts it needs, and keep side effects in code

Two of the article's five criteria describe facts that its four-field state does not contain. “A fresh artifact for this already exists” and “enough sources are already gathered” can only be judged if code tells Jev which artifact exists and how many sources were read. The fifth, `ask_human` for steps that send, publish, pay or delete, is known from the tool being called. We move it into code, before any request:

```python
from typesafe_sdk import Choice, TypeSafeError

MODEL = "jev-1.14.0"          # pinned; jev-latest is an alias that moves
FLOOR = {"reuse_cache": 0.80, "stop_retry": 0.80, "research_capped": 0.70}  # placeholders
SIDE_EFFECTS = {"send", "publish", "pay", "delete"}

QUESTION = Choice(
    instructions="Given the goal, task type, last error and listed facts, what should the agent do next?",
    criteria={
        "proceed": "Nothing in the state suggests the next step will fail or repeat finished work",
        "reuse_cache": "The state lists an existing artifact that already answers this goal",
        "stop_retry": "The last error shows the same approach failing the same way again",
        "research_capped": "The sources already gathered are enough to write up the answer",
    },
)

def route(goal, task_type, last_error, repeats, *, step_kind, artifact, sources, client):
    if step_kind in SIDE_EFFECTS:
        return {"action": "ask_human", "by": "code"}
    state = (f"goal: {goal}\ntask: {task_type}\nlast error: {last_error or 'none'} x{repeats}\n"
             f"existing artifact: {artifact or 'none'}\nsources gathered: {sources}")
    try:
        r = client.system_one(state=state, questions={"action": QUESTION}, model=MODEL)
        a = r.choices["action"]
    except (TypeSafeError, KeyError) as e:
        return {"action": "proceed", "by": "fallback", "error": type(e).__name__}
    action = a.choice
    if action != "proceed" and a.confidence < FLOOR[action]:
        action = "proceed"   # an uncertain skip falls back to the normal work
    if action == "reuse_cache" and not artifact:
        action = "proceed"   # the state must contain the evidence
    return {"action": action, "by": "jev", "model": r.model, "choice": a.choice,
            "confidence": a.confidence, "probabilities": dict(a.probabilities)}
```

The caller appends each return value, the inputs and a timestamp to `decisions.jsonl`, as the article suggests. The floors are placeholders: `confidence` is a statistic of the probability spread, defined in the [confidence documentation](https://docs.typesafe.ai/confidence), not a probability that the skip is correct. Its scale also depends on the number of options. Fix the values from the shadow log in step 5.

The failure direction matters. Every uncertain, missing or failed answer becomes `proceed`, which is the work the agent would have done without a router. No answer can remove the approval for a side effect.

### 4. Install the skill and keep it in source control

Write the skill as the article describes: trigger before browser sessions, research passes, retries and extra bots; call `route()`; honour the returned action; write one line per decision into the run report. Keep the skill and router in your own repository and treat the copy on the Grok Bot computer as a deployment. A skill is an instruction the agent follows, not an interceptor. If the agent skips the call, nothing enforces it.

[Grok Bot Jev](../../projects/tools/grok-bot-jev.md) is an **independent JevList suggestion** that already packages this shape. rody does not name it. At the catalog's pinned commit, its `jev-usage-router` skill, shadow and active modes, `enabled: false` switch and `bypass jev` marker closely match the article. Its router also checks in code that a cached artifact exists before honouring `reuse_cache`. It defaults to `jev-latest` and to illustrative thresholds; pin both before relying on it. If your concern is consequential tool calls rather than wasted retries, [grok-jev-guard](../../projects/tools/grok-jev-guard.md) puts local hard stops for secrets, deletion and payments ahead of Jev and returns a narrower action envelope.

### 5. Run a shadow week and read the disagreements

In shadow mode the router is called, logged and ignored. Shadow mode is not free or offline: every call still sends the state to TypeSafe and may be billed. Only `enabled: false` stops the calls.

At the end of the week, label a sample of logged decisions by what actually happened. Did a retry the router wanted to stop later succeed? Did the agent reuse the artifact anyway, and was it current? Did the capped research miss something the final answer needed? For each action, choose the lowest confidence floor at which the skips you would have accepted outnumber the harmful ones by the margin you need, and leave actions with too few examples at `proceed`. The article's week is a reasonable minimum for a busy routine. A routine that fires a few times a day needs longer before its log says much.

### 6. Go active with a kill switch, and keep logging

Flip `mode` to `active` only for actions whose floors the log supports. Keep both kill switches, keep writing the decision log, and copy it to your own storage on each run, since Grok Bot's run history is not an archive. Compare an active week with the shadow week: skipped browser sessions, retries and research passes, against tasks that ended incomplete. A router that saves money by quietly stopping work early is a regression, not a saving.

As the article recommends, start with the one routine that keeps failing the same way, and expand only after its log is boring.

## Copyable build prompt

```text
Build a shadow-first Jev router for one Grok Bot routine.

Inputs:
- Routine to route: [NAME AND WHAT IT DOES]
- Steps that trigger the router: [BROWSER / RESEARCH / RETRY / EXTRA BOT]
- Pinned model: jev-1.14.0 (or jev-1.13.0); never the jev-latest alias
- Private repo for the code and skill: [REPO]

References to read first:
- https://x.com/0x_rody/article/2112558839589417355 (source workflow)
- https://docs.typesafe.ai/primitives/choice
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/models
- https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807
  (independent reference package; MIT; not named by the article)

Requirements:
1. Ask me for TYPESAFE_API_KEY through the masked secret flow. Never echo,
   log, commit or put it in a skill. Confirm only that it is readable.
2. route() returns ask_human from code, without any API call, for steps that
   send, publish, pay or delete.
3. One Choice question with proceed, reuse_cache, stop_retry and
   research_capped. State = goal, task type, last error with repeat count,
   existing artifact (path and age, or none) and sources gathered.
4. Per-action confidence floors in config, default to proceed below them.
   reuse_cache needs a real artifact in the state.
5. TypeSafe errors, timeouts and missing answers return proceed with the
   error recorded. Never skip work or remove approval on failure.
6. Config: {"enabled": false, "mode": "shadow"} by default; "bypass jev"
   in a message skips the router for that run.
7. Append every decision (inputs, model ID, choice, probabilities,
   confidence, what the agent actually did) to decisions.jsonl and copy it
   to my repo daily.
8. Offline tests with a mocked transport: side effect, confident skip,
   floored skip, missing artifact, HTTP 500, missing answer, kill switch.
9. Daily shadow report: call count, action split, and every disagreement
   between the logged action and what the agent did.

Do not switch to active mode. I will choose per-action floors after
reviewing at least a week of shadow logs. Report what was tested offline
versus what still needs live traffic.
```

## Validation and limits

- **Source inspected:** the complete article and all seven code blocks, read through the X API on 23 October 2026. The shared-computer limit was checked against the Grok Bot overview; the masked secret flow and the 20-run-record limit were not independently confirmed.
- **Offline example tested:** the router sketch above ran against a mocked HTTP transport with `typesafe-sdk` 0.7.5. Seven cases passed: code-side `ask_human` without a request, a confident `stop_retry`, a floored `stop_retry`, `reuse_cache` rejected without an artifact and accepted with one, and HTTP 500 and missing-answer fallbacks. Grok Bot Jev's dry run with `enabled: false` exited 0 with no Jev call.
- **Not tested:** live TypeSafe calls, installing the skill in Grok Bot, a shadow week, active mode, cost or latency. The floors in the sketch are placeholders. We make no claim that this router reduces usage; the article makes none either, and asks readers to measure it.
- **Design limits:** the router adds a network call before every triggered step. A skill can be ignored by the agent. Confidence floors tuned on one routine and one model version do not transfer to another.

## Adoption questions

### Does Jev replace the model that runs Grok Bot?

No. Grok Bot still plans, writes and uses tools. The router asks Jev one bounded question before expensive steps, such as whether to reuse an artifact or stop a failing retry, and the skill decides what to do with the answer.

### Is the TypeSafe key safe on the Grok Bot computer?

It is kept out of chat and files, but every bot on the account shares the same computer and can read the environment variable. Use a dedicated key with a spending limit, rotate it if a bot handles untrusted content, and never log it.

### Why run the router in shadow mode first?

Shadow mode records what the router would have done while the agent keeps working normally. Comparing those records with what actually happened shows whether stop_retry or research_capped would have cut off work that later succeeded, before the router is allowed to act.

### Should Jev decide when to ask a human?

Not for side effects. Sending, publishing, paying and deleting are known from the tool being called, so code should require approval for them before any Jev call. Jev can still suggest asking for help when a task is ambiguous.

### What happens if the Jev call fails?

The router should return proceed and record the error, so the agent does the work it would have done anyway. A provider failure must not silently skip work, and it must never remove an approval step.

### Does shadow mode avoid TypeSafe charges?

No. Shadow mode still sends each router state to TypeSafe and may be billed; it only ignores the answer. To stop calls entirely, set enabled to false.

## Sources, credits and corrections

- **Main source:** [rody's X article](https://x.com/0x_rody/article/2112558839589417355), 20 October 2026. The seven-step structure, five actions, four-field state, shadow week and kill switches are the author's. Moving side effects into code, adding artifact and source facts to the state, pinning the model and the failure defaults are Appit Studio's editorial additions.
- **Platform and API references:** [Grok Bot overview](https://cursor.com/docs/grok-bot), [Choice](https://docs.typesafe.ai/primitives/choice), [confidence](https://docs.typesafe.ai/confidence) and [models](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connections:** [Grok Bot Jev](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807) and [grok-jev-guard](https://github.com/0xwhrari/grok-jev-guard/tree/6083fb0584ffc61857fac755447e93d121925b48), both MIT, suggested by JevList. Neither is named or endorsed by the source author, and no affiliation with their maintainers is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The article's cover is not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
