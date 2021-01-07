#!/usr/bin/python
'''AAT_reducer.py'''
import sys

output_array = []
#for line in sys.stdin:

    line = line.strip()
    line = line.decode('utf-8')
    j, k, vals = line.split('\t')
    j = int(j)
    k = int(k)
    vals = vals.strip()
    vals = vals.strip('][').split(',')
    vals = [int(i) for i in vals]
    print('%s\t%s\t%s' % (j,k,sum(vals)))


