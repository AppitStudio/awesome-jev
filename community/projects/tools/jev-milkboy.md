# jev-milkboy (Milkboy cornflakes comedy routine where Jev decides, line by line, whether each clue describes cornflakes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python CLI built around the Milkboy manzai routine: each line describing "Mom's favourite breakfast" is sent to Jev with one yes/no question (does this feature fit cornflakes?), and the probability picks the comeback ("that's cornflakes!" or "so it's not cornflakes"), with an adjustable threshold. The maker wrote it to try Jev 1.14's improved multilingual (Japanese) handling. README is in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kaitoy/jev-milkboy) |
| Maintainer | [kaitoy](https://github.com/kaitoy). Independently curated. |
| Format | Python CLI (uv) |
| Requirements | Python and uv (via mise) and a `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/kaitoy3_/status/2121783320019403019)). |
| Jev evidence | [`jev_milkboy/judge.py`](https://github.com/kaitoy/jev-milkboy/blob/84a6a51ead2d63afac73d12a06028a702ab3d811/jev_milkboy/judge.py) at the pinned commit. |

## When to use

- See a minimal one-question Noul program in Japanese, end to end.
- Mismatch: a reusable classifier; the prompt and replies are fixed to one comedy routine.

## How it works

`jev_milkboy/judge.py` uses the TypeSafe Python SDK (`AsyncTypeSafeClient` with a `Noul` question, default model `jev-latest`) and maps the yes probability to a reply; offline tests stub the client. Integration evidence: [`jev_milkboy/judge.py`](https://github.com/kaitoy/jev-milkboy/blob/84a6a51ead2d63afac73d12a06028a702ab3d811/jev_milkboy/judge.py).

## Get started

Install with uv, add your key, and pipe in lines.

```sh
git clone https://github.com/kaitoy/jev-milkboy && cd jev-milkboy
mise install && uv sync --extra test
cp .env.example .env    # TYPESAFE_API_KEY=...
uv run jev-milkboy lines.txt --threshold 0.7
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/kaitoy/jev-milkboy/blob/84a6a51ead2d63afac73d12a06028a702ab3d811/README.md](https://github.com/kaitoy/jev-milkboy/blob/84a6a51ead2d63afac73d12a06028a702ab3d811/README.md)
- Maker's blog post: [www.kaitoy.xyz/2026/11/15/jev-milkboy/](https://www.kaitoy.xyz/2026/11/15/jev-milkboy/)
- Maker's X post: [x.com/kaitoy3_/status/2121783320019403019](https://x.com/kaitoy3_/status/2121783320019403019)

## Limits and data handling

Each line is sent to TypeSafe on your key. The bundled lines are quoted from a third-party note.com article. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 84a6a51ead2d](https://github.com/kaitoy/jev-milkboy/tree/84a6a51ead2d63afac73d12a06028a702ab3d811). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
