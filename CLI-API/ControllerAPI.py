import requests
import json
import config as cf

class ControllerAPI:

    _server=cf.SERVER

    def __init__():

        pass

    def manageError(code):


    def authenticateUser(username, password):
        message= {"username": username, "password": password}
        task="/auntenticate/"
        path= _server+task

        resp = requests.put(path, json=message)
        if resp.status_code != 201:
            raise ApiError('PUT /authenticate/ {}'.format(resp.status_code))
            return False
        elif (resp.json()["Respuesta"]=="False"):
            return False
        else:
            return True

    def makeRequest(username,text):
        message= {"username": username, "solicitud": text}
        task="/request/"
        path=_server+task

        resp = requests.put(path, json=message)
        if resp.status_code != 201:
            raise ApiError('PUT /request/ {}'.format(resp.status_code))
            return "error"
        else:
            return resp.json()["Respuesta"]

            ##Respuesta puede ser un json por si contiene elementos importantes dentro.
