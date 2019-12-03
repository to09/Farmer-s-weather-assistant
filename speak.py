from gtts import gTTS
import os,json
from datetime import date as dt

def speak(message,name,date):
    while True:
        language ="hi"
        mytext = message
        myobj = gTTS(text=mytext, lang=language, slow=False)
        def save_file():
            try:
                today_date = str(dt.today())
                file_input = name+today_date+date
                audio_file = (file_input + ".mp3")
                os.mkdir(file_input)#creating a directory
                os.chdir(os.getcwd() + '/' + file_input)#changing the directory
                myobj.save(audio_file)

                os.system(audio_file)
                txt_file = open(file_input + ".txt", "w")
                txt_file.write(mytext)
                txt_file.close()
                exit(0)
            except:
                print("Message already send")
        save_file()
#speak("kaise ho","prajjwal","12-12-12")