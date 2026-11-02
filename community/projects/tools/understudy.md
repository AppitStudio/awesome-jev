# Understudy (CPU-only drop-in proxy that learns your repeated Jev questions and answers the graduated ones itself)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in proxy for System One models such as Jev: it forwards each request to the lead model, trains small CPU "understudents" on the answers, and lets one serve a question only after it reaches near-parity, while sampled audits against Jev demote any that slip. Aimed at high-volume pipelines that ask the same narrow questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Endgame-Labs/understudy) |
| Maintainer | [Endgame-Labs](https://github.com/Endgame-Labs). Independently curated. |
| Format | Rust server (CLI) |
| Requirements | Rust toolchain or a release binary; a lead model endpoint such as TypeSafe Jev's `/v1/systemone` with your key. |
| License | [MIT](https://github.com/Endgame-Labs/understudy/blob/ae1167970b5e51ca4ee04ff620db2905b9dc0a16/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/proxy.rs`](https://github.com/Endgame-Labs/understudy/blob/ae1167970b5e51ca4ee04ff620db2905b9dc0a16/src/proxy.rs) at the pinned commit. |

## When to use

- Cut the Jev bill for millions of repeated yes/no, routing or triage questions.
- Mismatch: it only helps narrow, repetitive questions; novel ones still go to Jev.

## How it works

`src/proxy.rs` forwards requests to the configured lead (Jev, Rune, Clef or OpenAI Decisions) and returns its answers in the same shape, storing them as training examples; graduated questions are answered locally and audited against the lead. With the TypeSafe SDK you only set `TYPESAFE_BASE_URL`. Integration evidence: [`src/proxy.rs`](https://github.com/Endgame-Labs/understudy/blob/ae1167970b5e51ca4ee04ff620db2905b9dc0a16/src/proxy.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install --git https://github.com/endgame-labs/understudy
understudy serve --lead-url <your lead's /v1/systemone URL>
export TYPESAFE_BASE_URL=http://127.0.0.1:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Lead setup pages: [github.com/Endgame-Labs/understudy/tree/main/docs/leads](https://github.com/Endgame-Labs/understudy/tree/main/docs/leads)
- Understudent designs: [github.com/Endgame-Labs/understudy/tree/main/docs/understudents](https://github.com/Endgame-Labs/understudy/tree/main/docs/understudents)

## Limits and data handling

Requests and Jev's answers are stored locally as training data; shadow mode still sends every request to the lead. Local answers can differ from Jev's; review the graduation and audit settings. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit ae1167970b5e](https://github.com/Endgame-Labs/understudy/tree/ae1167970b5e51ca4ee04ff620db2905b9dc0a16). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
