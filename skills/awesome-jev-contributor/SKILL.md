---
name: awesome-jev-contributor
description: Review and prepare Jev projects or starter kits for Awesome Jev, or submit them when requested. Use for contribution readiness checks, resource entries, and example or reference-project pull requests to AppitStudio/awesome-jev.
---

# Contribute to Awesome Jev

Help a developer make one focused, evidence-backed contribution to [Awesome Jev](https://github.com/AppitStudio/awesome-jev). Produce a useful proposal that follows the repository's current rules; acceptance belongs to its maintainers.

## Establish the contribution

Identify the project URL or local path, its Jev-specific benefit, and the requested outcome: review, prepare a patch, or submit. Infer these from the conversation and source; ask only for missing information that affects the result. Confirm affiliation and commercial relationships without guessing them.

Choose the appropriate route:

- **External project or starter kit:** add a project detail page, list it in the community directory's closest category, and retain a concise entry in the README. Keep its code in its own repository. A starter kit does not have to be copied into Awesome Jev to qualify.
- **Code contributed to Awesome Jev:** use `examples/` for a small teaching workflow or the existing `projects/` conventions for a more complete tool. Apply the repository's example requirements to either, scaled to the contribution.
- **Existing entry:** make a focused correction or update instead of adding a duplicate.

Use the user's requested route when it fits. Do not turn a listing request into an application rewrite or impose this repository's Python tooling on an external project.

## Read the current rules

In an Awesome Jev checkout, read its `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `docs/maintaining.md`, and the applicable submission template. Otherwise retrieve their current contents from these canonical sources:

- [Contribution rules](https://github.com/AppitStudio/awesome-jev/blob/main/CONTRIBUTING.md).
- [Catalog and categories](https://github.com/AppitStudio/awesome-jev/blob/main/README.md).
- [Community directory](https://github.com/AppitStudio/awesome-jev/blob/main/community/README.md) and [project page template](https://github.com/AppitStudio/awesome-jev/blob/main/community/PROJECT_TEMPLATE.md).
- [Maintainer review process](https://github.com/AppitStudio/awesome-jev/blob/main/docs/maintaining.md).
- [Pull-request template](https://github.com/AppitStudio/awesome-jev/blob/main/.github/PULL_REQUEST_TEMPLATE.md) or [resource suggestion form](https://github.com/AppitStudio/awesome-jev/blob/main/.github/ISSUE_TEMPLATE/resource.yml).
- [Agent guidance](https://github.com/AppitStudio/awesome-jev/blob/main/AGENTS.md) and [license boundaries](https://github.com/AppitStudio/awesome-jev/blob/main/LICENSE.md).

The current repository rules govern eligibility; this skill is a workflow, not a separate policy. Search the README, community directory and project pages, and open issues/PRs for the canonical URL and project name. If current rules, source, or duplicate checks are inaccessible, state which checks remain unverified. Do not claim submission readiness until required evidence is available.

## Review the actual artifact

Inspect the README, license, installation path, relevant Jev integration, and tests where available. Record the reviewed commit or version and date. For closed-source resources, inspect the public artifact and access terms, and state the limits of source review.

Assess these requirements against evidence:

| Area | What to establish |
| --- | --- |
| Relevance | A concrete Jev use and distinct reader benefit; a working, publicly reachable artifact. |
| Adoption | Prerequisites, setup/run instructions, licensing or access terms, account/payment needs, and where submitted data goes. |
| Compatibility | The documented API/model version, with any differences from the current TypeSafe API made explicit. |
| Reliability | What code does with uncertainty, missing/invalid answers, service failures, and any downstream actions, as relevant to the resource. |
| Evidence | What was inspected or executed and its limits; no invented test results, metrics, or personal experience. |
| Disclosure | Contributor affiliation, commercial interests, AI assistance, and the contributor's actual review. |

Self-submissions, new projects, and paid or closed-source resources can qualify. Do not invent star-count, age, open-source, or live-evaluation requirements. Reject paid placement, referral/tracking links, placeholders, and unsupported claims under the current contribution rules. A missing test run is a disclosed evidence gap, not automatically proof that the project is unsuitable.

Use documented offline checks when practical. Inspect commands before running them, avoid exposing ambient credentials to candidate code, and distinguish source inspection, mocked execution, and live evaluation. Do not load private `.env` files just to review a submission. Live calls require the user's authorization, suitable data, and a request bound; never treat mock outputs as measured Jev results.

For compatibility questions or implementation changes, consult the [current TypeSafe documentation](https://docs.typesafe.ai/llms.txt); use the official `typesafe-ai` skill if available. Do not require that skill to write a catalog entry. Typed questions express narrow judgments; code owns parsing, arithmetic, policy, permissions, and downstream effects. Identify consequential problems in those boundaries without demanding unrelated redesigns.

Report concrete blockers separately from optional improvements. Fix relevant issues in the contributor's project when the requested scope includes fixes; otherwise give a short actionable list. Keep review notes, copied source, datasets, and raw response captures outside the public Awesome Jev tree.

## Prepare the contribution

For an external resource, use its canonical HTTPS URL and one factual sentence:

```markdown
- [Resource name](https://example.com/resource) - Classifies support requests with Jev and documents a review fallback.
```

Choose the narrowest existing category and alphabetize within it unless it explicitly follows a learning sequence. Keep community projects separate from official TypeSafe resources. Do not copy the project's README, add empty categories, or pad the list with several unrelated links.

For an external application, starter kit, tool, or integration, prepare all three connected parts:

1. **Project page:** create `community/projects/<slug>.md` from the current page template. Explain when to use it, how Jev fits, prerequisites and setup, real examples/demos, data handling and costs, limitations, license, affiliation, and version-specific review evidence. Include one canonical HTTPS link labeled `Source` and a link back to its directory category. Distinguish inspected instructions from commands you actually ran.
2. **Category index:** link the page once under its primary category in `community/README.md`, with a concise use case and stack/format. Reuse an existing category when it fits.
3. **README entry:** keep the canonical upstream link and factual sentence in `Community projects`, and append a link to the local project page. Do not replace the original list with the directory.

Articles and cookbook links do not need project pages. Update the guide's resource map when it helps discovery, but a `solutions.md` mention alone is not a complete project submission. For corrections or removals, keep the README, directory, and detail page consistent.

For code hosted in Awesome Jev, include a problem statement, prerequisites, a runnable command and expected output, clearly synthetic offline fixtures, explicit live opt-in and key/cost instructions, documented versions, uncertainty/error behavior, meaningful tests, and licensing/provenance. Follow the nearby example or project structure. Preserve existing user changes and keep the patch focused.

Fill the repository's current PR template with:

- The reader benefit, category, canonical URL, and affiliation.
- The exact revision reviewed, commands run and observed results, supported versions, access requirements, and limitations.
- AI assistance and what the contributor actually reviewed. Do not claim human review that has not happened.
- Honest checklist states: leave unperformed checks unchecked and explain them.

For a resource issue, use the corresponding form's fields instead. Include the proposed category and enough information to write the project page; an accepted project patch still needs all three parts. Prefer one issue or one PR, not duplicate proposals. Show a suggested README entry even when the chosen route is an issue.

In the Awesome Jev checkout, follow its current check instructions. At the time of writing these require Node.js 22+ and Python 3.10+:

```sh
npm ci --ignore-scripts
npm run check
```

These checks apply to the catalog repository; use the candidate project's own toolchain for its tests. The included `check:community` check verifies that the README, category index, and project pages connect correctly; it cannot verify the page's factual claims. Confirm setup and example links against upstream instructions, including whether commands need credentials or make live calls. Confirm external links separately. Review the diff for secrets, private paths/data, unrelated files, and claims beyond the evidence. Do not present formatting or link checks as editorial approval.

## Deliver or submit

For a review or preparation request, return the readiness findings, proposed entry/patch, and completed proposal text without publishing anything. Store drafts outside the public tree or in the user-designated location.

If the user has explicitly requested submission, that is authorization to create the scoped issue or PR; do not request the same permission again. Once the proposal meets the applicable requirements, use the existing authenticated GitHub tools. For a PR, use a focused branch in the contributor's fork or an authorized writable checkout, targeting `AppitStudio/awesome-jev`'s current default branch. Check for an existing matching proposal before creating a new one; update it when appropriate. Never push directly to the target's default branch or merge as part of submitting a contribution.

If a publication attempt has an uncertain outcome, inspect the branch and open proposals before retrying. If authentication or permissions are unavailable, provide the completed patch/text and a precise manual next step; never request a token in chat or claim the proposal was submitted.

Finish with the proposed change, verified evidence and remaining gaps, and either the local artifact paths or actual issue/PR URL. Clearly distinguish a prepared proposal, a submitted proposal, and maintainer acceptance.
