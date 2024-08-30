# String Operations 

student = ["Miraj,Kushagra,Nilesh,Shubham,"]

print(student)  # This will print the list
print(type(student))  # This will tell us the type of the variable
print(student.reverse())  # This will reverse the list
print(student.sort())  # This will sort the list in ascending order
print(student.sort(reverse=True))  # This will sort the list in descending order
print(student.index("Miraj"))  # This will give us the index of 'Miraj' in the list
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
