# jevry

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Go command-line tool for TypeSafe Jev: pipe text with `--question` to print the probability of yes, or send a full request JSON to print the raw response (defaults to `jev-latest`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeffrydegrande/jevry) |
| Maintainer | [jeffrydegrande](https://github.com/jeffrydegrande). Independently curated. |
| Format | Go CLI (`go install`) |
| Requirements | Go; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/jeffrydegrande/jevry/blob/3dafa4d8654b6dc2ca6ad723aa312a2ec77671a2/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Quick shell experiments and scripts.
- Mismatch: minimal; no batching or retries documented.

## How it works

See the upstream [README](https://github.com/jeffrydegrande/jevry/blob/3dafa4d8654b6dc2ca6ad723aa312a2ec77671a2/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
go install github.com/jeffrydegrande/jevry@latest
echo "Win a free iPhone now!!!" | jevry --question "Is this spam?"
```

## Limits and data handling

Input text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 3dafa4d8654b](https://github.com/jeffrydegrande/jevry/tree/3dafa4d8654b6dc2ca6ad723aa312a2ec77671a2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
