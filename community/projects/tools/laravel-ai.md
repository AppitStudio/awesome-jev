# Laravel AI

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Add inspectable support-message routing to a Laravel application using typed Jev answers and Laravel's testing tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/laravel/ai) |
| Maintainer | [Laravel](https://github.com/laravel); independently curated here, not an upstream submission. |
| Format | PHP SDK with a TypeSafe classification provider; the routing policy below is our original adaptation. |
| Requirements | PHP 8.3+, Composer, Laravel/Illuminate 12 or 13. The reviewed source specifically requires `illuminate/json-schema` `^12.62` or `^13.15`. Live use needs a TypeSafe account and server-side `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/LICENSE.md). |

## When to use

Use this when an existing Laravel application needs a semantic judgment: which support queue fits a message, whether someone explicitly requests urgent help, or how a comment scores against a written rubric. Laravel supplies typed response objects, events, provider configuration, and fakes; you supply the application policy.

Keep exact checks such as subscription status, invoice totals, and account permissions in ordinary PHP. This SDK does not include a complete ticketing application. For a ready-made batch workflow, explore [Support Router](../../../projects/support-router/README.md).

**Version caveat:** on September 19, 2026, [Packagist](https://packagist.org/packages/laravel/ai) still listed `v0.11.2` as stable. TypeSafe classification was merged afterward in [PR #1010](https://github.com/laravel/ai/pull/1010) and is present in the reviewed `1.x-dev` source. An unqualified `composer require laravel/ai` does not establish that this feature is installed. Start in a disposable checkout of the revision below; review release availability before adopting it in an application.

## How it works

```text
Selected message → independent typed questions → TypeSafe / Jev
                                               ↓
Laravel answer objects → PHP review policy → suggested queue
```

The [gateway](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/src/Gateway/TypeSafeGateway.php) sends state and questions to `POST https://api.typesafe.ai/v1/systemone`. Its names differ slightly from the [HTTP API](https://docs.typesafe.ai/api):

| Laravel interface | TypeSafe meaning |
| --- | --- |
| `Choice($instructions, $options)` | One option; returns `choice`, `probabilities`, and nullable `confidence`. |
| `Boolean($instructions, $criteria)` | Noul; wire field `noul` becomes `BooleanAnswer->probability`, the probability of yes. |
| `Score($instructions, $levels)` | Ordered rubric; returns a weighted `score`, distribution, legend, and nullable confidence. `normalized()` divides by the highest level index. |

A Boolean has no separate confidence. Its `isTrue()` helper defaults to a 0.5 cutoff; use explicit review boundaries when that default would hide uncertainty. [Choice confidence](https://docs.typesafe.ai/confidence) summarizes the distribution, not permission to act. Question IDs connect answers to code; write complete instructions in the question itself.

## Get started

**Setup downloads source and packages; it makes no inference requests.** Run outside your application and this catalog. No API key is needed. This is the source-checkout path reproduced during review, not a stable package installation:

```sh
git clone https://github.com/laravel/ai.git laravel-ai-review
cd laravel-ai-review
git checkout ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73
composer install --no-plugins --no-scripts --prefer-dist
```

**Offline worked example.** Save the following as `tests/Feature/AwesomeTriageTest.php` inside that checkout. The message and answers are synthetic. The fixture deliberately supplies every answer. Bare `Classification::fake()` generates random answers, and partial fixtures randomly fill omitted questions too. `preventStrayClassifications()` blocks a request without a fake response; it does not reject omitted questions within a supplied fixture.

```php
<?php

use Illuminate\Support\Facades\Http;
use Laravel\Ai\Classification;
use Laravel\Ai\Classification\Boolean;
use Laravel\Ai\Classification\Choice;
use Laravel\Ai\Responses\Data\BooleanAnswer;
use Laravel\Ai\Responses\Data\ChoiceAnswer;

test('support routing keeps uncertain answers for review', function () {
    Http::preventStrayRequests();
    Classification::fake([[
        'department' => new ChoiceAnswer(
            'billing', ['billing' => 0.94, 'technical' => 0.04, 'other' => 0.02], 0.9
        ),
        'urgent' => new BooleanAnswer(0.95),
    ]])->preventStrayClassifications();

    $response = Classification::of([
        'message' => 'My receipt has the wrong company name. '
            .'Please fix it today; our expense deadline is tonight.',
    ])->questions([
        'department' => new Choice('Which team should handle `message`?', [
            'billing' => 'Invoices, receipts, charges, and refunds',
            'technical' => 'Broken product behavior and integrations',
            'other' => 'No listed team fits, or the request is unclear',
        ]),
        'urgent' => new Boolean(
            'Does `message` explicitly request time-sensitive assistance?'
        ),
    ])->classify(provider: 'typesafe', model: 'jev-1.13.0');

    // Preserve mapped answers and model metadata before applying policy.
    $record = json_decode(json_encode($response, JSON_THROW_ON_ERROR), true);

    // Illustrative thresholds; evaluate them on your own labeled cases.
    $decide = function ($team, $urgent): string {
        if (! $team instanceof ChoiceAnswer || ! $urgent instanceof BooleanAnswer
            || ! in_array($team->choice, ['billing', 'technical'], true)
            || $team->confidence === null || ! is_finite($team->confidence)
            || $team->confidence < 0.8 || $team->confidence > 1
            || ! is_finite($urgent->probability)
            || $urgent->probability < 0 || $urgent->probability > 1
            || ($urgent->probability > 0.2 && $urgent->probability < 0.8)) {
            return 'manual_review';
        }

        return $team->choice.($urgent->probability >= 0.8 ? ':priority' : ':normal');
    };

    $decision = $decide(
        $response->answers['department'] ?? null,
        $response->answers['urgent'] ?? null,
    );
    expect($decision)->toBe('billing:priority');
    expect($decide($response['department'], new BooleanAnswer(0.5)))
        ->toBe('manual_review');
    expect($decide(null, $response['urgent']))->toBe('manual_review');
    expect($decide(new ChoiceAnswer('billing', [], 1.5), $response['urgent']))
        ->toBe('manual_review');
    expect($record['answers']['department']['confidence'])->toBe(0.9);
    Http::assertNothingSent();
    echo $decision.PHP_EOL;
});
```

**Run offline**, from the same checkout:

```sh
php vendor/bin/pest tests/Feature/AwesomeTriageTest.php
```

The test prints `billing:priority` and passes. It also checks that ambiguous urgency, a missing department, and invalid confidence produce `manual_review`. These results establish PHP behavior with fixtures, not Jev's routing quality. Nothing is assigned, refunded, or sent.

### Optional live adoption

In a compatible Laravel application, first install a release containing classification or explicitly choose the development revision after reviewing its constraints. Follow the [SDK installation guide](https://laravel.com/docs/ai-sdk#installation) for general setup; its stable documentation may lag this feature. Configure `ai.providers.typesafe` with driver `typesafe` and key from `TYPESAFE_API_KEY`, as in the [package configuration](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/config/ai.php).

Move the classification and decision code into a service, keep the fake in tests, and invoke the service once with the synthetic message only when you explicitly enable live testing. Removing the fake makes a real request; the message and question text go to TypeSafe and input-token charges apply. Keep the model explicit and capture `$response->meta->model` and usage. This application-installation and live path was source-reviewed, not executed here.

## Adaptation tips

- Replace the two teams with your real taxonomy, retaining `other` and distinguishing overlapping responsibilities in their descriptions.
- Supply only needed message fields. Account IDs, payment details, and full Eloquent records rarely help this judgment.
- Keep urgency separate from department. Add independent questions together only when their answers affect the workflow.
- Save the mapped answers, model version, and policy version under your application's retention rules. Re-evaluate thresholds on representative cases; do not treat the synthetic numbers as calibrated recommendations.
- Test low or absent confidence, unknown labels, malformed answers, and unavailable providers before connecting the suggestion to a queue assignment.

## Examples and demos

The [classification fake tests](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/tests/Feature/ClassificationFakeTest.php) demonstrate closures, explicit answers, and stray-call prevention. The [HTTP-fake tests](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/tests/Feature/Providers/TypeSafe/ClassificationTest.php) exercise payloads, answer mapping, and service errors without a provider call. The [integration test](https://github.com/laravel/ai/blob/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73/tests/Integration/ClassificationTest.php) is a credentialed support example; it was not run. No separate hosted classification demo was verified. [Taylor Otwell's announcement](https://x.com/taylorotwell/status/2100700952923713641) is discovery context.

## Limits and data handling

Unknown answer types are skipped; accessing a missing answer throws `InvalidArgumentException`. The gateway does not comprehensively validate response semantics or probability ranges. A live service should retain the item for review on malformed responses, connection errors, rate limits, overload, or authentication failure. The adapter maps several failures to SDK exceptions; it does not add automatic backoff retries.

Classification itself adds no database persistence, but dispatches events containing the prompt and response, so application listeners or observability tools may retain them. Provider-side retention depends on [TypeSafe's terms](https://docs.typesafe.ai/legal). Check [current pricing](https://docs.typesafe.ai/models) before a live run. The default model alias is `jev-latest`; moving aliases can change behavior.

## Review and maintenance

Reviewed September 19, 2026 at [ca8d9bf](https://github.com/laravel/ai/commit/ca8d9bf4735aa53c107a6cf422c8ab6dd68bfc73). AI-assisted review inspected the license, Composer constraints, configuration, questions, gateway, response objects, fakes, events, and failure handling. In an isolated environment without provider keys, dependency installation succeeded on PHP 8.4.23; the two upstream fake suites passed **26 tests / 70 assertions**. The worked example passed **1 test / 6 assertions** offline. Laravel 12, PHP 8.3, stable-package adoption, live inference, and model quality were not tested.

Related: [Support routing concepts](../../../examples/support-routing/README.md) · [Evaluating routing policies](../../../evaluations/README.md).
