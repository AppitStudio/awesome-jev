# Guard LangChain agent tool calls with Jev and human approval

To guard a LangChain agent's tool calls with Jev, run deterministic permission rules first. Then let LangChain's experimental `AutoModeMiddleware` ask Jev whether a proposed call looks risky, and send anything that needs consent to a separate human-approval step. Jev returns a typed probability rather than text, so your code keeps the final decision. Log each raw answer, policy decision and outcome.

**Based on:** [“Building a Harness with Jev”](https://x.com/sydneyrunkle/article/2100754364545761643) by [Sydney Runkle](https://x.com/sydneyrunkle), published 18 September 2026. This is an original Appit Studio guide, drafted with AI assistance. Sydney did not write or endorse this guide. No human reviewer is claimed.

Sydney's article explains where a fast, typed decision model can help an agent harness: a generative model handles open-ended work, while Jev judges bounded questions such as which model to use or whether a proposed tool call seems risky. The article demonstrates LangChain's `TypeSafeClassifier`, experimental model-routing middleware and experimental Auto Mode middleware. It cites TypeSafe's speed and cost claims for classification; those are provider claims, not measurements of this recipe.

## Key takeaways

- Agent loops have many small decision points. Ask Jev narrow questions about a shared state and let application code act on typed answers.
- The article's model router chooses a model for the **whole run** from the latest user message. Its Auto Mode checks selected tool calls **before execution** and can block them.
- A classifier is not an authorization system. A blocked call still needs a recovery path; an allowed call still needs normal permissions, sandboxing and auditability.
- Independent questions can share one request, but later questions that depend on new tool results need fresh state. Measure cost and latency in your workload instead of adopting the article's benchmark figures.

## Build a small tool-call gate

The primary path uses [LangChain's TypeSafe integration](https://docs.langchain.com/oss/python/integrations/providers/typesafe) and its experimental `AutoModeMiddleware`. Start with a harmless, read-only tool and a synthetic request. Keep write, deletion, credential and network tools outside the automatic set until a person has defined permission rules. The middleware is a screening layer, not a replacement for LangChain's [human-in-the-loop middleware](https://docs.langchain.com/oss/python/langchain/human-in-the-loop).

1. Create an isolated Python 3.10+ project. Follow the [current integration setup](https://docs.langchain.com/oss/python/integrations/providers/typesafe#setup) for `langchain-typesafe[experimental]`, `langchain-openai` and compatible LangChain packages. A live run needs `TYPESAFE_API_KEY` and the chosen chat provider's key; both providers may charge for requests.
2. Define the exact tool names and arguments that may reach the classifier. Strip secrets and unnecessary conversation history before sending state to TypeSafe. Add a deterministic allow/deny policy ahead of model screening. A deny rule should stop execution even if the classifier says “safe.”
3. Configure `AutoModeMiddleware(tools=[...])` with the specific tool names or tool objects (the integration docs accept either). Its risk classification can return an error `ToolMessage` instead of calling a tool. Add an independent approval checkpoint for any action that requires consent; the middleware does **not** ask for approval itself.
4. Record the proposed tool, sanitized state, raw decision/probability, policy decision and final execution outcome. If the classifier times out, fails or gives an unusable answer, route the call to review or refuse it. Never silently treat missing evidence as permission.
5. Test a read-only allowed call, a clearly disallowed call, an uncertain call and a service failure with fakes. Only then run a bounded live trace, inspect decisions and false allows/blocks, and tune thresholds on representative cases before enforcement.

**Expected result:** an agent can use an explicitly permitted read-only tool; a dangerous or unapproved action is held or refused before execution, with a visible reason. This is a design and acceptance target, not a live result claimed by this guide.

For a different deployment shape, [Agent Chaperone](../../projects/tools/agent-chaperone.md) offers MCP proxy and client hook screening with shadow mode. It is **independently suggested by JevList**, not mentioned by Sydney. Its Apache-2.0 source was catalog-reviewed at commit `4220149`; live tool content may go to TypeSafe and incur charges. Shadow mode logs decisions without blocking. If your next problem is choosing among coding-agent subscriptions, [Agent Router](../../projects/tools/agent-router.md) applies deterministic eligibility before Jev ranking, but it is a **separate MIT pre-release CLI** requiring TypeSafe, agent logins and Herdr for launches. It does not replace LangChain's per-run router. Use one path that fits your stack.

Sydney's closing examples include Jarrod Watts's trading agent. [Jev Trader](../../projects/tools/jev-trader.md) is that project; the article links to it through Jarrod's post. There, Jev chooses buy or sell and ordinary code applies position and margin rules before placing orders. It is a **source-mentioned teaching example** of keeping a limit between a typed judgment and an irreversible action, not a harness to copy for trading. Its MIT source defaults to a local mock heuristic; `MODEL=jev` uses paid TypeSafe calls, and live orders need a wallet and funds. Keep `DRY_RUN=true` and never test with money you cannot lose.

The repository's [Support Router example](../../../projects/support-router/README.md) is a teaching resource for the same separation of model judgments and code policy. It is not a community project listing or a tool-call firewall. Its offline mode is useful before a billed call.

## Copyable build prompt

Copy the following into your coding agent and fill the bracketed inputs. Review its proposed permissions before running a live agent.

```text
Build a small LangChain agent harness for [YOUR READ-ONLY TASK] in [YOUR PYTHON PROJECT]. Use the current official LangChain TypeSafe integration: https://docs.langchain.com/oss/python/integrations/providers/typesafe and the TypeSafe quick start: https://docs.typesafe.ai/introduction/quickstart. Inspect installed package versions before using APIs.

Define exactly two tools: [READ-ONLY TOOL NAME AND INPUTS] and [PROPOSED HIGH-RISK TOOL NAME AND INPUTS]. Use synthetic inputs only in the first run. Put exact allow/deny rules and user approval requirements in ordinary code. Use Jev only for the bounded semantic judgment about a proposed tool call; do not ask Jev to generate prose or grant permission. Configure the experimental AutoModeMiddleware only for the named tools, then pair it with a separate human approval mechanism for actions that need it. Do not make live provider calls by default.

Deliver the runnable project, pinned dependency list, explicit data-flow/secret-redaction notes, and tests with fake classifier responses for allowed, blocked, uncertain and unavailable-service cases. Preserve raw classifier answers separately from final policy decisions. On missing or invalid answers, refuse or request review. Show exactly which tool calls ran and which did not. Provide an opt-in, bounded live command only after the offline tests pass; explain provider costs and that synthetic tests establish policy behavior, not model accuracy or prompt-injection resistance. If you compare a separate MCP/hook layer, use https://github.com/agent-chaperone/agent-chaperone as an alternative, not an extra required dependency.
```

## Validation and limits

On 25 September 2026 we read the full article and its visible examples, the current [LangChain integration documentation](https://docs.langchain.com/oss/python/integrations/providers/typesafe) and [TypeSafe quick start](https://docs.typesafe.ai/introduction/quickstart), plus the two pinned catalog project pages. We ran the repository's Support Router with six **authored synthetic tickets**: three automatic suggestions, three human-review records and no errors. That exercise validates the example's deterministic review flow only. We did **not** execute this LangChain harness, call TypeSafe, measure latency or cost, or evaluate safety on a real trace dataset. The article showed an edited indicator; we could not verify its edit history. We reread it on the same day for this refresh and found no substantive change. The guide image is an original Appit Studio diagram (CC0), not an image from the article. Recheck experimental middleware APIs before implementation.

## Adoption questions

### What is Jev, and how is it different from an LLM?

Jev is TypeSafe AI's System One model. It answers typed questions about a state with probabilities instead of generating text. Use an LLM for open-ended work and Jev for fast, bounded judgments that your code acts on.

### Does LangChain's AutoModeMiddleware ask a person to approve risky tool calls?

No. The documented middleware refuses risky calls; use a separate approval flow when a person must decide. Keep explicit permissions in code.

### Can I rely on a Jev probability as proof that a tool call is safe?

No. Typed output constrains shape, not correctness. Evaluate false allows and false blocks on representative traces, and maintain sandbox and permission boundaries.

### Must I install all linked projects?

No. The primary recipe uses LangChain's TypeSafe integration. Agent Chaperone is an alternative screening layer; Agent Router addresses model choice; Jev Trader is a source-mentioned example of limits around actions; Support Router demonstrates an offline decision-policy pattern.

## Sources, credits and corrections

Original article: [Sydney Runkle, “Building a Harness with Jev”](https://x.com/sydneyrunkle/article/2100754364545761643). Sydney credits @huntlovell, @hwchase, @ccurme, @veryboldbagel and Nathan Drenzer for review and contributions to that article; those credits belong to the source, not this guide. LangChain also published the article on [its blog](https://www.langchain.com/blog/building-a-harness-with-jev) on 17 September 2026, credited to Sydney Runkle and Hunter Lovell. Technical references: [LangChain TypeSafe integration](https://docs.langchain.com/oss/python/integrations/providers/typesafe), [TypeSafe quick start](https://docs.typesafe.ai/introduction/quickstart), and the linked project pages. The guide was written by Appit Studio with AI assistance; no paid placement, affiliate link or human review is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) for a stale API, mismatched project or attribution error.
