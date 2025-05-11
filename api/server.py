from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from faster_whisper import WhisperModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        model = WhisperModel("medium", compute_type="int8")
        segments, _ = model.transcribe(filepath, language="vi")
        result = " ".join([segment.text for segment in segments])
        return {"transcript": result}
    except Exception as e:
        print("LỖI:", e)
        return {"error": str(e)}
