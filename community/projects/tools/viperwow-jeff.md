# jeff (Viperwow)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single-binary Rust classifier server with an admin page: one `/v1/systemone`-shaped API in front of Jev-compatible models — TypeSafe Jev in the cloud, a local Contrastive-LM (CLM) it installs, or Laya/PipeLLM/any compatible server — with access keys and a playground.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Viperwow/jeff) |
| Maintainer | [Viperwow](https://github.com/Viperwow). Independently curated. |
| Format | Server binary (API on :8080, admin UI on :8081); v0.1.0 release at review |
| Requirements | Linux/macOS/Windows; a TypeSafe key for Jev, or a GPU for local CLM; Docker compose for CLM deployment optional. |
| License | [MIT](https://github.com/Viperwow/jeff/blob/f5cf4f0d8c97b5b0a9b05b430a2ceac85b80f87f/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Self-host a decision API that apps call with noul/choice/score questions, regardless of which model answers.
- Try a local model next to hosted Jev from the same admin playground.
- Mismatch: distinct from the Jeff bookshelf app and from firelex's Jeff models of the same name.

## How it works

Clients send `{model, state, questions}` to `/v1/systemone`; jeff routes to the configured provider (`clm/...`, TypeSafe Jev, or another compatible server) and returns probabilities per answer. Access keys and providers are managed in the admin page ([`src/main.rs`](https://github.com/Viperwow/jeff/blob/f5cf4f0d8c97b5b0a9b05b430a2ceac85b80f87f/src/main.rs), [`src/keys.rs`](https://github.com/Viperwow/jeff/blob/f5cf4f0d8c97b5b0a9b05b430a2ceac85b80f87f/src/keys.rs)).

## Get started

Download a release archive (or build with Cargo), start it, and configure providers in the admin page:

```sh
# from https://github.com/Viperwow/jeff/releases/latest
tar xzf jeff-v0.1.0-x86_64-unknown-linux-gnu.tar.gz && ./jeff
# admin http://127.0.0.1:8081 ; API http://127.0.0.1:8080/v1/systemone
```

Requests routed to TypeSafe Jev are billed to your key; local CLM runs on your GPU.

## Examples and demos

- README *Call the API* curl with noul, choice and score questions.

## Limits and data handling

Early release (v0.1.0). Local CLM quality is not Jev's; no comparison verified. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit f5cf4f0d8c97](https://github.com/Viperwow/jeff/tree/f5cf4f0d8c97b5b0a9b05b430a2ceac85b80f87f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
