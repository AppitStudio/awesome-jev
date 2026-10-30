# samplepick (describe a sound in words and Jev ranks the samples in your own library)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

For music producers: type something like "a warm piano loop around 80 bpm" and Jev ranks the samples in your library from their file names, folder tags, pack, key and tempo (plus an optional short sound description from local listening analysis). You listen, tick the keepers, and they are copied into a folder ready for your DAW. Audio never leaves your machine and files are only copied, never moved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tenplus1000/samplepick) |
| Maintainer | [tenplus1000](https://github.com/tenplus1000). Independently curated. |
| Format | Python CLI and local web server |
| Requirements | Python 3 and an OpenRouter key (or another compatible judge endpoint). |
| License | [MIT](https://github.com/tenplus1000/samplepick/blob/7a4a8f33acdf67a3a1b6342c709a868e807e47f6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`judge.py`](https://github.com/tenplus1000/samplepick/blob/7a4a8f33acdf67a3a1b6342c709a868e807e47f6/judge.py) at the pinned commit. |

## When to use

- Find a sample in a big, badly named library without scrolling folders.
- Mismatch: works from names and tags; the optional listening analysis adds detail.

## How it works

`judge.py` sends sample descriptions to `typesafe/jev-1.13` through OpenRouter's decisions endpoint and sorts by the returned scores. Integration evidence: [`judge.py`](https://github.com/tenplus1000/samplepick/blob/7a4a8f33acdf67a3a1b6342c709a868e807e47f6/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tenplus1000/samplepick && cd samplepick
python3 -m pip install .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tenplus1000/samplepick#readme](https://github.com/tenplus1000/samplepick#readme)

## Limits and data handling

Sample names and tags (text only) go to OpenRouter; audio stays local.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 7a4a8f33acdf](https://github.com/tenplus1000/samplepick/tree/7a4a8f33acdf67a3a1b6342c709a868e807e47f6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
