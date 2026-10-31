# HarnessRouter Community Edition (self-hosted unified API for 30 agent harnesses, including a System One harness for Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted, Apache-2.0 gateway that runs Codex, Claude Code, Hermes, Pi, DeepSeek Harness and about 25 other agent harnesses behind one Unified Harness Protocol API, with sessions, streaming, files, cancellation and explicit end states. One of the harness bases is System One, which drives the open System One Harness with Jev as the decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HarnessRouter/harnessrouter) |
| Maintainer | [HarnessRouter](https://github.com/HarnessRouter). Independently curated. |
| Format | Docker image (Console, Gateway and Runner) + HTTP API |
| Requirements | Docker and about 4 GB of disk; your own provider keys (a TypeSafe or OpenRouter key for the System One harness). |
| License | [Apache-2.0](https://github.com/HarnessRouter/harnessrouter/blob/e94398d9c91a21ae7e01c630e2eeffa4defe1cfb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/HARNESSROUTER/status/2116560833417490864)). |
| Jev evidence | [`runner/systemone_driver.py`](https://github.com/HarnessRouter/harnessrouter/blob/e94398d9c91a21ae7e01c630e2eeffa4defe1cfb/runner/systemone_driver.py) at the pinned commit. |

## When to use

- Pick a harness and a model per task behind one API, including decision-only runs on Jev.
- Mismatch: Jev is one of 30 harness bases; most harnesses use generative models.

## How it works

`runner/systemone_driver.py` runs the open [System One Harness](https://github.com/HarnessRouter/SystemOneHarness) inside the runner, sending typed questions to TypeSafe `/v1/systemone` (or a `/alpha/decisions` host) so Jev picks actions while code gates and executes them. Integration evidence: [`runner/systemone_driver.py`](https://github.com/HarnessRouter/harnessrouter/blob/e94398d9c91a21ae7e01c630e2eeffa4defe1cfb/runner/systemone_driver.py).

## Get started

From the upstream README (not run on the review host):

```sh
docker run -d --name harnessrouter -p 127.0.0.1:3000:3000 -v harnessrouter:/data harnessrouter/harnessrouter
# open http://127.0.0.1:3000 and connect a provider key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [harnessrouter.ai](https://harnessrouter.ai)
- Announcement on X: [x.com/HARNESSROUTER/status/2116560833417490864](https://x.com/HARNESSROUTER/status/2116560833417490864)

## Limits and data handling

Prompts and files go to whichever providers you configure. A managed Cloud edition also exists; this listing covers the self-hosted Community Edition only. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit e94398d9c91a](https://github.com/HarnessRouter/harnessrouter/tree/e94398d9c91a21ae7e01c630e2eeffa4defe1cfb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
