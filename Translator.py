
#import the following necessary modules from pypi.org
import os
import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound

#To recognise the audio
r = sr.Recognizer()

#To translate the audio - text 
trasnlator = google_translator()


#Continued loop asking for audio input

while True:
    with sr.Microphone() as source:
        print('Hey this is Ziya!')
        print('What you want me to Translate?')

        #To Listen the audio from source and store in the variable
        audio = r.listen(source)

        try:
            #Recognising the audio and converting it into text fromat
            speech_text = r.recognize_google(audio, language='en')
            print(speech_text)


            if(speech_text == 'exit'):
                break
        
        except sr.UnknownValueError:
            print('Could not Understand')
        
        except sr.RequestError:
            print('Cound not process your request')


        #Transalting the text in desired language   
        translated_text= trasnlator.translate(speech_text, lang_tgt='fr')
        print(translated_text)

        #Converting translated text to audio file
        voice = gTTS(translated_text, lang='fr')
        voice.save('voice.mp3')

        #Reading the audio file
        playsound('voice.mp3')
        os.remove('voice.mp3')
    
