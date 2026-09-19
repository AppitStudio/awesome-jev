# Maintaining Awesome Jev

Keep the list small enough that every entry has a reason to be here. Useful curation depends on selecting, explaining, checking, and sometimes removing resources. These practices follow the [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md); they do not establish endorsement by its maintainers.

## Review a proposed entry

1. Open the primary resource and identify who maintains it. Confirm that it actually uses Jev or teaches a relevant decision pattern.
2. Check the current installation or reading path. For reusable code, inspect its license, representative implementation, tests, and documented prerequisites. For a service, identify access requirements and where input data goes.
3. Record what was checked in the pull request: URL, version or commit, date, commands run, and limitations. Distinguish source inspection, offline execution, and live evaluation.
4. Explain the specific benefit in one sentence. Place the entry in the narrowest existing category, avoid duplicates, and disclose author affiliation.
5. Have a maintainer assess the recommendation. Passing checks establishes formatting and reachability, not resource quality. The maintainer may request stronger evidence or decline an entry that adds little value.

Use [CONTRIBUTING.md](../CONTRIBUTING.md) as the acceptance standard. First-party examples receive the same scrutiny as external submissions. Do not rank entries by stars, accept payment for placement, or add filler to make a section look complete.

For community projects, review the [detail page](../community/PROJECT_TEMPLATE.md), [category index](../community/README.md), and original README entry together. Verify setup and examples against the cited upstream version, distinguish executed checks from reported results, and keep all three surfaces consistent when updating or removing a project. `check:community` checks their connections, not factual accuracy. Keep the contributor and guide skills aligned with these conventions.

## Maintain links and relevance

Review the scheduled link-check results weekly. A 403 or 429 may be a host blocking automated checks; inspect it manually before removing an otherwise useful resource. Retry transient failures. Fix moved links, replace misleading descriptions, and remove persistently unavailable or unsuitable resources with an explanation in the pull request.

Revisit the official API and model references monthly and whenever a breaking change is reported. Review community entries for relevance each quarter. A quiet repository is not automatically abandoned: a small complete library may need few commits. Look for broken installation, incompatible APIs, unanswered defects, and misleading claims.

Treat this cadence as a maintainer responsibility; CI cannot perform editorial review. If maintenance pauses, say so in the README and invite help rather than displaying an unsupported “actively maintained” claim.

## Update examples deliberately

- Keep synthetic fixtures labeled and deterministic. Never replace them with undocumented recorded responses.
- Put questions and policy constants where reviewers can find them. Keep setup and expected results next to each example.
- Run the repository checks and the offline tests before merging. Check error, uncertainty, and fallback paths when behavior changes.
- Live evaluations require an explicitly configured key and may incur charges. Record version, dataset, sample size, method, and results before making performance or accuracy claims.
- A new model version or question wording deserves a new evaluation. Do not carry thresholds forward as if they were universally valid.

## Prepare a public release

Read the README as a newcomer, follow its first-run instructions in a clean checkout, verify license boundaries, and confirm that no credentials, local research, or generated artifacts are tracked. Enable GitHub Actions, inspect the first run, and require the `Checks` workflow's `offline` check before merging once repository settings permit it.

Suggested GitHub description: “Curated Jev resources and runnable examples for typed AI decisions.” Suggested topics: `awesome`, `awesome-list`, `jev`, `typesafe-ai`, `system-one`, `ai`, `decision-making`. These are setup suggestions, not automatically configured repository settings.

Publish only what can be supported by evidence. Prefer demonstrating one working example over announcing a catalog size or making an unmeasured “best” claim. Add new categories only when useful reviewed entries need them.

## Provenance and upstream directories

The initial list, documentation, and examples were produced by AI agents and checked against linked primary sources. Subsequent validation includes offline checks and explicit live requests; see [validation scope](validation.md). Maintainers and contributors must report their own review and testing honestly; generated descriptions are not personal experience.

The central [Awesome submission guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) currently exclude AI-generated lists and fully AI-generated pull requests. Its [creation guide](https://github.com/sindresorhus/awesome/blob/main/create-list.md) also specifies a maturity period, and submissions may be paused. This repository does not claim eligibility, inclusion, or endorsement. A passing linter, human review, or elapsed time does not by itself override those rules.
