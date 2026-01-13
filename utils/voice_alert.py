import pyttsx3

def speak_alert(risk_data):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    message_map = {
        "HIGH": "കടലിലേക്ക് പോകരുത്. ഇന്ന് കടൽ അപകടകരമാണ്.",
        "MODERATE": "കരയ്ക്ക് അടുത്ത് മാത്രം മീൻപിടിക്കുക. നേരത്തെ തിരികെ വരണം.",
        "LOW": "ഇന്ന് മീൻപിടിക്കാൻ സുരക്ഷിതമാണ്."
    }

    message = message_map.get(
        risk_data["risk_level"],
        "കടൽ വിവരങ്ങൾ ലഭ്യമല്ല"
    )

    engine.say(message)
    engine.runAndWait()
