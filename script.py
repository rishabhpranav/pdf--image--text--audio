from pdf2image import convert_from_path
import pytesseract
from gtts import gTTS
import os
from mutagen.mp3 import MP3
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pages = convert_from_path('sample.pdf')

i=1;
for page in pages:
    page.save("%s-page%d.jpg" % ('sample.pdf',pages.index(page)), "JPEG")
    st="  page no "+str(i)
    tex=pytesseract.image_to_string(page)
    tts=gTTS(text=st+tex,lang="en")
    
    audio = MP3("hello-"+str(i)+".mp3")
    if(i==1):
        tts.save("hello-"+str(i)+".mp3")
        os.system("start hello-1.mp3")
    else:
        tts.save("hello-"+str(i)+".mp3")
        sleep(audio.info.length)    
        os.system("start hello-"+str(i)+".mp3")
    i=i+1    
