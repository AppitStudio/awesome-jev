# ghostel-ai (natural-language commands for Emacs ghostel with a Jev gate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Emacs minor mode for ghostel's line mode: Jev decides whether what you typed is a shell command or a plain-words instruction and flags destructive input for confirmation; gptel turns instructions into commands for review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dakra/ghostel-ai) |
| Maintainer | [dakra](https://github.com/dakra). Independently curated. |
| Format | Emacs package (Emacs Lisp) |
| Requirements | Emacs 30.1, ghostel 0.57.0, gptel 0.9.9; a TypeSafe API key. |
| License | [GPL-3.0](https://github.com/dakra/ghostel-ai/blob/b6f9c4afc4ac652a0f7544beff7baeb4612e4e49/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ghostel-ai.el`](https://github.com/dakra/ghostel-ai/blob/b6f9c4afc4ac652a0f7544beff7baeb4612e4e49/ghostel-ai.el) at the pinned commit. |

## When to use

- Type plain words at a shell prompt in Emacs and get a command to review.
- Get a y-or-n prompt before destructive commands run.
- Mismatch: needs ghostel and a configured gptel backend.

## How it works

`ghostel-ai.el` posts the input to `https://api.typesafe.ai/v1/systemone` with `jev-latest` to classify it and rate how destructive it is; translation and completion use gptel. Integration evidence: [`ghostel-ai.el`](https://github.com/dakra/ghostel-ai/blob/b6f9c4afc4ac652a0f7544beff7baeb4612e4e49/ghostel-ai.el).

## Get started

From the upstream README (not run on the review host):

```sh
(use-package ghostel-ai
  :vc (:url "https://github.com/dakra/ghostel-ai")
  :hook (ghostel-mode . ghostel-ai-mode))
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dakra/ghostel-ai#readme](https://github.com/dakra/ghostel-ai#readme)

## Limits and data handling

Typed input is sent to TypeSafe; translations also go to your gptel provider.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b6f9c4afc4ac](https://github.com/dakra/ghostel-ai/tree/b6f9c4afc4ac652a0f7544beff7baeb4612e4e49). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
