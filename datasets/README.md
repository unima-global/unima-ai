📂 **UNIMA Voice – Hướng dẫn lưu trữ và chuẩn hóa dữ liệu huấn luyện**

---

## 🗂️ Cấu trúc thư mục dữ liệu đề xuất

```
datasets/
  ├── common_voice_vi/
  │     ├── clips/                  # file .mp3 hoặc .wav
  │     └── validated.tsv          # transcript
  ├── vivos/
  │     ├── wav/                   # file .wav
  │     └── text/                  # transcript
  ├── youtube_cc/
  │     ├── audio/                 # .mp3 tải từ yt-dlp
  │     ├── subtitles/             # .vtt hoặc .srt phụ đề
  │     └── whisper_transcript/    # .txt sau khi xử lý
  ├── user_recordings/
  │     ├── voice.webm             # giọng người dùng ghi âm
  │     └── transcript.txt         # kết quả transcript
  └── metadata.csv                 # tổng hợp: filename, transcript, nguồn, giấy phép
```

---

## 🛠️ Chuẩn hóa dữ liệu audio

* Format audio chuẩn: **mono**, **16kHz**, **.wav** (nếu huấn luyện mô hình nội bộ)
* Dùng `ffmpeg` để chuyển:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

---

## 🧾 File `metadata.csv` mẫu

| filename        | transcript             | source          | license |
| --------------- | ---------------------- | --------------- | ------- |
| cv\_vi\_001.wav | Tôi tên là Minh.       | common\_voice   | CC0     |
| vivos\_010.wav  | Em muốn đi siêu thị.   | vivos           | CC-BY   |
| yt\_abc123.mp3  | Xin chào các bạn...    | youtube\_cc     | CC-BY   |
| rec001.webm     | Tôi đang thử nghiệm... | user\_recording | UNIMA   |

---

✅ Lưu trữ và chuẩn hóa đúng giúp huấn luyện AI ổn định, pháp lý rõ ràng, và dễ quản lý theo thời gian.
