import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

def setup():
    '''Sets up the pins'''
    Motor1A = 4 #pin A
    Motor1B = 17 #pin B
    Motor1E = 18 #pin Enable
 
    #tell pi what these pins are and whether they are in or output - in this case output... 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

def go_clockwise(): 
    print "Going clockwise"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

def stop():
     print "Stopping motor"
     GPIO.output(Motor1E,GPIO.LOW)
     
setup()
go_clockwise() 
sleep(2)
stop()
 
 
GPIO.cleanup()