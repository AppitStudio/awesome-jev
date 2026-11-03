# agent-ops-sample (AWS Q&A agent sample whose Langfuse traces are scored by Jev on groundedness, tool choice and goal; Japanese)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Sample code for a Japanese technical-book chapter on operating and evaluating AI agents: a policy Q&A agent (Strands Agents on Amazon Bedrock with Knowledge Bases and AgentCore Runtime) with traces in Langfuse, and an evaluation job that pulls recent traces and asks Jev four typed questions per exchange (is every claim supported, were the right tools called, were the arguments right, was the goal achieved). The company and policies are fictional and the README is in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/umitsu-tech/agent-ops-sample) |
| Maintainer | [umitsu-tech](https://github.com/umitsu-tech). Independently curated. |
| Format | Python and CDK sample (uv, TypeScript infrastructure) |
| Requirements | Python 3.12+ and uv, Node 22.12+, an AWS account (us-east-1) with Bedrock model access, a Langfuse account and a TypeSafe key. |
| License | [MIT](https://github.com/umitsu-tech/agent-ops-sample/blob/16349203715eed39c57f4b3e58998c7823b3c37d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`evals/jev_judge.py`](https://github.com/umitsu-tech/agent-ops-sample/blob/16349203715eed39c57f4b3e58998c7823b3c37d/evals/jev_judge.py) at the pinned commit. |

## When to use

- See a concrete trace-scoring job that uses Jev as a cheap judge of agent behaviour.
- Mismatch: a book sample on AWS, with fictional data, not a drop-in evaluation service.

## How it works

`evals/jev_judge.py` posts each trace's question, tool calls and answer to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with the four judging questions batched into one request, since extra questions barely change latency. Integration evidence: [`evals/jev_judge.py`](https://github.com/umitsu-tech/agent-ops-sample/blob/16349203715eed39c57f4b3e58998c7823b3c37d/evals/jev_judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/umitsu-tech/agent-ops-sample.git
cd agent-ops-sample
cp .env.example .env   # keys
uv sync
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese) with the flow and evaluation steps: [github.com/umitsu-tech/agent-ops-sample#readme](https://github.com/umitsu-tech/agent-ops-sample#readme)

## Limits and data handling

Trace text goes to TypeSafe on your key, and deploying the sample incurs AWS charges; the sample's scores are illustrations on fictional policies, not benchmarks. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 16349203715e](https://github.com/umitsu-tech/agent-ops-sample/tree/16349203715eed39c57f4b3e58998c7823b3c37d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
