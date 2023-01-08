from gtts import gTTS
import os
import vlc
from mutagen.mp3 import MP3

class TextToSpeech:
    def __init__(self):
        pass

    def speaker_1(self, text):
        if os.path.exists("response.mp3"):
            os.remove("response.mp3")
        language = 'en'        
        welcome = gTTS(text=text, lang=language, slow=False)
        welcome.save("response.mp3")

        audio = MP3("C:\\Users\\charl\\Desktop\\Speechtotext\\response.mp3")
        length = audio.info.length

        player = vlc.MediaPlayer("response.mp3")
        player.play()
        return length

    def speaker_2(self, text):
        if os.path.exists("response1.mp3"):
            os.remove("response1.mp3")
        language = 'en'
        welcome = gTTS(text=text, lang=language, slow=False)
        welcome.save("response1.mp3")

        audio = MP3("C:\\Users\\charl\\Desktop\\Speechtotext\\response1.mp3")
        length = audio.info.length

        player = vlc.MediaPlayer("response1.mp3")
        player.play()
        return length
