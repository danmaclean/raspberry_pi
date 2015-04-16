#!/usr/bin/env python
# encoding: utf-8
"""
stepper_motor.py


Created by Dan MacLean (TSL) on 2014-08-10.
Copyright (c) 2014 Dan MacLean. All rights reserved.
"""

import sys
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class StepperMotor:
    
    def __init__(self, pin1,pin2,pin3,pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
        GPIO.output(self.pin3, False)
        GPIO.output(self.pin4, False)
        self.sequence = [[True,False,False,False],
        [True,True,False,False],
        [False,True,False,False],
        [False,True,True,False],
        [False,False,True,False],
        [False,False,True,True],
        [False,False,False,True],
        [True,False,False,True]]
        self.reverse_sequence = reversed(self.sequence)
    
    def clockwise(self,steps,delay=(1/1000.0)):
        print "clockwise"
        StepperMotor.move(self,self.sequence,steps,delay)
    
    def anticlockwise(self,steps,delay=(1/1000.0)):
        StepperMotor.move(self,self.reverse_sequence,steps,delay) 
    
    def move(self,sequence,steps, delay=(1/1000.0)):
        print "move"
        for i in range(0,steps):
            print i
            for s in sequence:
                print s
                StepperMotor.set_step(self,s,delay)
    
    def set_step(self,s,delay):
        print "s is", s
        GPIO.output(self.pin1, s[0])
        time.sleep(delay)
        GPIO.output(self.pin2, s[1])
        time.sleep(delay)
        GPIO.output(self.pin3, s[2])
        time.sleep(delay)
        GPIO.output(self.pin4, s[3])
        time.sleep(delay)
    

try:
    print "trying motor"
    motor = StepperMotor(17,18,21,22)
    motor.clockwise(512) 
    #motor.anticlockwise(4)
    GPIO.cleanup()
except:
    GPIO.cleanup()

'''
def main():
	GPIO.setmode(GPIO.BCM)
	enable_pin = 18
	coil_A_1_pin = 4
	coil_A_2_pin = 17
	coil_B_1_pin = 23
	coil_B_2_pin = 24
	
	GPIO.setup(enable_pin, GPIO.OUT)
	GPIO.setup(coil_A_1_pin,GPIO.OUT)
	GPIO.setup(coil_A_2_pin, GPIO.OUT)
	GPIO.setup(coil_B_1_pin, GPIO.OUT)
	GPIO.setup(coil_B_2_pin, GPIO.OUT)
	GPIO.output(enable_pin,1)
	
	def forward(delay,steps):
		for i in range(0,steps):
			setStep(1,0,1,0)
			time.sleep(delay)
			setStep(0,1,1,0)
			time.sleep(delay)
			setStep(0,1,0,1)
			time.sleep(delay)
			setStep(1,0,0,1)
			time.sleep(delay)
	
	def backwards(delay,steps):
		for i in range(0,steps):
			setStep(1,0,0,1)
			time.sleep(delay)
			setStep(0,1,0,1)
			time.sleep(delay)
			setStep(0,1,1,0)
			time.sleep(delay)
			setStep(1,0,1,0)
			time.sleep(delay)
	
	def setStep(w1,w2,w3,w4):
		GPIO.output(coil_A_1_pin, w1)
		GPIO.output(coil_A_2_pin, w2)
		GPIO.output(coil_B_1_pin, w3)
		GPIO.output(coil_B_2_pin, w4)
	
	while True:
		delay = raw_input("Delay between steps (ms)?")
		steps = raw_input("How many steps forward?")
		forward(int(delay) / 1000.0, int(steps) )
		steps = raw_input("How many steps backwawrds?")
		backwards(int(delay) / 1000.0, int(steps) )

if __name__ == '__main__':
	main()
'''
