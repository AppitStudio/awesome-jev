# General Viral Gene Annotator by Arli Aditya Parikesit (two-tier viral FASTA triage with k-mer evidence, Jev, then Gemini for discordant calls)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Research pipeline that triages viral FASTA records against a five-pathogen panel (Japanese encephalitis virus, SARS-CoV-2, H5N1, poliovirus, HIV-1). A local k-mer containment step scores each sequence offline; TypeSafe System One then makes a six-way Choice with a confidence; a call is auto-processed only when it is confident and agrees with the k-mer top hit, and otherwise escalates to Gemini. Without keys it reports the k-mer profile alone. The abstract was accepted for an oral presentation at a November 2026 New York conference; every call is framed as a computational hypothesis to confirm in the lab.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Johnkecops/General-Viral-Gene-Annotator) |
| Maintainer | [Johnkecops](https://github.com/Johnkecops). Independently curated. |
| Format | Python script with sample FASTA panels (GPL-3.0) |
| Requirements | Python with `typesafe-sdk`, `google-genai` and `httpx`; `TYPESAFE_API_KEY` for Tier 1 and `GEMINI_API_KEY` for Tier 2. Runs alignment-only without keys. |
| License | [GPL-3.0](https://github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev sequence alignment.py`](https://github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/jev%20sequence%20alignment.py) at the pinned commit. |

## When to use

- See a decision model used as a confidence-gated middle tier between offline sequence evidence and an LLM in a bioinformatics triage.
- Mismatch: clinical or diagnostic use; the author states every call must be confirmed by BLAST, RT-qPCR or sequencing.

## How it works

`jev sequence alignment.py` builds an `AsyncTypeSafeClient` and calls `system_one` with a `Choice` over the five viruses plus `none`, using the sequence length, a preview and the k-mer profile as state; confidence below 0.85, or disagreement with the k-mer hit, triggers Gemini. Integration evidence: [`jev sequence alignment.py`](https://github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/jev%20sequence%20alignment.py).

## Get started

Install the SDKs, set the keys, and run the script on the sample FASTA.

```sh
git clone https://github.com/Johnkecops/General-Viral-Gene-Annotator
cd General-Viral-Gene-Annotator
pip install google-genai typesafe-sdk httpx
export TYPESAFE_API_KEY=...  GEMINI_API_KEY=...
python "jev sequence alignment.py" jev_samples.fasta
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/README.md](https://github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/README.md)
- Jev prompt notes: [github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/Jev-prompt.md](https://github.com/Johnkecops/General-Viral-Gene-Annotator/blob/74b9272e43ae2b5a2c04c18ab4d00555fb51818a/Jev-prompt.md)

## Limits and data handling

Sequence previews and k-mer profiles are sent to TypeSafe, and escalated cases to Google. The README notes its 94% figure came from an earlier one-question version and was not repeated with the current six-class panel. Research code, not a validated diagnostic tool. Note: "JEV" in the name refers to Japanese encephalitis virus.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 74b9272e43ae](https://github.com/Johnkecops/General-Viral-Gene-Annotator/tree/74b9272e43ae2b5a2c04c18ab4d00555fb51818a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
