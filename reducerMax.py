#!/usr/bin/python

# Mark Ruddy 
# 2017-04-11 
# Reducer to find the maximum value within a key

import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Defensive programming. Something has gone wrong. Skip this line.
        continue

    # Name elements of the array 'data_mapped'
    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey: # If keys different we need to print out results of the previous key/value group
            print oldKey, "\t", salesMax
            oldKey = thisKey;
            salesMax = float(thisSale);
    else:
        # If keys the same, compare sale from new line with current maximum sale
        if salesMax <= float(thisSale): 
            salesMax = float(thisSale);
            oldKey = thisKey;

# Capture last line to finish the loop 
if oldKey != None:
    print oldKey, "\t", salesMax


