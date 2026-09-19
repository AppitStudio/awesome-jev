# Contributing

Help readers find resources that make working with Jev easier. A useful correction or a small, well-understood addition matters more than the size of the list.

## Use the contributor skill

The [Awesome Jev contributor skill](skills/awesome-jev-contributor/SKILL.md) helps a coding agent review your app, developer project, or starter kit, identify gaps, and prepare its project page, category listing, README entry, and proposal with verification evidence. It supports both external project listings and code contributed here. These contribution rules remain the source of truth; the skill does not guarantee acceptance.

Install it from your project directory with the [Skills CLI](https://github.com/vercel-labs/skills), then select your agent:

```sh
npx skills add AppitStudio/awesome-jev --skill awesome-jev-contributor
```

For Codex specifically, add `--agent codex`; add `--global` if you want it available across projects. You can also give an agent the linked `SKILL.md` directly without installing it.

Example requests:

- “Use awesome-jev-contributor to prepare a directory listing for my Jev-powered app: APP_URL. Explain what Jev powers, platforms, and access requirements.”
- “Use awesome-jev-contributor to check this Jev starter kit for submission readiness: PROJECT_URL.”
- “Use awesome-jev-contributor to review my project and prepare its project page, category listing, README entry, and PR text. Keep the proposal local.”
- “Use awesome-jev-contributor to submit my project to Awesome Jev. I maintain it; review the source and tests and disclose the AI assistance.”

A review or preparation request produces local artifacts. An explicit submission request allows the agent to open the scoped issue or PR once ready. The contributor remains responsible for reviewing the proposal, and maintainers decide whether to accept it.

## Suggest a resource

Open a resource suggestion or send a pull request for one resource at a time. Search existing entries and open proposals first. Self-submissions are welcome; disclose your involvement and any commercial relationship.

An entry should:

- Have a publicly reachable, working artifact with a clear Jev-specific use.
- Explain what it does, how to use it, and any account, payment, license, or environment requirements.
- Match the current API, or identify the version it supports and its limitations.
- Add a distinct benefit rather than duplicate an existing resource.
- Include evidence of inspection or execution. Explain what was checked, by whom or with which tools, without overstating the review.

We do not require a star count, popularity ranking, or minimum project age. We do not accept paid placement, referral links, tracking URLs, placeholders, unsupported performance claims, or generic AI material without a concrete Jev connection. Closed-source or paid resources can qualify when their access requirements and benefit are clear.

Use the canonical HTTPS URL and one concise, factual sentence:

```markdown
- [Resource name](https://example.com/resource) - Classifies support requests with Jev and documents a review fallback.
```

Choose the closest existing category. Keep resources alphabetized within that category unless the section explicitly describes a learning sequence. Use objective descriptions rather than words such as “best,” “revolutionary,” or “production-ready.” Identify official TypeSafe resources separately from community resources. Do not add empty categories for future links.

## Add a community project

External applications, starter kits, libraries, and tools get a browsable page in this repository while their code stays upstream. A project PR includes all three:

1. **A detail page** at `community/projects/apps/<project-slug>.md` for an app or `community/projects/tools/<project-slug>.md` for a developer resource, based on the [project-page template](community/PROJECT_TEMPLATE.md). Explain when to use it, how it works, prerequisites and key setup, the shortest real usage path, examples/demo links, limitations/data flow, license, affiliation, and dated verification evidence.
2. **An index entry** under one primary category in the matching [app directory](community/projects/apps/README.md) or [tools directory](community/projects/tools/README.md), linking to the full page. Apps include tags, Jev's role, platform, and access requirements; developer resources use the closest workflow category and describe their use and stack. Prefer an existing category; create a new one only when the submitted project needs it. Alphabetize projects within a category.
3. **The existing README entry** under Community projects, keeping its canonical upstream HTTPS link and concise description, plus a `Project guide` link to the new page.

The page must have one canonical HTTPS link labeled `Source` matching that README entry and a link back to its category. `npm run check:community` catches missing pages, missing/duplicate index entries, mismatched sources, and disconnected README entries. These checks verify navigation, not the truth of a project's claims.

Use real examples and accurate commands. A dry run can still read an external service; mocked components do not make every part of a demo offline. Explain what requires an account, where data goes, and which tests you ran versus results reported by someone else. If a separate demo is unavailable, say so and provide the best verified usage link. See [Testimonial miner](community/projects/tools/testimonial-miner.md) for a complete page.

Update the guide skill's resource map only when a new workflow needs specific routing guidance, using the project's local guide as its entry point. A change to `solutions.md` alone is not a project submission. Documentation articles and individual cookbooks can remain ordinary resource links without a project page.

For an issue suggestion, supply the same information in the form; the accepted project needs its page and both listings before the catalog change is merged. Updates and removals should keep these three locations consistent.

### List a Jev-powered app

The [app directory](community/projects/apps/README.md) welcomes applications people can use for a real task: desktop and mobile apps, web products, and hosted services. Makers can promote their own work through a factual, reviewed listing. An app may be open-source or closed-source, free or paid, hosted or built from source. An early release can qualify if a working artifact is available and its stage is stated clearly; a waitlist or announcement alone is not enough.

Jev must power a concrete user-facing feature or decision. It can be one part of a larger system; using Gemini or another model alongside it is fine. Name the feature, explain what Jev decides, identify what other components do, and link evidence such as implementation code, technical documentation, or a reproducible demonstration. A badge or unsupported claim that an app uses Jev is not sufficient. For closed-source products, record what the public evidence establishes and what could not be inspected.

Use the same three-part submission above, keeping the detail page in `community/projects/apps/<slug>.md`. Add these details to the page:

- **Product and availability:** what users can do, supported platforms, release stage, and a working launch, download, or source-build link. Label source-only access and beta restrictions explicitly.
- **Access and costs:** account requirements, free/paid access or a pricing link, bring-your-own-key requirements, and any separate inference or hosting charges. Do not describe free source code as free hosted inference; mark unverified pricing or access limits honestly.
- **Jev's role and evidence:** the actual feature, integration evidence, supported model/API when known, other models involved, and any optional or disabled-by-default Jev mode.
- **Practical use:** the shortest setup/use path, an example or demo if available, permissions, data recipients, limitations, dated review evidence, and affiliation.

Apply the [app tags and disclosure rules](community/APP_TAGS.md). Source access and pricing are independent: choose one source tag (`Open source`, `Source available`, `Closed source`, or `Source unverified`) and one pricing tag (`Free`, `Free source build`, `Freemium`, `Paid`, or `Pricing unverified`). Add `Commercial` for paid offerings and `BYOK` where required. Repeat the tags in the app directory and root README; include the required product-homepage, pricing/access, Jev-evidence, and disclosure rows in the full page.

**Closed-source commercial apps are welcome.** Use the product homepage as the canonical Source when there is no public repository. Link the official pricing or sales/access page and public evidence of Jev integration. Explicitly disclose that the implementation could not be inspected, distinguish vendor claims from verified behavior, and state paid access, restrictions, and affiliation. No source-code disclosure or purchase is required for submission, but a product description alone does not verify Jev use. Unknown pricing stays labeled `Pricing unverified`.

In the root README, list apps under **Community projects → Apps powered by Jev** and developer resources under **Developer projects and integrations**. Keep one primary category entry per project. A library, SDK, starter kit, or integration recipe belongs in `community/projects/tools/`; a small demo UI alone does not turn it into an end-user app. Root `projects/` holds reference code maintained in this repository; the [external project directory](community/projects/README.md) separates app and tool listings.

[Open an app/resource suggestion](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) or prepare a PR using the [page template](community/PROJECT_TEMPLATE.md). Self-submissions require an affiliation disclosure; paid placement and tracking/referral links remain excluded. Maintainers review all listings, and inclusion is not endorsement.

## Add an example

Original examples live in [examples](examples/README.md). Keep them small enough to understand and adapt. Include:

- A problem, prerequisites, one command to run, and expected output.
- Synthetic input and clearly labeled mock responses that work offline by default.
- An explicit opt-in for live calls, account/key setup, and a note that calls may incur provider charges.
- The documented API/model version and primary documentation links.
- Application behavior for uncertain, missing, and invalid answers; thresholds are illustrative until evaluated on representative data.
- Named results, independent questions, deterministic calculations in code, and tests for meaningful decision branches.
- Honest limitations and provenance. Mock tests establish code behavior, not model quality.

Never include credentials, personal records, copied customer content, or unlicensed third-party examples. Keep model output separate from permissions or authorization decisions. Do not claim prompt-injection immunity or validated accuracy without evidence.

## Review and maintenance

A maintainer reads the proposed artifact, checks relevance and accessibility, and reproduces the documented command where practical before merging. Automated checks help catch formatting, link, and code problems; they do not establish resource quality.

AI assistance must be disclosed in a proposal. The contributor remains responsible for understanding, reviewing, and verifying the submission; bulk machine-generated link dumps are not useful contributions. This project's contribution policy is its own and does not imply acceptance by any other Awesome directory.

Report a broken link, incompatible API, misleading claim, or abandoned resource using the correction issue form. Propose a canonical replacement where available. Maintainers can remove entries that stop meeting the criteria and should record the reason in the pull request. A repaired resource can be proposed again.

Keep discussion respectful, specific, and about the work. Harassment, discriminatory language, and disclosure of private information are not acceptable; maintainers may remove such content or limit participation.

## Run checks

Use Node.js 22 or later and Python 3.10 or later. The examples need no third-party Python packages.

```sh
npm ci
npm run check
```

`npm run lint` checks Markdown, `npm run check:links` checks local targets and heading anchors, and `npm run check:community` checks the project directory's coverage and navigation. The `test:community`, `test:examples`, `test:projects`, `test:evaluations`, and `test:skills` scripts exercise the checks and offline behavior. A separate weekly/manual workflow checks remote URLs with bounded retries; transient failures need human review before removing a resource.

By contributing, you agree to the [license terms for the relevant files](LICENSE.md): CC0 for list/documentation text, MIT for original code and configuration. External projects keep their own licenses.
