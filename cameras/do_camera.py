
import picamera
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

prefix = 'ir_image'
suffix = '.jpg'
number = 0
filename = prefix + str(number) + suffix

files = os.listdir('.')

while filename in files:
    number += 1
    filename = prefix + str(number) + suffix

cam = picamera.PiCamera()
cam.start_preview()
GPIO.output(17,True)
print "press Enter to shoot"
raw_input("...")
cam.hflip=True
cam.vflip=True
cam.capture(filename)
GPIO.output(17,False)