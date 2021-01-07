#!/usr/bin/python
'''eigen_mapper'''
import sys

#for line in sys.stdin:

    line = line.strip()
    line = line.decode('utf-8')
    j, k, val = line.split('\t')
    j = int(j)
    k = int(k)
    print('%s\t%s\t%s' %(j,k,val))
