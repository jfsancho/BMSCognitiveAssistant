

import Assistant.py
import ControllerNFC.py
import ControllerAPI.py
import config.py as cf
def main():
    assi=Assistant()
    cNFC=ControllerNFC()
    cAPI=ControllerAPI()


    def convertAndPlay(msj):
        assi._translator.textToSpeech(str(msj))
        assi.playAudio()

    def setChatMode(intent):
        if(intent==cf.CHAT_INTENT):
            return assi.setChatMode("on")
        else:
            return assi.setChatMode("off")


    def saludar(name):
        saludo='hola '+ name
        convertAndPlay(saludo)

    while(1):
        try:
            if(assi._chat_mode=="off"):

                (id,text)=cNFC.readRFID()
                validation=cAPI.autenticateUser(text.split()[0],id)
                #(validation,name,room,personID)=c.IDvalidation(id)
                saludar(text.split()[0])

            if(validation):
                file_name=assi.getAudio()
                text=assi._translator.speechToText(file_name)
                #print(texto)

                (audioa,intent,entity)=assistant.Awatson(texto)

                response=cAPI.makeRequest(text)
                #print(audioa)
                chat_mode=setChatMode(response.json()["intent"])
                convertAndPlay(response.json()["text"])
                
        except Exception as e:
            print('Error ocurred : '+str(e))

main()
