# ChineseChest

親子歡樂象棋＆暗棋二合一 — a single-page Chinese chess (象棋) and Dark chess (暗棋) game, packaged as an installable, offline-capable PWA.

- `index.html` – the game
- `manifest.webmanifest`, `icons/` – install metadata and icons (192/512, plus maskable)
- `sw.js` – service worker (cache-first; caches the CDN assets after the first online visit)
- `make_icons.py` – regenerates the icons (needs Pillow)

All paths are relative, so it works on GitHub Pages (project sites under `/<repo>/`). Run locally with `python -m http.server` and open http://localhost:8000; install from the browser's address bar or menu. Bump `CACHE` in `sw.js` when releasing changes.