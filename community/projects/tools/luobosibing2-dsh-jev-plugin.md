# dsh-jev-plugin (luobosibing2)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Native DeepSeek Harness plugin that uses TypeSafe Jev as a System One layer for selection, supervision, corrections, and approvals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luobosibing2/dsh-jev-plugin) |
| Maintainer | [luobosibing2](https://github.com/luobosibing2). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | DeepSeek Harness (DSH) Cordis plugin package. |
| Requirements | DSH ~0.1.7-rc.2 per upstream; TypeSafe API key for live judgments. Features disabled by default. |
| License | [MIT](https://github.com/luobosibing2/dsh-jev-plugin/blob/cd041b90a3a291d832d75030ea92975501280f63/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [dsh-jev-plugin (jackie-cqz)](jackie-cqz-dsh-jev-plugin.md) and other dsh-jev* listings. |

## When to use

Use when a DeepSeek Harness agent should add optional TypeSafe Jev gates at selection/supervision/approval points. Prefer a narrower dsh-jev* plugin if you already standardize on one tool name.

## How it works

Hooks DSH extension points and optionally calls TypeSafe Jev for skill/file ranking, drift/completion/goal checks, shared-finding corrections, log admission, and workspace-write approvals. Separate Jev connection from the main model. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/luobosibing2/dsh-jev-plugin.git
cd dsh-jev-plugin
git checkout cd041b90a3a291d832d75030ea92975501280f63
# install via DSH Web UI from the GitHub URL, or follow upstream README
```

Pin revision `cd041b90a3a291d832d75030ea92975501280f63` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Early-stage; tested with DSH 0.1.7-rc.2. Live DSH/TypeSafe paths not run on the review host. Distinct from jackie-cqz/dsh-jev-plugin and other dsh-jev* listings.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit cd041b9](https://github.com/luobosibing2/dsh-jev-plugin/tree/cd041b90a3a291d832d75030ea92975501280f63). AI-assisted README and LICENSE inspection; install/live paths not executed.
