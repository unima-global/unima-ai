import whisper

# ⚠ Nếu không có GPU: bật dòng dưới
# import os; os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Tải mô hình chất lượng cao hơn
model = whisper.load_model("medium")  # hoặc "large" nếu máy đủ mạnh

def transcribe_audio(file_path):
    result = model.transcribe(file_path, language='vi')
    return result["text"]
