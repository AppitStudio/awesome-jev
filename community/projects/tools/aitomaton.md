# aitomaton (error-to-fix automation with a Jev decision tier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Service that listens to Sentry, urgentry and Alertmanager, analyses each error alone, in bursts and as long-term patterns across a Docker Swarm, and decides what to do through a chain of rules, the open Laya model, Jev and an LLM; code defects can go to a coding agent that opens a pull request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sirmmo/aitomaton) |
| Maintainer | [sirmmo](https://github.com/sirmmo). Independently curated. |
| Format | Python service (Docker Swarm stack) |
| Requirements | Docker Swarm; Sentry or urgentry (optionally Prometheus and Alertmanager); an OpenRouter key for the Jev tier; optional LLM key. |
| License | [MIT](https://github.com/sirmmo/aitomaton/blob/e05e38c2c61079ef0c3ffa37d9ce3ecd0b37c0f8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`aitomaton/deciders.py`](https://github.com/sirmmo/aitomaton/blob/e05e38c2c61079ef0c3ffa37d9ce3ecd0b37c0f8/aitomaton/deciders.py) at the pinned commit. |

## When to use

- Triage production errors automatically and route real code defects to a fix.
- Keep cheap tiers first and ask Jev only when rules and Laya are unsure.
- Mismatch: built for Docker Swarm labels; other orchestrators are not supported.

## How it works

`aitomaton/deciders.py` defines the decision tiers; the `jev` tier calls TypeSafe's Jev on OpenRouter (`typesafe/jev-router`) through the same chat API as the LLM tier, and each service's policy caps what may happen. Integration evidence: [`aitomaton/deciders.py`](https://github.com/sirmmo/aitomaton/blob/e05e38c2c61079ef0c3ffa37d9ce3ecd0b37c0f8/aitomaton/deciders.py).

## Get started

From the upstream README (not run on the review host):

```sh
docker build -t aitomaton:0.1 . && docker build -t aitomaton-laya:0.1 laya
docker stack deploy -c stack.yml aitomaton
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site and live demo: [ingmmo.com/aitomaton/](https://ingmmo.com/aitomaton/)
- Decision chain docs: [github.com/sirmmo/aitomaton/blob/main/docs/decisions.md](https://github.com/sirmmo/aitomaton/blob/main/docs/decisions.md)

## Limits and data handling

Error events and context are sent to OpenRouter when the Jev or LLM tiers run; fixes can push code if your policy allows it.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit e05e38c2c610](https://github.com/sirmmo/aitomaton/tree/e05e38c2c61079ef0c3ffa37d9ce3ecd0b37c0f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
