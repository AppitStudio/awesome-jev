# frigate-decisions by andrewmagness (Frigate NVR sidecar that publishes decision-model answers to MQTT)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Sidecar that asks a decisions API (Gemini Decisions by default, OpenAI, TypeSafe Jev or OpenRouter) typed yes/no, choice and score questions about Frigate NVR events, schedules or on-demand requests, and publishes the answers to MQTT as Home Assistant sensors. Separate from the nat-e project of the same name.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrewmagness/frigate-decisions) |
| Maintainer | [andrewmagness](https://github.com/andrewmagness). Independently curated. |
| Format | Docker sidecar (Python, MIT) |
| Requirements | Frigate, an MQTT broker, Docker Compose, and a key for the chosen provider (TypeSafe for Jev). |
| License | [MIT](https://github.com/andrewmagness/frigate-decisions/blob/d7f1ad4b38fce2618bf092472ca9948010c00236/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/frigate_decisions/decisions.py`](https://github.com/andrewmagness/frigate-decisions/blob/d7f1ad4b38fce2618bf092472ca9948010c00236/src/frigate_decisions/decisions.py) at the pinned commit. |

## When to use

- Drive Home Assistant automations from typed camera questions with thresholds.
- Mismatch: Jev is one of several providers, not the default.

## How it works

`decisions.py` includes a SystemOne provider that posts each snapshot, clip or frame with the question set to `{base}/v1/systemone` (TypeSafe Jev or a compatible gateway such as OpenRouter); answers become MQTT state with confidence and probability attributes. Integration evidence: [`src/frigate_decisions/decisions.py`](https://github.com/andrewmagness/frigate-decisions/blob/d7f1ad4b38fce2618bf092472ca9948010c00236/src/frigate_decisions/decisions.py).

## Get started

Copy the example env, questions and compose files, choose a provider and start the container.

```sh
cp .env.example .env
mkdir -p config && cp questions.example.yaml config/questions.yaml
docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/andrewmagness/frigate-decisions/blob/d7f1ad4b38fce2618bf092472ca9948010c00236/README.md](https://github.com/andrewmagness/frigate-decisions/blob/d7f1ad4b38fce2618bf092472ca9948010c00236/README.md)

## Limits and data handling

Camera snapshots, clips or frames go to the provider you choose, on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit d7f1ad4b38fc](https://github.com/andrewmagness/frigate-decisions/tree/d7f1ad4b38fce2618bf092472ca9948010c00236). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
