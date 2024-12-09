import numpy as np

one_d_array1 = np.array([1,2,3])
one_d_array2 = np.array([4,5,6])
result = np.union1d(one_d_array1,one_d_array2)
print(f"Union of 1D array is : {result}")

two_d_array1 = np.array([[1,2,3],[4,5,6]])
two_d_array2 = np.array([[7,8,9],[10,11,12]])
result_2d = np.union1d(two_d_array1,two_d_array2)
print(f"Union of 2D array is :{result_2d}")

three_d_array1 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
three_d_array2 = np.array([[[13,14,15],[17,18,19]],[[20,21,22],[23,24,25]]])
result_3d = np.union1d(three_d_array1,three_d_array2)
print(f"Union of 3D array is : {result_3d}")

three_d_array3 = np.array([[[12,14,15],[17,18,19]],[[20,21,22],[23,24,25]]])
result_int_3d = np.intersect1d(three_d_array1,three_d_array3)
print(f"Intersection of array is : {result_int_3d}")
# result_int_unique_3d = np.unique(three_d_array1,three_d_array3)
# print(f"Unique of array is : {result_int_unique_3d}")

# This is for 1D array
array1 = np.array([1,2,3,4,5])
result = array1 + 10
print(f"The Vectorization of array is : {result}")

# This is for 2D array 
array_vec = two_d_array1 + two_d_array2
print(f"Vectorization of 2D array is : {array_vec}")

# Masking of Array 


