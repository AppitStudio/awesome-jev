# CE187 decision-model comparison demo by gnutar (Japanese single-file CGI demo comparing Jev, OpenAI Decisions and Gemini Decisions on the same input)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Education and research demo in Japanese that sends the same yes/no, multiple-choice or score question to Jev, OpenAI Decisions and Gemini Decisions and shows each answer, probability bars, confidence, response time and estimated cost side by side.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gnutar/jev_demo) |
| Maintainer | [gnutar](https://github.com/gnutar). Independently curated. |
| Format | Python single-file CGI script (Apache2), standard library only |
| Requirements | Ubuntu + Apache2 with CGI; API keys for TypeSafe, OpenAI and/or Google in the env file. |
| License | [Unlicense](https://github.com/gnutar/jev_demo/blob/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_demo.cgi`](https://github.com/gnutar/jev_demo/blob/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc/jev_demo.cgi) at the pinned commit. |

## When to use

- Show students or an audience how three decision APIs differ on the same question.
- Mismatch: non-Japanese audiences (the UI is Japanese) or hosts without CGI.

## How it works

`jev_demo.cgi` posts `noul`, `choice` or `score` questions to `JEV_ENDPOINT` (default `https://api.typesafe.ai/v1/systemone`) with Python's `urllib`, and calls the OpenAI and Gemini decision APIs for the same input; keys stay on the server. Integration evidence: [`jev_demo.cgi`](https://github.com/gnutar/jev_demo/blob/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc/jev_demo.cgi).

## Get started

Copy the CGI script and the example env file onto an Apache2 CGI host and fill in the keys.

```sh
git clone https://github.com/gnutar/jev_demo.git
# copy jev_demo.cgi to your cgi-bin and jev-demo.env.example to the env path the README describes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/gnutar/jev_demo/blob/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc/README.md](https://github.com/gnutar/jev_demo/blob/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc/README.md)

## Limits and data handling

Inputs go to TypeSafe, OpenAI and Google, billed to your keys. Prices in the demo are configured unit prices with a fixed 160 yen per USD rate, not live pricing. CGI v14 at review.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ba9fd9daf8dc](https://github.com/gnutar/jev_demo/tree/ba9fd9daf8dcdf918341ab6f3d4d98f49b1c2dbc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
