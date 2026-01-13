from gtts import gTTS
import os
from datetime import datetime

def generate_voice(text, lang):
    os.makedirs("audio", exist_ok=True)
    filename = f"audio/alert_{datetime.now().strftime('%H%M%S')}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
