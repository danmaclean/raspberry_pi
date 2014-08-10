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

def main():
	GPIO.setmode(GPIO.BCM)
	enable_pin = 18
	coil_A_1_pin = 4
	coil_A_2_pin = 17
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

