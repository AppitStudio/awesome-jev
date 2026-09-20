# Hx

[All projects](../README.md) · [Web apps](README.md#web-apps)

Clinical documentation aid: as a doctor types or dictates a note, Hx opens the checklist the note implies, ticks items against clauses copied from the text, and highlights what is still undocumented—without generating clinical prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doitrous/hx) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [https://hx.semicoded.com](https://hx.semicoded.com) (public demo; rate- and spend-limited) |
| Pricing and access | Source MIT; hosted demo requires no purchase but uses the operator's TypeSafe budget with per-IP/day caps. Self-host needs `TYPESAFE_API_KEY`. Accounts/Postgres optional. Checked 2026-09-21. |
| Jev evidence | [`server/jev.mjs`](https://github.com/doitrous/hx/blob/5adffd1798100b4e84bd1875a58a94475f6ed603/server/jev.mjs) posts typed questions to `https://api.typesafe.ai/v1/systemone`. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement or medical advice. Not a medical device. Source inspected; live clinical demo traffic and Postgres-backed suites were not fully run on the review host. |
| Maintainer | [doitrous](https://github.com/doitrous). Independently curated. |
| Format | Node/Express API + Vite/React web UI; Obsidian vault source for question bundles. |
| Platform and availability | Web (self-host or public demo). Release: public MIT repo with demo at hx.semicoded.com. |
| Jev's role | Typed yes/no, choice, and score judgments over note clauses to tick checklist items; never free-text generation. |
| Requirements | Node for server/web; `TYPESAFE_API_KEY`. Postgres for accounts/records when enabled. |
| License | [MIT](https://github.com/doitrous/hx/blob/5adffd1798100b4e84bd1875a58a94475f6ed603/LICENSE). |

## When to use

Use it when clinical notes should drive a documentation checklist with citeable clauses from the note itself. Do not treat checklist ticks as diagnosis or care decisions—the clinician remains responsible.

## How it works

Vault-defined question sets compile into server bundles. Analysis sends bounded note context through the Jev client; application code maps answers onto checklist state and UI. Patient names and MRNs are documented as never sent to the model. The public demo stores nothing by default.

## Get started

```sh
git clone https://github.com/doitrous/hx.git
cd hx
git checkout 5adffd1798100b4e84bd1875a58a94475f6ed603
export TYPESAFE_API_KEY=…   # required for live analyze; incurs TypeSafe charges
(cd server && npm ci --ignore-scripts && npm start)  # :4820
(cd web && npm ci && npm run dev)                    # :4830
# Or open the public demo: https://hx.semicoded.com
```

## Examples and demos

- Public demo: [hx.semicoded.com](https://hx.semicoded.com).
- Server unit tests (`cd server && npm test`) and live eval scripts under `server/eval/` (need a key).

## Limits and data handling

Not a medical device; does not diagnose or advise. Demo spend/rate limits apply. On the review host, **30** unit tests passed and **23** failed when Postgres-backed auth/demo/encounter hooks could not start (`AggregateError`)—treat account/persistence suites as requiring Docker Postgres. Live TypeSafe analyze was not run here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 5adffd1](https://github.com/doitrous/hx/tree/5adffd1798100b4e84bd1875a58a94475f6ed603): MIT. AI-assisted source review of README, `server/jev.mjs`, and privacy notes. Offline: partial server `npm test` as above. No live TypeSafe calls. X discovery: [post](https://x.com/omarelbasat/status/2101786937526739398)

Related: [JevEye](jeveye.md) (visual judgments), [Transcript Lens](transcript-lens.md).
