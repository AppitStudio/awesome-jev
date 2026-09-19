# App tags and disclosures

[App directory](projects/apps/README.md) · [Submit an app](../CONTRIBUTING.md#list-a-jev-powered-app)

Every app page has a `Tags` row in its at-a-glance table. Write each tag as inline code, separated by `·`, and repeat the same tags beside the app in the directory and root README. In the app directory, follow the existing format: a platform heading, an app subheading, tags before the full-guide link, and product/access details. Source access and pricing are separate: an open-source app can also be a commercial product.

## Source access

Choose exactly one tag:

| Tag | Meaning and evidence |
| --- | --- |
| `Open source` | Public source with an open-source license. Link the license; a public repository alone is insufficient. |
| `Source available` | Publicly readable source with restricted or non-open-source terms. Link and summarize those terms. |
| `Closed source` | Implementation is not publicly available. Link the product homepage and public evidence of Jev use. |
| `Source unverified` | Source access or licensing could not be established. State the gap; do not imply an open-source license. |

## Pricing and commercial access

Choose exactly one pricing tag for the primary access path described in the listing:

| Tag | Meaning |
| --- | --- |
| `Free` | The described app access is verified as free. Separate paid features and provider costs must still be stated. |
| `Free source build` | The described source build has no app purchase fee. Build requirements, hosting, and inference costs remain separate. |
| `Freemium` | A continuing free tier and paid tiers/features are documented. A temporary trial alone is not a free tier. |
| `Paid` | The described product access requires payment, including products with an introductory trial. |
| `Pricing unverified` | Price or access terms could not be established. This must be shown to readers, not treated as free. |

Add **`Commercial`** for a paid offering, including freemium products and paid hosted versions of open-source apps. `Paid` and `Freemium` always require this tag. `Commercial` does not mean closed-source or paid placement. Link the official pricing page, or a vendor contact/access page if prices are quote-based. Note the date checked; do not copy an unverified price.

Add **`BYOK`** when the described setup requires users to supply their own provider API keys. State inference and hosting charges separately; `BYOK` and a free source license do not establish free operation.

## Required product details

App pages include these at-a-glance rows:

- **Tags:** one source tag, one pricing tag, and `Commercial` / `BYOK` where applicable.
- **Product homepage:** a canonical HTTPS product page; a project's own README can serve for a source-built app without a separate website.
- **Pricing and access:** official pricing/access link, account and trial/free-tier restrictions, separately charged services, and dated verification or an explicit unknown.
- **Jev evidence:** a link to inspected integration code, technical documentation, or a reproducible public demo. Identify vendor claims separately from independently observed behavior.
- **Disclosure:** commercial status, source-review limits, and affiliation. A listing is not an endorsement or a purchase recommendation.

Keep the existing **Source** link as the canonical artifact used in the root README. For a closed-source product, its product homepage is a valid Source; no public repository is required. Put licensing or access terms in the **License** row.

## Closed-source and commercial disclosure

For a closed-source app, explicitly say that its implementation could not be inspected, identify the evidence supporting its Jev integration, and distinguish vendor-reported capabilities from any hands-on checks. For example: “Closed source. The implementation was not inspected; Jev use is documented by the vendor in the linked integration notes. No live workflow was tested.” Adjust that wording to the actual evidence.

For a commercial app, state the paid access near the recommendation or listing, link pricing, and disclose any relationship to the vendor. For example: “Commercial product with paid hosted plans; a trial may be available. Check current pricing. This listing is not an endorsement.” If the app is also closed-source, include both disclosures. Makers may submit their own products; referral links and paid placement are not accepted.

## How the guide recommends apps

The guide skill must show the selected app's tags and cost/access information with the recommendation. A paid option must be labeled **Commercial · Paid** or **Commercial · Freemium**, linked to the product homepage, pricing, and full guide. Closed-source options must also carry **Closed source** and a short source-review limitation. Show **Pricing unverified** when applicable.

Respect requests for free-only, open-source-only, local-only, or no-account solutions. If no listed app meets the constraints, explain the gap rather than quietly suggesting a paid or closed-source product. Do not equate open source with free hosted access, or a free trial with a free tier.
