#!/usr/bin/env python
# encoding: utf-8
"""
turn_table.py


Created by Dan MacLean (TSL) on 2015-04-16.
Copyright (c) 2015 Dan MacLean. All rights reserved.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../motors")
import stepper_motor

class TurnTable:
    
    def __init__(self, sections=6, motor_pins=[17,18,21,22]):
        print "sections:", sections
        print "oins:", motor_pins
        self.sections = sections
        self.motor = StepperMotor(motor_pins)
        self.steps_between_sections = self.get_steps_between_sections(sections)
        self.steps_to_sections_from_origin = self.get_steps_to_sections(sections)
        self.current_section = 1
        
        print "steps_between_sections:", self.steps_between_sections
        print "steps_to_sections_from_origin", self.steps_to_sections_from_origin
        print "current section", self.current_section
    
    def get_steps_between_sections(self,sections):
        '''divides the 512 steps into specified sections'''
        return 512.0 / sections
    
    def get_steps_to_sections(self,sections):
        '''gets the number of steps to each section from the origin'''
        distances = [(self.steps_between_sections * i) - self.steps_between_sections for i in range(1,sections + 1)]
        distance_to_section = {}
        for i in range(1, sections + 1):
            distance_to_section[i] = distances[i]
        return distance_to_section 
    
    def go_to_section(self,target_section):
        '''sends the motor to a particular section'''
        steps_to_go = TurnTable.get_steps_to(self,target_section)
        if steps_to_go < 0:
            self.motor.anticlockwise(abs(steps_to_go))
        else:
            self.motor.clockwise(steps_to_go)
    
    def get_steps_to(self,target_section):
        '''gets the number of steps from self.current_section to target section.'''
        return self.steps_to_section[target_section] - current
        



print "running!"
table = TurnTable(6,[17,18,21,22])
print type(table)
stops = [1,5,4,2,3]
for s in stops:
    print s
    table.go_to_section(s)
