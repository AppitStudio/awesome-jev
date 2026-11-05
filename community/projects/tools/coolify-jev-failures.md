# coolify-jev-failures (triage Coolify deploy failures with typed Jev questions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python service that reads Coolify failure context and asks Jev typed questions to triage what went wrong and what to try next, instead of dumping raw logs into a chat model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/coolify-jev-failures) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python app (MIT) |
| Requirements | Python 3, Coolify API access as configured upstream, and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/gbesse/coolify-jev-failures/blob/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/gbesse/coolify-jev-failures/blob/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d/jev.py) at the pinned commit. |

## When to use

- Classify recurring Coolify deploy failures into actionable buckets.
- Keep triage cheap with typed questions instead of long chat completions.
- Mismatch: Coolify-specific; needs your Coolify credentials as documented upstream.

## How it works

`jev.py` / `app.py` read `TYPESAFE_API_KEY` and post typed triage questions about failure payloads to TypeSafe Jev. Integration evidence: [`jev.py`](https://github.com/gbesse/coolify-jev-failures/blob/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
# follow README to point at your Coolify instance and run the triage service
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/coolify-jev-failures/blob/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d/README.md](https://github.com/gbesse/coolify-jev-failures/blob/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d/README.md)

## Limits and data handling

Failure logs and metadata you configure are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 579e5ef58c69](https://github.com/gbesse/coolify-jev-failures/tree/579e5ef58c697b56c95b8cba1ffcd01ce5a4b70d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
