# jev.zig

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Zig client for the TypeSafe System One API (Jev) with compile-time typed questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jakeknowlton/jev.zig) |
| Maintainer | [jakeknowlton](https://github.com/jakeknowlton). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Zig library (`jev.zig`) packaged for `zig fetch`. |
| Requirements | Zig 0.16.0; `TYPESAFE_API_KEY` for live calls. |
| License | [MIT](https://github.com/jakeknowlton/jev.zig/blob/9fd800c10f059e6f3c2be0eb9c750367fcc94212/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when a Zig program needs typed System One / Jev decisions. Prefer official Python/JS SDKs for mainstream stacks.

## How it works

Declares questions as Zig structs; misspelled options and invalid score shapes are compile errors. Unofficial community client. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/jakeknowlton/jev.zig.git
cd jev.zig
git checkout 9fd800c10f059e6f3c2be0eb9c750367fcc94212
# or: zig fetch --save git+https://github.com/jakeknowlton/jev.zig#v0.1.0
# see examples/triage.zig
```

Pin revision `9fd800c10f059e6f3c2be0eb9c750367fcc94212` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Unofficial SDK. Live TypeSafe calls not run on the review host. Zig 0.16 required.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 9fd800c](https://github.com/jakeknowlton/jev.zig/tree/9fd800c10f059e6f3c2be0eb9c750367fcc94212). AI-assisted README and LICENSE inspection; install/live paths not executed.
