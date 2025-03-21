# Program 1: Solid Square Pattern
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# Program 2: Right-Angled Triangle (Increasing)
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

# Program 3: Right-Angled Triangle (Decreasing)
for i in range(5):
    for j in range(i, 5):
        print("*", end="")
    print()

# Program 4: Right-Aligned Decreasing Triangle
for i in range(5):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, 5):
        print("*", end="")
    print()

# Program 5: Right-Aligned Increasing Triangle
for i in range(5):
    for j in range(i, 5):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()

# Program 6: Pyramid Pattern
for i in range(5):
    for j in range(i, 5):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print()

# Program 7: Inverted Pyramid Pattern
for i in range(5):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, 5-1):
        print("*", end="")
    for j in range(i, 5):
        print("*", end="")
    print()

# Program 8: Full Pyramid
for i in range(5):
    for j in range(i, 5):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print()

# Program 9: Diamond Shape Upper Part
for i in range(5):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, 5-1):
        print("*", end="")
    for j in range(i, 5):
        print("*", end="")
    print()

# Program 10: Diamond Shape Lower Part
for i in range(5-1):
    for j in range(i, 5):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i+1):
        print("*", end="")
    print()

# Program 11: Inverted Full Pyramid
for i in range(5):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, 5):
        print("*", end="")
    for j in range(i, 5-1):
        print("*", end="")
    print()

print("-" * 20)

# Program 12: Number Pyramid
n = 12  # Number of rows
for i in range(1, n + 1):  
    print(" " * 2 * (n - i), end="")  # Print spaces for alignment
    
    for j in range(1, i + 1):  
        print(f"{j:02}", end="")  # Print increasing numbers
    
    for j in range(i - 1, 0, -1):  
        print(f"{j:02}", end="")  # Print decreasing numbers

    print()  # Move to next line

# Program 13: Triangle with Space Between Two Triangles
n = 5  # Number of rows for the upper half

# Upper Half
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Middle Row
print("*" * (2 * n - 1))

# Lower Half
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Program 14 : Diamond Shape Pattern

n = 5  # Number of rows

for i in range(n):
    for j in range(n - i - 1):  # Print leading spaces
        print(" ", end="")

    for j in range(i + 1):  # Print stars with spaces in between
        if j == 0 or j == i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()  # Move to the next line

# 

num = 1
for i in range(0, 3):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print()

num = 1
for i in range(0, 5):
    for j in range(0, i + 1):
        print(num, end=" ")
        num = num + 1
    print()
