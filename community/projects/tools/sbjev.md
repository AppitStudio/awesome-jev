# sbjev (draft SponsorBlock segments with TypeSafe Jev, then review before submit)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

YouTube userscript plus local Python service that asks TypeSafe Jev (or Cloudflare Workers AI) which caption spans are sponsors, self-promotion, intros and outros, snaps edges with a local speech model, and opens unsubmitted SponsorBlock drafts for you to review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Landed9771/sbjev) |
| Maintainer | [Landed9771](https://github.com/Landed9771). Independently curated. |
| Format | Python service + Tampermonkey userscript (MIT) |
| Requirements | Python 3.10+, Tampermonkey/Violentmonkey, SponsorBlock, and a TypeSafe, Vercel AI Gateway, or Cloudflare Workers AI key. |
| License | [MIT](https://github.com/Landed9771/sbjev/blob/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sbjev.py`](https://github.com/Landed9771/sbjev/blob/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3/sbjev.py) at the pinned commit. |

## When to use

- Draft SponsorBlock segments from captions before you submit.
- Prefer human review of every draft.
- Mismatch: Windows installer is the one-step path; not a fully automatic submitter.

## How it works

`sbjev.py` POSTs System One questions to `https://api.typesafe.ai/v1/systemone` (or Cloudflare `typesafe/jev`) with caption windows and returns typed segment labels used to build SponsorBlock drafts. Integration evidence: [`sbjev.py`](https://github.com/Landed9771/sbjev/blob/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3/sbjev.py).

## Get started

Clone, run the Windows installer or Python server per README, install the userscript, and set a TypeSafe (or Cloudflare/Vercel) key.

```sh
git clone https://github.com/Landed9771/sbjev.git && cd sbjev
export TYPESAFE_API_KEY=...
# follow README install.ps1 or Python server + userscript
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Landed9771/sbjev/blob/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3/README.md](https://github.com/Landed9771/sbjev/blob/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3/README.md)

## Limits and data handling

Video captions and candidate segment text are sent to the configured classifier on your key. Nothing is submitted to SponsorBlock automatically.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 06c0da5fdf1d](https://github.com/Landed9771/sbjev/tree/06c0da5fdf1d92bb6c3ccf49afc858f9c51a15b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
