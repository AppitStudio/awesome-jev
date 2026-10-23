# jevtophoto (finding junk photos with Jev, an experiment)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment on what Jev is good for, using phone photo-library cleanup: code extracts on-device features, Jev judges delete or keep with a confidence, and a human confirms; it reports where Jev adds little over written rules and what it is good and bad at from about 740 probe calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qeoplkm/jevtophoto) |
| Maintainer | [qeoplkm](https://github.com/qeoplkm). Independently curated. |
| Format | Experiment with a Mac extractor, iOS app and JavaScript capability study |
| Requirements | A Mac or iPhone for the extractor and app; an OpenRouter API key. |
| License | [MIT](https://github.com/qeoplkm/jevtophoto/blob/2f541493a926e20a2fc20248afce3cca70adc0c7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ios/JevPhoto/JevPhoto/Pipeline/JevClient.swift`](https://github.com/qeoplkm/jevtophoto/blob/2f541493a926e20a2fc20248afce3cca70adc0c7/ios/JevPhoto/JevPhoto/Pipeline/JevClient.swift) at the pinned commit. |

## When to use

- Learn practical strengths and pitfalls of Jev before designing a classifier.
- Reuse the probe-study approach for your own task.
- Mismatch: research write-up; not a finished photo cleaner.

## How it works

`JevClient.swift` posts a JSON `state` of photo metadata and questions to OpenRouter's decisions endpoint with model `~typesafe/jev-latest`; Jev never sees pixels. Integration evidence: [`ios/JevPhoto/JevPhoto/Pipeline/JevClient.swift`](https://github.com/qeoplkm/jevtophoto/blob/2f541493a926e20a2fc20248afce3cca70adc0c7/ios/JevPhoto/JevPhoto/Pipeline/JevClient.swift).

## Get started

Clone and open the iOS project (not run on the review host):

```sh
git clone https://github.com/qeoplkm/jevtophoto
open jevtophoto/ios/JevPhoto
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Findings and feature schema in the README: [github.com/qeoplkm/jevtophoto#readme](https://github.com/qeoplkm/jevtophoto#readme)

## Limits and data handling

Only derived metadata is sent to OpenRouter and TypeSafe; findings are from the author's probes with an earlier question set.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 2f541493a926](https://github.com/qeoplkm/jevtophoto/tree/2f541493a926e20a2fc20248afce3cca70adc0c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
