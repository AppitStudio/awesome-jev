# Pi Jev Gate (permission gate for Pi that blocks dangerous actions and asks Jev about consequential calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that lets routine work through locally, blocks obvious catastrophes by rule, and asks Jev as a second-stage judge about recognized consequential tool calls; only those flagged calls fail closed when Jev cannot answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dys-org/pi-jev-gate) |
| Maintainer | [dys-org](https://github.com/dys-org). Independently curated. |
| Format | Pi extension installed from a GitHub release (TypeScript, MIT) |
| Requirements | Pi 0.99.0 or newer and a key for the chosen Jev provider: TypeSafe (`TYPESAFE_API_KEY`, the default), OpenRouter or Vercel AI Gateway. |
| License | [MIT](https://github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/src/jev.ts) at the pinned commit. |

## When to use

- Keep a Pi agent from running destructive commands without blocking ordinary development.
- Get a second opinion from Jev only on calls a rule marks as consequential.
- Mismatch: Pi only; the policy thresholds have not been live-validated yet.

## How it works

`src/jev.ts` resolves the classifier through Pi's native model registry (`jev-latest` on TypeSafe, `typesafe/jev-1.13` on OpenRouter, `typesafe-ai/jev` on Vercel AI Gateway) and only accepts a `typesafe-system-one` classifier; the extension owns the policy and the final allow/block decision. The author notes the consequence-first policy is not yet live-validated. Integration evidence: [`src/jev.ts`](https://github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/src/jev.ts).

## Get started

Install the pinned release in Pi (or try it for one run with `pi -e`) and set the key for the default TypeSafe provider; `/jev-gate provider` switches providers.

```sh
pi install git:github.com/dys-org/pi-jev-gate@v0.2.0
export TYPESAFE_API_KEY="your-key"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/README.md](https://github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/README.md)
- Offline eval cases: [github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/eval/consequence-first.offline.jsonl](https://github.com/dys-org/pi-jev-gate/blob/7a177a17f8a83c69165f2b0e4568b5d005004a6f/eval/consequence-first.offline.jsonl)

## Limits and data handling

Details of flagged tool calls are sent to the chosen Jev provider on your key; routine calls are decided locally.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 7a177a17f8a8](https://github.com/dys-org/pi-jev-gate/tree/7a177a17f8a83c69165f2b0e4568b5d005004a6f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
