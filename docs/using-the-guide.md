# Find a starting point for your workflow

Describe what you want to do to your coding agent. The Awesome Jev Guide skill helps it find a suitable project or example, explain what needs adapting, and guide you through setup. If the repo does not already cover your workflow, it can help build a small starter in your preferred language or framework.

## Install the guide

From your project directory, run:

```sh
npx skills add AppitStudio/awesome-jev --skill awesome-jev-guide
```

Select your agent when prompted. Add `--agent codex` for Codex or `--global` to make it available across projects. See the [Skills CLI](https://github.com/vercel-labs/skills) for supported agents. You can also point an agent to the [skill and its linked guides](../skills/awesome-jev-guide/SKILL.md) without installing it.

This is the repository's independent guide. It uses the official [TypeSafe skill and documentation](https://docs.typesafe.ai/agent-skill) for integration details when needed. Installing the guide does not create an API account, install application dependencies, or make paid calls.

## Explain your need

You do not need to know Jev's terminology. For example:

> Use awesome-jev-guide. We receive support emails and manually choose billing, technical, or account support. We use Node.js. Help me choose a starting point and build a demo that sends unclear cases for review.

Or:

> Use awesome-jev-guide. I have a Python search tool and want to choose better passages before generating an answer. Recommend something from this repo and guide me through setup. I do not have an API key yet.

Or simply:

> Use awesome-jev-guide. I am new to Jev. Help me work out whether it can help with my workflow, then show me the simplest useful example.

Share what comes in, what you do today, what you want to happen, and any existing stack or constraints. A fictional input example is enough. Do not share API keys or private customer records in the conversation.

## What to expect

The agent should recommend one starting point and explain why it fits, what already works, and what needs building. It should preserve your stack and explain where ordinary code or another service is needed. Jev supplies typed judgments; a resource that selects relevant text does not also generate an answer or connect to your business tools.

Setup progresses through a runnable offline example, optional TypeSafe account/key setup, and an explicitly requested live check. You can stop after the recommendation or ask the agent to adapt/build the solution in your project. New applications need their own evaluation; there is no universally perfect starter or guaranteed production accuracy.

## Try a demo directly

With Python 3.10+ in a checkout of this repo:

```sh
python3 skills/awesome-jev-guide/scripts/try_example.py support-routing
```

You should see JSON marked as synthetic and a computed routing decision. No Python packages, account, or API key are needed. The other choices are `quality-rubric`, `span-selection`, and `rag-triage`.

For browser or native-app workflows, start with the [computer-use walkthrough](computer-use.md). Its standalone demo uses a different command:

```sh
python3 examples/computer-use/run.py
```

Expect `simulated_verified` and five passing checks. This simulates a form edit and exact source extraction without controlling a device. Follow the walkthrough to choose a real implementation with its own installation and first-task guide.

If you want a real request, first follow the [guided key setup](../skills/awesome-jev-guide/references/setup.md#2-obtain-and-configure-a-key-when-live-access-is-wanted). Then run:

```sh
python3 skills/awesome-jev-guide/scripts/try_example.py support-routing --live
```

This sends the example input to TypeSafe and may incur charges. It uses an existing `TYPESAFE_API_KEY` or asks for the key privately in an interactive terminal. The helper makes at most one HTTP attempt, does not save the entered key, and does not change any tickets. Use `--show-request` to inspect the request without calling the API. See [full setup and troubleshooting](../skills/awesome-jev-guide/references/setup.md) for other environments.

When your own project is ready to share, use the separate [contributor skill](../CONTRIBUTING.md#use-the-contributor-skill) to prepare a submission.
