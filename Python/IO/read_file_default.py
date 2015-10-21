#!/usr/bin/python
import os
import sys

try:
    os.path.isfile(sys.argv[1])
except:
    print 'no file specified, try python read_file.py 1.fq'
    sys.exit()

filehd = open (sys.argv[1], 'r')
for line in filehd:
    line = line.rstrip()
    print 'reading line: %s' %(line)
filehd.close()
