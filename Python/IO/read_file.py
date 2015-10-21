#!/usr/bin/python
import os
import sys

try:
    os.path.isfile(sys.argv[1])
except:
    print 'no file specified, try python read_file.py 1.fq'
    sys.exit()

with open (sys.argv[1], 'r') as filehd:
   for line in filehd:
       line = line.rstrip()
       print 'reading line: %s' %(line)
