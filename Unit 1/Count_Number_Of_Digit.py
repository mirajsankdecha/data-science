# Count the number of digits in a number and sum of digits in a number
num = int(input("Enter The Number: "))  # Take input from the user
count = 0  # Initialize count to 0

while num > 0:
    num = num // 10  # Remove the last digit from the number
    count += 1  # Increase the count by 1

print("Number of digits:", count)

# Sum of digits in a number
num = int(input("Enter the Number: "))  # Take input from the user
sum_digits = 0  # Initialize sum to 0

while num > 0:
    sum_digits += num % 10  # Add the last digit to sum
    num = num // 10  # Remove the last digit from the number

print("Sum of digits:", sum_digits)
