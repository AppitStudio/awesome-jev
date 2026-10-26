# sony-pdf-repository-tools (repair, OCR and Jev relevance filtering for a 95,000-document Sony manual dump)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Scripts behind the EveryCRT wiki's use of the Sony PDF Repository: they repair PDFs truncated at 1 MiB, index and OCR the dump, and use Jev as a first-pass yes/no filter for CRT and video-gear manuals before a local LLM labels each kept document; includes a 400-document hand-labelled evaluation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ArclightAutomata/sony-pdf-repository-tools) |
| Maintainer | [ArclightAutomata](https://github.com/ArclightAutomata). Independently curated. |
| Format | Python scripts and evaluation set |
| Requirements | Python 3; a TypeSafe API key for the Jev classification pass; Chrome, Xvfb and patchright only for live re-downloads. |
| License | [MIT](https://github.com/ArclightAutomata/sony-pdf-repository-tools/blob/67013bc648c69a28047ce1da2e36463b410294f2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_eval/run_eval.py`](https://github.com/ArclightAutomata/sony-pdf-repository-tools/blob/67013bc648c69a28047ce1da2e36463b410294f2/jev_eval/run_eval.py) at the pinned commit. |

## When to use

- Filter a large document archive down to the files relevant to your topic before slower labelling.
- Reuse the evaluation approach (filename plus the first 2,000 characters) to choose how much text to send.
- Mismatch: the questions and categories are EveryCRT-specific; the repo contains no Sony documents, only code and metadata.

## How it works

`jev_eval/run_eval.py` posts the filename and opening text of each document with a yes/no relevance question to `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.14.0`); the README reports that this found all 156 relevant documents in the 400-document set at about 92% precision, and warns that Jev's product-kind answers were often wrong, so a later labelling step decides the kind. Integration evidence: [`jev_eval/run_eval.py`](https://github.com/ArclightAutomata/sony-pdf-repository-tools/blob/67013bc648c69a28047ce1da2e36463b410294f2/jev_eval/run_eval.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ArclightAutomata/sony-pdf-repository-tools && cd sony-pdf-repository-tools
export TYPESAFE_API_KEY=...
python jev_eval/run_eval.py   # see jev_eval/README.md for the evaluation setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ArclightAutomata/sony-pdf-repository-tools#readme](https://github.com/ArclightAutomata/sony-pdf-repository-tools#readme)
- EveryCRT wiki: [wiki.everycrt.com](https://wiki.everycrt.com)

## Limits and data handling

Filenames and opening text of each document go to TypeSafe. The README's precision and cost figures (about $6 for the full corpus) are the authors' own, not verified here.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 67013bc648c6](https://github.com/ArclightAutomata/sony-pdf-repository-tools/tree/67013bc648c69a28047ce1da2e36463b410294f2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
