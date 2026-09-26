# Jev for Splunk

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Splunk search command `jev`: typed Jev questions over events become fields.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sispehar/jev-for-splunk) |
| Maintainer | [sispehar](https://github.com/sispehar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Splunk Enterprise search-head app with custom search command. |
| Requirements | Splunk Enterprise 9.3+; KV store; outbound HTTPS to api.typesafe.ai; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/sispehar/jev-for-splunk/blob/553b0399ea5c3e82eb2b5aa95c626657228a9380/LICENSE). LICENSE file is Apache-2.0; GitHub SPDX currently NOASSERTION. Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to turn support tickets or logs into calibrated probability metrics inside SPL via the `jev` command.

## How it works

Named event fields + question go to TypeSafe; answers cached per model/question/state in KV store for dashboards and repeats. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
Download release tarball from https://github.com/sispehar/jev-for-splunk/releases/latest
# Apps > Manage Apps > Install app from file; restart Splunk
# Jev for Splunk > Setup; paste TypeSafe key; run self-test
```

Pin revision `553b0399ea5c3e82eb2b5aa95c626657228a9380` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Not on Splunkbase (name collision warning with unrelated app). Event fields named in the search leave Splunk when the `jev` command runs. Live Splunk path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 553b039](https://github.com/sispehar/jev-for-splunk/tree/553b0399ea5c3e82eb2b5aa95c626657228a9380). AI-assisted README and LICENSE inspection; install/live paths not executed.
