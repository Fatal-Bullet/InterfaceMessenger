import speech_recognition as sr


def reconhece():
	rec = sr.Recognizer()

	with sr.Microphone() as s:
