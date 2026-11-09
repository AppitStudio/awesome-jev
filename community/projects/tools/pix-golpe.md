# Pix Race (split-screen demo: Rust + TypeSafe Jev vs Python + DeepSeek detecting Pix scams)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Portuguese-language video demo where the same simulated messages go to Rust + Jev and Python + DeepSeek; each side flags Pix scams and traces money through a 10M-transaction simulated graph.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sandeco/pix-golpe) |
| Maintainer | [sandeco](https://github.com/sandeco). Independently curated. |
| Format | Rust + Python demo (no license file) |
| Requirements | Rust, Python 3.12, a TypeSafe key and a DeepSeek key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/sandeco/pix-golpe/blob/24894a80f4b4a52d76b47bfb98de6b3e9af44df1/src/jev.rs) at the pinned commit. |

## When to use

- Watch a side-by-side latency comparison of Jev and an LLM.
- Reuse the typed-question pattern for fraud triage.
- Mismatch: no license file; ask the author before reuse.

## How it works

`src/jev.rs` posts four typed questions per message (scam? type? urgency? asks for Pix?) to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; the README compares latency and accuracy with DeepSeek. Integration evidence: [`src/jev.rs`](https://github.com/sandeco/pix-golpe/blob/24894a80f4b4a52d76b47bfb98de6b3e9af44df1/src/jev.rs).

## Get started

Clone, copy `.envexemple` to `.env` with both keys, install the Python worker requirements and run the Rust app per the README.

```sh
git clone https://github.com/sandeco/pix-golpe.git && cd pix-golpe
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sandeco/pix-golpe/blob/24894a80f4b4a52d76b47bfb98de6b3e9af44df1/README.md](https://github.com/sandeco/pix-golpe/blob/24894a80f4b4a52d76b47bfb98de6b3e9af44df1/README.md)

## Limits and data handling

All data is simulated; messages are sent to TypeSafe and DeepSeek on your keys.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 24894a80f4b4](https://github.com/sandeco/pix-golpe/tree/24894a80f4b4a52d76b47bfb98de6b3e9af44df1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
