# Daily News (AI news digest with Jev relevance and quality decisions)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Chinese-language daily AI news collector and digest site whose backend can use Jev for intent classification, AI relevance, quality, importance and prompt-injection checks while an LLM writes the summaries.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZJM189/Daily_News) |
| Maintainer | [ZJM189](https://github.com/ZJM189). Independently curated. |
| Format | Web app with Python API (MIT) |
| Requirements | Python 3.12+, the web front end, an OpenAI-compatible model key, and `JEV_API_KEY` for the Jev layer. |
| License | [MIT](https://github.com/ZJM189/Daily_News/blob/e96419ae95f38993831295ca30c67bcc958010f9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`api/app/infrastructure/typesafe_jev/client.py`](https://github.com/ZJM189/Daily_News/blob/e96419ae95f38993831295ca30c67bcc958010f9/api/app/infrastructure/typesafe_jev/client.py) at the pinned commit. |

## When to use

- Filter and rank news items with typed decisions before summarizing.
- Mismatch: docs mostly Chinese; Jev is optional.

## How it works

`api/app/infrastructure/typesafe_jev/client.py` calls `{base}/v1/systemone`; `docs/design/jev-integration.md` (Chinese) splits duties so Jev makes the decisions and the LLM writes summaries and answers. Integration evidence: [`api/app/infrastructure/typesafe_jev/client.py`](https://github.com/ZJM189/Daily_News/blob/e96419ae95f38993831295ca30c67bcc958010f9/api/app/infrastructure/typesafe_jev/client.py).

## Get started

Deploy per the README and set `JEV_API_KEY` and `JEV_MODEL` in the server `.env`.

```sh
git clone https://github.com/ZJM189/Daily_News.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev integration doc: [github.com/ZJM189/Daily_News/blob/e96419ae95f38993831295ca30c67bcc958010f9/docs/design/jev-integration.md](https://github.com/ZJM189/Daily_News/blob/e96419ae95f38993831295ca30c67bcc958010f9/docs/design/jev-integration.md)

## Limits and data handling

News item text goes to TypeSafe on your key; summaries go to your LLM provider.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit e96419ae95f3](https://github.com/ZJM189/Daily_News/tree/e96419ae95f38993831295ca30c67bcc958010f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
