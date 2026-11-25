# pg_prompt_jev by Jose Mejias (PostgreSQL extension that returns typed Jev decisions as jsonb from SQL)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PostgreSQL extension (`pg_prompt_jev`) with a MotherDuck-style `prompt_jev()` function: evaluate row text with Jev and get a probability, choice, score or several answers back as `jsonb`. Supports TypeSafe, Vercel AI Gateway and Cloudflare AI Gateway. Distinct from the separately listed realZachi/pg-jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mejiasd3v/pg-jev) |
| Maintainer | [Jose Mejias](https://github.com/mejiasd3v). Independently curated. |
| Format | PostgreSQL extension (PL/Python) |
| Requirements | PostgreSQL 14 to 18 with `plpython3u`, outbound HTTPS, and a TypeSafe, Vercel or Cloudflare key. |
| License | [MIT](https://github.com/mejiasd3v/pg-jev/blob/8dcf052f3ebf4280b986948b2dfb9043e3cff087/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/pg_prompt_jev.py`](https://github.com/mejiasd3v/pg-jev/blob/8dcf052f3ebf4280b986948b2dfb9043e3cff087/src/pg_prompt_jev.py) at the pinned commit. |

## When to use

- Classify or score rows with Jev directly from SQL.
- Mismatch: on managed Postgres that does not allow `plpython3u`.

## How it works

`src/pg_prompt_jev.py` builds System One requests for `https://api.typesafe.ai` (default model `jev-latest`) or the Vercel and Cloudflare gateways, restricted by `PROMPT_JEV_ALLOWED_PROVIDERS`. Integration evidence: [`src/pg_prompt_jev.py`](https://github.com/mejiasd3v/pg-jev/blob/8dcf052f3ebf4280b986948b2dfb9043e3cff087/src/pg_prompt_jev.py).

## Get started

Build and install the extension, then create it in your database.

```sh
make
sudo make install
# in psql:
CREATE EXTENSION plpython3u;
CREATE EXTENSION pg_prompt_jev;
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark harness: [github.com/mejiasd3v/pg-jev/tree/8dcf052f3ebf4280b986948b2dfb9043e3cff087/bench](https://github.com/mejiasd3v/pg-jev/tree/8dcf052f3ebf4280b986948b2dfb9043e3cff087/bench)

## Limits and data handling

Row text leaves the database for TypeSafe or the selected gateway (Vercel and Cloudflare are third-party hosts), and each call is billed. Public execution is revoked by default; grant it deliberately. Do not persist keys with `ALTER SYSTEM`.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 8dcf052f3ebf](https://github.com/mejiasd3v/pg-jev/tree/8dcf052f3ebf4280b986948b2dfb9043e3cff087). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
