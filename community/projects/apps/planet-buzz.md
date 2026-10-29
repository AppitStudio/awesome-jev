# Planet.buzz (Reddit-style discovery feed from many web sources, with Jev classifying topics, motivations and content warnings)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Early-stage web feed that brings posts, stories, videos and conversations from several web sources into an old-Reddit-style interface with topics, comments and votes. Per the maker, Jev classifies public post metadata into topics, reader motivations (learning, staying informed, entertainment, feel-good) and content warnings; application code validates and caches those answers and ranks posts from your topic preferences, content limits and feedback. Jev does not write posts or set the feed order directly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://planet.buzz/) |
| Tags | `Closed source` · `Pricing unverified` |
| Product homepage | [planet.buzz](https://planet.buzz/) |
| Pricing and access | Guest feed browsable in a browser without an account or payment (HTTP 200 on review); sign-in for participation. Account limits and any future pricing were not verified. Checked **2026-10-29**. |
| Jev evidence | Maker's implementation note ([gist](https://gist.github.com/vinayagg/8e8cfcfd8a7dd7de18ebc35a112244d3)) describing typed score and yes/no questions sent to TypeSafe's System One API. Implementation was **not** inspected (private repository); TypeSafe traffic was **not** observed on the review host. |
| Disclosure | Closed source. Jev use is documented by the maker, not independently observed. Self-submitted by the maker through [issue #2272](https://github.com/AppitStudio/awesome-jev/issues/2272) ("I work on Planet.buzz"). AI-assisted catalog review; no affiliation with the maker. Listing is not an endorsement. |
| Maintainer | Vinay Aggarwal / Planet.buzz team ([support@planet.buzz](mailto:support@planet.buzz)). |
| Format | Hosted web application. |
| Platform and availability | Web browser; no native app claimed. |
| Jev's role | Maker claim: classifies public post metadata (topics, motivations, content warnings); ranking stays in application code. |
| Requirements | A modern browser; an account only to post, comment or vote. |
| License | Proprietary hosted product; no public repository. |

## When to use

- Browse a mixed feed of links, stories and videos you can tune by topic, motivation and content limits.
- Mismatch: a small, early community; imported vote and comment counts are not local engagement, and federation is experimental.

## How it works

Per the maker's note: the backend sends public post metadata to Jev with typed score questions for topics and motivations and yes/no questions for content warnings; answers are validated and cached, missing ones fall back to metadata, and the feed is ranked from your preferences and private more/less feedback. Question wording and thresholds were not inspected.

## Get started

1. Open [planet.buzz](https://planet.buzz/) and browse the guest feed or pick a topic.
2. Sign in only if you want to post, comment, vote or save preferences.

## Examples and demos

- Live product: [planet.buzz](https://planet.buzz/)
- Maker's implementation note: [gist.github.com/vinayagg/8e8cfcfd8a7dd7de18ebc35a112244d3](https://gist.github.com/vinayagg/8e8cfcfd8a7dd7de18ebc35a112244d3)

## Limits and data handling

Public post metadata goes to TypeSafe for classification. Content-warning classifications can be wrong. Opening source links sends normal browser requests to those sites. Imported YouTube comments are read-only copies.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia). Primary sources: the live homepage (HTTP 200), the maker's implementation note and the submission in [issue #2272](https://github.com/AppitStudio/awesome-jev/issues/2272). AI-assisted curation; no account was created and no personalization was tested. De-dupe: no existing Awesome Jev listing for planet.buzz.
