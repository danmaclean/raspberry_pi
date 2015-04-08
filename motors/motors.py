import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

class Motor:
    
    def __init__(self, a,b,e):
        self.a = a
        self.b = b
        self.e = e
        
        GPIO.setup(self.a, GPIO.OUT)
        GPIO.setup(self.b, GPIO.OUT)
        GPIO.setup(self.e, GPIO.OUT)
    
    def go_clockwise(self):
        GPIO.output(self.a,GPIO.HIGH)
        GPIO.output(self.b,GPIO.LOW)
        GPIO.output(self.e,GPIO.HIGH)

    def stop(self):
        GPIO.output(self.e,GPIO.LOW)
    


     
motor = Motor(4,17,18)
motor.go_clockwise() 
sleep(2)
motor.stop()
 
 
GPIO.cleanup()