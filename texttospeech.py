from gtts import gTTS
import os
import vlc
import time

class TextToSpeech:
    def __init__(self):
        pass

    def speaker_1(self, text):
        if os.path.exists("response.mp3"):
            os.remove("response.mp3")
        language = 'en'        
        welcome = gTTS(text=text, lang=language, slow=False)
        welcome.save("response.mp3")
        player = vlc.MediaPlayer("response.mp3")
        player.play()
    
    def speaker_2(self, text):
        if os.path.exists("response1.mp3"):
            os.remove("response1.mp3")
        language = 'en'        
        welcome = gTTS(text=text, lang=language, slow=False)
        welcome.save("response1.mp3")
        player = vlc.MediaPlayer("response1.mp3")
        player.play()
        return player.get_length()
