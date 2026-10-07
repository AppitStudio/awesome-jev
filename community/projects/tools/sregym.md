# SREGym

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Platform and benchmark for AI agents that resolve production incidents in live Kubernetes environments (90 SRE problems, SREGym-Lite starter set), with optional Jev decision support that reviews an agent's diagnostic tests and submissions using evidence sent to TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SREGym/SREGym) |
| Product homepage | [sregym.com](https://sregym.com) |
| Maintainer | [SREGym](https://github.com/SREGym). Independently curated. |
| Format | Python platform (uv) with Kubernetes/kind environments, agents and an optional `clients/jev` decision-support client |
| Requirements | Python 3.12+, Docker, Helm 4+, a self-managed Kubernetes cluster (or kind for a subset); an LLM provider key for the agent; `TYPESAFE_API_KEY` for the optional Jev support. |
| License | [MIT](https://github.com/SREGym/SREGym/blob/28db97289323d888f6c75b0f273c3d8406cd129c/LICENSE.txt). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Benchmark incident-response agents on failures modelled on public postmortems (Cloudflare WAF regex, Kafka poison pill, conntrack exhaustion…).
- Compare agent runs with and without Jev reviewing diagnostic tests and submissions (`--jev-model jev-latest`).
- Mismatch: Jev is optional and off by default; most of the platform is about environments and agents, not Jev.

## How it works

Agents (e.g. the included Stratus agent, or Codex) diagnose and mitigate problems injected into a live cluster. With `--jev-model`, the client in [`clients/jev/`](https://github.com/SREGym/SREGym/tree/28db97289323d888f6c75b0f273c3d8406cd129c/clients/jev) — [`review.py`](https://github.com/SREGym/SREGym/blob/28db97289323d888f6c75b0f273c3d8406cd129c/clients/jev/review.py), [`submission.py`](https://github.com/SREGym/SREGym/blob/28db97289323d888f6c75b0f273c3d8406cd129c/clients/jev/submission.py) — sends evidence to Jev to review diagnostic tests and submissions. The SREGym blog post *Jev-Driven SRE Diagnosis: What Worked and What Failed* (via Hacker News) discusses the results.

## Get started

With a cluster ready (see README *Setup your cluster*), run Codex with Jev support:

```sh
git clone https://github.com/SREGym/SREGym.git && cd SREGym
export TYPESAFE_API_KEY=...
uv run main.py --agent codex --model gpt-5.6-luna --reasoning-effort medium \
  --problem <problem-id> --jev-model jev-latest --force-build
```

Agent model usage, cluster hosting and Jev reviews are each billed by their providers.

## Examples and demos

- SREGym blog: [Jev-Driven SRE Diagnosis: What Worked and What Failed](https://www.sregym.com/blog/jev-driven-sre-diagnosis).
- Starter problem set: [`docs/SREGym-Lite.md`](https://github.com/SREGym/SREGym/blob/28db97289323d888f6c75b0f273c3d8406cd129c/docs/SREGym-Lite.md).

## Limits and data handling

Diagnostic evidence is sent to TypeSafe when Jev support is enabled. Results discussed in the blog are the SREGym team's. Not run on the review host (requires a Kubernetes cluster).

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 28db97289323](https://github.com/SREGym/SREGym/tree/28db97289323d888f6c75b0f273c3d8406cd129c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
