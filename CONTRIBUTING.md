# Contributing

Help readers find resources that make working with Jev easier. A useful correction or a small, well-understood addition matters more than the size of the list.

## Use the contributor skill

The [Awesome Jev contributor skill](skills/awesome-jev-contributor/SKILL.md) helps a coding agent review your project or starter kit, identify gaps, and prepare a focused entry and proposal with verification evidence. It supports both external project listings and code contributed here. These contribution rules remain the source of truth; the skill does not guarantee acceptance.

Install it from your project directory with the [Skills CLI](https://github.com/vercel-labs/skills), then select your agent:

```sh
npx skills add AppitStudio/awesome-jev --skill awesome-jev-contributor
```

For Codex specifically, add `--agent codex`; add `--global` if you want it available across projects. You can also give an agent the linked `SKILL.md` directly without installing it.

Example requests:

- “Use awesome-jev-contributor to check this Jev starter kit for submission readiness: PROJECT_URL.”
- “Use awesome-jev-contributor to review my project and prepare a README entry and PR text. Keep the proposal local.”
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

`npm run lint` checks Markdown, `npm run check:links` checks local targets and heading anchors, and the `test:examples`, `test:projects`, and `test:evaluations` scripts run offline behavior tests. A separate weekly/manual workflow checks remote URLs with bounded retries; transient failures need human review before removing a resource.

By contributing, you agree to the [license terms for the relevant files](LICENSE.md): CC0 for list/documentation text, MIT for original code and configuration. External projects keep their own licenses.
