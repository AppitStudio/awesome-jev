# Working on Awesome Jev

Keep this repository a selective directory of Jev-powered apps and developer resources, with small, runnable reference projects. Read `CONTRIBUTING.md` before changing entries and `docs/maintaining.md` before preparing a release.

For app, project, or starter-kit submissions, use the [contributor skill](skills/awesome-jev-contributor/SKILL.md). Keep its guidance aligned with `CONTRIBUTING.md`; it must work when installed outside this checkout.

Every Community projects entry needs a [detail page and category listing](community/projects/README.md) alongside its original README link. Follow the [page template](community/PROJECT_TEMPLATE.md); a skill resource-map mention alone does not complete a submission.

Put user-facing apps in `community/projects/apps/` and developer tools in `community/projects/tools/`, each with a full detail page and an entry in its own directory README. Follow the [app listing rules](CONTRIBUTING.md#list-a-jev-powered-app) and [tags/disclosures](community/APP_TAGS.md). Closed-source and commercial apps can qualify: show source and pricing tags, product/pricing links, Jev evidence, and source-review limitations. Skills must flag paid and closed-source recommendations at the point of recommendation. Root `projects/` is for code maintained here.

For workflow discovery, resource selection, guided setup, or adapting a starter for a user, use the [Awesome Jev Guide skill](skills/awesome-jev-guide/SKILL.md). Keep its references current and user-specific projects outside this public catalog unless the user requests a contribution.

## TypeSafe integrations

Use the installed `typesafe-ai` skill when changing Jev questions, policy, API handling, or examples. Its source is the [official TypeSafe skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md). If it is unavailable, read the relevant current pages from the [documentation index](https://docs.typesafe.ai/llms.txt) and state that limitation.

Keep questions atomic and complete; question IDs are not model instructions. Keep application policy, arithmetic, exact parsing, and downstream actions in code. Preserve raw typed answers for inspection, and distinguish synthetic fixtures from recorded responses.

## Validation and privacy

- Run `npm run check` for public changes; keep CI offline and credential-free.
- Default commands must use synthetic data without contacting the provider. Live requests require explicit opt-in and bounded request counts.
- Keep API keys, raw evaluation runs, research drafts, and source checkouts outside this repository. Never read or display unrelated credentials.
- Do not publish performance claims from synthetic fixtures or small smoke checks. Record exactly which behavior was tested.
- Add resources only after inspecting their primary source, license, instructions, and relevant implementation. Disclose limitations and affiliations.
