# decision-harness (clef-decide: a tribunal of System One judges, including Jev, for coding-agent gates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Helper for coding agents where judges make every gated decision: routine gates go to one SystemOne-compatible judge and high-stakes ones to a majority panel; `jev` is one of the named judges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Thingscorp/decision-harness) |
| Maintainer | [Thingscorp](https://github.com/Thingscorp). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python 3 and keys for the judges you configure (TypeSafe for `jev`). |
| License | [MIT](https://github.com/Thingscorp/decision-harness/blob/4b96b45452f007388cb6ad8b09a4fdab8e7889a0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/clef-decide`](https://github.com/Thingscorp/decision-harness/blob/4b96b45452f007388cb6ad8b09a4fdab8e7889a0/bin/clef-decide) at the pinned commit. |

## When to use

- Gate agent steps with structured judge votes.
- Mix Jev with other System One models in a panel.
- Mismatch: provider-agnostic; Jev is optional.

## How it works

`bin/clef-decide` posts state files and question sets to SystemOne endpoints; the built-in `jev` judge is used for risk triage and adversarial second opinions alongside Clef and SubQ. Integration evidence: [`bin/clef-decide`](https://github.com/Thingscorp/decision-harness/blob/4b96b45452f007388cb6ad8b09a4fdab8e7889a0/bin/clef-decide).

## Get started

Clone, define judges in `~/.config/clef-decide/config`, and run `bin/clef-decide --state-file state.md --questions questions.json --judge jev`.

```sh
git clone https://github.com/Thingscorp/decision-harness.git && cd decision-harness
bin/clef-decide --state-file state.md --questions questions.json --judge jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Thingscorp/decision-harness/blob/4b96b45452f007388cb6ad8b09a4fdab8e7889a0/README.md](https://github.com/Thingscorp/decision-harness/blob/4b96b45452f007388cb6ad8b09a4fdab8e7889a0/README.md)

## Limits and data handling

State blobs go to whichever judge endpoints you configure.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 4b96b45452f0](https://github.com/Thingscorp/decision-harness/tree/4b96b45452f007388cb6ad8b09a4fdab8e7889a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
