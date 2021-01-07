#!/usr/lib/python
'''mmult_reducer.py'''

import sys
m_r=3 #num of rows of first matrix
m_c=3 # num of cols of first matrix
n_r=3 #num of rows of second matrix
n_c=2 #num of cols of second matrix
matrix=[]
for row in range(m_r):
    r=[]
    for col in range(n_c):
        s=0
        for el in range(m_c):
            mul=1
            for num in range(2):
                line = sys.stdin.readline()
                line = line.decode('utf-8')
                line = line.split('\t')
                line = [float(x) for x in line]
                n = line[-1]
                mul*=n
            s+=mul
        r.append(s)
    matrix.append(r)
print('\n'.join([str(x) for x in matrix]))