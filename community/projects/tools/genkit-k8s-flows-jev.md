# Genkit flows on Kubernetes routed by Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go example where each step of a support-ticket pipeline is a Genkit flow running as a Kubernetes pod through senro; Jev decides department, urgency and escalation through Genkit's System One plugin and then reviews Gemini's draft reply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xavidop/genkit-k8s-flows-jev) |
| Maintainer | [xavidop](https://github.com/xavidop). Independently curated. |
| Format | Example project (Go, Genkit, kind) |
| Requirements | Go 1.27+, Docker, kind, kubectl; `GEMINI_API_KEY` and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/xavidop/genkit-k8s-flows-jev/blob/017fa5add004b4dd4dff0128a435dbb5f9720af9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`flows.go`](https://github.com/xavidop/genkit-k8s-flows-jev/blob/017fa5add004b4dd4dff0128a435dbb5f9720af9/flows.go) at the pinned commit. |

## When to use

- See how Genkit's System One plugin routes a multi-step workflow.
- Use Jev as a guardrail that fails a step when a draft breaks the playbook.
- Mismatch: a companion demo for an article, not a library.

## How it works

Run one triages the ticket: Gemini extracts it and Jev (`typesafe/jev-latest`, see `flows.go`) returns the verdict, which becomes run parameters for run two, where only the chosen branch runs and Jev verifies the draft before send. Integration evidence: [`flows.go`](https://github.com/xavidop/genkit-k8s-flows-jev/blob/017fa5add004b4dd4dff0128a435dbb5f9720af9/flows.go).

## Get started

From the upstream README (not run on the review host):

```sh
scripts/cluster-up.sh
source scripts/cluster-env.sh
go run . -ticket tickets/double-charge.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Wiring diagram in the README: [github.com/xavidop/genkit-k8s-flows-jev#readme](https://github.com/xavidop/genkit-k8s-flows-jev#readme)

## Limits and data handling

Ticket text goes to Google (Gemini) and TypeSafe (Jev). Sample tickets only.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 017fa5add004](https://github.com/xavidop/genkit-k8s-flows-jev/tree/017fa5add004b4dd4dff0128a435dbb5f9720af9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
