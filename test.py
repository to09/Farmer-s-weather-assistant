from gtts import gTTS
text= input("enter\n")
myobj = gTTS(text=text, lang="hi", slow=False)
myobj.save("hello.mp3")