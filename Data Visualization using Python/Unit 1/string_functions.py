import numpy as np

array1 = np.array(["Miraj", "Kushagra"])
lowercase_array = np.char.lower(array1)
print(f"Lower of Array is : {lowercase_array}")
uppercase_array = np.char.upper(array1)
print(f"Upper of Array is : {uppercase_array}")
array2 =np.array(["Vrushti","Jaylakshmi"])
add_array = np.char.add(array1,array2)
print(f"Add of Array is : {add_array}")
join_array = np.char.join(array1,array2)
print(f"The Join of Array is :{join_array}")
multiply_array = np.char.multiply(array1,5)
print(f"Multiplay of Array is : {multiply_array}")
check_equal_array = np.char.equal(array1,array2)
print(f"Is it equal Array : {check_equal_array} ")
capitalize_array = np.char.capitalize(array2)
print(f"Capitalize the Array is : {capitalize_array}")

