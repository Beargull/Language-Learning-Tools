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
			transText = ts.sogou(said, from_language='zh', to_language='en')
			print(said + '\n')
			print(pinyin.get(said, format="strip", delimiter=" ") + '\n')
			print(pinyin.get(said, format="numerical") + '\n')
			print(transText + '\n')
		except Exception as e:
			print('L2ChineseBruh :) ' + str(e))

	return said.lower()


while True:
	text = get_audio()
