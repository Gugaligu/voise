import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.say('Привет')
engine.runAndWait()