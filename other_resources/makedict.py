#!/usr/bin/env python
import os

mypath = "girlpictures/"
pictures = [mypath+f for f in os.listdir(mypath) if os.path.isfile(mypath+f)]
pickeys = [(os.path.splitext(f)[0]).replace(" ","") for f in os.listdir(mypath) if os.path.isfile(mypath+f)]
#print pictures

dictpics = dict(zip(pickeys,pictures))
for k,v in dictpics.items():
	print("key:",k,"\t\t value:",v)

