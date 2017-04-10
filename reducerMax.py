#!/usr/bin/python

# Reducer to find the maximum value within a key

import sys

salesMax = 0
oldKey = None
counter = 0

# print type(sys.stdin)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # Name elements of the array 'data_mapped'
    thisKey, thisSale = data_mapped

    counter += 1

    if oldKey and oldKey != thisKey:
        if counter == 1:
            print thisKey, "\t", thisSale, "-", counter
            oldKey = thisKey;
            salesMax = 0;
            counter = 0
        else:
            print oldKey, "\t", salesMax, "-", counter
            oldKey = thisKey;
            salesMax = thisSale;
            counter = 0
    else:
        if salesMax <= float(thisSale):
            salesMax = float(thisSale);
            oldKey = thisKey



# Capture last line to finish the loop 
# if oldKey != None:
#     print oldKey, "\t", salesMax


