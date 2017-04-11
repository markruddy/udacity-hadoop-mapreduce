#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# mapper for Common Log Format file

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
	if len(data) == 10:
		data_mapped = [data[0],data[1],data[2]]
print len(data_mapped)