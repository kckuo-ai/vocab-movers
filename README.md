# YLE 單字與自然發音練習

Cambridge YLE（Starters / Movers / Flyers）單字與 42 個自然發音的練習網頁。

- Movers：`index.html`
- Starters：`starters-vocab.html`
- Flyers：`flyers-vocab.html`
- 自然發音：`phonics.html`

## 發音來源

1. **真人錄音**：Wikimedia Commons 上志工錄製的英文發音檔（例如 `En-uk-*.ogg`、`En-us-*.ogg`），各檔依其頁面上的授權使用（多為 CC BY-SA 或公有領域），作者資訊請見各檔在 Commons 的頁面。
2. **預錄發音**（`audio/uk`、`audio/us`）：沒有真人錄音的單字與片語，用開源語音合成模型 [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)（Apache-2.0 授權）產生，英式聲音為 Lewis（`bm_lewis`），美式聲音為 Heart（`af_heart`），語速 0.9。每個字先放在「Okay. ＜單字＞.」裡唸，再剪出單字，避免單獨唸短字時開頭多出母音；產生後再用語音辨識模型 Whisper small.en（MIT 授權，透過 sherpa-onnx）逐一檢查，聽錯的字改用其他唸法重新產生。
3. **裝置系統語音**：以上都無法播放時的最後備援。

## 圖片來源

`img/` 中的單字圖片取自 Google [Noto Emoji](https://github.com/googlefonts/noto-emoji) 的 SVG 檔（Apache License 2.0），檔名 `e_<Unicode 編碼>.svg`。
`img/c_*.svg` 是為本專案另外繪製的圖（介系詞、星期、月份、時鐘、方位、身體部位、人名的漫畫人物、公車站等），與專案一同提供。
部分 `c_*.svg`（浴室、臥室、書店、書櫃、叉子、乾淨的盤子、棒球棒等）是把 Noto Emoji 的零件與手繪圖形組合而成，Noto 部分同樣依 Apache License 2.0 使用。
