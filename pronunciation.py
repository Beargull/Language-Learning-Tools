import speech_recognition as sr
import pinyin
import translators as ts


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='zh-CN')
            said1 = pinyin.get(said, format="numerical")
            print(said1 + '\n')
        except Exception as e:
            print('L2ChineseBruh :) ' + str(e))


print('Use pinyin and 1,2,3,4 instead of accent')
check = input("What word would you like to practice?: ")
print(check)


while True:
    text = get_audio()
    pinyin = check
    if text == pinyin:
        print('Good job:')
    else:
        print('Try again')
