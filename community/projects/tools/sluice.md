# Sluice (minimal state-machine agent harness where Jev can be the judge of every transition; Chinese)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pure-standard-library Python agent harness: a worker runs a normal ReAct loop, and a pluggable judge (a chat LLM or Jev) decides each state-machine transition the worker requests, with an external watchdog loop. A mock Jev client lets you run the demo without a key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Potterluo/sluice) |
| Maintainer | [Potterluo](https://github.com/Potterluo). Independently curated. |
| Format | Python library + CLI (no dependencies) |
| Requirements | Python 3; a chat-model key for the worker; `SLUICE_JEV_API_KEY` (TypeSafe) or `OPENROUTER_API_KEY` for the Jev judge. |
| License | [MIT](https://github.com/Potterluo/sluice/blob/8f15f17fb61b5b53695136e86545e6335b0b1ace/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sluice/jev.py`](https://github.com/Potterluo/sluice/blob/8f15f17fb61b5b53695136e86545e6335b0b1ace/sluice/jev.py) at the pinned commit. |

## When to use

- Gate an agent's plan, implement and verify phases with a fast typed judge.
- Mismatch: docs are in Chinese; the worker still needs a chat model.

## How it works

`sluice/jev.py` sends the transition request and context to Jev (`typesafe/jev-1.14`) as typed questions with retries and candidate endpoints; the harness only allows edges declared in the JSON FlowSpec. Integration evidence: [`sluice/jev.py`](https://github.com/Potterluo/sluice/blob/8f15f17fb61b5b53695136e86545e6335b0b1ace/sluice/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python main.py --mock-jev
python main.py --judge jev --goal "<your goal>"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample run log: [github.com/Potterluo/sluice/blob/main/docs/sample-run.txt](https://github.com/Potterluo/sluice/blob/main/docs/sample-run.txt)

## Limits and data handling

Task context is sent to TypeSafe or OpenRouter for each judgment and to your chat provider for the worker. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 8f15f17fb61b](https://github.com/Potterluo/sluice/tree/8f15f17fb61b5b53695136e86545e6335b0b1ace). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
