import PyPDF4
from gtts import gTTS 
from playsound import playsound

reader = PyPDF4.PdfFileReader('sample10.pdf')
text = ""
for pagenum in range(reader.numPages):
    page = reader.getPage(pagenum)
    text += page.extractText()

language = 'en'  

myobj = gTTS(text=text, lang=language, slow=False) 
myobj.save("welcome.mp3") 
print(text)
playsound('welcome.mp3')
