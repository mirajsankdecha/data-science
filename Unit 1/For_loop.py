# # Pratice Of Asterisk Using For Loop Pattern 

# # Simple
# for i in range(1,6,1) :
#     for j in range(1,i+1) :
#         print("* ",end="")
#     print()
# # Reverse
# for i in range(5,0,-1) :
#     for j in range(i) :
#         print("* ",end="")
#     print()     
# # Reverse Short Program
# for i in range(5,0,-1) :
#     print("* " * i)
# # Range Increment
# for i in range(1,10,4) :
#     print("* \n")
# # Nested Range Increments
# for i in range(1,6) :
#     for j in range(1,6):
#         print("* \n")
#     print() 
# # Square Pattern 
# for i in range(1,6) :
#     for j in range(1,6):
#         print("* ", end=" ")
#     print()       

# # Number of rows for the triangle
# num_rows = int(input("Enter the number of rows for the triangle: "))

# # Print the triangle
# for i in range(num_rows):
#     # Print leading spaces
#     print(' ' * (num_rows - i - 1), end='')
    
#     # Print the border of the triangle
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == num_rows - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
    
#     print()  # Move to the next line


# # Number of rows for the diamond (top half)
# num_rows = int(input("Enter the number of rows for the diamond: "))

# # Print the top half of the diamond
# for i in range(num_rows):
#     # Print leading spaces
#     print(' ' * (num_rows - i - 1), end='')
    
#     # Print the border of the top half of the diamond
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == num_rows - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
    
#     print()  # Move to the next line

# # Print the bottom half of the diamond
# for i in range(num_rows - 2, -1, -1):
#     # Print leading spaces
#     print(' ' * (num_rows - i - 1), end='')
    
#     # Print the border of the bottom half of the diamond
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == 0:
#             print('*', end='')
#         else:
#             print(' ', end='')
    
#     print()  # Move to the next line

Number_List = [1,2,3,4,5,6,7,8,9,10]
Item_List = ["Apple","Banana","Cherry","Date","Elderberry","Fig","Grape","Honeydew","Indian Plum","Jackfruit"]

for index, element in enumerate(Number_List):
    print(Item_List[index], ":", element)
    
