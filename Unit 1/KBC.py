# Initialize score
score = 0

# Question 1
q1 = "Who developed Python Programming Language?"
print(q1)
print("1:", "Wick van Rossum")
print("2:", "Rasmus Lerdorf")
print("3:", "Guido van Rossum")
print("4:", "Niene Stom")
answer = input("Enter the option number (1-4): ")
if answer == "3":
    score += 1

# Question 2
q2 = "Which type of Programming does Python support?"
print(q2)
print("1:", "object-oriented programming")
print("2:", "structured programming")
print("3:", "functional programming")
print("4:", "all of the mentioned")
answer = input("Enter the option number (1-4): ")
if answer == "4":
    score += 1

# Question 3
q3 = "Is Python case sensitive when dealing with identifiers?"
print(q3)
print("1:", "no")
print("2:", "yes")
print("3:", "machine dependent")
print("4:", "none of the mentioned")
answer = input("Enter the option number (1-4): ")
if answer == "2":
    score += 1

# Question 4
q4 = "Which of the following is the correct extension of the Python file?"
print(q4)
print("1:", ".python")
print("2:", ".pl")
print("3:", ".py")
print("4:", ".p")
answer = input("Enter the option number (1-4): ")
if answer == "3":
    score += 1

# Question 5
q5 = "Is Python code compiled or interpreted?"
print(q5)
print("1:", "Python code is both compiled and interpreted")
print("2:", "Rasmus Lerdorf")
print("3:", "Guido van Rossum")
print("4:", "Niene Stom")
answer = input("Enter the option number (1-4): ")
if answer == "1":
    score += 1

# Question 6
q6 = "All keywords in Python are in"
print(q6)
print("1:", "Capitalized")
print("2:", "lower case")
print("3:", "UPPER CASE")
print("4:", "None of the mentioned")
answer = input("Enter the option number (1-4): ")
if answer == "4":
    score += 1

# Question 7
q7 = "What will be the value of the following Python expression? 4 + 3 % 5"
print(q7)
print("1:", "7")
print("2:", "2")
print("3:", "4")
print("4:", "1")
answer = input("Enter the option number (1-4): ")
if answer == "1":
    score += 1

# Question 8
q8 = "Which of the following is used to define a block of code in Python language?"
print(q8)
print("1:", "Indentation")
print("2:", "Key")
print("3:", "Brackets")
print("4:", "All of the mentioned")
answer = input("Enter the option number (1-4): ")
if answer == "1":
    score += 1

# Question 9
q9 = "Which keyword is used for function in Python language?"
print(q9)
print("1:", "Function")
print("2:", "def")
print("3:", "Fun")
print("4:", "Define")
answer = input("Enter the option number (1-4): ")
if answer == "2":
    score += 1

# Question 10
q10 = "Which of the following character is used to give single-line comments in Python?"
print(q10)
print("1:", "//")
print("2:", "#")
print("3:", "!")
print("4:", "/*")
answer = input("Enter the option number (1-4): ")
if answer == "2":
    score += 1

# Check the final score
if score == 10:
    print("Congratulations! You won 7 Crores!")
else:
    print("Sorry, you lose! Better luck next time.")
