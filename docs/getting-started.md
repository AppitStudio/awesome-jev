# Run your first decision workflow

Start with a synthetic support ticket and inspect how typed answers become an application decision. The default example makes no network requests and needs no API key.

## 1. Run locally

Install Python 3.10 or newer, clone the repository, and run:

```bash
git clone https://github.com/AppitStudio/awesome-jev.git
cd awesome-jev
python3 examples/run.py support-routing --mock
```

If you already have a checkout, run the final command from its root. There are no Python packages to install.

The output identifies mock mode and shows a decision computed from a synthetic response. Open the [support-routing guide](../examples/support-routing/README.md) to inspect its questions, fixture, policy, and expected behavior. The model values in that fixture are authored examples, not recorded Jev responses or evidence of accuracy.

## 2. Inspect the request

```bash
python3 examples/run.py support-routing --show-request
```

The request contains `state`, a model ID, and named `questions`. This workflow combines a Choice for the support queue and a Noul for explicit urgency. Each question evaluates the same state independently. Code reads the named answers and applies the review policy. The quality-rubric example introduces Score.

Try the other workflows:

```bash
python3 examples/run.py quality-rubric --mock
python3 examples/run.py span-selection --mock
python3 examples/run.py rag-triage --mock
```

Read [Designing a Jev decision](decision-patterns.md) when adapting the questions to your own task.

## 3. Opt into a live request

Obtain access and a key through the [TypeSafe console](https://console.typesafe.ai/). Configure `TYPESAFE_API_KEY` in your shell through your usual secret-management method, then run:

```bash
python3 examples/run.py support-routing --live
```

Live mode sends the example's state and questions to TypeSafe and can incur usage charges. It needs network access and an authorized key. It prints the resulting decision without performing the downstream action. A live answer can differ from the synthetic fixture.

The examples default to the documented version `jev-1.13.0`. Consult the [example configuration](../examples/README.md) for overrides and the [current models](https://docs.typesafe.ai/models) page before changing it. Recheck your policy when changing model versions or question wording.

## 4. Build on the right layer

The small HTTP client in these examples exists to make the request and failure paths inspectable. For an application, start with the official [Python SDK](https://docs.typesafe.ai/sdk/python) or [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript), which document typed interfaces and retry configuration.

Replace the sample state with a deliberately selected input, give each question one concrete job, and define review/fallback behavior before connecting a result to an action. Use labeled data to evaluate the whole policy. Running a mock fixture successfully verifies the program path; it does not validate a threshold for your workload.

For repository development, follow the checks in [CONTRIBUTING.md](../CONTRIBUTING.md). Node.js is needed for those development checks, not for running the Python examples.
