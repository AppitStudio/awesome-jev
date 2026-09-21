# Jev Symfony Bundle

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Symfony 7.4/8 bundle for TypeSafe Jev: typed HTTP client, validator constraints, Messenger evaluation, Workflow guards, profiler panel, and console helpers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vbcherepanov/jev-symfony-bundle) |
| Maintainer | [vbcherepanov](https://github.com/vbcherepanov). Independently curated; this page is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | PHP Composer package (`vbcherepanov/jev-symfony-bundle`); Symfony Flex recipe under `recipe/`. |
| Requirements | PHP 8.4+; Symfony 7.4 or 8.x HttpClient stack; optional validator/messenger/workflow/profiler packages; `TYPESAFE_API_KEY` (optional `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`). |
| License | [Apache-2.0](https://github.com/vbcherepanov/jev-symfony-bundle/blob/05aae643935d1a9911358a79a117fe662a57b31f/LICENSE). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. PHP/Composer unavailable on the Linux review host—source + upstream CI badge inspected; unit/functional PHPUnit suite not executed locally. Live TypeSafe calls not run. Distinct from [Laravel AI](laravel-ai.md). |

## When to use

Use it when a Symfony app needs typed Jev decisions wired through DI, validation attributes, async Messenger, or workflow transition guards. Prefer [Laravel AI](laravel-ai.md) for Laravel; prefer raw SDKs when you do not need Symfony integration surfaces.

## How it works

[`JevClient.php`](https://github.com/vbcherepanov/jev-symfony-bundle/blob/05aae643935d1a9911358a79a117fe662a57b31f/src/Client/JevClient.php) posts `v1/systemone` (default base `https://api.typesafe.ai/`). [`RequestEncoder.php`](https://github.com/vbcherepanov/jev-symfony-bundle/blob/05aae643935d1a9911358a79a117fe662a57b31f/src/Serialization/RequestEncoder.php) encodes evaluations; validator attributes `#[JevNoul]` / `#[JevChoice]`, Messenger handler, and Workflow `JevGuardListener` consume decisions in application code. `JevClientFake` supports tests without HTTP. State and question payloads leave the host on live calls.

## Get started

```sh
composer require vbcherepanov/jev-symfony-bundle
# or pin reviewed source:
git clone https://github.com/vbcherepanov/jev-symfony-bundle.git
cd jev-symfony-bundle
git checkout 05aae643935d1a9911358a79a117fe662a57b31f
# composer install && vendor/bin/phpunit   # needs PHP 8.4+
```

Configure `TYPESAFE_API_KEY` via `.env.local` or Symfony secrets. Live calls bill TypeSafe.

## Examples and demos

- Upstream README covers validator, Messenger, Workflow, profiler, and `jev:ask` / `jev:models`.
- Upstream CI workflow badge on the repository.
- This listing: source/LICENSE/tests tree inspected; PHPUnit not run (no PHP 8.4 on review host). No live TypeSafe call.

## Limits and data handling

Evaluation state and questions are sent to TypeSafe when configured. Bundle is unofficial. Metrics/logging hooks are optional. Cost/latency claims were not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 05aae64](https://github.com/vbcherepanov/jev-symfony-bundle/tree/05aae643935d1a9911358a79a117fe662a57b31f): Apache-2.0; AI-assisted source review of README, LICENSE, `src/`, and `tests/` layout. PHPUnit and live TypeSafe not run on this host.

Related: [Laravel AI](laravel-ai.md), [jev-java](jev-java.md), [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md).
