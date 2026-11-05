# jev-unreal-statetree (Unreal Engine 5.8 StateTree tasks for finite, revision-guarded Jev decisions)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Native Unreal Engine 5.8 plugin that adds StateTree tasks for finite Jev decisions with revision guards and an expected model pin (default `jev-1.13.0`). Keeps gameplay decisions typed and auditable inside StateTree.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-unreal-statetree) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Unreal Engine 5.8 C++ plugin (MIT) |
| Requirements | Unreal Engine 5.8+, and a gateway or subsystem configuration that supplies TypeSafe credentials outside packaged builds as documented upstream. |
| License | [MIT](https://github.com/gbesse/jev-unreal-statetree/blob/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Source/JevStateTree/Private/StateTreeJevDecisionTask.cpp`](https://github.com/gbesse/jev-unreal-statetree/blob/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c/Source/JevStateTree/Private/StateTreeJevDecisionTask.cpp) at the pinned commit. |

## When to use

- Drive StateTree branches with typed Jev outcomes.
- Pin the expected model and reject mismatched replies.
- Mismatch: UE 5.8-specific; needs your own secret handling for shipping builds.

## How it works

`StateTreeJevDecisionTask` and `JevDecisionSubsystem` issue revision-guarded requests; settings default `ExpectedModel` to `jev-1.13.0`. Integration evidence: [`Source/JevStateTree/Private/StateTreeJevDecisionTask.cpp`](https://github.com/gbesse/jev-unreal-statetree/blob/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c/Source/JevStateTree/Private/StateTreeJevDecisionTask.cpp).

## Get started

From the upstream README (not run on the review host):

```sh
# open the .uplugin in UE 5.8, enable JevStateTree, configure the subsystem per README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-unreal-statetree/blob/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c/README.md](https://github.com/gbesse/jev-unreal-statetree/blob/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c/README.md)

## Limits and data handling

Decision context leaves the game process toward your configured TypeSafe endpoint.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit d8e9db62c5ef](https://github.com/gbesse/jev-unreal-statetree/tree/d8e9db62c5efb8a54002b9d553bc6e52f2657e3c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
