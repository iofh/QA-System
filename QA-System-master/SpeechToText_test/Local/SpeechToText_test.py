#transfer live audio to text

import speech_recognition as sr #import python SpeechRecognition library
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source) #using speech_recognition lisen function



print(r.recognize_google(audio)) #print text