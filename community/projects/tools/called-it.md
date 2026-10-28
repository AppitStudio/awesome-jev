# Called It! (grade someone's annual predictions at strict, standard and lenient bars, with Jev as the grader)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Claude Code skill that finds a person's or company's annual predictions, turns each into three bars (strict, standard, lenient) before gathering evidence, then grades every claim and bar against the year's public evidence with Jev, committing every receipt so anyone can replay the scorecard; a gallery site shows graded subjects.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rickmanelius/called-it) |
| Maintainer | [rickmanelius](https://github.com/rickmanelius). Independently curated. |
| Format | Claude Code plugin with Python scripts (standard library) |
| Requirements | Claude Code; a TypeSafe API key to grade (cached runs replay without one). |
| License | [MIT](https://github.com/rickmanelius/called-it/blob/144a865ea01da64771a291c8627f356eba2b79f0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/called-it/scripts/lib/jev.py`](https://github.com/rickmanelius/called-it/blob/144a865ea01da64771a291c8627f356eba2b79f0/skills/called-it/scripts/lib/jev.py) at the pinned commit. |

## When to use

- Score prediction lists fairly, with the strictness visible.
- Mismatch: grading quality depends on the evidence gathered; scorecards are the author's runs.

## How it works

`skills/called-it/scripts/lib/jev.py` calls TypeSafe's System One API and caches every request by hash with the model that answered, so a run can be replayed offline. Integration evidence: [`skills/called-it/scripts/lib/jev.py`](https://github.com/rickmanelius/called-it/blob/144a865ea01da64771a291c8627f356eba2b79f0/skills/called-it/scripts/lib/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add rickmanelius/called-it
/plugin install called-it@called-it
/called-it Every 2026 https://every.to/context-window/every-s-2026-predictions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gallery: [rickmanelius.github.io/called-it/](https://rickmanelius.github.io/called-it/)
- README: [github.com/rickmanelius/called-it#readme](https://github.com/rickmanelius/called-it#readme)

## Limits and data handling

Claims and gathered public evidence go to TypeSafe for grading.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 144a865ea01d](https://github.com/rickmanelius/called-it/tree/144a865ea01da64771a291c8627f356eba2b79f0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
