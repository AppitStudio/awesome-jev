# jev_naics

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Classifies a business's description of operations into one of the 1,012 NAICS 2022 industries for insurance applications, or holds it for a person; code builds the shortlist and Jev makes the single pick.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmurray10/jev_naics) |
| Maintainer | [jmurray10](https://github.com/jmurray10). Independently curated. |
| Format | Python backend + web frontend (Docker Compose, Postgres) |
| Requirements | Docker and git; a `NAICS_API_KEYS` service key in `.env` (the API will not start without one); TypeSafe API key in the same `.env` for live picks (recorded replay runs without one). |
| License | [MIT](https://github.com/jmurray10/jev_naics/blob/b6abd36793cf55f45537924854645af5408797f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/jmurray10_/status/2110584887942246585)). |
| Jev evidence | [`backend/src/jev_naics/search_pick.py`](https://github.com/jmurray10/jev_naics/blob/b6abd36793cf55f45537924854645af5408797f5/backend/src/jev_naics/search_pick.py) at the pinned commit. |

## When to use

- Assign NAICS codes while a broker types a description, with an explicit hold when the answer is not clear.
- Study a design where code owns search, gates and holds, and the decision model only chooses among real candidate codes.
- Mismatch: accuracy figures (blind-set counts) are the author's own and were not reproduced here.

## How it works

Postgres full-text search over the official Census text, spelling correction and a walk down the NAICS tree build a short list of real industries; Jev answers a choice question over that list with probabilities. Code owns every gate and the hold action, so Jev cannot invent a code or skip the review path. Integration evidence: [`backend/src/jev_naics/search_pick.py`](https://github.com/jmurray10/jev_naics/blob/b6abd36793cf55f45537924854645af5408797f5/backend/src/jev_naics/search_pick.py).

## Get started

From the upstream README (not run on the review host). The API refuses to start without a service key in a git-ignored `.env`, so create it before bringing the stack up:

```sh
git clone https://github.com/jmurray10/jev_naics.git && cd jev_naics
python3 -c "import secrets; print('NAICS_API_KEYS=' + secrets.token_urlsafe(32))" > .env
docker compose up -d --build
```

The second line writes one `NAICS_API_KEYS` service key (callers send it as `Authorization: Bearer <key>`; Compose forwards `.env` to the API). To classify your own text live, add `TYPESAFE_API_KEY=<your key>` to the same `.env` and never commit it; without it the stack replays recorded answers. Then open the classifier page at `http://127.0.0.1:8097` (API docs at `http://127.0.0.1:8095/docs`) and stop it with `docker compose down`.

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: PEAS.md, DESIGN.md and CALIBRATION.md in the repository.
- Author's demo post on X (linked in the disclosure row).

## Limits and data handling

Business descriptions are sent to TypeSafe for the pick and billed to your key; the service and its Postgres database run on your own host.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b6abd36793cf](https://github.com/jmurray10/jev_naics/tree/b6abd36793cf55f45537924854645af5408797f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Get-started steps re-checked against the upstream README on **2026-10-16** at the same commit (added the required `.env` service-key step). Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
