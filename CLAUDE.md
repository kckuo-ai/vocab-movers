# vocab-movers — notes for Claude sessions

Cambridge YLE / KET / PET vocabulary pages for a child, used daily on iPhone/iPad Safari,
published with GitHub Pages (kckuo-ai.github.io/vocab-movers). Reply in Traditional Chinese.

## Every session, before the first commit
- `git config core.hooksPath .githooks` — the pre-commit hook refreshes the offline manifests.

## Offline updates must stay incremental (required)
- Whenever a picture (`img/`), sound (`audio/`), data file (`data/*.json`), page (`*.html`)
  or `manifest.webmanifest` changes, run `python3 tools/offline/build_manifest.py` and commit
  `offline-manifest.json`, `offline-manifest-uk.json`, `offline-manifest-us.json` with it.
  The hook does this automatically; `python3 tools/offline/build_manifest.py --check` verifies.
- The pages compare these fingerprints with what each device stored, so 設定 → 離線使用 → 更新
  downloads only new or changed files. A stale manifest means devices miss updates.
- Keep the offline block identical in index.html, starters-vocab.html and flyers-vocab.html
  (index.html is the template for tools/levels/port_level.py). Don't rename files without need:
  a changed picture can keep its file name; the fingerprint handles the update.
- `.github/workflows/offline-manifest.yml` rebuilds the manifests after a push as a safety net.

## Publishing
- Commit locally, show previews (screenshots / audio checks), and push only after the user
  says 發布 / push / 推送 / 發送.
- After pushing, list what to test on iPhone Safari, including 設定 → 離線使用 → 更新.

## Pictures
- Check each new or redrawn picture still matches its 對或錯 sentences (`pic` / `pfalse` in
  `data/*-sentences.json`) and the example sentence.
