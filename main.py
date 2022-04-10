import numpy as np
arr=np.array([[1,2,3],[4,5,6]])#syntax for declaring array in numpy 
print(arr)

#addition
mat1=np.array([np.arange(0,3),np.arange(3,6)])#arange is used to get evenly spaced values within a given range. works till n-1.
mat2=np.array([np.arange(6,9),np.arange(9,12)]) 
print("Matrix1: n ",mat1)
print("Matrix2: n ",mat2)
print("Scalar addition:  n ",mat1+1)
print("Element wise addition to two matrices ",mat1+mat2)

#subtraction
mat1=np.array([np.arange(0,3),np.arange(3,6)])
mat2=np.array([np.arange(6,9),np.arange(9,12)])
print("Matrix1: n ",mat1)
print("Matrix2: n ",mat2)
print("Scalar addition:  n ",mat1-1)
print("Element wise addition to two matrices ",mat1-mat2)

#multiplication
mat1=np.array([np.arange(0,3),np.arange(3,6)])
mat2=np.array([np.arange(6,9),np.arange(9,12)])
print("Matrix1: n ",mat1)
print("Matrix2: n ",mat2)
print("Scalar addition:  n ",mat1*2)
print("Element wise addition to two matrices ",mat1*mat2)

#division
mat2=np.array([np.arange(0,3),np.arange(3,6)])
print("Matrix: n",mat2)
print("Division : n ",mat2/2)
