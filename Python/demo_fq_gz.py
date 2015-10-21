#!/usr/bin/python
import os
from fnmatch import fnmatch
import sys
import gzip
#from numpy import *

try:
    files = os.listdir(sys.argv[1])
except:
    print 'no diretory specified, try python demo.py ./data/'
    sys.exit()     

def mean(read_len):
    length_total = 0
    for length_read in read_len:
        length_total += length_read
    length_mean  = float(length_total)/len(read_len)
    return length_mean

ofile = open('demo.sum', 'w')
print >> ofile, '%-25s%-10s%-10s' %('Sample', '#Reads', 'Average')
for file_name in sorted(files):
    file_name = '%s/%s' %(sys.argv[1], file_name)
    if fnmatch(file_name, '*.fq.gz'):
        read_num = 0
        read_len = []
        line_num = 0
        with gzip.open (file_name, 'r') as fq_file:
            for line in fq_file:
                line = line.rstrip()
                line_num += 1
                if line_num%4 == 2:
                    read_len.append(len(line))
                    read_num += 1
        print >> ofile, '%-25s%-10d%-10.2f' %(file_name, read_num, mean(read_len))
