# YLE 單字與自然發音練習

Cambridge YLE（Starters / Movers / Flyers）、A2 Key（KET）、B1 Preliminary（PET）單字與 42 個自然發音的練習網頁。

- Movers：`index.html`
- Starters：`starters-vocab.html`
- Flyers：`flyers-vocab.html`
- KET（A2 Key）：`ket-vocab.html`
- PET（B1 Preliminary）：`pet-vocab.html`
- 自然發音：`phonics.html`

## 例句（Movers、Flyers）

`data/movers-sentences.json` 收錄 Movers 每個單字一句例句（附中文翻譯），由本專案撰寫，句中只使用 Cambridge Pre A1 Starters 與 A1 Movers 單字表裡的字，並沿用劍橋考試常見的人名。例句顯示在學習卡背面與單字表，「對或錯」遊戲則用另外寫的看圖說話句：`pic` 只描述圖裡畫的東西（顏色、數量、動作），`pfalse` 是同一張圖但改掉一個細節的錯誤句，音檔分別在 `audio/*/p`、`audio/*/q`；可選「讀句子」或「聽句子」（文字隱藏，練聽力），答完再顯示例句。整句發音在 `audio/uk/s`、`audio/us/s`，用 Kokoro-82M 產生：英式主要為 Fable（`bm_fable`，少數句子用 George 或 Lewis），美式為 Heart（`af_heart`），語速 0.95；發音標註用 Kokoro 官方的 misaki（Apache-2.0，依詞性分辨 lives 這類同形字），過長的停頓會縮短，再以 Whisper small.en 逐句檢查。由兩句組成的例句（如 fine、hungry、wait），美式音檔是每句分開產生再接起來，中間停頓約 0.35 秒，避免問句語調不自然；英式維持整句產生。

`data/flyers-sentences.json` 是 Flyers 的例句（478 句）與看圖句（167 句，其中 122 句附改掉一個細節的錯誤句），格式相同，句中只使用 Starters、Movers、Flyers 三級單字表裡的字（以 `tools/sentences/vocab_check.py` 檢查）；看圖句逐張對照 `img/` 裡的圖片撰寫。音檔放在 `audio/uk/flyers/`、`audio/us/flyers/`，聲音與設定同 Movers 例句（英式 Fable、美式 Heart，語速 0.95，misaki 標註發音；Fable 唸不清楚的 8 句英式改用 George 或 Lewis，列在 `data/flyers-sentences-voices.json`），由 `tools/sentences/make_audio.py` 產生，再用 `tools/sentences/check_audio.py`（Whisper small.en）逐句檢查。

Flyers 頁面（`flyers-vocab.html`）由 Movers 頁面為範本，以 `python3 tools/levels/port_level.py flyers` 產生：保留 Flyers 自己的單字、圖片、顏色與進度儲存位置，其餘功能與 Movers 相同。之後改了 Movers 頁面，重新執行這個指令即可同步到 Flyers。

## 單字來源

KET、PET 單字取自 Cambridge English 官方《A2 Key and A2 Key for Schools Vocabulary List》與《B1 Preliminary and B1 Preliminary for Schools Vocabulary List》（2025 年 8 月版），分類依官方 Topic Lists，不在主題表中的字依詞性分類；中文解釋為本專案撰寫。單字表版權屬 Cambridge University Press & Assessment，本專案與 Cambridge 無關聯。

## 發音來源

1. **真人錄音**：Wikimedia Commons 上志工錄製的英文發音檔（例如 `En-uk-*.ogg`、`En-us-*.ogg`），各檔依其頁面上的授權使用（多為 CC BY-SA 或公有領域），作者資訊請見各檔在 Commons 的頁面。
2. **預錄發音**（`audio/uk`、`audio/us`）：沒有真人錄音的單字與片語，用開源語音合成模型 [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)（Apache-2.0 授權）產生，英式聲音為 Lewis（`bm_lewis`），美式聲音為 Heart（`af_heart`），語速 0.9。每個字先放在「Okay. ＜單字＞.」裡唸，再剪出單字，避免單獨唸短字時開頭多出母音；產生後再用語音辨識模型 Whisper small.en（MIT 授權，透過 sherpa-onnx）逐一檢查，聽錯的字改用其他唸法重新產生。
3. **裝置系統語音**：以上都無法播放時的最後備援。

## 圖片來源

`img/` 中的單字圖片取自 Google [Noto Emoji](https://github.com/googlefonts/noto-emoji) 的 SVG 檔（Apache License 2.0），檔名 `e_<Unicode 編碼>.svg`。
`img/c_*.svg` 是為本專案另外繪製的圖（介系詞、星期、月份、時鐘、方位、身體部位、人名的漫畫人物、公車站等），與專案一同提供。
部分 `c_*.svg`（浴室、臥室、書店、書櫃、叉子、乾淨的盤子、棒球棒等）是把 Noto Emoji 的零件與手繪圖形組合而成，Noto 部分同樣依 Apache License 2.0 使用。
`img/m_*.svg` 是 KET、PET 中描述感受、個性、角色或動作的字所用的日式漫畫風格人物圖，為本專案繪製；人物手上拿的物品取自 Noto Emoji。
`img/t_*.svg` 是寶箱貼紙（5 套共 40 張）的日式漫畫風格圖，為本專案繪製，由 `tools/stickers/` 的程式產生（`python3 tools/stickers/build.py`）。
