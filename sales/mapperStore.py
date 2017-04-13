#!/usr/bin/python
# Mark Ruddy 
# 2017-04-11 
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
    	# Write out to standard output, separated by a tab
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

