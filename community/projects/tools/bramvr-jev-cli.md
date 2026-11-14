# jev-cli (BramVR) (dependency-free Python CLI and agent skill for classifying one record or a JSONL batch with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-file Python 3.9+ standard-library CLI: write a question document, then classify one JSON record or batch JSONL (one request per line) and get the answers back as JSON; ships example question sets and a `SKILL.md` so coding agents can run classify-many loops.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BramVR/jev-cli) |
| Maintainer | [BramVR](https://github.com/BramVR). Independently curated. |
| Format | Single-file Python CLI plus agent skill |
| Requirements | Python 3.9+. By default it calls OpenCode's free Jev endpoint with no key; for TypeSafe pass `--base-url https://api.typesafe.ai/v1` and set `TYPESAFE_API_KEY` (or a macOS Keychain item). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/jev.py) at the pinned commit. |

## When to use

- Label a JSONL file or let a coding agent classify many records from the shell.
- Mismatch: confidential data with the default endpoint; records go to OpenCode's free service unless you point it at TypeSafe.

## How it works

`jev.py` defaults to `https://opencode.ai/zen/v1` with model `jev-1.13-free` and appends `/systemone`; it attaches a TypeSafe key only when the origin is exactly `https://api.typesafe.ai`, and other origins get no Authorization header. Integration evidence: [`jev.py`](https://github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/jev.py).

## Get started

Write a question file, then pipe records in.

```sh
git clone https://github.com/BramVR/jev-cli && cd jev-cli
printf '%s\n' '{"id":"t1","state":"Charged twice"}' | python3 jev.py classify --questions questions.json
# TypeSafe instead of the free default:
TYPESAFE_API_KEY=... python3 jev.py batch --base-url https://api.typesafe.ai/v1 --model jev-1.14.0 --questions examples/failure-patterns.json < records.jsonl
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/README.md](https://github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/README.md)
- Agent skill: [github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/SKILL.md](https://github.com/BramVR/jev-cli/blob/254f05b6bf4a813b99d5222ed1b3a943f0279926/SKILL.md)

## Limits and data handling

The default sends record text to OpenCode's free endpoint (a third party, not TypeSafe); switch the base URL for TypeSafe. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 254f05b6bf4a](https://github.com/BramVR/jev-cli/tree/254f05b6bf4a813b99d5222ed1b3a943f0279926). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
