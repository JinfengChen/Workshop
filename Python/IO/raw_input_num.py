#!/usr/bin/python
import re
str = raw_input("Enter your input integer: ");
str.rstrip()
print "Received input is %5d: " %(int(str))

str = raw_input("Enter your input float: ");
str.rstrip()
print "Received input is %5.2f: " %(float(str))
