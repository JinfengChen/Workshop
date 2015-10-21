#!/usr/bin/python
import os
import sys

try:
    os.path.isfile(sys.argv[1])
except:
    print 'no file specified, try python write_file.py ../data/1.fq'
    sys.exit()

ofile = open('new_file.fq', 'w')
with open (sys.argv[1], 'r') as filehd:
   for line in filehd:
       line = line.rstrip()
       print >> ofile, 'reading line: %s' %(line)
ofile.close()
