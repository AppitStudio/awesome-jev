# dsh-agent-kit (DeepSeek Harness services for always-on agent workers, with a Jev check service)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness plugin kit for always-on agent workers: WebSocket intake, DingTalk, Feishu and WeCom messaging, Claude Code and Codex task delegation, and a `ctx.jev` service that checks agent results with typed Jev Choice, Noul and Score answers and escalates to a person when a check fails; Chinese documentation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/byx-darwin/dsh-agent-kit) |
| Maintainer | [byx-darwin](https://github.com/byx-darwin). Independently curated. |
| Format | TypeScript DSH plugin packages (npm `@baoyx/dsh-agent-kit`) |
| Requirements | DeepSeek Harness (`@deepseek-ai/dsh`); a TypeSafe API key for the Jev service, or a self-hosted Laya endpoint. |
| License | [MIT](https://github.com/byx-darwin/dsh-agent-kit/blob/e2afbd157815624b77b867d2db8498162e15c1d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/service.ts`](https://github.com/byx-darwin/dsh-agent-kit/blob/e2afbd157815624b77b867d2db8498162e15c1d8/src/jev/service.ts) at the pinned commit. |

## When to use

- Build a resident worker that receives business events and has agents act on them with cheap verification.
- Reuse ready messaging and delegation services instead of writing them per project.
- Mismatch: every service is disabled by default; Jev is one of seven services.

## How it works

`src/jev/service.ts` calls TypeSafe-hosted Jev through `@typesafe-ai/sdk` (or a local Laya server speaking `POST /v1/systemone`) and returns typed answers with probabilities that the business package uses to pass, escalate or hand work to a person. Integration evidence: [`src/jev/service.ts`](https://github.com/byx-darwin/dsh-agent-kit/blob/e2afbd157815624b77b867d2db8498162e15c1d8/src/jev/service.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm i -g @deepseek-ai/dsh
dsh plugin --profile my-agent add @baoyx/dsh-agent-kit
# enable ctx.jev in the profile's cordis.patch.yml and set TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site: [byx-darwin.github.io/dsh-agent-kit/](https://byx-darwin.github.io/dsh-agent-kit/)
- README: [github.com/byx-darwin/dsh-agent-kit#readme](https://github.com/byx-darwin/dsh-agent-kit#readme)

## Limits and data handling

Agent results you ask the service to check go to TypeSafe (or your Laya host). Messaging services send to the channels you configure.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit e2afbd157815](https://github.com/byx-darwin/dsh-agent-kit/tree/e2afbd157815624b77b867d2db8498162e15c1d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
