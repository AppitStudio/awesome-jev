# jevqwen (OpenAI-compatible endpoint where Jev answers what it can, Python computes the rest and Qwen3-4B thinks only when needed)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Self-hosted OpenAI-compatible chat endpoint built from three parts: TypeSafe Jev answers the questions it can, Python computes what can be computed, and a Qwen3-4B model thinks only when it has to. Callers can request an answer type (for example yes/no) per request. On the maker's 1,757 held-out tasks it reports 87.8% accuracy against 82.6% for Qwen3-4B thinking on every task, using about 19% of Qwen's compute. Runs with Docker on an NVIDIA GPU, or against Qwen already served by vLLM, llama.cpp, LM Studio, Ollama or mlx.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nathanglon/jevqwen) |
| Maintainer | [nathanglon](https://github.com/nathanglon). Independently curated. |
| Format | Python server (Docker Compose or pip) |
| Requirements | A TypeSafe key, an API key you choose for your callers, and either an NVIDIA GPU with 16 GB+ or an OpenAI-compatible Qwen3-4B server. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevqwen/system.py`](https://github.com/nathanglon/jevqwen/blob/6c222befdfda0a8373fcc876d5f07eb2282eecee/jevqwen/system.py) at the pinned commit. |

## When to use

- Cut the cost of a small reasoning model by answering easy typed questions with Jev first.
- Mismatch: long-form generation; the router is tuned for tasks with checkable answers.

## How it works

`jevqwen/system.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default and decides from Jev's answer whether to return it, compute it or hand the task to Qwen. Integration evidence: [`jevqwen/system.py`](https://github.com/nathanglon/jevqwen/blob/6c222befdfda0a8373fcc876d5f07eb2282eecee/jevqwen/system.py).

## Get started

Start with Docker Compose, or point it at an existing Qwen server, then call it like any OpenAI endpoint.

```sh
git clone https://github.com/nathanglon/jevqwen && cd jevqwen
cp .env.example .env    # TYPESAFE_API_KEY and JEVQWEN_API_KEY
docker compose up -d    # or: pip install . && jevqwen serve --port 8800
# OpenAI client: base_url http://<server>:8800/v1, model jev-qwen3-4b
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nathanglon/jevqwen/blob/6c222befdfda0a8373fcc876d5f07eb2282eecee/README.md](https://github.com/nathanglon/jevqwen/blob/6c222befdfda0a8373fcc876d5f07eb2282eecee/README.md)

## Limits and data handling

Requests go to TypeSafe on your key and to your Qwen server. Benchmark figures are the maker's own. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 6c222befdfda](https://github.com/nathanglon/jevqwen/tree/6c222befdfda0a8373fcc876d5f07eb2282eecee). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
