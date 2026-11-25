# jev-sanitizer by William Nunes (Jev client that masks PII and secrets before every request and blocks the send when something cannot be masked)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-free Python client for Jev, usable as a CLI, an MCP server or a library, that masks e-mail addresses, Brazilian CPF numbers, IPs, tokens and other secrets in the state, instructions and criteria before sending, and blocks the request when something unsafe is left. Network failures come back as an explicit `unavailable` status, and a local log keeps hashes and sizes, not content. Docs are in Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uilhamello/jev-sanitizer) |
| Maintainer | [William Nunes](https://github.com/uilhamello). Independently curated. |
| Format | Python library, CLI and MCP server (pipx) |
| Requirements | Python 3.11+; a TypeSafe API key (or a Vercel AI Gateway key for the Vercel route). |
| License | [MIT](https://github.com/uilhamello/jev-sanitizer/blob/56976cef9a3ad18623ba8fe6076143b5128c1f12/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_sanitizer/client.py`](https://github.com/uilhamello/jev-sanitizer/blob/56976cef9a3ad18623ba8fe6076143b5128c1f12/src/jev_sanitizer/client.py) at the pinned commit. |

## When to use

- Send logs, tickets or database text to Jev without leaking personal data or secrets.
- Mismatch: if you need a complete DLP system; masking is rule-based and region-specific.

## How it works

`src/jev_sanitizer/client.py` sends the sanitized request to the configured endpoint; `config.py` defines a direct `typesafe` route (`https://api.typesafe.ai/v1/systemone`) and a `vercel` route through Vercel AI Gateway. Masking rules come from the author's separate `text-sanitizer-core` and regional packages such as `text-sanitizer-br`. Integration evidence: [`src/jev_sanitizer/client.py`](https://github.com/uilhamello/jev-sanitizer/blob/56976cef9a3ad18623ba8fe6076143b5128c1f12/src/jev_sanitizer/client.py).

## Get started

Install with pipx, put your key in a 600-permission key file, and copy the example config.

```sh
pipx install git+https://github.com/uilhamello/jev-sanitizer.git
cp jev-sanitizer.example.toml ~/.config/jev-sanitizer/config.toml
jev-sanitizer --version
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Examples: [github.com/uilhamello/jev-sanitizer/tree/56976cef9a3ad18623ba8fe6076143b5128c1f12/examples](https://github.com/uilhamello/jev-sanitizer/tree/56976cef9a3ad18623ba8fe6076143b5128c1f12/examples)

## Limits and data handling

Masking is pattern-based (the default region is Brazil); anything the rules miss is sent. The optional Vercel route is a third-party host. Portuguese-only documentation.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 56976cef9a3a](https://github.com/uilhamello/jev-sanitizer/tree/56976cef9a3ad18623ba8fe6076143b5128c1f12). Inspected the README, config and client code at the pinned commit; the client was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
