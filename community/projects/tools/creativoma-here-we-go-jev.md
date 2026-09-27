# here-we-go-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local playground and test bench for Jev System One with mock and LLM baseline backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/creativoma/here-we-go-jev) |
| Maintainer | [creativoma](https://github.com/creativoma). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Bun/TypeScript web playground. |
| Requirements | Bun; optional `OPENROUTER_API_KEY` / `TYPESAFE_API_KEY` (mock works offline). |
| License | [MIT](https://github.com/creativoma/here-we-go-jev/blob/c14d9c01dcb4392b5097c46f0bbfa9aaeee72ce3/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to learn Jev question shapes and compare against an LLM baseline. Prefer official SDKs for app integration.

## How it works

Server proxies keep keys off the browser; UI inspects distributions and request payloads for Choice/Noul/Score. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/creativoma/here-we-go-jev.git
cd here-we-go-jev
git checkout c14d9c01dcb4392b5097c46f0bbfa9aaeee72ce3
bun install
bun run dev
```

Pin revision `c14d9c01dcb4392b5097c46f0bbfa9aaeee72ce3` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Dev playground, not a production SDK. Live backends not exercised on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit c14d9c0](https://github.com/creativoma/here-we-go-jev/tree/c14d9c01dcb4392b5097c46f0bbfa9aaeee72ce3). AI-assisted README and LICENSE inspection; install/live paths not executed.
