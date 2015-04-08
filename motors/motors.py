import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

class Motor:
    
    SECONDS_PER_REVOLUTION = 4.0
    SECONDS_PER_DEGREE = SECONDS_PER_REVOLUTION / 360.0
    
    def __init__(self, a,b,e):
        self.a = a
        self.b = b
        self.e = e
        
        GPIO.setup(self.a, GPIO.OUT)
        GPIO.setup(self.b, GPIO.OUT)
        GPIO.setup(self.e, GPIO.OUT)

    def degrees_to_time(degrees):
        return degrees * SECONDS_PER_DEGREE
        
    def go_clockwise(self,degrees=360):
        print degrees, " degrees to do"
        GPIO.output(self.a,GPIO.HIGH)
        GPIO.output(self.b,GPIO.LOW)
        GPIO.output(self.e,GPIO.HIGH)
        sleep(degrees_to_time(degrees))
        self.stop()

    def go_anticlockwise(self,degrees=360):
        GPIO.output(self.a,GPIO.LOW)
        GPIO.output(self.b,GPIO.HIGH)
        GPIO.output(self.e,GPIO.HIGH)
        sleep(self.degrees_to_time(degrees))
        self.stop()        

    def stop(self):
        GPIO.output(self.e,GPIO.LOW)
    
    def cleanup(self):
        GPIO.cleanup()

try:
    motor = Motor(4,17,18)
    motor.go_clockwise(360) 
    #sleep(2)
    motor.go_anticlockwise(360)
    #sleep(2)
    motor.cleanup()
    #motor.stop()
except:
    GPIO.cleanup()