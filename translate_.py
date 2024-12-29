from deep_translator import GoogleTranslator
def translate(text,language):
    return (GoogleTranslator(source='auto', target=language).translate(text))



text="я гулял и встретил деда мороза c лягушкой на голове"
print(translate(text,"en"))
