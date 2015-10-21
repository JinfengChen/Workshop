#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=int, default='1')
args = parser.parse_args()

print 'the input parameter is : %s' %(args.input)
