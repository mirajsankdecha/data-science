# # Age Calculator
# birth_year = int(input("Enter your birth year : "))
# current_year = int(input("Enter the current year : "))
# age = current_year - birth_year
# print(f"Your age is {age}")


# # Weight Converter from lbs to Kilogram
# weight = int(input("Enter your weight in lbs : "))
# kg = weight * 0.45
# print(f"Your weight in kilogram is {kg}")


# print("Miraj Sankdecha" * 10)


# # Downpayment Calculator
# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     downpayment = 0.1 * price
# else : 
#     downpayment = 0.2 * price
# print(f"Downpayment : ${downpayment}")


# # Weight Converter 
# weight = int(input("Enter your weight : "))
# tp = input("Enter the type of weight (L for lbs and k for kg) : ")
# tp = tp.upper()
# if tp == "L" :
#     kg = weight * 0.45
#     print(f"Your weight in kilogram is {kg}")
# elif tp == "K" :
#     lbs = weight / 0.45
#     print(f"Your weight in lbs is {lbs}")
# else:
#     print("Invalid Input")
    
# # Loop 
# i = 1 
# while i <=5 : 
#     print("*" * i)
#     i+=1

# Guessing Game 
import random 
import math
sn = math.floor(random.random() * 10) + 1
count = 0 
chances = 3

while count < chances:
    guess = int(input("Guess the number : "))
    count +=1
    if guess == sn:
        print("Congratulations! You guessed the correct number")
        break
    else:
        print("Sorry! Try again")
