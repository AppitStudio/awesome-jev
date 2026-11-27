# System One Decision Models with Jev by Packt (crash-course code using Jev with LangChain: primitives, model routing, risky-tool blocking and browser agents)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Runnable lessons for Packt's Jev crash course, one file each: calling Jev, the Noul, Choice and Score primitives, passing messages as structured state, LangChain middleware where Jev picks a fast or powerful chat model and blocks risky tool calls (including a prompt-injected delete), guarding an agent with jes, image questions with Box, and Browser Use's jev-ultrafast.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev) |
| Maintainer | [Packt Publishing](https://github.com/PacktPublishing) (code by jayeshsingh7). Independently curated. |
| Format | Python lessons (uv project, LangChain) |
| Requirements | Python with uv, a TypeSafe key, and an OpenAI key for the chat-model lessons; jev-ultrafast needs Python 3.12+. |
| License | [MIT](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/f285a369223cf84f2314e875cca9bd5318ff4f78/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`04_model_router_middleware.py`](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/f285a369223cf84f2314e875cca9bd5318ff4f78/04_model_router_middleware.py) at the pinned commit. |

## When to use

- LangChain developers who want short, runnable examples of putting Jev into an agent harness.
- Mismatch: the earlier Packt Jev Essentials book code, which is listed separately.

## How it works

Lessons use `langchain-typesafe` (`TypeSafeClassifier`, `Choice`, `Noul`) and its experimental `ModelRouterMiddleware` and `AutoModeMiddleware`, which call TypeSafe's System One API; lesson 01 can also point the same class at a local `tev1` model on Ollama. Integration evidence: [`04_model_router_middleware.py`](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/f285a369223cf84f2314e875cca9bd5318ff4f78/04_model_router_middleware.py).

## Get started

Clone, sync and run the lessons in order.

```sh
git clone https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev && cd System-One-Decision-Models-with-Jev
uv sync
export TYPESAFE_API_KEY=... OPENAI_API_KEY=...
uv run python 01_hello_jev.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Lesson 05 (risky tool calls): [github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/main/05_auto_mode_middleware.py](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/main/05_auto_mode_middleware.py)
- Lesson 07 (images and browser agent): [github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/main/07_images_and_browser_agent.py](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/blob/main/07_images_and_browser_agent.py)

## Limits and data handling

Pinned to an alpha `langchain-typesafe` release, so APIs may change. Lessons make billed TypeSafe and OpenAI calls.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit f285a369223c](https://github.com/PacktPublishing/System-One-Decision-Models-with-Jev/tree/f285a369223cf84f2314e875cca9bd5318ff4f78). Inspected the README, LICENSE, `pyproject.toml` and lessons 03 and 04 at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
