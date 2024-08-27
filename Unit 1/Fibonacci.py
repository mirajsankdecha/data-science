# Number of terms to display in the Fibonacci sequence
num_terms = int(input("Enter the number of terms: "))

# Initialize the first two numbers in the sequence
first, second = 0, 1

print("Fibonacci sequence:")
# Generate and display the Fibonacci sequence
for _ in range(num_terms):
    print(first, end=' ')
    # Update values for the next term
    first, second = second, first + second
