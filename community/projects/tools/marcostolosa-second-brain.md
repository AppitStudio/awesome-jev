# SecondBrain (local-first LLM wiki for Windows with Claude Code, Obsidian and TypeSafe Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local-first personal LLM wiki for Windows 11 that captures sources into Obsidian with Claude Code, using TypeSafe Jev for policy, dedupe and routing decisions; cited, injection-hardened, pt-BR.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marcostolosa/second-brain) |
| Maintainer | [marcostolosa](https://github.com/marcostolosa). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Windows 11, Python 3.11+, Claude Code, Obsidian, and a TypeSafe API key. |
| License | [MIT](https://github.com/marcostolosa/second-brain/blob/d96712e7e04daeb875897cfb7cb67a911d3cabc7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/secondbrain/jev_client.py`](https://github.com/marcostolosa/second-brain/blob/d96712e7e04daeb875897cfb7cb67a911d3cabc7/src/secondbrain/jev_client.py) at the pinned commit. |

## When to use

- Build a cited personal wiki from captured links.
- Use Jev for fast capture/dedupe decisions before Claude writes.
- Mismatch: Windows-focused; Portuguese-first docs.

## How it works

`src/secondbrain/jev_client.py` calls `https://api.typesafe.ai/v1/systemone` (configurable, default `jev-latest`) with a token from Windows Credential Manager. Integration evidence: [`src/secondbrain/jev_client.py`](https://github.com/marcostolosa/second-brain/blob/d96712e7e04daeb875897cfb7cb67a911d3cabc7/src/secondbrain/jev_client.py).

## Get started

Clone, copy `config/config.example.yaml`, store your TypeSafe token, and run the CLI.

```sh
git clone https://github.com/marcostolosa/second-brain.git && cd second-brain
export TYPESAFE_API_KEY=...
pip install -e . && secondbrain --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/marcostolosa/second-brain/blob/d96712e7e04daeb875897cfb7cb67a911d3cabc7/README.md](https://github.com/marcostolosa/second-brain/blob/d96712e7e04daeb875897cfb7cb67a911d3cabc7/README.md)

## Limits and data handling

Captured content is sent to TypeSafe and Claude on your accounts.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit d96712e7e04d](https://github.com/marcostolosa/second-brain/tree/d96712e7e04daeb875897cfb7cb67a911d3cabc7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
