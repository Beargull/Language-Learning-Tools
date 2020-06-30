import speech_recognition as sr
from transliterate import translit
import translators as ts

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='ru-RU')
            transText = ts.sogou(said, from_language='ru', to_language='en')
            print(said + '\n')
            print(translit(text, 'ru', reversed=True) + '\n')
            print(transText + '\n')
        except Exception as e:
            print('Сука блять :) ' + str(e))
    return said.lower()


while True:
    text = get_audio()

