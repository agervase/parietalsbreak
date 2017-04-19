#!/usr/bin/env python
import string
import sys

def printPrompt(prompt):
    numbchars = len(prompt)
    counter = 0
    ycoord = 0
    while counter < numbchars-64:
        linechars = 0
        for word in prompt[counter:numbchars].split():
            linechars = linechars+len(word)+1
            if linechars > 64:
                break
        if counter < numbchars:
            line = prompt[counter:counter+linechars].strip()
            print line
            ycoord + 20
        counter = counter+linechars
    line = prompt[counter:numbchars].strip()
    print line 

printPrompt("So you wake up one fine Friday morning in your dorm room to your alarm. You have an 8:20 class, but you aren't sure you want to go to it. Do you go? I love coding so much I just want to write python forever i am filling up this prompt so I can see if it works with multiple lines i hope it does i really dont want to have to write it again that would literally by awful")
