num = int(input("Enter The Number: "))  # Take input from the user
count = 0  # Initialize count to 0

while num > 0:
    num = num // 10  # Remove the last digit from the number
    count += 1  # Increase the count by 1

print("Number of digits:", count)
