# Working on Awesome Jev

Keep this repository a selective resource list with small, runnable reference projects. Read `CONTRIBUTING.md` before changing entries and `docs/maintaining.md` before preparing a release.

## TypeSafe integrations

Use the installed `typesafe-ai` skill when changing Jev questions, policy, API handling, or examples. Its source is the [official TypeSafe skill](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md). If it is unavailable, read the relevant current pages from the [documentation index](https://docs.typesafe.ai/llms.txt) and state that limitation.

Keep questions atomic and complete; question IDs are not model instructions. Keep application policy, arithmetic, exact parsing, and downstream actions in code. Preserve raw typed answers for inspection, and distinguish synthetic fixtures from recorded responses.

## Validation and privacy

- Run `npm run check` for public changes; keep CI offline and credential-free.
- Default commands must use synthetic data without contacting the provider. Live requests require explicit opt-in and bounded request counts.
- Keep API keys, raw evaluation runs, research drafts, and source checkouts outside this repository. Never read or display unrelated credentials.
- Do not publish performance claims from synthetic fixtures or small smoke checks. Record exactly which behavior was tested.
- Add resources only after inspecting their primary source, license, instructions, and relevant implementation. Disclose limitations and affiliations.
