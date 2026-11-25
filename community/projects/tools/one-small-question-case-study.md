# One Small Question Before Every Big Answer by Charlie Krueger (six-week production case study of Jev as the router in front of a local-first agent fleet)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

White paper with a 6-page plain-language edition and a 17-page technical companion: since 13 October 2026 every request from a five-agent fleet passes a local router that asks Jev two questions, which capability tier the request needs (Choice among six) and whether it is security-critical (Noul), before any generation model runs. Reports 17,355 Jev classifications at 195 ms median for about $2.79, and a documented spend incident.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milo-M4/jev-case-study) |
| Maintainer | Charlie Krueger, MediaCivic ([milo-M4](https://github.com/milo-M4)). Independently curated. |
| Format | PDF white paper with a sanitized policy excerpt and sample decision |
| Requirements | None to read; the router itself is not published. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`policy-excerpt-sanitized.yaml`](https://github.com/milo-M4/jev-case-study/blob/b497e0d4db4760759f3fb5b8c98622e22fa9da9b/policy-excerpt-sanitized.yaml) at the pinned commit. |

## When to use

- See real-world numbers and failure modes for Jev as a model router and security gate.
- Mismatch: if you want runnable code; only a policy excerpt and a sample decision are published.

## How it works

`policy-excerpt-sanitized.yaml` gives the exact two Jev questions, thresholds and the six tier definitions; `sample-decision.json` is one logged routing decision. Deterministic policy can only raise Jev's choice, never lower it ("Jev proposes; policy disposes"). Integration evidence: [`policy-excerpt-sanitized.yaml`](https://github.com/milo-M4/jev-case-study/blob/b497e0d4db4760759f3fb5b8c98622e22fa9da9b/policy-excerpt-sanitized.yaml).

## Get started

Read the plain-language edition, then the technical companion.

```sh
git clone https://github.com/milo-M4/jev-case-study
open jev-case-study/One-Small-Question-Prospect-Edition.pdf
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Technical companion: [github.com/milo-M4/jev-case-study/blob/b497e0d4db4760759f3fb5b8c98622e22fa9da9b/Technical-Companion.pdf](https://github.com/milo-M4/jev-case-study/blob/b497e0d4db4760759f3fb5b8c98622e22fa9da9b/Technical-Companion.pdf)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. All figures are the author's own production logs (the author says they were checked against TypeSafe usage records). The documents were drafted by the author's AI agents under his direction, as the README states. Generation models in the fleet are non-TypeSafe (for example DeepSeek through OpenRouter).

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit b497e0d4db47](https://github.com/milo-M4/jev-case-study/tree/b497e0d4db4760759f3fb5b8c98622e22fa9da9b). Inspected the README, policy excerpt and sample decision at the pinned commit; the PDFs were not reviewed in full. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
