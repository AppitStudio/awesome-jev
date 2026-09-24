# jev-browser-bridge

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Bridge any CDP-speaking browser—cloud, local, or self-hosted, including no-render engines—into Jev browser automation, with verified runs across many providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lexmount/jev-browser-bridge) |
| Maintainer | [lexmount](https://github.com/lexmount). Independently curated. |
| Format | Python package/bridge. |
| Requirements | Python 3.11+; a CDP browser endpoint; TypeSafe Jev for action choice. |
| License | [Apache-2.0](https://github.com/lexmount/jev-browser-bridge/blob/0d34c80a70bb8b64d4f3f4a4fba285b763d168bf/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live multi-browser matrix not re-run. Vendor pass-rate table is upstream-reported. |

## When to use

Use when you need **one Jev browser loop** across cloud/local CDP browsers (including headless/no-render). Prefer [Jev Ultrafast](jev-ultrafast.md) for the core Python browser agent without multi-provider bridging.

## How it works

The bridge adapts browser CDP sessions so Jev can complete the same web tasks across providers; README publishes pass rates on a fixed five-task suite.

## Get started

```sh
git clone https://github.com/lexmount/jev-browser-bridge.git
cd jev-browser-bridge
git checkout 0d34c80a70bb8b64d4f3f4a4fba285b763d168bf
# follow README “Plug in a browser” for Moli/Browserbase/local CDP
```

## Examples and demos

- README results table across 14 browsers.
- Overview asset diagram.

## Limits and data handling

Page content and task goals reach TypeSafe. Cloud browser vendors may also receive session traffic.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 0d34c80](https://github.com/lexmount/jev-browser-bridge/tree/0d34c80a70bb8b64d4f3f4a4fba285b763d168bf). AI-assisted README inspection; live CDP/Jev not run.

Related: [Jev Ultrafast](jev-ultrafast.md), [jev-qa (moonshot-partners)](moonshot-partners-jev-qa.md).
