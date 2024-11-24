#!/usr/bin/python3
import os
import sys
import math


thrust_file = "postProcessing/forces/0/forces.dat"

ct_error = 5
experimental = 24
def line2dict(line):
    tokens_unprocessed = line.split()
    tokens = [x.replace(")","").replace("(","") for x in tokens_unprocessed]
    floats = [float(x) for x in tokens]
    data_dict = {}
    data_dict['time'] = floats[0]
    data_dict['thrust'] = floats[1]
    return data_dict

total_thrust = 0
count = 0
with open(thrust_file,"r") as datafile:
	for line in datafile:
    count+=1
		if line[0] == "#":
			continue
		data_dict = line2dict(line)
		total_thrust += [data_dict['thrust']]
datafile.close()
avg_thrust = total_thrust/count


if ct_error<abs(avg_thrust-experimental):
	print("J=0.5: FAILED: thrust does not meet the requirements")
else: print("PASSED")
    
