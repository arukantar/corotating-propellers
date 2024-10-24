#!/usr/bin/python3

import os
import sys
import math

velocity_file = "postProcessing/probes1/0/U"

def line2dict(line):
    tokens_unprocessed = line.split()
    tokens = [x.replace(")","").replace("(","") for x in tokens_unprocessed]
    floats = [float(x) for x in tokens]
    data_dict = {}
    data_dict['time'] = floats[0]
    #data_dict['velocity_x'] = floats[1]**2
    #data_dict['velocity_y'] =floats[1]**2
    #data_dict['velocity_z'] = floats[3]**2
    data_dict['velocity_mag'] = math.sqrt(floats[1]**2 + floats[2]**2 + floats[3]**2)
    return data_dict

time = []
vel_mag = []

with open(velocity_file,"r") as datafile:
	for line in datafile:
		if line[0] == "#":
			continue
		data_dict = line2dict(line)
		time += [data_dict['time']]
		vel_mag += [data_dict['velocity_mag']]
datafile.close()

outputfile = open('velocity.txt','w')
for i in range(0,len(time)):
	outputfile.write(str(time[i])+', '+str(vel_mag[i])+'\n')
outputfile.close()
