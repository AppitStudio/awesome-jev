# rpilayer (HumanLayer's Research-Plan-Implement workflow run locally in Claude Code and Pi, with Jev reading your replies)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill and Pi package that run HumanLayer's Research-Plan-Implement workflow without the HumanLayer app: task state comes from local documents, a progress band draws the steps, and Jev decides what a chat message means for the task (advance, iterate or question).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gecm0/rpilayer) |
| Maintainer | [gecm0](https://github.com/gecm0). Independently curated. |
| Format | Claude Code plugin / Pi package (Python) |
| Requirements | Python 3, Git, Claude Code or Pi; `TYPESAFE_API_KEY` for `judge`. |
| License | [Apache-2.0](https://github.com/gecm0/rpilayer/blob/82f143f8c0ce9cf87f88ee38e7bdab6d19b24ea8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`rpilayer.py`](https://github.com/gecm0/rpilayer/blob/82f143f8c0ce9cf87f88ee38e7bdab6d19b24ea8/rpilayer.py) at the pinned commit. |

## When to use

- Use the RPI workflow locally with an intent check on each reply.
- Mismatch: the workflow and step instructions are HumanLayer's, fetched on first use.

## How it works

`rpilayer.py judge` sends the task state and your message to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), trimming state to stay within Jev's 32k token budget, and returns advance, iterate or question. Integration evidence: [`rpilayer.py`](https://github.com/gecm0/rpilayer/blob/82f143f8c0ce9cf87f88ee38e7bdab6d19b24ea8/rpilayer.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin install rpilayer --marketplace gecm0/rpilayer
pi install git:github.com/gecm0/rpilayer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- HumanLayer upstream: [github.com/humanlayer/humanlayer](https://github.com/humanlayer/humanlayer)

## Limits and data handling

Task documents and chat messages are sent to TypeSafe for `judge`. Independent project; not affiliated with TypeSafe or HumanLayer.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 82f143f8c0ce](https://github.com/gecm0/rpilayer/tree/82f143f8c0ce9cf87f88ee38e7bdab6d19b24ea8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
