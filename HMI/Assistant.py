
import speech_recognition as sr
import config.py as cf
import os

class Assistant:

    _chat_mode= ""
    _language= ""
    _translator=Translator()

    def __init__(self):

        self._chat_mode= cf.CHAT_MODE
        self._language=cf.LANGUAGE

    def getAudio(self):
        CHUNK_SIZE= 512
        sample_rate = 44100
        mic_name="USB PnP Sound Device: Audio (hw:0,0)"

        r = sr.Recognizer()
        #mic_list = sr.Microphone.list_microphone_names()

        for i, microphone_name in enumerate(mic_list):
            if microphone_name == mic_name:
                device_id = i
                name=microphone_name

        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                                chunk_size = CHUNK_SIZE) as source:
            r.adjust_for_ambient_noise(source)

            #listens for the user's input
            audio = r.listen(source, timeout=30, phrase_time_limit=30)

        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())
        return audio_file

    def playAudio(self):
        outputAudio=cf.AUDIO_OUTPUT
        os.system("aplay "+outputAudio)

    def getChatMode():
        return self._chat_mode

    def setChatMode(pchat_mode):
        self._chat_mode=pchat_mode

    def getLanguage():
        return self._language

    def setLanguage():
        self._language
