#!/usr/bin/python
#'''AAT_mapper'''

import sys

A = sys.stdin
myarray = []

for line in A:
    line = line.decode('utf-8')
    line = line.strip()
    line = line.split(',')
    myarray.append(line)

myarray = [[int(float(j)) for j in i] for i in myarray]

rows = len(myarray)
cols = len(myarray[0])
kv_dict = {}
for j in range(rows):
    for k in range(rows):
        kv_dict[(j, k)] = []
        for i in range(cols):
            kv_dict[(j, k)].append(myarray[j][i] * myarray[k][i])

for kvp in kv_dict.keys():
    print('%s\t%s\t%s' %(kvp[0],kvp[1],kv_dict[kvp]))
