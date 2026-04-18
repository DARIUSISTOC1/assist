import sounddevice as sd
import queue
import json
import os
import webbrowser
import pyttsx3
from vosk import Model, KaldiRecognizer
from difflib import SequenceMatcher

# -----------------------
# VOIX
# -----------------------
engine = pyttsx3.init()

def speak(text):
    print("IA:", text)
    engine.say(text)
    engine.runAndWait()

# -----------------------
# LOAD JSON
# -----------------------
with open("apps.json", "r", encoding="utf-8") as f:
    apps = json.load(f)

# -----------------------
# PATH RESOLVE
# -----------------------
def resolve(path):
    path = path.replace("%APPDATA%", os.environ["APPDATA"])
    path = path.replace("%LOCALAPPDATA%", os.environ["LOCALAPPDATA"])
    return path

# -----------------------
# NORMALISATION VOCALE
# -----------------------
def normalize(text):
    text = text.lower()

    fixes = {
        "team": "steam",
        "steem": "steam",
        "discore": "discord",
        "vs code": "vscode",
        "v s code": "vscode"
    }

    for k, v in fixes.items():
        text = text.replace(k, v)

    return text

# -----------------------
# WAKE WORD (tolérant)
# -----------------------
WAKE_WORDS = ["bybo", "bibo", "bibeau", "vivo", "by bo", "baibo"]

def check_wake_word(text):
    text = text.lower()

    # match direct
    for w in WAKE_WORDS:
        if w in text:
            return True

    # fuzzy match
    for word in text.split():
        for w in WAKE_WORDS:
            if SequenceMatcher(None, word, w).ratio() > 0.75:
                return True

    return False

# -----------------------
# FIND APP
# -----------------------
def find_app(text):
    text = normalize(text)

    for name, data in apps.items():
        for kw in data.get("keywords", []):
            if kw in text:
                return name, data

    return None, None

# -----------------------
# OPEN APP
# -----------------------
def open_app(name, data):
    try:
        if data["type"] == "exe":
            os.startfile(resolve(data["path"]))
            speak(f"J'ouvre {name}")

        elif data["type"] == "shortcut":
            os.startfile(resolve(data["path"]))
            speak(f"J'ouvre {name}")

        elif data["type"] == "steam":
            webbrowser.open(data["url"])
            speak(f"Je lance {name}")

    except:
        speak("Impossible d'ouvrir l'application")

# -----------------------
# COMMAND HANDLER
# -----------------------
def handle(text):
    text = normalize(text)
    print("TU:", text)

    if "stop" in text or "arrête" in text:
        speak("Arrêt")
        exit()

    name, data = find_app(text)
    if name:
        open_app(name, data)
        return

# -----------------------
# VOSK SETUP
# -----------------------
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))

# -----------------------
# MAIN LOOP
# -----------------------
speak("Bybo en ligne")

active = False

with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype='int16',
    channels=1,
    callback=callback
):

    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = normalize(result.get("text", ""))

            if not text:
                continue

            print("RAW:", text)

            # -----------------------
            # WAKE WORD
            # -----------------------
            if not active:
                if check_wake_word(text):
                    active = True
                    speak("Oui ?")
                continue

            # -----------------------
            # COMMAND MODE
            # -----------------------
            handle(text)

            active = False