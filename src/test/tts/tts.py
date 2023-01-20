from gtts import gTTS
import os

is_next = True
while is_next:
    os.system("clear")

    language = input("Language to speech (id/en): ")
    text = input("Text to convert: ")

    myobj = gTTS(text=text, lang=language, slow=False)
    filename = " ".join(text.split(" ")[:3])

    myobj.save(f"./audio/{filename}.mp3")

    con = input(f"\nAgain? (y/n): ")
    is_next = True if con == "y" else False
    
os.system("clear")
