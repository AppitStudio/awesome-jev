# GoModel (Go AI gateway with a Jev provider and an OpenAI Decisions API endpoint that can be answered by Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Open-source AI gateway and proxy in Go with one OpenAI-compatible API in front of many providers. A `jev` provider (hosted TypeSafe System One or a self-hosted server) enables `POST /v1/decisions`, which answers OpenAI Decisions requests by translating them to and from System One, and `POST /v1/systemone`, which forwards System One requests natively so the TypeSafe SDK can point at the gateway. Pricing for Jev can be declared so the gateway costs decision requests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ENTERPILOT/GoModel) |
| Maintainer | [ENTERPILOT](https://github.com/ENTERPILOT). Independently curated. |
| Format | Go service (Docker image, install script and Helm chart) |
| Requirements | Docker or the install script; a `JEV_API_KEY` to turn on the Jev provider. |
| License | [MIT](https://github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/providers/jev/jev.go`](https://github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/internal/providers/jev/jev.go) at the pinned commit. |

## When to use

- Put Jev behind a shared gateway with usage tracking and use OpenAI-style Decisions clients or the TypeSafe SDK against it.
- Mismatch: Jev is one provider among many, and images only work on hosted Jev.

## How it works

`internal/providers/jev/jev.go` and `decisions.go` forward System One requests to `https://api.typesafe.ai` (or another base URL) with your key and translate Decisions API requests and answers both ways. Integration evidence: [`internal/providers/jev/jev.go`](https://github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/internal/providers/jev/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
docker run --rm -p 8080:8080 -v gomodel_data:/app/data enterpilot/gomodel
# configure a provider of `type: jev` with api_key: ${JEV_API_KEY}, then call POST /v1/decisions or /v1/systemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with install and providers: [github.com/ENTERPILOT/GoModel#readme](https://github.com/ENTERPILOT/GoModel#readme)
- Decisions API guide: [github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/docs/advanced/decisions-api.mdx](https://github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/docs/advanced/decisions-api.mdx)
- Example Jev provider config: [github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/config/config.example.yaml](https://github.com/ENTERPILOT/GoModel/blob/c4bc4a4a703274ff63e0b51bc908150eaf73a974/config/config.example.yaml)

## Limits and data handling

Requests passing through the gateway reach TypeSafe (or the other provider you configure) on your key and are billed there; GoModel's own data handling and dashboard were not reviewed. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit c4bc4a4a7032](https://github.com/ENTERPILOT/GoModel/tree/c4bc4a4a703274ff63e0b51bc908150eaf73a974). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
