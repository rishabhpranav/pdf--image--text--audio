from pdf2image import convert_from_path
import pytesseract
from gtts import gTTS
import os
from mutagen.mp3 import MP3
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
pages = convert_from_path('sample.pdf')

i=1;
for page in pages:
    page.save("%s-page%d.jpg" % ('sample.pdf',pages.index(page)), "JPEG")
    st="  page no "+str(i)
    tex=pytesseract.image_to_string(page)
    tts=gTTS(text=st+tex,lang="en")
    i=i+1
    tts.save("hello.mp3")
    audio = MP3("hello.mp3")
    os.system("start hello.mp3")
    sleep(audio.info.length)
