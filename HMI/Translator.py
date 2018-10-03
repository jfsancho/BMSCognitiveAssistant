
import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
#converts speech from "audioName" file to text
import config.py as cf

from google.cloud import texttospeech

class Translator:
    _language=cf.LANGUAGE

    def __init__(self):

        pass

    def speechToText(audioName):
        # Instantiates a client
    	client = speech.SpeechClient()

    	# The name of the audio file to transcribe
    	file_name = os.path.join(
    	    os.path.dirname(__file__),
    	    audioName)

    	# Loads the audio into memory
    	with io.open(file_name, 'rb') as audio_file:
    	    content = audio_file.read()
    	    audio = types.RecognitionAudio(content=content)

    	config = types.RecognitionConfig(
    	    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    	    language_code=self._language)

    	# Detects speech in the audio file
    	response = client.recognize(config, audio)

    	for result in response.results:

    	    return (format(result.alternatives[0].transcript))

    def textToSpeech(text):
        client = texttospeech.TextToSpeechClient() #client of the Google text to speech API
        input_text = texttospeech.types.SynthesisInput(text=text) #convertion of the input text variable


        voice = texttospeech.types.VoiceSelectionParams( #configuration of the used voice
            language_code=self._language,
            ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

        response = client.synthesize_speech(input_text, voice, audio_config)

        # the audio is stored in the output.mp3 file
        with open(cf.AUDIO_OUTPUT, 'wb') as out:
            out.write(response.audio_content)
            #print('archivo de audio creado')
