# def function_name() :
#     print("Hello from function")

# function_name()

# def function_name(name) :
#     print("Hello from function",name)
    
# print("Enter your name : ")
# name = input()
# function_name(name)

# def function_name(name) :
#     return name

# print("Enter your name : ")
# name = input()
# print(function_name(name))

# Concatenation of two strings using function

# def Concatenation(name1,name2) :
#     combine_string = name1 + " " + name2
#     print(combine_string)
 
# print("Enter your first name : ")
# name1 = input()
# print("Enter your last name : ")
# name2 = input()
# Concatenation(name1,name2) 

# Arbitrary Arguments, *args

# def group(*name) :
#     print("Hello",name)
# group("Miraj","Rahul","Aryan","Satyam")

# # Keyword Arguments
    
# def technology(js,python,cpp) :
#     print("Hello",js,python,cpp)
        
# technology(js = "Javascript",python = "Python",cpp = "C++")    
       

# Arbitrary Keyword Arguments, **kwargs
# def bf(**name) :
#     print("Hello",name["name1"],name["name2"],name["name3"])

# bf(name1 = "Miraj",name2 = "Rahul",name3 = "Aryan")      
# print(type(bf))

# # Default Parameter Value

# def my_function(country = "India") :
#     print("I am from",country)
    
# my_function("USA")
# my_function()

# List as an Argument

# def my_function(food) :
#     for x in food :
#         print(x)
        
# fruits = ["Apple","Banana","Cherry"]
# my_function(fruits)

# # Return Values 
# res = sum([1,2,3,4,5])
# print(res)

# User defined function to calculate the product of the list
# def product(ls) :
#     s = 1 
#     for i in ls:
#         s = s*i
#     return s

# ls = [1,2,3,4,5] 
# print(product(ls))     

# #  The pass Statement
# def my_function(x) :
#     return 5*x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# pass statement

def myfunction() :
    pass
