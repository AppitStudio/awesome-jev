# effortless-hermes

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent port of effortless: a fast judge (Jev/TypeSafe, local model or custom) picks reasoning effort per turn by rewriting existing effort fields.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ivcained/effortless-hermes) |
| Maintainer | [ivcained](https://github.com/ivcained). Independently curated. |
| Format | Hermes Agent plugin (Python) |
| Requirements | Hermes Agent; TypeSafe key or local/custom judge endpoint. |
| License | [MIT](https://github.com/ivcained/effortless-hermes/blob/ebc743fee654a91a36d731fd7059f16a231542f5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`judge.py`](https://github.com/ivcained/effortless-hermes/blob/ebc743fee654a91a36d731fd7059f16a231542f5/judge.py) at the pinned commit. |

## When to use

- Lower effort for easy Hermes turns without changing the model or prompt-cache prefix.
- Mismatch: port of HeyCubit/effortless (already listed) for a different host.

## How it works

Once per user turn a middleware asks the judge; it rewrites only effort carriers already present. Explicit effort phrases win; unsure (<0.5) or failed judges fall through to a fallback, then keep current effort. Integration evidence: [`judge.py`](https://github.com/ivcained/effortless-hermes/blob/ebc743fee654a91a36d731fd7059f16a231542f5/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
# install as a Hermes plugin per README, then set TYPESAFE_API_KEY (or the typesafe_key setting)
/effortless test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- `/effortless` shows the last 50 verdicts.
- Tests: `tests/`.

## Limits and data handling

User message and recent context go to the judge provider.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit ebc743fee654](https://github.com/ivcained/effortless-hermes/tree/ebc743fee654a91a36d731fd7059f16a231542f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
