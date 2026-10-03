# jevpilot (bloudhood)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP browser that finishes goals with TypeSafe Jev picking each step (distinct from standardagents/jevpilot driving demo).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bloudhood/jevpilot) |
| Maintainer | [bloudhood](https://github.com/bloudhood). Independently curated. |
| Format | MCP server: goal-level browser automation with TypeSafe Jev choosing each step. |
| Requirements | Chrome; MCP host; TypeSafe or OpenRouter Jev key. |
| License | [MIT](https://github.com/bloudhood/jevpilot/blob/293d01b763af07aac8eae030cfec042a01de96a6/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Distinct from standardagents/jevpilot (driving simulation). |

## When to use

Use for goal-level browser tasks with abstention. Distinct from the JevPilot driving simulation listing.

## How it works

jevpilot runs a real Chrome session; Jev selects actions; safety rules catch login/pay walls before the model.

## Get started

```sh
git clone https://github.com/bloudhood/jevpilot.git
cd jevpilot
git checkout 293d01b763af07aac8eae030cfec042a01de96a6
# follow upstream MCP install; distinct from standardagents/jevpilot
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 293d01b](https://github.com/bloudhood/jevpilot/tree/293d01b763af07aac8eae030cfec042a01de96a6). AI-assisted README and license inspection; install/live paths not executed.
