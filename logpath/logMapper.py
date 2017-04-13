#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# Mapper for Common Log Format file

import sys

for line in sys.stdin:
    data = line.strip().split(" ") # Split on non-breaking whitespace
    if len(data) == 10: # Defensive programming against non-standard log lines
    	# Combine 
    	data_mapped = [data[0], data[1], data[2], data[3]+" "+data[4], data[5], data[6], data[7], data[8], data[9]]
    	ipaddress, identity, username, time, requestStart, requestUrl, requestEnd, status, size = data_mapped
    	print "{0}\t{1}".format(ipaddress, requestUrl)