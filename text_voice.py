# Import the required module for text  
# to speech conversion 
from gtts import gTTS 

from faker import Faker

fake = Faker()

  
# This module is imported so that we can  
# play the converted audio 
import os 
from playsound import playsound
  
# The text that you want to convert to audio 
# mytext = "Welcome to Pune, It is beautiful location to hangout"
# mytext = fake.country()

# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('sample1.pdf', 'rb') 

# print(pdfFileObj.extractText())
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 
# print(pageObj )
  
# extracting text from page 
print(pageObj.extractText()) 
  
# closing the pdf file object 
pdfFileObj.close() 

# mytext = pageObj.extractText()
# for i in range(0, 1):
    # pageObj = pdfReader.getPage(i) 
    # mytext += pageObj.extractText()

# print(mytext.read())  


# Language in which you want to convert 
language = 'en'  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
# myobj = gTTS(text=mytext, lang=language, slow=False) 
  


# Saving the converted audio in a mp3 file named 
# welcome  
# myobj.save("welcome.mp3") 
  
# Playing the converted file 
# os.system("mpg321 welcome.mp3") 
# playsound('welcome.mp3')


