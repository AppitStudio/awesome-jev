# stalwart-jev (Stalwart mail spam classifier answered by Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small Go service that answers the Stalwart mail server's LLM spam classifier (SpamLlm) from Jev: one choice question over subject and body returns Unsolicited, Commercial, Harmful or Legitimate with a confidence and probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mikluko/stalwart-jev) |
| Maintainer | [mikluko](https://github.com/mikluko). Independently curated. |
| Format | Go service, Docker image and Helm chart |
| Requirements | Kubernetes with Helm (or the container image); Stalwart Enterprise (SpamLlm is an Enterprise feature); a TypeSafe API key. |
| License | [MIT](https://github.com/mikluko/stalwart-jev/blob/27d317132e5bdf1339a4dc74851e0682d1c5f8db/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`main.go`](https://github.com/mikluko/stalwart-jev/blob/27d317132e5bdf1339a4dc74851e0682d1c5f8db/main.go) at the pinned commit. |

## When to use

- Add a cheap, calibrated spam verdict to a self-hosted Stalwart server.
- Weigh LLM_<CATEGORY>_<CONFIDENCE> tags with your own SpamTag scores.
- Mismatch: without a Stalwart Enterprise license the classifier is never called.

## How it works

`main.go` serves `POST /v1/chat/completions` in the shape Stalwart calls, forwards the message to Jev through its `internal/jev` client as one Choice question, and replies `<Category>,<High|Medium|Low>,p=<probability>`. Integration evidence: [`main.go`](https://github.com/mikluko/stalwart-jev/blob/27d317132e5bdf1339a4dc74851e0682d1c5f8db/main.go).

## Get started

From the upstream README (not run on the review host):

```sh
helm install stalwart-jev oci://sarak.sh/mikluko/charts/stalwart-jev \
  --namespace mail --set apiKey=<TypeSafe API key>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Stalwart AiModel, SpamLlm and SpamTag setup in the README: [github.com/mikluko/stalwart-jev#readme](https://github.com/mikluko/stalwart-jev#readme)

## Limits and data handling

Each classified message's subject and body are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 27d317132e5b](https://github.com/mikluko/stalwart-jev/tree/27d317132e5bdf1339a4dc74851e0682d1c5f8db). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
