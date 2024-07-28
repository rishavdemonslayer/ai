import numpy as np
a1 = np.array([4,2,3])
a2 = np.array([1,2,5], dtype='int64') 
a3 = np.array([[5.0,2.5,6.0],[2.0,5.4,3.0]], dtype='float32')
print("a1:",a1)
print("a2:",a2)
print("a3:",a3)
print("a1 dimension:",a1.ndim)
print("a1 shape:",a1.shape)
print("a1 datatype:",a1.dtype)
print("size of a1:", a1.itemsize,
      "In bytes:",a1.nbytes
)
ar = np.array([[1,2,3,4,5],[11,12,13,14,15],[21, 22, 23,24,25]])

#accessing elements:
print(ar[1][4])

#accessing specific row
print(ar[0, :])

#accessing specific column
print(ar[:, 3])

#Accessing particular rows and columns
print(ar[[0],[1,3,4]])

#Accessing selective subsection 
print(ar[0, 1:4:2])

#slicing of an array
print(ar[1,2])

#negative referencing
print(ar[-2,-2])

# Create the array
c_arr = np.linspace(1, 20, 20).reshape(5, 4)
print("Array:\n", c_arr)

# Q1. Access red element
red_element = c_arr[0, 3]
print("\nRed element:", red_element)

# Q2. Access yellow elements
yellow_elements = c_arr[[0, 1, 2], [1, 2, 3]]
print("\nYellow elements:", yellow_elements)

# Q3. Access green elements
green_elements = c_arr[[2, 2, 3, 3], [0, 1, 0, 1]]
print("\nGreen elements:", green_elements)

# Q4. Access blue elements
blue_elements = c_arr[[3, 4], [2, 2]]
print("\nBlue elements:", blue_elements)

A = np.random.randint(0,10,10)
print(" The Array is : ", A)


# Minimum
minVal = np.min(A)
print("minimum Value of Array : " , np.min(A))


# maximum 
maxVal = np.max(A)
print("maximum Value of Array : " , np.max(A))
# Sum
sum = np.sum(A)
print("maximum Value of Array : " , np.sum(A))
# Mean
mean = np.mean(A)
print("mean Value of Array    : " , np.mean(A))


#stddev
stddev = np.std(A)
print("Std Dev of Array       : " , np.std(A)) 

az0= np.zeros((2,3))
print(az0)
print(az0.shape)

az1= np.ones((2,3))
print(az1)
print (az1.shape)

azf = np.full((4, 5), 1)
print(azf)
print(azf.shape)

arn=np.random.rand(3,2)
print(arn)

arint=np.random.randint(-3,5, size=(3,3))
print(arint)

I=np.identity(3)
print(I)

A = np.random.randint(1,10,(3,3))
print("original:\n",A)
A1 = A + 2  #add
print("addition:\n",A1)
A2 = A - 2  #Sub
print("subtraction:\n",A2)
A3 = A * 2  #Multiply
print("multiplication:\n",A3)
A4 = A/2 #Division
print("division:\n",A4)
A5 = A^2 #power
print("to the power:\n",A5)
A6 = np.sin(A) 
print("sin:\n",A6)
#matrix multiplication
A = np.random.rand(2,3)
print("A:\n",A)
B = np.random.rand(3,4)
print("B:\n",B)
#first way
C = np.matmul(A,B)
print("C:\n",C)
#second way
C = A@B
print("C:\n",C)

print("A:\n",A)
print("B BEFORE:\n",B)
#first way
B=A
print("B AFTER:\n",B)
#second way
B=A.copy()
print("B AFTER:\n",B)

#determinent 
A = np.random.rand(4,4)
print("Determinant of A " , np.linalg.det(A))

B = np.random.randint(0, 10, (3, 3))
print("\n2D Array for Eigenvalues and SVD:")
print(B)

# Eigenvalues and Eigenvectors
E, W = np.linalg.eig(B)
print("\nEigenvalues of 2D Array:", E)
print("Eigenvectors of 2D Array:\n", W)

# Singular Value Decomposition
U, S, V = np.linalg.svd(B)
print("\nSingular Value Decomposition of 2D Array:")
print("U:\n", U)
print("S:\n", S)
print("V:\n", V)


# vector
A = np.array([1,2,3,4,5])
print("Norm of vector A : " , np.linalg.norm(A,2))
# Matrix
print("Norm of Matrix A : " , np.linalg.norm(A,2))

# vstack
v1 = np.array([1,2,3])
v2 = np.array([5,6,7])
print(np.vstack([v1,v2,v1,v2]))
# hstack
h1 = np.array([[1,2,3],[3,4,6]])
h2=  np.zeros((2,2))
print("h1:",h1)
print("h2:",h2)
np.hstack((h1,h2))
