import os
from gtts import gTTS
import uuid

def speak(text, lang="en"):
    """
    Convert text to speech and play it.
    """
    os.makedirs("audio", exist_ok=True)

    filename = f"audio/alert_{uuid.uuid4().hex}.mp3"

    tts = gTTS(
        text=text,
        lang=lang,
        slow=False
    )

    tts.save(filename)
    return filename
