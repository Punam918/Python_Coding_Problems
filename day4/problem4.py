# You need to perform matrix and linear algebra operations, such as matrix multiplication,
#  finding determinants, solving linear equations, and so on. (explore numpy). 

import numpy as np
A = np.array([[1, 2], [3, 4]]) 
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
C = np.dot(A, B) 
print("Matrix Multiplication (A * B):\n", C)
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)


A_inv = np.linalg.inv(A)
print("Inverse of A:\n", A_inv)

b = np.array([9, 10])  
x = np.linalg.solve(A, b) 
print("Solution x:\n", x)


eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

A_T = A.T
print("Transpose of A:\n", A_T)

vector = np.array([3, 4])
norm = np.linalg.norm(vector)
print("Norm of the vector:", norm)  

U, S, V = np.linalg.svd(A)
print("U:\n", U)
print("Singular values:\n", S)
print("V:\n", V)
