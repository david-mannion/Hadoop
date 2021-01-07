#!/usr/lib/python
'''mmult_mapper'''
import sys

m_r=3 #num of rows of first matrix
m_c=3 # num of cols of first matrix
n_r=3 #num of rows of second matrix
n_c=2 #num of cols of second matrix
i=0

for line in data:
    line = line.decode('utf-8')
    line = line.split()
    line = [float(x) for x in line]
    el = line

    if(i<m_r):
        for j in range(len(el)):
            for k in range(n_c):
                print("{0}\t{1}\t{2}\t{3}".format(i, k, j, el[j]))
    else:
        for j in range(len(el)):
            for k in range(m_r):
                print("{0}\t{1}\t{2}\t{3}".format(k, j, i-m_r, el[j]))
    i=i+1