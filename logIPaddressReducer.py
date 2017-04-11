#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# Reducer to give total count for a specific IP address

import sys

counter = 0
ip = '10.99.99.186'

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		# Defensive programming. Something has gone wrong. Skip this line.
		continue

	thisKey, requestUrl = data # Where thisKey is the IP address

	if thisKey == ip:
		counter += 1
		# print thisKey, "\t", requestUrl
print counter







