# Separ8 (AETHER's early-access web app that sorts every row of a CSV with Jev, then measures how far its confidence can be trusted)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Upload a CSV of up to 500 rows, describe a decision in plain English (route a ticket, flag a refund request, score a lead), and Separ8 drafts typed questions that run on every row in parallel on Jev. You mark 20 to 50 rows by hand and it measures how often the model agreed with you at each confidence level, then proposes the line above which rows can be handled automatically and below which a person looks. A free demo with sample data is on the site; self-serve and done-for-you setups are in early access.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://separ8.8ther.io/) |
| Tags | `Closed source` · `Pricing unverified` |
| Product homepage | [separ8.8ther.io](https://separ8.8ther.io/) |
| Pricing and access | The demo with sample data is free and accepts your own CSV of up to 500 rows. The site says pricing for the self-serve app and for the done-for-you setups "will be shared with the waitlist first", so no price is published; access to the full product is by early-access waitlist. Checked **2026-11-05**. |
| Jev evidence | The [launch post](https://separ8.8ther.io/blog/introducing-separ8/) (2026-11-03) and the homepage say every question runs on Jev, and the post reports demo timings and model costs on three self-written datasets. Implementation was **not** inspected (no public source) and TypeSafe API traffic was **not** captured on the review host. |
| Disclosure | Closed source. Jev use is a claim from the vendor's site and post, not independently observed System One calls. AI-assisted catalog review; no affiliation with AETHER. Listing is not an endorsement. Discovered via X ([post](https://x.com/Aether_Studi0/status/2117874229186003050)). |
| Maintainer | AETHER, the publisher of [separ8.8ther.io](https://separ8.8ther.io/); X [@Aether_Studi0](https://x.com/Aether_Studi0) (creator link not verified). Independently curated. |
| Format | Hosted web application (CSV in, per-row answers and a trust check out). |
| Platform and availability | Web browser; live connections to inboxes, helpdesks or CRMs are only part of the done-for-you setup. HTTP 200 on review. |
| Jev's role | Vendor claim: Jev answers the plain-English questions about each row with probabilities; code measures agreement with your own labels and sets the automation threshold. |
| Requirements | A modern browser and a CSV; for the trust check, 20 to 50 rows you label yourself. |
| License | Proprietary hosted product; no public repository. |

## When to use

- Sort a pile of tickets, leads, reviews or applications by questions you define, and see how far the confidence numbers can be trusted on your own data before automating.
- Mismatch: the product is in early access, pricing is unpublished, and for hiring the vendor says it should flag and people should decide.

## How it works

Per the vendor's site and launch post: you describe the decision, Separ8 drafts the questions and their answer choices (including a way out for rows that fit nothing), and each question runs on each row in parallel on Jev. You label 20 to 50 rows; Separ8 measures agreement at each confidence level and recommends a cut-off for your accuracy target. Question schemas and thresholds were not inspected.

## Get started

1. Open [separ8.8ther.io](https://separ8.8ther.io/), pick a sample dataset or upload your own CSV (up to 500 rows in the demo) and describe the decision.
2. Edit the drafted questions, run the sort, then mark 20 to 50 rows to see the trust line.
3. For recurring decisions or live connections, join the early-access waitlist on the site.

## Examples and demos

- Live demo with sample data: [separ8.8ther.io](https://separ8.8ther.io/)
- Launch post (two-minute walkthrough linked from the site): [Introducing Separ8](https://separ8.8ther.io/blog/introducing-separ8/)
- X announcement: [x.com/Aether_Studi0/status/2117874229186003050](https://x.com/Aether_Studi0/status/2117874229186003050)

## Limits and data handling

The site says uploaded rows are sent to the decision model for sorting and results return to your browser, and that Separ8 itself does not save them; done-for-you setups are scoped in writing. The launch post's timings, costs and accuracy figures come from three fictional datasets the vendor wrote and a 20-email trust check, so they are not independent results; the post also advises removing names and personal details first.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia). Primary sources: the live homepage and launch post (HTTP 200) and the announcement on X. AI-assisted curation; no account, key or paid feature was used and the demo was not run. De-dupe: no existing Awesome Jev listing for separ8.8ther.io.

**X attribution:** `https://x.com/Aether_Studi0/status/2117874229186003050`
