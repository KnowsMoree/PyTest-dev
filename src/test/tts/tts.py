from gtts import gTTS
import os

os.system("clear")

language = input("Language to speech (id/en): ")
text = input("Text to convert: ")

myobj = gTTS(text=text, lang=language, slow=False)
filename = " ".join(text.split(" ")[:3])

myobj.save(f"./audio/{filename}.mp3")
os.system("clear")
