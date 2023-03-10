import speechtotext
import texttospeech
import question
import time

get_text = speechtotext.SpeechToText()
ai_interface = question.ArtificialIntelligence()
get_speech = texttospeech.TextToSpeech()

def main():
    get_speech.speaker("Hello, do you have a question?")
    while True:       
        question = get_text.get_question()
        print(question)
        answer = ai_interface.post_chatgpt_question(question)
        print(answer[1])
        if answer[0] == True:
            text_answer = ai_interface.get_text(answer[1])
            print(text_answer)
            length = get_speech.speaker(text_answer)
        else:
            print(answer[1])
            length = get_speech.speaker(answer[1])
        print(length)
        time.sleep(length + 2)

if __name__ == '__main__':
    main()

