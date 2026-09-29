# jev-ultrafast-skill (SherseaHe)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Portable Agent Skill instructions and bounded runner for Jev-powered Chrome automation via browser-use/jev-ultrafast.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SherseaHe/jev-ultrafast-skill) |
| Maintainer | [SherseaHe](https://github.com/SherseaHe). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent Skill (`SKILL.md`) + small Python runner; depends on separate jev-ultrafast checkout. |
| Requirements | Agent host that loads skills; separate [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) runtime + TypeSafe key. |
| License | [MIT](https://github.com/SherseaHe/jev-ultrafast-skill/blob/59516e0d0991cdfc58c916e61b03244479899436/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Wrapper around [Jev Ultrafast](jev-ultrafast.md); not a second runtime. |

## When to use

Use to install Ultrafast as a Codex/agent Skill. Prefer the upstream [Jev Ultrafast](jev-ultrafast.md) repo for the runtime itself.

## How it works

Skill tells the agent how to invoke a bounded observation→Jev→act loop with optional viewport/URL verification. Does not vendor the Ultrafast runtime or keys. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/SherseaHe/jev-ultrafast-skill.git
cd jev-ultrafast-skill
git checkout 59516e0d0991cdfc58c916e61b03244479899436
# npx skills add SherseaHe/jev-ultrafast-skill --skill jev-ultrafast
# configure upstream jev-ultrafast per references/setup.md
```

Pin revision `59516e0d0991cdfc58c916e61b03244479899436` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Community wrapper; not affiliated with Browser Use or TypeSafe. Live Chrome/Jev not run on the review host. Distinct from the [Jev Ultrafast](jev-ultrafast.md) runtime listing.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 59516e0](https://github.com/SherseaHe/jev-ultrafast-skill/tree/59516e0d0991cdfc58c916e61b03244479899436). AI-assisted README and LICENSE inspection; install/live paths not executed.
