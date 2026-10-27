# stable-computer-use (precise macOS computer use from the accessibility tree, with Jev as an optional step)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

macOS computer use for any AI agent that reads the accessibility tree and gives every element a reference that stays stable across snapshots, acting by reference instead of pixel coordinates; a six-tier decision ladder tries fast local scoring first and only asks Jev (closed choice among up to eight candidates) or your own LLM when local scoring is unsure, saving confident Jev answers to memory. Sister project of stable-chrome; Chinese and English docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhangyinglong3550/stable-computer-use) |
| Maintainer | [zhangyinglong3550](https://github.com/zhangyinglong3550). Independently curated. |
| Format | Swift runtime with a Python CLI |
| Requirements | macOS with accessibility permission, Swift toolchain; a TypeSafe API key only for the optional Jev tier. |
| License | [MIT](https://github.com/zhangyinglong3550/stable-computer-use/blob/ca7c6c7183eaa4240a709658347f9a971dcfb706/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cli/scu`](https://github.com/zhangyinglong3550/stable-computer-use/blob/ca7c6c7183eaa4240a709658347f9a971dcfb706/cli/scu) at the pinned commit. |

## When to use

- Drive Mac apps reliably without screenshots and coordinates.
- Mismatch: macOS only; Jev is an optional accelerator, not required.

## How it works

`cli/scu` posts the candidate elements as a Choice to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) when local scoring is below its confidence line. Integration evidence: [`cli/scu`](https://github.com/zhangyinglong3550/stable-computer-use/blob/ca7c6c7183eaa4240a709658347f9a971dcfb706/cli/scu).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/zhangyinglong3550/stable-computer-use && cd stable-computer-use
cd runtime && swift build -c release && cd ..
./cli/scu doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zhangyinglong3550/stable-computer-use#readme](https://github.com/zhangyinglong3550/stable-computer-use#readme)

## Limits and data handling

Element labels for up to eight candidates go to TypeSafe only on the Jev tier; everything else runs locally.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit ca7c6c7183ea](https://github.com/zhangyinglong3550/stable-computer-use/tree/ca7c6c7183eaa4240a709658347f9a971dcfb706). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
