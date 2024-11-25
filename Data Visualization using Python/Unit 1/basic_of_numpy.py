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

