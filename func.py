import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


def micro(language):
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Говорите...")
        audio = r.listen(source, 10, 15)

    try:
    # Преобразуем записанный звук в текст
        text = r.recognize_google(audio, language=language)
        print("Вы сказали: " + text)
        return text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))

def translate(text,language):
    try:
        t_text=(GoogleTranslator(source='auto', target=language).translate(text))
        print("you say: " + t_text)
        return t_text
    except:
        print("неудача")

def text_voice(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[2].id)
    engine.say(text)
    engine.runAndWait()
