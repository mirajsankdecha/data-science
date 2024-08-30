
student = ["Miraj,Kusagra,Nilesh,Shubham,"]
print(student) # This will print the list
print(type(student)) # This will tell us the type of the variable
print(student.reverse()) # This will reverse the list
print(student.sort()) # This will sort the list in ascending order
print(student.sort(reverse=True)) # This will sort the list in descending order
print(student.index("Miraj"))   # This will give us the index of 'Miraj' in the list
print(student[0]) # This will give us the first element in the list

student_marks = [90, 80, 70, 60]
print(student_marks) 

student_marks.pop(2) # This will remove the element at index 2
print(student)

student_marks.append(55) # This will add 55 to the end of the list
print(student_marks)

nm = "Miraj" 
print("_" + nm[:2] +  "_" + nm[2:5]   )   # This will print 'Mi_raj'

nm = " Mir aj"
print(nm.replace(" ","")) # This will remove all spaces from the string

