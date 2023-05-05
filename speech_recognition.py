import speech_recognition as sr

def listen():
    """
    Uses the speech recognizer object to listen for user input and returns the transcribed text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return r.recognize_google(audio)
