# jev-classify-prompt (policy-based text moderation with Jev, as a Go library and CLI)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go library and command-line tool, standard library only, that checks a text against a moderation policy: each class is one yes/no question, all go to Jev in one call, and a class matches when its probability reaches its line; a missing or malformed answer is an error, never a pass. Ships a ten-class default policy and started as the moderation in Human42.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DataAlchemy/jev-classify-prompt) |
| Maintainer | [DataAlchemy](https://github.com/DataAlchemy). Independently curated. |
| Format | Go library and CLI |
| Requirements | Go; a TypeSafe API key (file or environment). |
| License | [Apache-2.0](https://github.com/DataAlchemy/jev-classify-prompt/blob/7682ffcfa9b38f384170ca821f6ba05cbd865f71/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`typesafe.go`](https://github.com/DataAlchemy/jev-classify-prompt/blob/7682ffcfa9b38f384170ca821f6ba05cbd865f71/typesafe.go) at the pinned commit. |

## When to use

- Screen prompts or user posts before an LLM or a person sees them.
- Write your own policy as plain yes/no questions with per-class thresholds.
- Mismatch: thresholds were tuned by the author on jev-1.13.0; re-run your own sets after editing questions.

## How it works

`typesafe.go` posts the policy's questions to `https://api.typesafe.ai/v1/systemone`; `classifier.go` reads each probability against its line and refuses on any match. Integration evidence: [`typesafe.go`](https://github.com/DataAlchemy/jev-classify-prompt/blob/7682ffcfa9b38f384170ca821f6ba05cbd865f71/typesafe.go).

## Get started

From the upstream README (not run on the review host):

```sh
go install github.com/DataAlchemy/jev-classify-prompt/cmd/jev-classify@latest
jev-classify -key-file ~/typesafe.key -expect passed testdata/passes.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with default policy and tuning notes: [github.com/DataAlchemy/jev-classify-prompt#readme](https://github.com/DataAlchemy/jev-classify-prompt#readme)

## Limits and data handling

Texts go to TypeSafe for each check. Tuning sets are not published; results quoted in the README are the author's.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 7682ffcfa9b3](https://github.com/DataAlchemy/jev-classify-prompt/tree/7682ffcfa9b38f384170ca821f6ba05cbd865f71). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
