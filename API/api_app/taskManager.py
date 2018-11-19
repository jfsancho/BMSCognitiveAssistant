
from flask import session, jsonify
from .database.DBController import DBController
from .watson.watsonController import WatsonController

class TaskManager:

    db=None
    assistant=None
    def __init__(self):
        self.db=DBController()
        self.assistant=WatsonController("2018-09-20",
                                        "56ce5465-5a58-4346-895c-ffd2073c87a8",
                                        "ZPE2stC7ecX2",
                                        "https://gateway.watsonplatform.net/assistant/api",
                                        "6ea03f15-9f26-4b49-9dc3-eaff1a2050a0")

    def verifyUser(self, username, password):
        user= self.db.getUser(username)

        if(user==None):
            return False
        else:
            if(user.Password==password):
                return True
            else:
                return False
    def clasifyWatsonResponse(self, wResponse):
        intent=wResponse.intents[0]
        if(intent=="Turn_off"):
            #verify if is the end of conversation 
            #verify the needed variables from watson
            return wResponse.output
        elif(intent=="Turn_on"):
            #verify if is the end of conversation
            #get the needed variables from watson
            return wResponse.output

        else:
            return wResponse.output 
   
    def callWatson(self,text):
        wResponse=self.assistant.sendMessage(text)
        print(jsonify(wResponse))
        textResponse=self.clasifyWatsonResponse(wResponse)
        return textResponse

    



    
