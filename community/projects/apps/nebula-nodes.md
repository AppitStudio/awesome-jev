# Nebula Nodes (local AI creation canvas with Jev Decide, Pick Best and Box nodes that gate or choose between generated images, video and text)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local node-graph studio for image, video, audio, text, 3D and world generation with your own provider keys. Jev decision nodes put a typed judge between generators: Jev Decide asks one yes/no, pick-one or score question about text or images and works as a pass/fail gate that skips the other branch, Jev Pick Best chooses among up to 10 candidate images, Jev Box (experimental) returns a box, crop and mask, and the video QC nodes have a Jev mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JustinPerea/nebula-nodes) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/JustinPerea/nebula-nodes#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (AGPL-3.0); you supply provider and TypeSafe keys and pay for generation and judging. Checked 2026-11-05. |
| Jev evidence | [`backend/handlers/jev_decide.py`](https://github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/backend/handlers/jev_decide.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JustinPerea](https://github.com/JustinPerea). Independently curated. |
| Format | FastAPI backend and React/TypeScript frontend run locally |
| Platform and availability | Web UI served locally (Python 3.12 + Node.js 24 source build) |
| Jev's role | Typed judge nodes that gate branches, pick the best candidate image and locate objects in images. |
| Requirements | Python 3.12, Node.js 24 and FFmpeg; a `TYPESAFE_API_KEY` for the Jev nodes and your own generator keys. |
| License | [AGPL-3.0](https://github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/LICENSE) |

## When to use

- Auto-reject bad generations before spending on the next step in a creative pipeline.
- Pick the best of several candidate images with one typed call.
- Mismatch: Jev is one feature among many nodes; the README flags image input and Jev Box as experimental.

## How it works

`backend/handlers/jev_decide.py`, `jev_pick_best.py` and `jev_box.py` send typed questions to TypeSafe System One; branch nodes skip work on the path not taken. Integration evidence: [`backend/handlers/jev_decide.py`](https://github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/backend/handlers/jev_decide.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/JustinPerea/nebula-nodes.git
cd nebula-nodes
# follow the README Quickstart: backend in one terminal, frontend in another
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the Jev decision nodes section: [github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/README.md](https://github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/README.md)
- Jev guide: [github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/docs/api-guides/typesafe.md](https://github.com/JustinPerea/nebula-nodes/blob/497ec244206feb4380ab5fe8712ddcddc91927ec/docs/api-guides/typesafe.md)

## Limits and data handling

Images and text you pass through Jev nodes go to TypeSafe on your key (README: at most $0.0027 per request, $0.011 with long context); AGPL-3.0 terms apply if you host a modified version for others. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 497ec244206f](https://github.com/JustinPerea/nebula-nodes/tree/497ec244206feb4380ab5fe8712ddcddc91927ec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
