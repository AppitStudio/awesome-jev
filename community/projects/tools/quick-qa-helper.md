# quick-qa-helper

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Android UI QA loop for coding agents: a planner model picks the next action, TypeSafe Jev picks the target element (Box on a screenshot when the UI tree lacks it) and independently verifies done, adb acts, and you get a pass/fail report with one summary image.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ouor/quick-qa-helper) |
| Maintainer | [ouor](https://github.com/ouor). Independently curated. |
| Format | Python CLI + on-device server + agent skill |
| Requirements | Python, adb and an Android device; planner key (Claude Haiku or Cerebras) and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/ouor/quick-qa-helper/blob/7c8dc82e2acab8ba0957415e6720c9fdf9302de6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`quickqa/llm.py`](https://github.com/ouor/quick-qa-helper/blob/7c8dc82e2acab8ba0957415e6720c9fdf9302de6/quickqa/llm.py) at the pinned commit. |

## When to use

- Let an agent run a multi-step Android UI check in one command.
- Want a fast element selector and an independent done check.
- Mismatch: needs a connected device; planner model is separate.

## How it works

`quickqa/llm.py` defines the Jev client (`/v1/systemone`) used as selector (Choice over UI nodes or Box on screenshots) and verifier; a planner model proposes steps. Integration evidence: [`quickqa/llm.py`](https://github.com/ouor/quick-qa-helper/blob/7c8dc82e2acab8ba0957415e6720c9fdf9302de6/quickqa/llm.py).

## Get started

From the upstream README: install, connect a device, set keys, then run `quickqa` with a task and app package.

```sh
quickqa "open settings and check dark mode toggles" --app com.example.app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- skills/quick-qa/SKILL.md

## Limits and data handling

Screenshots and UI trees go to TypeSafe and the planner provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7c8dc82e2aca](https://github.com/ouor/quick-qa-helper/tree/7c8dc82e2acab8ba0957415e6720c9fdf9302de6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
