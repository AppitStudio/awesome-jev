# Jev Codex Router (Abjcodes) (local terminal chat where Jev picks the Codex model and reasoning effort for each phase and the router learns from verified outcomes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local terminal chat in front of Codex: for each phase of a task, one Jev request asks independent Choice questions for capability, reasoning effort and a mandatory category, and the router runs Codex with that model/effort pair. `/why` explains each choice; approvals are forwarded, never auto-accepted. It records verified outcomes and corrections locally, and while idle can run sandboxed benchmark attempts to compare policy variants, promoting one only on held-out evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Abjcodes/SystemOne-Model-Router) |
| Maintainer | [Abjcodes](https://github.com/Abjcodes). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python with uv, Codex CLI 0.159+ signed in with ChatGPT (`codex login`; no API-key fallback), and `JEV_API_KEY` (environment or macOS Keychain). Native graders need macOS. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Router/src/model_router/jev.py`](https://github.com/Abjcodes/SystemOne-Model-Router/blob/27ac1bffd0b5e0126b69f9b611c2ed677b343307/Router/src/model_router/jev.py) at the pinned commit. |

## When to use

- Let Jev choose model and reasoning effort per phase while you keep Codex as the executor.
- Mismatch: OpenAI API-key users; coding runs require ChatGPT sign-in.

## How it works

`Router/src/model_router/jev.py` calls TypeSafe (`https://api.typesafe.ai/v1` from `config.py`) with a focused routing projection of the request (redacted, capped at 32 KiB) and maps the Choice answers to a configured Codex model and effort. Integration evidence: [`Router/src/model_router/jev.py`](https://github.com/Abjcodes/SystemOne-Model-Router/blob/27ac1bffd0b5e0126b69f9b611c2ed677b343307/Router/src/model_router/jev.py).

## Get started

Install the dependencies, add your Jev key, sign in to Codex and point the router at a repository.

```sh
git clone https://github.com/Abjcodes/SystemOne-Model-Router && cd SystemOne-Model-Router/Router
uv sync --no-editable
export JEV_API_KEY=...
codex login
uv run --no-editable router --cwd /absolute/path/to/your/repository
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Abjcodes/SystemOne-Model-Router/blob/27ac1bffd0b5e0126b69f9b611c2ed677b343307/README.md](https://github.com/Abjcodes/SystemOne-Model-Router/blob/27ac1bffd0b5e0126b69f9b611c2ed677b343307/README.md)

## Limits and data handling

Routing projections go to TypeSafe on your key; Codex runs use your ChatGPT account. Traces and snapshots stay local. The maker notes that confidence values are diagnostic, not measured success rates. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 27ac1bffd0b5](https://github.com/Abjcodes/SystemOne-Model-Router/tree/27ac1bffd0b5e0126b69f9b611c2ed677b343307). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
