import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it will modify the original array.
print(a[0,1])
b[0, 0] = 77
print(a[0,1])

row_r1 = a[1,:]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

a = np.array([[1,2], [3,4], [5,6]])

#These are same.
print(a[[0, 1, 2], [0, 1, 0]])
print(np.array([a[0,0], a[1,1], a[2,0]]))

# One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)

# Create an array of indices
b = np.array([0, 1, 2, 2])
print(a[np.arange(4), b])

a[np.arange(4), b] += 10
print(a)

# Boolean array indexing: Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some condition. Here is an example:
a = np.array([[1,2], [3,4], [5,6]])
bool_idx = (a > 2)
print(bool_idx)
# We use boolean array indexing to construct a rank 1 array consisting of the elements of a corresponding to the True values of bool_idx
print(a[bool_idx])
# We can do all of the above in a single concise statement:
print(a[a > 2])
