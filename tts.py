from gtts import gTTS

def speak(text):
    tts = gTTS(text, lang='vi')
    tts.save("output.mp3")
