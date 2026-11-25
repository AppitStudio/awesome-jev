# PhoneBench by Arush Wadhawan (benchmark of Jev and other decision models operating a real iPhone, graded on the phone's final state)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Benchmark that gives a decision model a goal and lets it operate a physical iPhone (or simulator) one action at a time through the accessibility tree and a screenshot; a programmatic check of the phone's final state decides success. The v0.7 preview compares Jev 1.13 and 1.14 with Gemini Decision 1 and Clef Omni over 31 tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SoulSniper-V2/phonebench) |
| Maintainer | [Arush Wadhawan](https://github.com/SoulSniper-V2). Independently curated. |
| Format | Python benchmark (standard library only) using phonedriver |
| Requirements | A Mac with Xcode, Python 3.10+, phonedriver, and an iPhone in Developer Mode (or a simulator); a TypeSafe key for the Jev runs. |
| License | [MIT](https://github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`phonebench/providers.py`](https://github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/phonebench/providers.py) at the pinned commit. |

## When to use

- Measure whether a decision model can drive real apps, and how often it declares success too early.
- Compare Jev's speed and accuracy with other decision models on device tasks.
- Mismatch: if you need an assistant that operates your phone day to day; this is a benchmark.

## How it works

`phonebench/providers.py` maps `jev-1.13` and `jev-1.14` to TypeSafe's System One API; each step asks the model to pick the next action from the options on screen, or FINISH. Integration evidence: [`phonebench/providers.py`](https://github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/phonebench/providers.py).

## Get started

Check the toolchain, then run the phone or simulator track.

```sh
npx -y phonedriver doctor
python3 -m phonebench.runner --providers jev-1.14 gemini-decision-1 --repeats 3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results v0.7: [github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/results/v0.7/RESULTS.md](https://github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/results/v0.7/RESULTS.md)
- Reproduce: [github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/docs/REPRODUCE.md](https://github.com/SoulSniper-V2/phonebench/blob/3bc198d65bc036fb1659dbad4c30d00a80bb8958/docs/REPRODUCE.md)

## Limits and data handling

Preview results with wide intervals: Gemini Decision 1 scored 82% and Jev 1.14 71%, with Jev deciding fastest (about 220 ms) but finishing early more often (14–18% false finishes). Figures are the author's own. Screenshots and on-screen text go to each model provider; the personal-data tasks use your own phone's data.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 3bc198d65bc0](https://github.com/SoulSniper-V2/phonebench/tree/3bc198d65bc036fb1659dbad4c30d00a80bb8958). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
