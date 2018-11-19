import requests
import json
import config as cf
import sys

class ControllerAPI:

    _server=""

    def __init__(self):
        self._server=cf.SERVER


    def manageError(self,response):
        if response.status_code >= 500:
            print('[!] [{0}] Server Error'.format(response.status_code))
            return None
        elif response.status_code == 404:
            print('[!] [{0}] URL not found:[{1}]'.format(response.status_code,response.url))
            return None
        elif response.status_code == 401:
            print('[!] [{0}] Authentication Failed'.format(response.status_code))
            return None
        elif response.status_code == 400:
            print('[!] [{0}] Bad Request'.format(response.status_code),"Reason:", response.reason)
            return None
        elif response.status_code >= 300:
            print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
            return None
        else:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

    def authenticateUser(self,username, password):
        message= {"username": username, "password": password}
        task="/auth/login"
        path= self._server+task

        try:
            resp= requests.post(path, data=message)
            if resp.status_code != 200:
                self.manageError(resp)
                return False
            else:
                print(resp.json())
                pass
            #elif (resp.json()["Respuesta"]=="False"):
            #    return False
            #else:
            #    return True
        except:
            print("Error inesperado:", sys.exc_info()[0], "Value:", sys.exc_info()[1])

    def makeRequest(self,text):
        message= {"solicitud": text}
        task="/request"
        path=self._server+task
        try:
            resp=requests.post(path, data=message,verify=False)
            if resp.status_code != 200:
                self.manageError(resp)
                return "error"
            else:
                return resp.json()["Respuesta"]
        except:
            print("Error inesperado:", sys.exc_info()[0])


            ##Respuesta puede ser un json por si contiene elementos importantes dentro.
