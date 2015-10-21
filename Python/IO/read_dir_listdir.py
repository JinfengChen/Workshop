#!/usr/bin/python
import os
from fnmatch import fnmatch
import sys

try:
    files = os.listdir(sys.argv[1])
except:
    print 'no diretory specified, try python read_dir.py ../data/'
    sys.exit()     

for file_name in sorted(files):
    if fnmatch(file_name, '*.txt'):
        print 'filename: %s' %(file_name)

