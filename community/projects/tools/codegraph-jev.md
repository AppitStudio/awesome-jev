# codegraph-jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research log: can a code graph plus TypeSafe Jev match a coding agent at finding and ordering functions?

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snemesh/codegraph-jev) |
| Maintainer | [snemesh](https://github.com/snemesh). Independently curated. |
| Format | Research log: code graph + Jev judge vs coding agent on find/order tasks. |
| Requirements | Python/bench harness per upstream; TypeSafe Jev for judge calls. |
| License | [MIT](https://github.com/snemesh/codegraph-jev/blob/14be0b94df5f2aa2f65a0915e5a8c543d6c8b33e/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for research on cheap code-reading stacks. Prefer coding agents for end-to-end implementation.

## How it works

Hybrid retrieval + Jev yes/no probabilities; author reports it approaches find but lags on order.

## Get started

```sh
git clone https://github.com/snemesh/codegraph-jev.git
cd codegraph-jev
git checkout 14be0b94df5f2aa2f65a0915e5a8c543d6c8b33e
# see upstream README for bench reproduction
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 14be0b9](https://github.com/snemesh/codegraph-jev/tree/14be0b94df5f2aa2f65a0915e5a8c543d6c8b33e). AI-assisted README and license inspection; install/live paths not executed.
