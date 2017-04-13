#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# with a key name and val is the sale amount
#
# All the sales for each key will be presented,
# then the key will change and we'll be dealing with the next key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # Name elements of the array 'data_mapped'
    thisKey, thisSale = data_mapped 

    # If oldKey has a value and value oldKey different to thisKey ie there's a newKey
    if oldKey and oldKey != thisKey:
	# Then print the running total salesTotal for oldKey, and then make salesTotal zero 
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0
    # Otherwise set thisKey to oldKey
    oldKey = thisKey
    # and add thisSale to the running total salesTotal
    salesTotal += float(thisSale)

# Capture last line to finish the loop 
if oldKey != None:
    print oldKey, "\t", salesTotal

