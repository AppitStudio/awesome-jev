# pi-jev-extension (rioliu)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Pi extension that exposes `jev_decide` for TypeSafe Jev typed questions with silent session-model fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rioliu/pi-jev-extension) |
| Maintainer | [rioliu](https://github.com/rioliu). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Pi package/extension (TypeScript/Bun). |
| Requirements | Pi agent host; `JEVMODEL_API_KEY` (and optional URL) for live Jev; Bun per upstream. |
| License | [MIT](https://github.com/rioliu/pi-jev-extension/blob/54db8bf21bb031ade5bf402d70ccdf1aadae3586/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from other catalogued pi-jev* extensions/tools. |

## When to use

Use when Pi should call typed Jev decisions as a tool. Prefer other pi-jev* packages if you already standardize on them.

## How it works

Registers `jev_decide` so agents get branchable choice/score/noul values. On failure/timeout/missing key, the same question goes to the session model with `source: "fallback"`. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/rioliu/pi-jev-extension.git
cd pi-jev-extension
git checkout 54db8bf21bb031ade5bf402d70ccdf1aadae3586
# pi install git:github.com/rioliu/pi-jev-extension — follow upstream README
```

Pin revision `54db8bf21bb031ade5bf402d70ccdf1aadae3586` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Default endpoint noted as jevmodel.org in README—confirm against your TypeSafe deployment. Live Pi/Jev not run on the review host. Distinct from other pi-jev* listings.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 54db8bf](https://github.com/rioliu/pi-jev-extension/tree/54db8bf21bb031ade5bf402d70ccdf1aadae3586). AI-assisted README and LICENSE inspection; install/live paths not executed.
