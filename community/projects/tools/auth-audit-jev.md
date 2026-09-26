# auth-audit-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental observation-only Python EventPlugin for OAuth/IAM authn/authz event envelopes: TypeSafe Jev evaluates allowlisted kinds asynchronously and may emit advisory alerts—never blocks or changes the auth flow.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ianlintner/auth-audit-jev) |
| Maintainer | [ianlintner](https://github.com/ianlintner). Independently curated. |
| Format | Python package + Docker demo + GitHub Pages docs. |
| Requirements | Python 3.11+ (stdlib runtime); optional TYPESAFE_API_KEY for live cloud; tests use fake transport. |
| License | [MIT](https://github.com/ianlintner/auth-audit-jev/blob/547bd057474006fccfd791d3b34901bca2a4ae85/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Docker demo uses fake transport. |

## When to use

Use to **shadow-audit** auth events with typed Jev judgments beside an existing EventBus. Do not put provider calls on the authorization critical path.

## How it works

[`src/auth_audit_jev/`](https://github.com/ianlintner/auth-audit-jev/tree/547bd057474006fccfd791d3b34901bca2a4ae85/src/auth_audit_jev) implements AuditPlugin: allowlisted kinds → async Jev assessment → optional alert callback with redacted `{event_kind, outcome, assessment}` only.

## Get started

```sh
git clone https://github.com/ianlintner/auth-audit-jev.git
cd auth-audit-jev
git checkout 547bd057474006fccfd791d3b34901bca2a4ae85
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m unittest discover -s tests -v
```

## Examples and demos

- docker compose synthetic demo on loopback (fake Jev transport).
- Docs: [https://ianlintner.github.io/auth-audit-jev/](https://ianlintner.github.io/auth-audit-jev/)

## Limits and data handling

Live mode sends allowlisted event fields to TypeSafe. Plugin must not enforce deny/grant. High-confidence alerts are review hints, not proof of malice.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 547bd05](https://github.com/ianlintner/auth-audit-jev/tree/547bd057474006fccfd791d3b34901bca2a4ae85). AI-assisted README and LICENSE inspection of package layout; install/live paths not executed.
