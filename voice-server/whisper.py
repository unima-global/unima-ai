import sys
from faster_whisper import WhisperModel

if len(sys.argv) < 2:
    print("❗ Vui lòng truyền vào đường dẫn file audio.")
    sys.exit(1)

audio_path = sys.argv[1]

# Dùng mô hình hỗ trợ đa ngôn ngữ, nhẹ
model = WhisperModel("base", compute_type="int8")

# Ép nhận diện tiếng Việt
segments, info = model.transcribe(audio_path, language="vi")

# Ghép kết quả thành một chuỗi
result_text = ""
for segment in segments:
    result_text += segment.text.strip() + " "

# Tránh lỗi mã hóa trên Windows (cp1252)
print(result_text.strip().encode('ascii', errors='ignore').decode())
