import speech_recognition as sr

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Talk to J.A.R.V.I.S: ")
	    audio = r.listen(source)
	try:
	    print(r.recognize_google(audio))
	    return r.recognize_google(audio)
	except sr.UnknownValueError:
	    offline_speak("I couldn't understand what you said! Would you like to repeat?")
	    return(listen())
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

listen()