#!/usr/bin/python
import os
import glob
import sys

try:
    files = glob.glob('%s/*.txt' %(sys.argv[1]))
except:
    print 'no diretory specified, try python read_dir.py ../data/'
    sys.exit()     

for file_name in sorted(files):
    print 'filename: %s' %(file_name)

