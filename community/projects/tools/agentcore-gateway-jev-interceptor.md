# AgentCore Gateway Jev interceptor (sample Lambda that has Jev screen conversations before Amazon Bedrock models see them)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Sample REQUEST interceptor for Amazon Bedrock AgentCore Gateway: a Lambda pulls the conversation out of each request, asks Jev one `noul` question per policy rule, and returns 403 without calling the answer model when any probability crosses its threshold; setup and teardown scripts create and remove all AWS resources.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yuu551/agentcore-gateway-jev-interceptor) |
| Maintainer | [yuu551](https://github.com/yuu551). Independently curated. |
| Format | AWS Lambda sample with setup/teardown scripts (Python 3.13, MIT; docs in Japanese) |
| Requirements | Python 3.13+, uv, AWS credentials allowed to create Secrets Manager, Lambda, IAM and AgentCore resources, and a TypeSafe key. |
| License | [MIT](https://github.com/yuu551/agentcore-gateway-jev-interceptor/blob/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lambda_function.py`](https://github.com/yuu551/agentcore-gateway-jev-interceptor/blob/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175/lambda_function.py) at the pinned commit. |

## When to use

- Add a semantic policy filter in front of Bedrock models behind AgentCore Gateway.
- Mismatch: production use as-is; thresholds were only tried on the author's samples.

## How it works

`lambda_function.py` posts to `https://api.typesafe.ai/v1/systemone` with `JEV_MODEL` (default `jev-1.13.0`), reading the key from Secrets Manager; rules and thresholds live in `semantic_filter_rules.json`. The author marks it as a verification sample, not for production. Integration evidence: [`lambda_function.py`](https://github.com/yuu551/agentcore-gateway-jev-interceptor/blob/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175/lambda_function.py).

## Get started

Create the AWS resources, send the four sample inputs through the gateway, then tear everything down.

```sh
uv run python setup.py
uv run python invoke.py
uv run python teardown.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/yuu551/agentcore-gateway-jev-interceptor/blob/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175/README.md](https://github.com/yuu551/agentcore-gateway-jev-interceptor/blob/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175/README.md)

## Limits and data handling

Conversation text passing through the gateway goes to TypeSafe on your key; AWS charges apply.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit a18a97ba1a70](https://github.com/yuu551/agentcore-gateway-jev-interceptor/tree/a18a97ba1a70c6bc346ebf9d1c4689c94c2c0175). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
