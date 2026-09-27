# Use Jev in Claude Code hooks and loops

Jev can answer bounded questions at three points in a Claude Code workflow: whether new work merits a run, whether a proposed tool call needs review, and whether the evidence supports stopping. Start with a **review-only PreToolUse gate** on synthetic commands. Keep permissions, exact checks, budgets and final actions in code and with people; a model score does not make a hook a security boundary.

**Based on:** [“Loop Engineering Meets Jev Engineering: How to Cut Your Claude Bill From $765 to $3 a Month”](https://x.com/polydao/article/2103689373774483815) by [Mr. Buzzoni](https://x.com/polydao), published 26 September 2026. This independent Appit Studio guide was drafted with AI assistance. Buzzoni did not write or endorse it; no human reviewer is claimed.

Buzzoni presents three sketches: a `PreToolUse` command gate, a `Stop` completion check and a GitHub-issue trigger. The cost table models many small decisions moving from a text model to Jev. The architecture is useful, but the article does not publish an audited overnight run of these three hooks, a representative error study or actual bills for the proposed setup.

## Key takeaways

- **Match the question to the event.** A Choice can label a proposed command or issue. A Noul can express evidence for a narrow completion claim. Claude still writes and repairs code; ordinary code controls permission, limits, state and side effects.
- **Let exact checks lead.** Run tests, path and permission rules, repository checks and cost limits without a model. A semantic answer can route the remaining ambiguity to a person. A command's text alone cannot prove what a shell will do.
- **Treat hooks as fallible.** [Claude Code's hook reference](https://code.claude.com/docs/en/hooks) says a timed-out `PreToolUse` *command* hook contributes no decision and the call continues through normal permissions. Keep those permissions in place; decide explicitly how missing keys, timeouts and invalid answers are handled.
- **Use separate evidence for stopping.** A green test exit code does not establish that every acceptance criterion is met. A Jev answer only judges the state supplied to it, and [Claude Code caps consecutive Stop-hook continuations](https://code.claude.com/docs/en/hooks). Show unresolved work to a person when the cap or an error ends the check.
- **Measure the complete bill.** The article's `$765` and `$3.02` columns are arithmetic over assumed decisions. They do not include the Claude turns that write code, retries, cache effects, hook upkeep or incorrect routing.

## Put each decision at the right boundary

| Boundary | Jev's bounded question | Code and human responsibility |
| --- | --- | --- |
| Before a run | Does a newly fetched issue have a reproducible code-fix request? | Verify repository, freshness, deduplication, allowed scope and daily run budget; review uncertain issues. |
| Before a tool call | Which risk class best describes the proposed call? | Enforce explicit deny and approval rules, keep Claude Code permissions, and log the final decision. |
| Before a turn ends | Does the supplied evidence cover each stated condition? | Run exact checks, preserve the goal and artifacts, cap continuation, and surface incomplete work. |

This is a sequence, not one interchangeable question. Issue triage sees issue text; a tool gate sees the proposed tool and its arguments; a Stop check needs the task criteria and actual check output. Do not pass secrets or full transcripts merely because a hook can read them. The [TypeSafe model page](https://docs.typesafe.ai/models) says `jev-1.13.0` receives text or JSON state and charges for input tokens, including questions. The [question guide](https://docs.typesafe.ai/primitives) says instructions carry meaning; IDs are lookup keys. Batch *independent* questions over shared state when it reduces repeated input, but do not ask a completion question before the tests it depends on have run.

## Start with a review-only tool gate

Claude Code sends JSON to a `PreToolUse` command hook on stdin. Its documented output can set `hookSpecificOutput.permissionDecision` to `allow`, `deny` or `ask`. Buzzoni's sample matches `Bash`, checks a few literal blocked strings, and sends the command and working directory to Jev as a five-option Choice. A high-confidence `read_only` or `local_edit` is allowed; `destructive` is denied; `external`, `other` and lower-confidence answers ask. We reproduced those branches with synthetic SDK response objects, **without running a shell command or calling Jev**.

For a pilot, keep every nontrivial result at `ask` while logging the raw Choice, distribution, model ID, proposed tool and eventual human decision. Test commands with quoting, pipelines, expansion, aliases, nested scripts, misleading comments and indirect writes. A literal `rm -rf /` list can miss equivalent destructive actions. Even a confident `read_only` label does not authorize a command outside the allowed path or erase built-in permission policy. Handle `TypeSafeError`, missing answers and a deadline by returning no automatic approval and recording the failure; [the SDK exception reference](https://docs.typesafe.ai/sdk/python/api/exceptions) distinguishes HTTP, connection, timeout and response-validation failures. A hook-level timeout itself cannot enforce this fallback, so keep Claude Code's normal permissions and separate deterministic controls.

[The Jev-enator](../../projects/tools/the-jev-enator.md) is an **independent JevList suggestion** for seeing a real `PreToolUse` hook and a `Stop` check together. Its MIT Python 3.10+ source includes offline cassette tests; the catalog inspected a pinned revision and ran those tests. Its finish check is **log-only by default**, so installing it is not equivalent to enforcing Buzzoni's Stop sketch. A live installation needs Claude Code and a TypeSafe key, sends selected tool arguments, output and transcript evidence to TypeSafe, and incurs provider charges. Review its install script and run its fixtures before letting it see a real workspace. Buzzoni did not mention the project.

## Make the stop condition observable

Run the exact, finite checks first and capture exit codes and bounded output. Then ask whether the *shown evidence* covers the stated goal; a Noul is a probability of yes, not a proof that the repository is correct. Buzzoni's sample uses `GOAL.md`, `.claude/checks.sh` and a counter. It blocks Stop on failed checks or a low Noul, writes `REVIEW.md` for a middle band, and stops after five pushes. That cap prevents endless continuation, but it can also end with known failing checks. A review record should retain those failures and the remaining conditions; it must not be presented as a completed task.

Give the hook a stable, task-scoped goal, a timeout for its check script and provider call, and an outcome for missing files or malformed state. Check `stop_hook_active` or a durable per-session attempt record to avoid repeated blocks; the [Claude reference](https://code.claude.com/docs/en/hooks) documents both this field and its own continuation cap. Compare hook judgments with human reviews on representative completed and incomplete tasks before enforcing a threshold. A test suite's success can be a prerequisite, while acceptance and documentation checks remain separate evidence.

## Wake the coding agent only for approved work

Buzzoni's third sketch lists up to 30 GitHub issues, classifies each, edits a label and launches `claude -p` for `code_fix`. Treat that as pseudocode for a scheduler, not a ready unattended runner. Its `gh` helper returns stdout even when the command fails, and the example has no durable deduplication, per-run spend ceiling, claim protocol or approval boundary before the coding process starts. The proposed `acceptEdits` mode is a meaningful permission choice; an issue body is untrusted task data.

[ghtriage](../../projects/tools/ghtriage.md) is a separate **JevList suggestion** for the classification stage. Its MIT Python 3.10+ package asks typed issue questions and applies code-owned write guards. The reviewed revision defaults label writes off; `--apply` and a GitHub token enable them. A live classify sends issue title and body to TypeSafe and incurs its charges. The catalog's checks were offline. ghtriage does **not** launch Claude Code or create PRs, so the owner still needs a reviewed scheduling and execution policy.

Start with a read-only queue: fetch a bounded set of issues, classify, record `code_fix` / `question` / `feature` / `other` plus raw answers, and show the proposed action to a maintainer. Verify repository identity, issue freshness, permission scope and duplicates in code. Only after reviewing real cases should the maintainer opt into labels. Keep an agent run count and spend cap separate from the Jev request cap. Missing, low-confidence or failed classifications stay for review.

## Rebuild the cost comparison from assumptions

The article models **200 turns × three decisions = 600 decisions per night**, each with about 4,000 input and 50 output tokens, over 30 nights. At its stated Fable list rates, `600 × (4,000 × $10 + 50 × $50) / 1,000,000 = $25.50` per night and `$765` per month. At the [TypeSafe price listed on 27 September 2026](https://docs.typesafe.ai/models), `600 × 4,000 × $0.042 / 1,000,000 = $0.1008` per night, or about `$3.02` over 30 nights. Those reproduce the article's *modeled decision-only inputs*. The article suggests about `$1.08` when three independent questions share one 4,000-token state call per turn; actual question tokens and request sizes need measurement.

The comparison only saves money if those Claude decision calls were separate, avoidable billed turns. A `PreToolUse` hook adds a Jev call to a tool that Claude has already proposed; it does not automatically remove the Claude model call that selected the tool. A Stop hook can add more work when it continues the turn. Subscription limits, prompt-cache reads, retries, output and error correction also change the ledger. Log actual request counts, input tokens, latency, Claude usage, cache charges, reviews and incorrect routes before reporting savings. The article's cited latency and calibration figures are TypeSafe or builder reports, not measurements of these three sketches.

## Copyable build prompt

```text
Build an offline-first Claude Code PreToolUse gate prototype in [PYTHON VERSION >= 3.10] for [ONE REPOSITORY]. Inputs: [ALLOWED ROOT], [EXACT DENY RULES], [TOOLS TO MATCH], [REVIEW POLICY], [MAX EVENT BYTES], [HOOK DEADLINE], [LOCAL LOG PATH], and [REPRESENTATIVE SYNTHETIC TOOL EVENTS]. I will provide the acceptance criteria and permission owner. Do not install the hook into a live Claude Code profile or call TypeSafe by default.

Read the current Claude hook contract at https://code.claude.com/docs/en/hooks and the TypeSafe Python SDK, question, model and error docs at https://docs.typesafe.ai/sdk/python/usage , https://docs.typesafe.ai/primitives , https://docs.typesafe.ai/models and https://docs.typesafe.ai/sdk/python/api/exceptions . Pin the installed SDK and a versioned Jev model; record the response model ID. Check the installed answer fields before coding. The Jev-enator (https://github.com/jakenbear/the-jev-enator) is an independent JevList teaching example, not source-author code; inspect its pinned hook and offline tests before adapting anything.

Deliver a small stdin-to-JSON hook, a pure policy function, synthetic fixtures and an offline replay report. Parse and size-limit the event. Apply exact repository and command restrictions first. Ask one complete Choice question about the remaining proposed tool call, with explicit read_only, local_edit, destructive, external and other criteria. Store the raw choice, probabilities, confidence, model version, rule result and final permission decision. In the first phase, return ask for every nontrivial call while collecting human labels; do not auto-allow from a model score. Keep Claude Code's ordinary permissions and explicit deny rules in force.

Test safe reads, in-repo edits, out-of-repo paths, pipes, shell expansion, nested commands, external sends, other, low confidence, missing key, malformed JSON, absent answer, HTTP failure, connection failure, provider timeout and the hook's own timeout. Confirm the documented PreToolUse output shape. Record that a timed-out command hook makes no decision and normal permissions continue. Do not claim the prototype enforces a hard security boundary. Make live Jev calls a separate opt-in with a maximum request count, spend cap, approved data path and key from the environment. Report what ran offline, what was reviewed by people and what remains unmeasured.
```

## Validation and limits

We read the complete X article in logged-in Chrome, including all three code blocks and its cost table; followed its embedded [Diogo Almeida launch post](https://x.com/CompleteSkeptic/status/2099925682726002904) and [1kpapers](https://www.1kpapers.com/); and checked current Claude and TypeSafe documentation. The launch post's speed and price multiples are provider claims. The 1kpapers site's published methodology describes its paper corpus and summary-model cost comparison, but does not establish the article's Jev classification-cost and latency figures. Exact-title searches found a third-party mirror, not a verified author republication. The source image has no stated reuse permission, so this guide uses an original CC0 diagram.

We inspected the two catalog pages and their pinned upstream files. With `typesafe-sdk` 0.7.1 in a scratch environment, synthetic SDK response objects exercised the article's Choice allow/deny/ask branches and Noul stop bands. We did not call TypeSafe, install the hooks in Claude Code, run an unattended scheduler, edit GitHub labels, test live latency or inspect a provider bill. The prompt is a specification for an offline pilot, not proof that a deployed hook works or saves money.

## Adoption questions

### Can a Jev hook replace Claude Code permissions?

No. A PreToolUse command hook can add an allow, deny or ask judgment, but a hook timeout does not block the tool call. Keep Claude Code permissions, deterministic deny rules and human approval for consequential actions.

### Does Jev cut a Claude Code bill from $765 to $3?

Those are the article's modeled monthly prices for 600 assumed small decisions per night, not measured bills. They exclude Claude's coding turns, hook maintenance, retries and other work; measure real token usage and cache behavior before claiming savings.

### Should a Stop hook trust a high Jev score?

Only after exact checks pass and the evidence covers the goal. A high Noul value is not proof of completion; keep a continuation limit, expose unresolved work for review and evaluate mistakes on representative tasks.

### How should a Jev issue trigger handle uncertain or failed answers?

Leave the issue in a human review queue. A missing, low-confidence, malformed or timed-out answer should not launch an unattended coding run or change labels silently. Limit input size, requests and agent runs separately.

## Sources, credits and corrections

The principal source is [Buzzoni's complete X article](https://x.com/polydao/article/2103689373774483815), published 26 September 2026. The [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) defines hook inputs, decisions and timeout behavior; TypeSafe's [model](https://docs.typesafe.ai/models), [questions](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [Python SDK](https://docs.typesafe.ai/sdk/python/usage) and [exceptions](https://docs.typesafe.ai/sdk/python/api/exceptions) pages define the API limits checked on 27 September 2026. The Jev-enator and ghtriage are Appit Studio editorial suggestions, with no source-author endorsement or paid placement. Appit Studio drafted this guide with AI assistance and no claimed human review. [Report a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) when a hook contract, price or project behavior changes.
