🎙️ **UNIMA Voice – Nguồn Dữ Liệu Giọng Nói Dùng Huấn Luyện (Data Sources)**

---

## ✅ 1. Mozilla Common Voice

* Trang: [https://commonvoice.mozilla.org/en/datasets](https://commonvoice.mozilla.org/en/datasets)
* Ngôn ngữ: >100, có tiếng Việt (\~40h)
* Giấy phép: **CC-0 (Public Domain)** → dùng thương mại 100%
* File tải: `.tsv` (transcript) + `.mp3`

---

## ✅ 2. VIVOS Corpus (Vietnamese Speech Corpus)

* Trang: [https://ailab.hcmus.edu.vn/vivos/](https://ailab.hcmus.edu.vn/vivos/)
* Ngôn ngữ: Tiếng Việt giọng chuẩn miền Bắc
* Giấy phép: CC-BY 4.0 → ghi nguồn khi sử dụng
* Tập tin: `.wav` + `.txt`

---

## ✅ 3. Lingua Libre (Wikimedia)

* Trang: [https://lingualibre.org](https://lingualibre.org)
* Nội dung: từ vựng + câu lẻ từ cộng đồng Wikimedia
* Giấy phép: CC0 / CC-BY-SA (có thể dùng nếu ghi nguồn)

---

## ✅ 4. YouTube (Creative Commons Filtering)

* Cách lọc: Vào YouTube → Bộ lọc → chọn “Creative Commons”
* Giấy phép dùng được: **CC-BY hoặc CC0**
* Công cụ đề xuất: `yt-dlp` + `whisper` để tự tạo transcript
* ⚠️ Không dùng video có bản quyền nhạc, clip phim, v.v.

---

## ✅ 5. TEDx / MTEDx Corpus

* Dự án: Multilingual TEDx (OpenSLR.org / HuggingFace)
* Có subtitle song ngữ (ví dụ English – Vietnamese)
* Giấy phép: CC-BY hoặc Public
* Dạng file: `.wav` + `.srt` hoặc `.json`

---

## ✅ 6. OpenSLR.org

* Trang: [http://openslr.org](http://openslr.org)
* Các bộ: LibriSpeech, AISHELL, THCHS-30, RIR, SLR61...
* Ngôn ngữ: Anh, Trung, Đức, Ả Rập, Tây Ban Nha...
* Nhiều bộ có transcript + audio chuẩn huấn luyện mô hình

---

## ✅ 7. HuggingFace Datasets

* Dữ liệu từ Mozilla, TEDx, CommonVoice có thể tải qua Hugging Face
* Lệnh: `datasets.load_dataset('mozilla-foundation/common_voice_11_0', 'vi')`

---

## ✅ 8. Tự thu thập qua hệ thống UNIMA Voice

* Người dùng ghi âm thực tế → lưu `.webm` + transcript
* Lưu lại dưới dạng cặp `giọng nói` ↔ `text` → dùng fine-tune

---

## 📁 Gợi ý thư mục lưu dữ liệu

```
/datasets
  ├── /common_voice_vi
  ├── /vivos
  ├── /tedx_vi
  ├── /youtube_cc
  ├── /user_recordings
  └── metadata.csv (gồm: filename, transcript, nguồn, license)
```

---

✅ Tất cả nguồn trên đều được phép sử dụng cho mục đích huấn luyện AI nếu tuân thủ đúng giấy phép (ghi nguồn hoặc CC-0).
