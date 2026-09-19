# Community project page template

Use this for an external application, starter kit, tool, or integration. Copy the Markdown inside the block into `community/projects/apps/your-app-slug.md` or `community/projects/tools/your-tool-slug.md`, replace every placeholder, and remove instructions that do not belong in the final page. Follow [the contribution rules](../CONTRIBUTING.md#add-a-community-project).

Keep the page useful on its own: explain the fit, show a real starting path, and link to actual examples. Summarize in your own words rather than copying the upstream README. Missing demos or live validation should be stated honestly, not invented. Closed-source or paid resources can use their canonical product page as the Source and describe their access terms.

For an app, follow [List a Jev-powered app](../CONTRIBUTING.md#list-a-jev-powered-app) and [app tags and disclosures](APP_TAGS.md), choose a platform category in the [app directory](projects/apps/README.md), and keep all app-specific rows below. Identify source-build requirements, account or paid access, release stage, and other models without implying Jev powers the entire product. For developer resources, use a category in the [tools directory](projects/tools/README.md) and adapt or omit app-specific rows.

````markdown
# Project name

[All projects](../README.md) · [Existing category](README.md#category-anchor)

One sentence describing the problem this project solves and who it helps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://example.com) |
| Tags | One source-access tag · one pricing tag · Commercial and/or BYOK if applicable. |
| Product homepage | [Product homepage](https://example.com) — product information or a source-built app's project homepage. |
| Pricing and access | Official pricing/access link, accounts, trial/free-tier limits, API/hosting costs, and date checked or an explicit unknown. |
| Jev evidence | Link to inspected integration code, public technical documentation, or reproducible demo; distinguish vendor claims from verified behavior. |
| Disclosure | Paid/commercial status, source-review limits, affiliation, and no endorsement. For closed source, explicitly state that implementation was not inspected. |
| Maintainer | Name, upstream link, and contributor affiliation/commercial relationship. |
| Format | Application, starter kit, library, CLI, MCP server, or another accurate type. |
| Platform and availability | Supported platforms, release stage, launch/download/source-build link, free/paid access or pricing link, and unverified access limits. |
| Jev's role | Concrete feature/decisions, integration evidence link, other models involved, and whether Jev use is optional. |
| Requirements | Language/runtime, dependencies, accounts, and key-variable names. |
| License | Link to the license, or clearly describe access/commercial terms. |

## When to use

Describe two or three concrete workflows and any important mismatch.

## How it works

Explain what Jev judges and what application code does. Link to relevant source
or architecture documentation. Do not imply capabilities beyond the actual artifact.

## Get started

Give the shortest real setup path, with the working directory and prerequisites.
Label an offline demo, dry run, integration fragment, or live command accurately.
Describe the expected result. State any charges and data transfer before a live step.
Link to upstream instructions for version-sensitive or longer setup.

## Examples and demos

Link to actual runnable samples, fixtures, tutorials, screenshots, or demos.
Explain what each demonstrates and whether it needs live credentials.
If no separate demo exists, say so and link to a verified usage example instead.

## Limits and data handling

Describe uncertainty/fallback behavior, known gaps, input data sent elsewhere,
local storage, and relevant usage costs. Avoid unsupported quality claims.

## Review and maintenance

State the review date and exact upstream commit/version with a link.
Separate your own inspection/execution from submitter or upstream reports.
Name commands/checks and results, and say which installation/live/quality paths
were not checked. Link to the submission or catalog validation when available.

Related: link to relevant local examples or other project pages when useful.
````

Use one canonical HTTPS link labeled `Source`; the directory check matches it to the existing README entry. For a closed-source app, this can be the product homepage. Put the page under one primary category in its own apps/tools index and link back to that category. Repeat app tags in the index and root README. Related links can connect it to other use cases without duplicating the index entry.

For a complete example, read [Testimonial miner](projects/tools/testimonial-miner.md). Keep research drafts, source clones, raw evaluations, private data, and credentials outside this public repository.
