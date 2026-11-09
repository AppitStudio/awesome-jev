# Multi-Decision for KiraAI (Chinese group-chat plugin with an optional JEV reply-or-not decision)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

KiraAI chat plugin that takes over group-chat triggering and context windows; its beta JEV mode asks a decision model such as Jev only for the probability of replying.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision) |
| Maintainer | [2skr1996-cloud](https://github.com/2skr1996-cloud). Independently curated. |
| Format | KiraAI plugin (Python, MIT; beta) |
| Requirements | KiraAI 3.0.0+ (3.1.1+ for host decision models), and a TypeSafe/OpenRouter/Vercel AI Gateway Jev endpoint for JEV mode. |
| License | [MIT](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/blob/70e6ab87e6ea329fcf817fbadad19e77376f9589/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`state/jev_phase.py`](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/blob/70e6ab87e6ea329fcf817fbadad19e77376f9589/state/jev_phase.py) at the pinned commit. |

## When to use

- Decide when a group bot should speak.
- Tune uncertainty thresholds for reply decisions.
- Mismatch: JEV mode is beta and lightly tested; docs are Chinese.

## How it works

`jev_phase.py` sends one `choice()` (reply / no reply) to a decision model; a custom backend posts directly to `{api_base}/v1/systemone`, with fallback models and an uncertainty band. Integration evidence: [`state/jev_phase.py`](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/blob/70e6ab87e6ea329fcf817fbadad19e77376f9589/state/jev_phase.py).

## Get started

Install in KiraAI, then enable 「JEV 决策」 in advanced mode and pick the model or third-party endpoint.

```sh
git clone https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/blob/70e6ab87e6ea329fcf817fbadad19e77376f9589/README.md](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/blob/70e6ab87e6ea329fcf817fbadad19e77376f9589/README.md)

## Limits and data handling

Recent chat records are sent to the chosen decision endpoint.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 70e6ab87e6ea](https://github.com/2skr1996-cloud/kira-ai-plugin-multi-decision/tree/70e6ab87e6ea329fcf817fbadad19e77376f9589). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
