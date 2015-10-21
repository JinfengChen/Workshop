#!/usr/bin/python
import os
from fnmatch import fnmatch
import sys

try:
    files = os.listdir(sys.argv[1])
except:
    print 'no diretory specified, try python demo.py ./data/'
    sys.exit()     

def readFastaEntry( fp ):
    name = ""
    seq = ""
    for line in fp:
        if line.startswith( ">" ):
            tmp = []
            tmp.append( name )
            tmp.append( seq )
            name = line
            seq = ""
            yield tmp
        else:
            seq = seq.join( line )

for file_name in sorted(files):
    file_name = '%s/%s' %(sys.argv[1], file_name)
    if fnmatch(file_name, '*.fa'):
        print 'filename: %s' %(file_name)
        read_num = 0
        read_len = []
        header   = ''
        sequence = []
        with open (file_name, 'r') as fa_file:
            #for line in fa_file:
            #    line = line.rstrip()
            #    if line[0] == '>':
            #        header = line[1:]
            #        sequence = []
            #    else:
            #        sequence.append(line)
            for seq in readFastaEntry(fa_file):
                print seq[0], seq[1]


