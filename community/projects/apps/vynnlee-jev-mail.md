# jev-mail (vynnlee)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Config-driven Gmail triage tool aiming at 24/7 zero-inbox automation: TypeSafe Jev System One judges how to label/archive/route mail under local policy, distinct from other Jev mail classifiers in the catalog.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vynnlee/jev-mail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [GitHub README](https://github.com/vynnlee/jev-mail) |
| Pricing and access | No app purchase fee for the MIT source. Gmail OAuth and TypeSafe usage are separate (BYOK). Checked 2026-09-24. |
| Jev evidence | [README](https://github.com/vynnlee/jev-mail/blob/61e346f9034161e4cb7ddf04907326841e01300b/README.md) and [jev-mail.example.yaml](https://github.com/vynnlee/jev-mail/blob/61e346f9034161e4cb7ddf04907326841e01300b/jev-mail.example.yaml) describe TypeSafe Jev System One triage under local policy. |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Live Gmail/Jev not run. Distinct from [Jevmail](jevmail.md), [Jev for Gmail](jev-for-gmail.md), and [Inbox Triage](inbox-triage.md). |
| Maintainer | [vynnlee](https://github.com/vynnlee). Independently curated. |
| Format | Application |
| Platform and availability | Source-built Node/TypeScript worker/CLI (see package.json). Not a Chrome Web Store extension. |
| Jev's role | Jev makes typed triage decisions (priority/label/archive-style judgments per config); application code applies Gmail API actions. |
| Requirements | Node.js; Gmail API OAuth; TypeSafe API key; YAML config. |
| License | [MIT](https://github.com/vynnlee/jev-mail/blob/61e346f9034161e4cb7ddf04907326841e01300b/LICENSE). |

## When to use

Use for **automated** Gmail triage with Jev judgments. Prefer [Jev for Gmail](jev-for-gmail.md) for in-browser badges without label writes.

## How it works

Config defines policies; runtime fetches messages, asks Jev, then executes Gmail mutations allowed by policy (per upstream docs).

## Get started

```sh
git clone https://github.com/vynnlee/jev-mail.git
cd jev-mail
git checkout 61e346f9034161e4cb7ddf04907326841e01300b
cp jev-mail.example.yaml jev-mail.yaml
# follow README for OAuth + TYPESAFE_API_KEY; run package scripts
```

## Examples and demos

- `examples/` and bilingual README.ko.md.
- `docs/` setup notes.

## Limits and data handling

Email metadata/bodies may reach TypeSafe. Misconfigured policies can archive or label incorrectly—start narrow.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 61e346f](https://github.com/vynnlee/jev-mail/tree/61e346f9034161e4cb7ddf04907326841e01300b). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [Jevmail](jevmail.md), [Jev for Gmail](jev-for-gmail.md), [Inbox Triage](inbox-triage.md).
