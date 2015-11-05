#!/usr/bin/python
import os
from fnmatch import fnmatch
import sys
import gzip
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
