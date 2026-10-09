# jev-inbox-triage

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Store-inbox triage where TypeSafe Jev answers eight parallel questions per email (topic, urgency, sentiment and more) and rules route it to one of four lanes with every decision logged; the author reports 19/20 test emails in the right lane and no risky email automated.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pentasir/jev-inbox-triage) |
| Maintainer | [pentasir](https://github.com/pentasir). Independently curated. |
| Format | Email triage workflow |
| Requirements | TypeSafe API key; an inbox to connect (see README). |
| License | [MIT](https://github.com/pentasir/jev-inbox-triage/blob/b9cc141803c3782400cb2fd241abdfdad67d66a8/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Small e-commerce support inbox routing.
- Mismatch: author-reported small test set.

## How it works

See the upstream [README](https://github.com/pentasir/jev-inbox-triage/blob/b9cc141803c3782400cb2fd241abdfdad67d66a8/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/pentasir/jev-inbox-triage.git
```

## Limits and data handling

Email content goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit b9cc141803c3](https://github.com/pentasir/jev-inbox-triage/tree/b9cc141803c3782400cb2fd241abdfdad67d66a8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
