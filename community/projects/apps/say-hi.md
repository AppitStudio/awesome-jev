# say-hi

[All projects](../README.md) · [Web apps](README.md#web-apps)

Educational demo where TypeSafe Jev (jev-1.13.0) types every reply one key at a time by choosing among keyboard options, with cost/keystroke caps and a live request inspector.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huemorgan2/say-hi) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/huemorgan2/say-hi#readme) |
| Pricing and access | Free source build; BYOK TypeSafe. Hard caps: 400 keystrokes and $0.50 per reply (configurable). Checked 2026-10-03. |
| Jev evidence | [Upstream README](https://github.com/huemorgan2/say-hi/blob/7b67dd8637d410bda80ef20fb4f5fa07706c5417/README.md) documents jev-1.13.0 chooser-as-chat with per-key requests and inspector chips. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. AGPL-3.0. Educational/demo experiment—not a production chatbot. Live install/UI paths not run on the Linux review host. |
| Maintainer | [huemorgan2](https://github.com/huemorgan2). Independently curated. |
| Format | Node.js local web demo (AGPL-3.0) |
| Platform and availability | Local Node web UI (Node 21.7+) |
| Jev's role | Jev is the chooser: plan goal, tournament-pick an answer word, then pick each keystroke. Application code owns the keyboard UI, caps, and logging. |
| Requirements | Node 21.7+; TYPESAFE_API_KEY in .env |
| License | [AGPL-3.0](https://github.com/huemorgan2/say-hi/blob/7b67dd8637d410bda80ef20fb4f5fa07706c5417/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Educational demo where TypeSafe Jev (jev-1.13.0) types every reply one key at a time by choosing among keyboard options, with cost/keystroke caps and a live request inspector. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/huemorgan2/say-hi.git
cd say-hi
git checkout 7b67dd8637d410bda80ef20fb4f5fa07706c5417
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 7b67dd8637d4](https://github.com/huemorgan2/say-hi/tree/7b67dd8637d410bda80ef20fb4f5fa07706c5417). AI-assisted README and license inspection; live paths not executed.
