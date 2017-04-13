#!/usr/bin/python

# Mark Ruddy 
# 2017-04-13
# Mapper for Common Log Format file
# Returns key=requestUrl / value=ipaddress
# using regex

import sys
import re

regex = '([(\d\.)]+) ([^\s]+) ([^\s]+) \[(.*?)\] "(\w+) ([^\s]+) ([^\s]+)" (\d+) ([^\s]+)'
r = re.compile(regex)

for line in sys.stdin:
    matches = r.match(line)
    if matches:
        print "{0}\t{1}".format(matches.groups()[5], 1)
    else:
        print 'No matches: %s' % line