GPIO.setmode(GPIO.BCM)
from time import sleep
import Rpi.GPIO as GPIO

import picamera

class PiCam(self):
     
     def __init__(self):
         self.cam = picamera.PiCamera()
    

class CableRelease(self,pin1,pin2):
    
    def __init__(self):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
    
    def shoot(self,wait=0.5):
        ##focus...
        GPIO.output(self.pin1,True)
        sleep(wait)
        ## shutter release
        GPIO.output(self.pin2, True)
        sleep(wait)
        ##clean up
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
    