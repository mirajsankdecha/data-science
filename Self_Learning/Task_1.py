# # write a easy program of palidrome of string wothout including space
# text = input("Enter the text: ")
# text = text.lower().replace(" ", "")
# if text == text[::-1]:
#     print("The text is palidrome")
# else:
#     print("The text is not palidrome")

# # Task 2 : Print the list of squares even number only
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i**2)
# print(list2)

# Task 3 : Create and Store the name and age of 5 students in dictionary and find a student exits or not
# students = {}
# for i in range(5):
#     name = input("Enter the name of student: ")
#     age = int(input("Enter the age of student: "))
#     students[name] = age
# print(students)
# name = input("Enter the name of student to check: ")
# if name in students:
#     print("The student exits")
# else:
#     print("The student does not exits")

# # Task 4 : Find the Common Number in two list
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# common = []
# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)

# Task 5 : Right half pyramid pattern
for i in range(1,6,1):
    for j in range(i,6,1):
        print("*",end="")
    print()
