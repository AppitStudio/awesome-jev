# JevAgentHarness (coding-agent proxy where Jev sends routine steps to a cheap model and hard steps to a strong one)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Alpha local OpenAI-compatible proxy for coding agents (Codex, pi, DeepSeek Harness, mini-swe-agent, Terminus-2): before each model call Jev answers whether the next step is routine or hard, routine steps go to a fast model and hard ones to the strong model; ships with a paper, Terminal-Bench 2.0 reproduction scripts and per-step cost logs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevAgentHarness/JevAgentHarness) |
| Maintainer | [JevAgentHarness](https://github.com/JevAgentHarness). Independently curated. |
| Format | Python package and local proxy (`jah`) |
| Requirements | Python 3.10+; keys for your strong and fast LLM tiers (Gemini by default, any OpenAI-compatible API); an OpenRouter or TypeSafe key for Jev, or the key-free rules decider. |
| License | [MIT](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Sumanth_077/status/2114309785407652201)). |
| Jev evidence | [`src/jevagentharness/decision.py`](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/decision.py) at the pinned commit. |

## When to use

- Cut the LLM bill of a coding agent by routing routine steps to a cheaper model without changing the agent.
- Reproduce or extend the paper's routing results on your own tasks with `jah report`.
- Mismatch: alpha software; savings are the authors' Terminal-Bench measurements, not verified here.

## How it works

`decision.py` posts the agent's current state and one Choice question (`routine` or `hard`) to `{base}/v1/systemone`, with presets for OpenRouter (`typesafe/jev-1.13`) and TypeSafe (`jev-latest`); the first step, the finish decision and any decision error always go to the strong model. Integration evidence: [`src/jevagentharness/decision.py`](https://github.com/JevAgentHarness/JevAgentHarness/blob/f2932199e1ef1d9f089b51d39430c87be0f560b5/src/jevagentharness/decision.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JevAgentHarness/JevAgentHarness.git && cd JevAgentHarness
pip install -e .
export GEMINI_API_KEY=...       # LLM tiers
export OPENROUTER_API_KEY=...   # Jev decision model
jah serve                       # then point your harness at http://127.0.0.1:8787/v1, model jah-auto
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project page: [jevagentharness.github.io/](https://jevagentharness.github.io/)
- Paper: [arxiv.org/abs/2610.21412](https://arxiv.org/abs/2610.21412)
- Reproduce: [github.com/JevAgentHarness/JevAgentHarness/blob/main/bench/README.md](https://github.com/JevAgentHarness/JevAgentHarness/blob/main/bench/README.md)

## Limits and data handling

Each step's agent state (about 2,000 tokens on Terminal-Bench) goes to the decision provider, and the full prompts go to your LLM tiers. Every step is logged locally with tier, tokens, cost and latency.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit f2932199e1ef](https://github.com/JevAgentHarness/JevAgentHarness/tree/f2932199e1ef1d9f089b51d39430c87be0f560b5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
