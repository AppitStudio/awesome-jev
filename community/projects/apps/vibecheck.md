# Vibe Check for X

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

A Chrome extension that adds Jev-powered feedback to the X composer so writers can review a draft before posting it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RafalWilinski/vibecheck) |
| Tags | `Source unverified` · `Pricing unverified` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/RafalWilinski/vibecheck#readme). |
| Pricing and access | [Installation and cost notes](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/README.md#install) describe loading the source with your own keys. No purchase step is documented, but explicit app pricing/access terms were not found as of 2026-09-19. TypeSafe and optional OpenAI usage can incur separate charges; upstream cost estimates were not verified. |
| Jev evidence | Inspected [API client](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/background.js), [rubrics](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/rubrics.js), and [composer integration](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/content.js); no live inference was tested. |
| Disclosure | Public source was inspected, but licensing and commercial status are unverified. Independently curated with AI assistance, not submitted on the upstream maintainer's behalf. The contributor reports no affiliation or commercial relationship with the project or maintainer. Inclusion is not endorsement. |
| Maintainer | [RafalWilinski](https://github.com/RafalWilinski). |
| Format | JavaScript Chrome Manifest V3 extension, with no package installation or build step documented. |
| Platform and availability | Manifest version **0.2.0**; source-only, unpacked Chrome installation. Content scripts target X, Twitter, and X Pro URLs. No store distribution or compatibility with other browsers was verified. |
| Jev's role | Scores draft qualities, judges yes/no properties, and selects an audience-reaction category. Optional OpenAI vision supplies media descriptions; code computes the overall verdict. |
| Requirements | Chrome with Developer mode, access to an X composer/account, and a TypeSafe account/API key. An OpenAI account/key is optional for media. Keys are entered in extension settings, without environment variables. |
| License | No license file or license declaration was found in the [reviewed tree](https://github.com/RafalWilinski/vibecheck/tree/badf9dad5deecababd8afe43a574a5ea6d376711); GitHub reports no license. Public readability does not establish reuse or redistribution permission. |

## When to use

Use it for feedback on a post's tone and clarity, or to inspect how configurable typed rubrics become a writing scorecard. It includes handling for replies, quote posts, and multi-post drafts. It displays advice; the inspected code does not publish posts or enforce its verdict on the Post button.

The judgments are subjective. Virality, regret, and whether writing sounds AI-generated are rubric outputs, not validated predictions or proof of authorship.

## How it works

The content script discovers X composer elements, extracts draft text and available reply/quote context, and inserts a scorecard. The background worker sends this state and typed questions to `https://api.typesafe.ai/v1/systemone` using `jev-latest`. The request and answer fields align with the [HTTP API reference](https://docs.typesafe.ai/api) inspected during review; live compatibility remains untested and the model alias can change.

The default set contains 13 rubrics: 11 for text and two additional media rubrics when draft media entries exist. Score, Noul, and Choice questions cover separate judgments. JavaScript normalizes scores, combines weighted positive and negative metrics, and applies a warning when a weighted negative metric reaches `0.75`. These weights and thresholds are application policy, without demonstrated calibration.

Optional media processing sends images or captured video frames to OpenAI Chat Completions, defaulting to `gpt-4o-mini`. Jev receives the resulting descriptions. Successful descriptions are cached in memory by media URL; page reloads, key/model changes, and failed descriptions can lead to additional calls.

## Get started

The following retrieves the reviewed source; it does not contact an inference provider:

```sh
git clone https://github.com/RafalWilinski/vibecheck.git
cd vibecheck
git checkout badf9dad5deecababd8afe43a574a5ea6d376711
```

Follow the pinned [installation instructions](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/README.md#install). The browser steps below were inspected, not executed.

1. Open `chrome://extensions`, enable **Developer mode**, choose **Load unpacked**, and select the cloned folder. Settings open on installation.
2. For a controlled first check, turn off **Auto-analyze while typing** and **Describe attached media** before saving your TypeSafe key. Leave the optional OpenAI key empty. This avoids automatic analysis as you compose.
3. Open [X's composer](https://x.com/compose/post), enter a non-sensitive sample such as “I shipped a small bug fix today. Here is what changed.”, and press the extension's **Check** button once. Expect a scorecard or a displayed error. Posting is a separate user action.

**The Check button makes a live, potentially billable request and sends the draft/context to TypeSafe.** One manual text check can make up to four HTTP attempts on retryable service errors. The settings page's TypeSafe **Test key** button also performs inference; it is not an offline validation step. Optional OpenAI setup and media descriptions add separate provider traffic and costs.

## Examples and demos

- [Usage instructions](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/README.md#usage) describe manual checks, shortcuts, metric tooltips, and viewing the media descriptions sent to Jev.
- [Rubric customization](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/README.md#customizing-rubrics) shows the settings JSON structure for changing questions and verdict weights.

No separate demo, automated test suite, or offline mock mode was found in the reviewed tree. The sample above is illustrative, with no recorded model result.

## Limits and data handling

Auto-analysis is enabled by default with a 1.2-second delay, so unpublished drafts can leave the browser before you press Post. Draft text, detected reply/quote text and author names, and media descriptions go to TypeSafe. When configured, OpenAI receives media images or URLs, including detected context photos. A single captured video frame cannot establish what happens throughout a video.

Both API keys and settings use `chrome.storage.sync`; they can sync through Chrome and are not stored in an OS credential vault. Media descriptions remain in an in-memory cache, while the panel's collapsed state uses page local storage. The short privacy statement in upstream settings does not describe all these paths; this guide follows the implementation.

The worker retries HTTP 429 and server errors up to four total attempts. Missing keys and request failures appear in the panel. Failed or disabled media descriptions become explanatory text passed onward to Jev, and media rubrics can still run. The code does not enforce complete answers or a confidence-based abstention rule: missing individual answers are skipped in the aggregate, so a partial response can still produce a verdict.

X DOM changes can break discovery. Draft extraction collects all matching composers in the document, so simultaneous composers may be treated as one thread. In-flight results are not checked against a fresh draft before rendering. These limitations, current X layout support, and browser permissions behavior need hands-on testing.

## Review and maintenance

Reviewed **2026-09-19** at [badf9da](https://github.com/RafalWilinski/vibecheck/commit/badf9dad5deecababd8afe43a574a5ea6d376711), manifest version **0.2.0**. AI-assisted review covered the README, complete file inventory and licensing gap, manifest, background worker, rubrics, composer script, settings HTML, and settings script. Catalog entries and open issues/PRs were searched for duplicates; none were found.

In a separate source checkout, all four JavaScript files passed `node --check`; Python parsed the manifest and verified all eight referenced script, stylesheet, options, and icon assets exist. These are syntax and packaging checks, not execution of the extension. Chrome installation, X integration, live provider requests, OpenAI model access, and judgment quality were not tested. Catalog checks follow the [validation scope](../../../docs/validation.md).

Related: the [offline quality-rubric example](../../../examples/quality-rubric/README.md) demonstrates combining independent judgments in application code without browser access.
