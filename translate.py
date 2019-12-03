from googletrans import Translator

def convert_into_hindi(message):
    translator = Translator()
    hindi_translate = translator.translate(message,  dest='hi')
    return hindi_translate.text