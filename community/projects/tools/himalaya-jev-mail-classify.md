# himalaya-jev-mail-classify

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI (`mail-classify`) that reads Gmail threads via himalaya’s Gmail backend, asks TypeSafe Jev (OpenRouter Decisions) typed questions per thread, and applies Gmail labels/colours—dry-run by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/initrd/himalaya-jev-mail-classify) |
| Maintainer | [initrd](https://github.com/initrd). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI package **`mail-classify` 0.1.0** (`uv tool install` / `pipx`; single-module wheel). |
| Requirements | Python **≥ 3.10**; [himalaya](https://github.com/pimalaya/himalaya) **≥ 2** with **Gmail** backend (IMAP-only will not work); OpenRouter API key; `uv`/`pipx` optional. |
| License | [MIT](https://github.com/initrd/himalaya-jev-mail-classify/blob/eb86c51d42d7da1b823194b125d647d44fe149e0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `mail_classify.py`, `pyproject.toml`). Offline tests and live Gmail/Jev were **not** run on the review host. |

## When to use

Use it for idempotent, dry-run-first Gmail labeling from the shell when himalaya is already your mail CLI. Prefer [Jev Inbox](../apps/jev-inbox.md) for in-browser list reorder without applying labels; prefer [Jev Inbox Queue](../apps/jev-inbox-queue.md) for a local queue UI.

## How it works

[`mail_classify.py`](https://github.com/initrd/himalaya-jev-mail-classify/blob/eb86c51d42d7da1b823194b125d647d44fe149e0/mail_classify.py) builds a vocabulary of questions from config, constructs a compact thread state, and calls `TypeSafeClient.system_one` (via `typesafe-sdk`) over OpenRouter. Answers map to Gmail labels and colours; `--apply` writes, default is dry-run. `--check` validates secret backend, himalaya Gmail visibility, and worklist query without classifying.

## Get started

```sh
git clone https://github.com/initrd/himalaya-jev-mail-classify.git
cd himalaya-jev-mail-classify
git checkout eb86c51d42d7da1b823194b125d647d44fe149e0
uv tool install .
mkdir -p ~/.config/mail-classify && cp config.example.toml ~/.config/mail-classify/config.toml
mail-classify --check
mail-classify --limit 4          # dry run
# mail-classify --apply         # writes labels (charges + side effects)
```

## Examples and demos

- README sample dry-run table with costs.
- `tests/test_offline.py` / `test_vocabulary.py` (not executed here).
- `contrib/` launchd/systemd timers.

## Limits and data handling

Thread content fields used in questions go to OpenRouter/TypeSafe. Requires Gmail API ids via himalaya Gmail backend. Dry-run prints decisions without writing. This listing did not call himalaya or Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit eb86c51](https://github.com/initrd/himalaya-jev-mail-classify/tree/eb86c51d42d7da1b823194b125d647d44fe149e0) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, `mail_classify.py`. No live TypeSafe/OpenRouter spend.

Related: [Jev Inbox](../apps/jev-inbox.md), [Jev Inbox Queue](../apps/jev-inbox-queue.md).
