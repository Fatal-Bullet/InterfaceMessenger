import speech_recognition as sr


def reconhece():
	rec = sr.Recognizer()

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)
