import numpy as np

list1 = [1,2,3,4,5]
array1 = np.array(list1)
print(array1)

list2 = [6,7,8,9,10]
array2 = np.array(list2)
print(array2)

array3 = np.zeros(4)
print(array3)

array4 = np.arange(10)
print(array4)

array5 = np.arange(1,9,2)
print(array5)

array6 = np.floor(np.random.rand(5) * 10)
print(array6)

array7 = np.empty(4)
print(array7)

array8 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array8)

array9 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(array9)

# Create 2D Array by using the zeros functions
array10 = np.zeros((3,4))
print(array10)
print("-"*20)
# Create 3D array by using the zeros functions
array11 = np.zeros((3,4,5))
print(array11)

array11 = np.ones((3,5))
print(array11)

array12 = np.ones((2,3,4))
print(array12)

array13 = np.full((2,2),5)
print(array13)

# 2D Random Array
array14 = np.floor(np.random.rand(2,2) * 10)
print(array14)
print("-"*20)
# 3D Random Array
array15 = np.floor(np.random.rand(2,2,2) * 10)
print(array15)

array16 = np.array([2,4,9])
print(array16.dtype) # Gives Data type of particular object

int_array = np.array([-3,-1,0,1])
float_array = np.array([0.1,0.2,0.3])
complex_array = np.array([1+2j,2+3j,3+4j])
print(int_array.dtype)
print(float_array.dtype)
print(complex_array.dtype)

array17 = np.array([1,3,7], dtype='int32')
print(array1,array1.dtype)

int_array1 = np.array([1,2,3], dtype='int8')
int_array2 = np.array([5,6,7], dtype='int16')
float_array = np.array([0.1,0.2,0.3], dtype='float32')
complex_array = np.array([1+2j,2+3j,3+4j], dtype='complex64')
print(int_array1.dtype)
print(int_array2.dtype)
print(float_array.dtype)
print(complex_array.dtype)


int_array = np.array([1,3,5,7])
# convert data type of int_array to float
float_array = int_array.astype('float64')
# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)


array18 = np.arange(1,10)
print("Check The Data Types ",array18.ndim)
print(array18)
print("Size of Array",array18.size)
print("Shape of Array",array18.shape)
array18 = array18.reshape(3,3)
print("Reshaped Array:\n",array18)
print("Item Size",array18.itemsize)
print("Current Array",array18.shape)
print("Memory Location",array18.data)
array20 = np.array([[1,2,3],[2,3,4]])
print(array20.ndim)
print(array20.shape)
array19= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array19.ndim)
print(array19.shape)

array21 = np.array([[1,2,3,4],[5,6,7,8]])
np.save('file1.npy',array21)
loaded_array = np.load('file1.npy')
print(loaded_array)
np.savetxt('file2.txt',array21)
loaded_array = np.loadtxt('file2.txt')
print(loaded_array)

array22 = np.array([[1,2,3],[4,5,6]])
print(array22)
print(array22[0][1])
print(array22[-1][-2])
# Resign at the given index
array22[0][1] = 5
print(f"After the modify the array : {array22}")
sec_row = array22[1,:]
print("Second Row :",sec_row)
third_col = array22[:,2]
print("Third Column :", third_col)

# Creating a 3D Array with Shape
threed_array = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]])
print(threed_array)
element = threed_array[1,2,1]
print(f"Element at Index (1,2,1) : {element}")
