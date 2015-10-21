#!/usr/bin/python
import sys

print 'the value of sys.argv[0] is : %s' %(sys.argv[0])
try:
    print 'the value of sys.argv[1] is : %s' %(sys.argv[1])
except:
    print 'parameter not specified, try: python argv.py 5'
    sys.exit()
