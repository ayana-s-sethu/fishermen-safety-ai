import os
import speech_recognition as sr
from utils.tts import speak
from district_map import DISTRICT_DATA

recognizer = sr.Recognizer()

# ---------------- LANGUAGE SELECTION ----------------
print("\n==============================")
print("Choose Language")
print("1 - English")
print("2 - Malayalam")
print("==============================")

choice = input("Enter choice (1 / 2): ").strip()

if choice == "2":
    lang = "ml"
    prompt_text = "🎤 ജില്ലയുടെ പേര് പറയുക..."
else:
    lang = "en"
    prompt_text = "🎤 Speak district name..."

# ---------------- SPEECH INPUT ----------------
with sr.Microphone() as source:
    print(prompt_text)
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

try:
    district = recognizer.recognize_google(audio, language="ml-IN" if lang == "ml" else "en-IN")
    district = district.strip().lower()
    print(f"You said: {district}")
except:
    print("Could not understand audio")
    exit()

# ---------------- FETCH DATA ----------------
data = DISTRICT_DATA.get(district)

if not data:
    msg = "District not found." if lang == "en" else "ജില്ല കണ്ടെത്താനായില്ല."
    print(msg)
    speak(msg, lang)
    exit()

risk = data["risk"]
wind = data["wind"]

# ---------------- CLEAN OUTPUT (IMPORTANT FIX) ----------------
if lang == "ml":
    message = (
        "മത്സ്യത്തൊഴിലാളികൾ ശ്രദ്ധിക്കുക. "
        f"ഈ പ്രദേശത്ത് അപകടനില {risk} ആണ്. "
        f"കാറ്റിന്റെ വേഗത മണിക്കൂറിൽ {wind} കിലോമീറ്റർ ആണ്. "
        "കടലിൽ പോകുമ്പോൾ അതീവ ജാഗ്രത പാലിക്കുക."
    )
else:
    message = (
        "Attention fishermen. "
        f"The risk level is {risk}. "
        f"Wind speed is {wind} kilometers per hour. "
        "Please be cautious while going to sea."
    )

# ---------------- OUTPUT ----------------
print("\n--- RESULT ---")
print(message)

audio_file = speak(message, lang)

# ---------------- PLAY AUDIO ----------------
os.startfile(audio_file)
