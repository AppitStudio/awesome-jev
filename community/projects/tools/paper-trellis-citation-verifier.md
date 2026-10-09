# Paper Trellis Citation Verifier

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Browser tool for peer reviewers and authors that pairs each citing sentence in a manuscript with the paper it cites, fetches the cited paper (PubMed, Crossref, OpenAlex, PMC, arXiv), has Claude propose a verbatim supporting quote that code then proves exists, and asks TypeSafe Jev for P(supports / contradicts / says nothing). Human verdicts are never overwritten. Hosted demo at verify.papertrellis.com.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MarissaFamularo/citation-verifier) |
| Maintainer | [MarissaFamularo](https://github.com/MarissaFamularo). Independently curated. |
| Format | Static web app (browser-side) with a stateless relay for TypeSafe calls |
| Requirements | A modern browser; your own Anthropic and/or TypeSafe API keys per the README. |
| License | [MIT](https://github.com/MarissaFamularo/citation-verifier/blob/fad6eb6ad1c8e0f235c3afbfab3efd6153ce915f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Check whether each citation in a manuscript actually supports the sentence that cites it.
- Mismatch: checks only open full text or abstracts; model scores are advisory.

## How it works

Code parses the .docx/PDF and resolves references; Claude proposes a quote that is string-matched against the fetched text; Jev scores the sentence/passage pair. (Summarized from the upstream [README](https://github.com/MarissaFamularo/citation-verifier/blob/fad6eb6ad1c8e0f235c3afbfab3efd6153ce915f/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Use the hosted tool at [verify.papertrellis.com](https://verify.papertrellis.com) or follow the repository README to run it yourself.

## Limits and data handling

README states there is no database or application server; the manuscript is read in the browser, and TypeSafe calls go through a stateless rewrite relay. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit fad6eb6ad1c8](https://github.com/MarissaFamularo/citation-verifier/tree/fad6eb6ad1c8e0f235c3afbfab3efd6153ce915f). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
