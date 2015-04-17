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
        self.motor = stepper_motor.StepperMotor(motor_pins)
        self.steps_between_sections = self.get_steps_between_sections(sections)
        print "steps_between_sections:", self.steps_between_sections
        self.steps_to_sections_from_origin = self.get_steps_to_sections(sections)
        self.current_section = 1
        print "steps_to_sections_from_origin", self.steps_to_sections_from_origin
        print "current section", self.current_section
    
    def get_steps_between_sections(self,sections):
        '''divides the 512 steps into specified sections.
        gives an integer on purpose - we must use an integer value of 
        steps'''
        return 512 / sections
    
    def get_steps_to_sections(self,sections):
        '''gets the number of steps to each section from the origin.
        Since the number of steps to each section might be a decimal,
        the extra steps are saved and shared whole between each section.
        
        EG. 512.0 / 6 = 85.3 
        but as we must work in integers..
        512 / 6 = 85
        85 * 6 = 510
        therefore we have 2 steps left over. 
        Put the first extra step in section 1, then the second in section 2 etc
        '''
        distances = [(self.steps_between_sections * i) - self.steps_between_sections for i in range(1,sections + 1)]
        ## now we need to add in the missing steps if any ( we should always have less remaining than there are sections)
        missing_steps = (512 - ((512/sections) * sections) )
        if missing_steps > 0:
            for m in range(1,missing_steps):
                distances[m] += 1
        
        print "distances", distances
        distance_to_section = {}
        for i in range(0, sections):
            distance_to_section[i + 1] = distances[i]
        print distance_to_section
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
        return self.steps_to_sections_from_origin[target_section] - self.current_section
        



print "running!"
table = TurnTable(6,[17,18,21,22])
print type(table)
stops = [1,5,4,2,3]
for s in stops:
    print s
    table.go_to_section(s)
