import speech_recognition as sr
from pyaudio import PyAudio
from speech_recognition import Microphone

# Создаём объект Recognizer
r = sr.Recognizer()

# Определяем источник звука
mic = sr.Microphone(1)

p = PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


while True:
    with mic as source:
        print("Говорите...")
        audio = r.listen(source)

    try:
        # Преобразуем записанный звук в текст
        text = r.recognize_google(audio, language="ru")
        print("Вы сказали: " + text)
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))