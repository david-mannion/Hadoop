#!/usr/bin/python
'''eigen_reducer.py'''
import sys
import numpy as np

data = sys.stdin
for line in data:
    line = line.strip()
    line = line.decode('utf-8')
    j, k, val = line.split('\t')
    j = int(j)
    k = int(k)


AAT = np.zeros((j+1,k+1))

#carrying out the rest of the SVD: Caluclating u and Sigma
for line in data:
    line = line.strip()
    line = line.decode('utf-8')
    j, k, val = line.split('\t')
    j = int(j)
    k = int(k)
    val = int(val)
    AAT[j,k] = val

def get_Sigma(AAT,n_elements = 2):
    eigvals, eigvec = np.linalg.eig(AAT)
    s = np.sqrt(eigvals)
    # create m x n Sigma matrix
    Sigma = np.zeros((AAT.shape[0], AAT.shape[1]))
    # populate Sigma with n x n diagonal matrix
    Sigma[:AAT.shape[0], :AAT.shape[0]] = np.diag(s)
    # select
    Sigma = Sigma[:, :n_elements]
    return Sigma

def get_U(AAT):
    eigvals, eigvec = np.linalg.eig(AAT)
    return eigvec


sig = get_Sigma(AAT)
U = get_U(AAT)

np.savetxt('matrices.txt',U,delimiter = ' ',fmt='%f') #writing first matrix to text file
f=open('matrices.txt','ab')
np.savetxt(f,sig,delimiter = ' ',fmt='%f') # writing second matrix to text file
f.close()