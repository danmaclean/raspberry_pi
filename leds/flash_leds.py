

 #!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GREEN = 18
RED = 23
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

x = 1
while True:
	if x == 1:
		GPIO.output(GREEN, True)
		GPIO.output(RED, False)
		x = 2
		time.sleep(1)
	elif x == 2:
		GPIO.output(GREEN, False)
		GPIO.output(RED, True)
		time.sleep(1)
		x = 1
	print "in loop\n"

