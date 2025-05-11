# UNIMA Voice – Trợ lý giọng nói AI

## 🎯 Mục tiêu
- Ghi âm giọng nói từ người dùng trên trình duyệt
- Dùng Whisper (OpenAI) để chuyển thành văn bản
- Phản hồi bằng AI (mẫu hoặc thật)
- Chuyển văn bản thành giọng nói với gTTS
- Phát lại giọng nói phản hồi trên trình duyệt

## 🚀 Cách chạy local
```bash
pip install -r requirements.txt  # hoặc thủ công: flask, gtts, whisper, torch
python server.py
