#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# Reducer to give total count for a specific url

import sys

counter = 0
url = '/assets/js/the-associates.js'

for line in sys.stdin:
	data = line.strip().split("\t")

	if len(data) != 2:
		# Defensive programming. Something has gone wrong. Skip this line.
		continue

	thisKey, requestUrl = data

	if requestUrl == url:
		counter += 1
		# print thisKey, "\t", requestUrl
print counter







