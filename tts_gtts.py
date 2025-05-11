from gtts import gTTS

text = "Xin chào bạn, tôi là UNIMA. Rất vui được trò chuyện với bạn bằng tiếng Việt."
tts = gTTS(text, lang='vi')
tts.save("output.mp3")
print("✅ Đã tạo file output.mp3 – bạn có thể mở để nghe lại.")
