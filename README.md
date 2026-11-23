# 親子歡樂象棋＆暗棋二合一

以第二版遊戲製作的 PWA，支援象棋與暗棋，可加入手機主畫面。

## 使用

開啟 GitHub Pages 網址後，保持連線直到頁面載入及離線快取安裝完成；之後可離線開啟遊戲。首次載入需要連線下載 Tailwind CSS；離線時字型可能改用系統字型。瀏覽器可能清除快取，清除後需重新連線。

在 iPhone 或 iPad 使用 Safari 的「分享」→「加入主畫面」；在 Android 使用 Chrome 的選單→「安裝應用程式」或「加到主畫面」。

## 本機測試

在此資料夾執行 `python -m http.server 8000`，並開啟 `http://localhost:8000/`。Service Worker 需要 HTTPS 或 localhost，直接開啟 HTML 檔案無法測試離線功能。

更新遊戲或快取資源時，請一併更新 `sw.js` 中的快取版本。圖示可使用 `make_icons.py` 重新產生（需要 Pillow）。
