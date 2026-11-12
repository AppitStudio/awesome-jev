# Buddy Jev action

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pipeline action in Buddy that asks Jev one typed question about a commit message, changelog or any file from the run, so later actions can branch on the answer or send unclear runs to a person.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://buddy.works/docs/integrations/typesafe) |
| Maintainer | [Buddy](https://buddy.works). |
| Format | Built-in pipeline action (`type: "JEV"`) in Buddy pipelines, configured in the UI, in YAML or through the REST API. |
| Requirements | Buddy account and workspace; TypeSafe API key added as a TypeSafe integration in Buddy (scoped to a workspace, project or environment). |
| License | Closed source, part of the hosted Buddy product. No public repository. |
| Pricing and access | Commercial product, see [Buddy pricing](https://buddy.works/pricing). Jev calls are billed to your own TypeSafe key (BYOK). |
| Jev evidence | [TypeSafe integration docs](https://buddy.works/docs/integrations/typesafe), [Jev YAML reference](https://buddy.works/docs/yaml/yaml-actions/jev), [launch post](https://buddy.works/blog/jev-action-typed-decisions-in-buddy-pipelines). Vendor documentation; the implementation could not be inspected. |
| Disclosure | Closed source and commercial. Listing is not an endorsement. |

## When to use

- Score deployment risk from the commit message and `CHANGELOG.md`, then post to a release channel or require manual approval only when the answer is `high`.
- Route a change by type (feature, bugfix, other) or owning team with a `CHOICE` question and run different actions per answer.
- Gate a step with a `BOOLEAN` question, for example whether the change touches database migrations.

It fits teams that already run pipelines in Buddy. Outside Buddy, use a GitHub Action or CLI from this directory instead.

## How it works

Each action has a state, one question and a question type:

- **State**: inline text with pipeline variables expanded at runtime, or `file: <path>` to read a file from the repository or from an earlier action.
- **Question type**: `SCORE` (ordered criteria, 2 to 10), `CHOICE` (unordered criteria, up to 255) or `BOOLEAN` (optional `true_when` / `false_when`).
- **Model**: optional `model` pins a Jev version such as `jev-1.13.0`; the default is `jev-latest`.

Jev returns one answer. The action writes it to variables, and Buddy's trigger conditions on later actions decide what runs:

| Variable | Holds |
| --- | --- |
| `BUDDY_ACTION_JEV_RESULT` | Matched criterion key, or `true` / `false` |
| `BUDDY_ACTION_JEV_CONFIDENCE` | Confidence from `0` to `1` |
| `BUDDY_ACTION_JEV_SCORE` | Position on the scale (`SCORE` only) |
| `BUDDY_ACTION_JEV_PROBABILITY` | Probability of `true` (`BOOLEAN` only) |
| `BUDDY_ACTION_JEV_PROBABILITY_*` | Probability per criterion (`SCORE`, `CHOICE`) |

Jev only answers the question. The decision to notify, wait for approval or deploy stays in the pipeline's conditions.

## Get started

1. In Buddy, add a TypeSafe integration with your TypeSafe API key.
2. Add the Jev action to a pipeline and reference the integration by its ID:

```yaml
- action: "Assess deployment risk"
  type: "JEV"
  integration: "typesafe"
  state:
    - "Commit: $BUDDY_RUN_COMMIT_MESSAGE"
    - file: "CHANGELOG.md"
  question: "How risky is this change to deploy?"
  question_type: "SCORE"
  criteria:
    none: "Touches only documentation or comments"
    low: "Touches application code covered by tests"
    high: "Touches database migrations or public API contracts"
```

3. Add a trigger condition to a later action, for example a Slack message or manual approval that runs only when confidence is below 0.7:

```yaml
  trigger_conditions:
    - trigger_condition: VAR_LESS_THAN
      trigger_variable_key: BUDDY_ACTION_JEV_CONFIDENCE
      trigger_variable_value: "0.7"
```

Each run sends a live request to TypeSafe under your key. There is no offline or mock mode.

## Examples and demos

- [TypeSafe integration docs](https://buddy.works/docs/integrations/typesafe): YAML for all three question types, the output variable table and two trigger-condition patterns.
- [Jev YAML reference](https://buddy.works/docs/yaml/yaml-actions/jev): every action field.
- [Launch post](https://buddy.works/blog/jev-action-typed-decisions-in-buddy-pipelines).

No separate public demo pipeline exists.

## Limits and data handling

- Everything listed in the state, including file contents, is sent to TypeSafe with each run.
- One question per action; ask several things with several actions.
- The 0.7 confidence threshold in the docs is an example, not a measured value.
- Source code is not public, so this listing relies on vendor documentation.

## Review and maintenance

Reviewed on **2026-11-12**: Buddy's TypeSafe integration page, the Jev YAML reference and the launch post. AI-assisted documentation review. **No live Buddy pipeline run or Jev call.** Catalog checks only validate Awesome Jev navigation.

Related: [Jev GitHub Action](jev-action.md), [go-decide](go-decide.md).
