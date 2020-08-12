import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)


print(r.recognize_google(audio))