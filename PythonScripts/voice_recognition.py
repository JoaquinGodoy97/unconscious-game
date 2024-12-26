# voice_recognition.py
import speech_recognition as sr
import json

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Say something!")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection")
        return ""

if __name__ == "__main__":
    speech_text = recognize_speech()
    with open("speech_output.json", "w") as f:
        json.dump({"speech_text": speech_text}, f)
