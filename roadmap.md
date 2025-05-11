🛣️ **UNIMA Voice – Roadmap Triển Khai Giai Đoạn 2025**

---

## 🧱 GIAI ĐOẠN 1: KIẾN TRÚC HẠ TẦNG (đã hoàn thành ✅)

* [x] Thiết kế giao diện ghi âm người dùng
* [x] Xử lý frontend + backend giao tiếp (index.html ↔ FastAPI)
* [x] Nhận diện giọng nói bằng Whisper `base`, `medium`, `large-v3`
* [x] Hiển thị transcript
* [x] Chạy thử thành công mô hình Whisper trên máy thật (12GB RAM)

---

## 🤖 GIAI ĐOẠN 2: AI PHẢN HỒI + PHÁT LẠI TTS (đang triển khai 🔄)

* [ ] Kết nối transcript → AI phản hồi (GPT-3.5 hoặc mô phỏng nội bộ)
* [ ] Phát lại câu trả lời bằng `gTTS`
* [ ] Cho phép chọn mô hình phản hồi (OpenAI / LLaMA / nội bộ)
* [ ] Lưu cặp transcript ↔ phản hồi vào file `.jsonl`

---

## 📊 GIAI ĐOẠN 3: THU THẬP & XÂY DỰNG DỮ LIỆU HUẤN LUYỆN

* [ ] Tạo thư mục `datasets/` lưu audio + transcript
* [ ] Tạo script thu thập Mozilla Common Voice + TEDx
* [ ] Xây script lọc video YouTube có giấy phép CC
* [ ] Chuẩn hóa dữ liệu về định dạng `.wav + .txt` hoặc `.jsonl`
* [ ] Tự ghi nguồn + giấy phép hợp pháp hoá dữ liệu

---

## 🧠 GIAI ĐOẠN 4: HUẤN LUYỆN AI RIÊNG & TRIỂN KHAI OFFLINE

* [ ] Fine-tune mô hình trả lời nội bộ (Mistral / Phi / LLaMA)
* [ ] Dịch ngôn ngữ: Meta NLLB + bộ dữ liệu mở
* [ ] Chạy mô hình bằng `llama.cpp` / `gguf`
* [ ] Kết nối toàn bộ pipeline offline: Giọng nói → AI → Dịch → TTS
* [ ] Tối ưu để chạy trên server cá nhân / edge device

---

## 🔐 GIAI ĐOẠN 5: ĐÓNG GÓI MỞ RỘNG VÀ THƯƠNG MẠI HÓA

* [ ] Đóng gói toàn bộ thành hệ thống mã nguồn mở
* [ ] Thiết kế module độc lập: `voice-client`, `voice-api`, `voice-model`
* [ ] Cấp quyền truy cập bằng API nội bộ
* [ ] Cho phép người dùng tự huấn luyện bằng giọng thật
* [ ] Đăng ký nhãn hiệu / phát hành bản thương mại (nếu muốn)

---

✅ Mỗi lần cập nhật tiến độ, sẽ push `roadmap.md` lên GitHub để ghi lại rõ giai đoạn & mốc hoàn thành.

👉 Bước tiếp theo: tạo file `data_sources.md` tổng hợp nguồn giọng nói huấn luyện được phép dùng.
