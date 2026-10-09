# Bud Decision Studio

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Cross-platform desktop app and local server for open Jev-like System One decision models (Laya, Kev, Lev, Jev-Omni and others): download and run models on GPU or CPU, try typed questions in a UI, and serve a TypeSafe-compatible `POST /v1/systemone` API on localhost so code written for Jev works by changing the base URL. Does not run official Jev weights.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BudEcosystem/Bud-Decision-Studio) |
| Maintainer | [BudEcosystem](https://github.com/BudEcosystem) (Bud Ecosystem). Independently curated. |
| Format | Desktop app (macOS Apple Silicon, Windows, Linux) + local HTTP server |
| Requirements | A supported OS; disk/RAM/VRAM for the chosen models. No TypeSafe key needed for local models. |
| License | **Unspecified** at the pinned commit (no LICENSE file in the repository); individual models keep their own licenses. Treat the source as readable but not licensed for reuse. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Evaluate or prototype against local open-weight decision models with the same request shape as hosted Jev.
- Mismatch: not a substitute validated against Jev; the maintainers' comparisons are their own, and the app's source has no license.

## How it works

The README documents a compatibility layer ([`basal/api_compat.py`](https://github.com/BudEcosystem/Bud-Decision-Studio/blob/613e189f37cffd77fc955834abe9838f604c05af/basal/api_compat.py)) for TypeSafe's `/v1/systemone`, Vercel AI Gateway and OpenRouter formats, with conformance tests against TypeSafe's published OpenAPI schema and both official SDKs ([`tests/test_conformance.py`](https://github.com/BudEcosystem/Bud-Decision-Studio/blob/613e189f37cffd77fc955834abe9838f604c05af/tests/test_conformance.py)). Inference uses open models only; decisions are kept in a local history for 30 days by default.

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/BudEcosystem/Bud-Decision-Engine/main/get.sh | sh
# or download an installer from the GitHub Releases page
```

## Limits and data handling

Runs locally; model weights download from each publisher's Hugging Face repository. The installer sets up a private Python/PyTorch runtime inside the app folder. No LICENSE file at the pinned commit. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 613e189f37cf](https://github.com/BudEcosystem/Bud-Decision-Studio/tree/613e189f37cffd77fc955834abe9838f604c05af). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
