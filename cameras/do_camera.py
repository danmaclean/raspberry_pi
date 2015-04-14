
import picamera
import os

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
print "press Enter to shoot"
raw_input("...")
cam.hflip=True
cam.vflip=True
cam.capture(filename)