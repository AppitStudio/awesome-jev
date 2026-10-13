# Flash (YouTube Q&A)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension: ask a YouTube video a question by voice or text and it jumps to the answer, or highlights where the topic comes up, using TypeSafe Jev to score transcript segments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/surbhit20/jev-on-yt) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [chromewebstore.google.com/detail/flash/mcfkndmlbcdlmjgkdkjkaolcodjjopbp](https://chromewebstore.google.com/detail/flash/mcfkndmlbcdlmjgkdkjkaolcodjjopbp) |
| Pricing and access | Free on the Chrome Web Store (checked 2026-10-13); needs your own TypeSafe key (billed per search); optional OpenAI key for the Accurate voice mode. |
| Jev evidence | [`src/config.js`](https://github.com/surbhit20/jev-on-yt/blob/88a1d5716ec2c875cd7b72c39cee4a9bd7b5e139/src/config.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [surbhit20](https://github.com/surbhit20). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Chrome (Chrome Web Store 0.1.0, or load unpacked from source) · YouTube videos with English captions |
| Jev's role | Jev scores transcript passages (with chapter context) against your question; a confident top passage triggers a jump, otherwise lime peaks mark matching regions on the progress bar. |
| Requirements | Chrome; TypeSafe API key; optional OpenAI API key. |
| License | No LICENSE file at the pinned commit (public source, no open-source grant); listed as Source available. Chrome Web Store build is free. |

## When to use

- Find the part of a long talk or podcast that answers a spoken question without scrubbing.
- Mismatch: No open-source license yet; English captions only.

## How it works

The extension reads the video transcript and chapters, sends passages and your question to Jev, then jumps or draws highlight peaks from the returned scores. (Summarized from the upstream [README](https://github.com/surbhit20/jev-on-yt/blob/88a1d5716ec2c875cd7b72c39cee4a9bd7b5e139/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install Flash from the Chrome Web Store (or load the repo unpacked), paste your TypeSafe key in Settings, then hold Control on a YouTube video and ask.

## Limits and data handling

Transcript text and your question go to TypeSafe with your key; OpenAI receives audio only in Accurate voice mode. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 88a1d5716ec2](https://github.com/surbhit20/jev-on-yt/tree/88a1d5716ec2c875cd7b72c39cee4a9bd7b5e139). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
