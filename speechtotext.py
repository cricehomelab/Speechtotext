import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def get_question(self):
        print("getting question")
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        text = self.recognizer.recognize_google(audio)
        return text

