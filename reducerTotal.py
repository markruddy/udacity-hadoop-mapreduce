#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# Reducer to find the total number and total value of sales across all stores

import sys

salesTotal = 0 # To keep track of total sales
oldKey = None
counter = 0 # To count the number of sales

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Defensive programming. Something has gone wrong. Skip this line.
        continue

    # Name elements of the array 'data_mapped'
    thisKey, thisSale = data_mapped

    # Add thisSale to running total
    salesTotal += float(thisSale)

    # Add 1 to counter
    counter += 1

# Capture last line to finish the loop 
print salesTotal, "\t", counter


