# import pyttsx3
import subprocess
import speech_recognition as sr
from os import path


def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 4000
        print("Listening")
        audio = r.listen(source)
    return audio


def transcribe(fs=44100):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "../myrecording.wav")
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        return r.recognize_whisper(audio, language="english")
    except sr.UnknownValueError:
        print("Whisper could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Whisper")
        return


def get_tts_engine(rate):
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    return engine


def synthesize(text, lang="en"):
    subprocess.run(["say", text])
    # engine.say(text)
    # engine.runAndWait()
    return
