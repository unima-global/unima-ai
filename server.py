from flask import Flask, request, jsonify, send_from_directory
import os
from tts import speak

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/output.mp3')
def output_audio():
    return send_from_directory('.', 'output.mp3')

@app.route('/process', methods=['POST'])
def process_audio():
    file = request.files['audio']
    file_path = os.path.join(UPLOAD_FOLDER, 'input.wav')
    file.save(file_path)

    # (Sau này bạn thay bằng Whisper hoặc thư viện STT thật)
    transcript = "Xin chào, bạn cần gì?"

    reply = f"Tôi nghe bạn nói: {transcript}. Tôi có thể giúp gì?"

    # Đọc phản hồi ra giọng nói
    speak(reply)

    return jsonify({
        'transcript': transcript,
        'reply': reply
    })

if __name__ == '__main__':
    app.run(port=8080)
