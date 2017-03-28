#!/usr/bin/env python
import string

print'"Hello! Welcome to Parietals Break'
person = raw_input('Enter your name: ')
print 'Hello', person

DORM = raw_input('What dorm are you in? PE or Knott? ')
if DORM.lower() == 'pe' or DORM.lower() == 'knott':
    DORM = DORM.lower();
else:
    print "Defaulting to pe"
    DORM = 'pe'

 
