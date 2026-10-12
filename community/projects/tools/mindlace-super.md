# super (superpowers-jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin marketplace with `supersonic` build plugins and `superpowers-jev`, which optionally inserts TypeSafe Jev typed judgments at thirteen decision points (shadow mode by default, fails open).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mindlace/super) |
| Maintainer | [mindlace](https://github.com/mindlace). Independently curated. |
| Format | Python · Claude Code plugin marketplace |
| Requirements | Claude Code; TypeSafe key when enabling live Jev judgments. |
| License | [MIT](https://github.com/mindlace/super/blob/0f5a9f0eabb06640cc180223e3d644f60ed731e2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Add optional System One checks beside Superpowers/supersonic workflows.
- Mismatch: Jev plugin is optional; default shadow mode does not block.

## How it works

Hooks call `jev-hook` / jevlib at configured decision points. Evidence: [`plugins/superpowers-jev/hooks/jev-hook`](https://github.com/mindlace/super/blob/0f5a9f0eabb06640cc180223e3d644f60ed731e2/plugins/superpowers-jev/hooks/jev-hook).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add mindlace/super
/plugin install superpowers-jev@super
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 0f5a9f0eabb0](https://github.com/mindlace/super/tree/0f5a9f0eabb06640cc180223e3d644f60ed731e2). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
