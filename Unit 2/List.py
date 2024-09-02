# String Operations 

student = ["Miraj,Kushagra,Nilesh,Shubham,"]

print(student)  # This will print the list
print(type(student))  # This will tell us the type of the variable
print(student.reverse())  # This will reverse the list
print(student.sort())  # This will sort the list in ascending order
print(student.sort(reverse=True))  # This will sort the list in descending order
# print(student.index("Miraj"))  # This will give us the index of 'Miraj' in the list
print(student[0])  # This will give us the first element in the list

nm = "Miraj"
print("_" + nm[:2] + "_" + nm[2:5])  # This will print 'Mi_raj'

nm = "Mir aj"
print(nm.replace(" ", ""))  # This will remove all spaces from the string

# Number Operations

student_marks = [10, 20, 30, 40, 50]
print(student_marks)  # This will print the list of student marks

for j in student_marks:
    print(j)  # This will print all the elements in the list
    print(j**2)  # This will print the square of each element

student_marks.pop(2)  # This will remove the element at index 2
print(student_marks)

student_marks.append(60)  # This will add 60 to the end of the list
print(student_marks)

new_list = []

for i in student_marks:
    new_list.append(i**2)  # This will append the square of each element to the new list
print(new_list)  # This will print the new list

new_list2 = [i**2 for i in student_marks]  # This is a more concise way of doing the same thing
print(new_list2)  # This will print the new list

# Hetereogeneous List

student_info = ["Miraj", True, 10, 20.5, [10, 20, 30]]
print(student_info)  # This will print the list of student

# 2D List

student_marks = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(student_marks)  # This will print the 2D list
print(student_marks[1])  # This will print the second row
print(student_marks[1][2])  # This will print the third element of the second row
print(student_marks[:]) # This will print the entire list
print(student_marks[1:3])  # This will print the second and third element of the second row
print(student_marks[1][0:2])  # This will print the first two elements of the second row 
print(student_marks[0:3:2]) # This will print the first and third row of the list 

matrix_list = [[1,2,3], [4,5,6], [7,8,9]]
matrix_list [0] [0] = 10
matrix_list [1] [1] = 20
matrix_list [2] [2] = 30

print(matrix_list)  # This will print the list

for row in matrix_list:
    for element in row:
        print(element, end=" ")
    print() # This will print the matrix in a 3x3 format

