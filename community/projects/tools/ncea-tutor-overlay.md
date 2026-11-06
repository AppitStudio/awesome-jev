# ncea-tutor-overlay (DeepTutor overlay with a TypeSafe Jev gate for NCEA grading)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Apache-2.0 overlay for HKUDS DeepTutor that turns it into an NCEA/NZQA Achievement Standard tutor: verified-answer grading, a TypeSafe Jev gate that can refuse to release a grade without evidence, and a location-only question index.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sigebolo/ncea-tutor-overlay) |
| Maintainer | [Sigebolo](https://github.com/Sigebolo). Independently curated. |
| Format | Python overlay for DeepTutor (Apache-2.0) |
| Requirements | DeepTutor install, NCEA materials you are allowed to use, and a TypeSafe API key for the optional Jev gate. |
| License | [Apache-2.0](https://github.com/Sigebolo/ncea-tutor-overlay/blob/492638678d39718e1e953744ae5af136ce9d069e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/ncea_jev_gate.py`](https://github.com/Sigebolo/ncea-tutor-overlay/blob/492638678d39718e1e953744ae5af136ce9d069e/scripts/ncea_jev_gate.py) at the pinned commit. |

## When to use

- Grade NCEA-style answers with an evidence gate.
- Keep exam paper text out of the index.
- Mismatch: NZQA-focused overlay; DeepTutor required.

## How it works

`scripts/ncea_jev_gate.py` asks TypeSafe System One typed questions and, on missing key/timeout/error, returns empty so the original reply is kept. Integration evidence: [`scripts/ncea_jev_gate.py`](https://github.com/Sigebolo/ncea-tutor-overlay/blob/492638678d39718e1e953744ae5af136ce9d069e/scripts/ncea_jev_gate.py).

## Get started

Install alongside DeepTutor per README and set `TYPESAFE_API_KEY` to enable the Jev gate.

```sh
git clone https://github.com/Sigebolo/ncea-tutor-overlay.git && cd ncea-tutor-overlay
export TYPESAFE_API_KEY=...
# follow README DeepTutor overlay setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Sigebolo/ncea-tutor-overlay/blob/492638678d39718e1e953744ae5af136ce9d069e/README.md](https://github.com/Sigebolo/ncea-tutor-overlay/blob/492638678d39718e1e953744ae5af136ce9d069e/README.md)

## Limits and data handling

Student answers and rubric/context under review are sent to TypeSafe on your key when the gate is enabled.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 492638678d39](https://github.com/Sigebolo/ncea-tutor-overlay/tree/492638678d39718e1e953744ae5af136ce9d069e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
