
#!/usr/bin/env python
import RPi.GPIO as GPIO

import SimpleMFRC522

class ControllerNFC:


    def __init__(self):

    def readRFID():
        reader = SimpleMFRC522.SimpleMFRC522()
        try:
            id, text = reader.read()
            return (id, text)
        except Exception as e:
            print( 'Error occurred : ' + str(e))
        finally:
            GPIO.cleanup()
