from gtts import gTTS
import os
import vlc
from mutagen.mp3 import MP3

class TextToSpeech:
    def __init__(self):
        pass

    def speaker(self, text):
        """this take a string of text and translates it to an mp3 file."""
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
