from fastapi import FastAPI, Query
from gtts import gTTS
import uuid
import os

from district_map import DISTRICT_DATA, MALAYALAM_DISTRICTS

app = FastAPI(
    title="Fishermen Safety AI",
    version="0.1.0"
)

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"status": "Fishermen Safety AI Running"}


@app.get("/predict-risk")
def predict_risk(
    district: str = Query(...),
    lang: str = Query("en")
):
    district_key = district.lower().strip()

    # Malayalam mapping
    if lang == "ml":
        district_key = MALAYALAM_DISTRICTS.get(district, "")

    if district_key not in DISTRICT_DATA:
        return {"error": "District not found"}

    # Dummy weather
    wind_speed = 18
    risk_level = "MODERATE"

    if lang == "ml":
        message = (
            "മത്സ്യത്തൊഴിലാളികൾ ശ്രദ്ധിക്കുക. "
            "ഈ പ്രദേശത്ത് അപകടനില MODERATE ആണ്. "
            "കാറ്റിന്റെ വേഗത മണിക്കൂറിൽ 18 കിലോമീറ്റർ ആണ്. "
            "കടലിൽ പോകുമ്പോൾ അതീവ ജാഗ്രത പാലിക്കുക."
        )
        tts_lang = "ml"
    else:
        message = (
            "Attention fishermen. "
            "The risk level is MODERATE. "
            "Wind speed is 18 kilometers per hour. "
            "Please be cautious while going to sea."
        )
        tts_lang = "en"

    filename = f"alert_{uuid.uuid4().hex}.mp3"
    audio_path = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=message, lang=tts_lang)
    tts.save(audio_path)

    return {
        "district": district,
        "risk_level": risk_level,
        "weather": {
            "wind_speed": wind_speed,
            "wave_height": 1.6,
            "rain": False,
            "visibility": "Good"
        },
        "message": message,
        "audio_file": audio_path
    }
