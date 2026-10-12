# corp-jev-skill

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill (`/corp-jev`) that runs a multi-department review corporation (builders, claim audit, hostile panel, integrator, verification) over one deliverable, adding TypeSafe Jev second opinions through OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bandersong/corp-jev-skill) |
| Maintainer | [bandersong](https://github.com/bandersong). Independently curated. |
| Format | Python · Claude Code skill |
| Requirements | Claude Code; OpenRouter key for Jev. |
| License | [MIT](https://github.com/bandersong/corp-jev-skill/blob/916ae06364869507b45564832e104e8bb1abf4c4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Stress-test a deliverable with adversarial review plus a fast Jev opinion.
- Mismatch: Heavier than plain `/corp`; needs API keys.

## How it works

Department scripts call `scripts/jev` for typed second opinions during the loop. Evidence: [`scripts/jev`](https://github.com/bandersong/corp-jev-skill/blob/916ae06364869507b45564832e104e8bb1abf4c4/scripts/jev).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bandersong/corp-jev-skill.git
# install skill per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 916ae0636486](https://github.com/bandersong/corp-jev-skill/tree/916ae06364869507b45564832e104e8bb1abf4c4). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
