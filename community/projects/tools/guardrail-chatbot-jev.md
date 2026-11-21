# guardrail-chatbot-jev by Nhat Nguyet (one policy file checks user input, bot replies and whole conversations with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Content safety for AI chatbots: one policy file defines 18 hazard categories mapped to MLCommons AILuminate, Llama Guard and OWASP, and Jev checks what users send, what the bot replies and the whole conversation; each verdict names the severity, the action and the standard it comes from. The same verdicts are available in Python, TypeScript and Go with no third-party dependencies, plus a Viet Nam compliance pack.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev) |
| Maintainer | [Nhat-Nguyet](https://github.com/Nhat-Nguyet). Independently curated. |
| Format | Python, TypeScript and Go libraries |
| Requirements | Python, Node or Go; a TypeSafe key for live checks (a replay transport runs with no key or network). |
| License | [CC BY-NC 4.0 (non-commercial; not OSI open source)](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Licensed CC BY-NC 4.0 (non-commercial), not an OSI open-source license. |
| Jev evidence | [`python/src/guardrail_chatbot_jev/client.py`](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/python/src/guardrail_chatbot_jev/client.py) at the pinned commit. |

## When to use

- Add input, output and multi-turn safety checks to a non-commercial chatbot from one policy file.
- Mismatch: commercial products; the CC BY-NC 4.0 license does not allow commercial use.

## How it works

`python/src/guardrail_chatbot_jev/client.py` (and `ts/src/client.ts`) send the message or conversation with the policy's questions to `https://api.typesafe.ai/v1/systemone` and map Jev's probabilities to named verdicts with severity and action; `scripts/calibrate.sh` calibrates thresholds. Integration evidence: [`python/src/guardrail_chatbot_jev/client.py`](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/python/src/guardrail_chatbot_jev/client.py).

## Get started

Install the Python package from the tagged release; it runs offline with replayed answers until you add a key.

```sh
pip install "git+https://github.com/Nhat-Nguyet/guardrail-chatbot-jev@python/v1.1.4#subdirectory=python"
export TYPESAFE_API_KEY=...   # for live Jev checks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [nhatnguyet.org/tro-ly-ai](https://nhatnguyet.org/tro-ly-ai)
- Guide: [github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/docs/guide.md](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/docs/guide.md)
- Multi-turn method: [github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/docs/multiturn.md](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/blob/34049b20a6ccc7fecff712f036af81f33d07f8b3/docs/multiturn.md)

## Limits and data handling

User messages, bot replies and conversation history are sent to TypeSafe on each check. The README's live multi-turn test figures are the author's and were not reproduced. Licensed CC BY-NC 4.0: source is readable and reusable for non-commercial purposes only.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 34049b20a6cc](https://github.com/Nhat-Nguyet/guardrail-chatbot-jev/tree/34049b20a6ccc7fecff712f036af81f33d07f8b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
