import sys
from faster_whisper import WhisperModel

if len(sys.argv) < 2:
    print("❗ Vui lòng truyền vào đường dẫn file audio.")
    sys.exit(1)

audio_path = sys.argv[1]
model = WhisperModel("base", compute_type="int8")

segments, info = model.transcribe(audio_path)
result_text = ""
for segment in segments:
    result_text += segment.text.strip() + " "

# FIX lỗi encoding Windows
print(result_text.strip().encode('utf-8', errors='ignore').decode())
