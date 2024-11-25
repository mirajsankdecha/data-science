num = int(input("Enter The Number: "))  # 1. Get the number from the user
rev = 0  # 2. Start with a reversed number as 0

# 3. Repeat until the number becomes 0
while num > 0:
    remainder = num % 10  # Get the last digit (for example, from 1234 get 4)
    rev = rev * 10 + remainder  # Add the last digit to the reversed number
    num = num // 10  # Remove the last digit (for example, 1234 becomes 123)

# 4. Print the reversed number
print("Reversed Number:", rev)
