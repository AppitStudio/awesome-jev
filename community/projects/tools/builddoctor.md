# BuildDoctor by pikespeak (1950s-tabloid CI reports for public GitHub Actions, with Jev as the fact-checker)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hacksgiving 2026 agent on one Fly.io Sprite that examines a public GitHub Actions pipeline, names what costs time or keeps failing, and prints it as a 1950s tabloid with headlines and AI press photos. A council of models and code refutes weak findings and can propose a small workflow patch; Jev then fact-checks each published finding against the facts it cites and picks the front page, with no vote on what is printed. Try it at builddoctor.app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pikespeak/builddoctor-agent) |
| Maintainer | [pikespeak](https://github.com/pikespeak). Independently curated. |
| Format | Go agent + Elixir/Phoenix web app |
| Requirements | Go and Elixir (Postgres for tests); for your own deployment, GitHub, OpenAI and TypeSafe gateways. |
| License | [MIT](https://github.com/pikespeak/builddoctor-agent/blob/59f3fa2b91d739238048a08d4b0fc370ed7eba59/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agent/doctor/typesafe.go`](https://github.com/pikespeak/builddoctor-agent/blob/59f3fa2b91d739238048a08d4b0fc370ed7eba59/agent/doctor/typesafe.go) at the pinned commit. |

## When to use

- Maintainers who want a readable, entertaining look at where their CI wastes time.
- Mismatch: root-cause analysis; build logs are not read.

## How it works

`agent/doctor/typesafe.go` sends each finding and its cited facts as structured state with `choice` questions (supports / contradicts / says nothing; addresses the problem or not) to `jev-1.14.0` through the TypeSafe gateway; answers are shown under the finding. Integration evidence: [`agent/doctor/typesafe.go`](https://github.com/pikespeak/builddoctor-agent/blob/59f3fa2b91d739238048a08d4b0fc370ed7eba59/agent/doctor/typesafe.go).

## Get started

Try the hosted app, or run the test suites; the `ops/` scripts are written for the authors' own Sprite.

```sh
git clone https://github.com/pikespeak/builddoctor-agent && cd builddoctor-agent
(cd agent && go test ./...)
(cd app && mix deps.get && mix test)   # needs Postgres
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted app: [builddoctor.app](https://builddoctor.app)
- Film: [youtu.be/AMyisqY_Mkk](https://youtu.be/AMyisqY_Mkk)

## Limits and data handling

Only public repositories are read and their code is never run. Findings and cited facts go to TypeSafe; the fact-checker was tested on the authors' own cases.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 59f3fa2b91d7](https://github.com/pikespeak/builddoctor-agent/tree/59f3fa2b91d739238048a08d4b0fc370ed7eba59). Inspected the README, LICENSE and `agent/doctor/typesafe.go` at the pinned commit and confirmed builddoctor.app loads (HTTP 200); nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
