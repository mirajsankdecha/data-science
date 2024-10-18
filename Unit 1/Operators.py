# Input numbers from the user
num_1 = int(input("Enter the First Number : "))
numb_2 = int(input("Enter the Second Number : "))

# Arithmetic Operators
print("\nArithmetic Operations:")
print("Addition (+) :", num_1 + numb_2)
print("Subtraction (-) :", num_1 - numb_2)
print("Multiplication (*) :", num_1 * numb_2)
print("Division (/) :", num_1 / numb_2)
print("Floor Division (//) :", num_1 // numb_2)
print("Modulus (%) :", num_1 % numb_2)
print("Exponentiation (**) :", num_1 ** numb_2)

# Relational Operators
print("\nRelational (Comparison) Operations:")
print("Is num_1 greater than numb_2? (>) :", num_1 > numb_2)
print("Is num_1 less than numb_2? (<) :", num_1 < numb_2)
print("Is num_1 equal to numb_2? (==) :", num_1 == numb_2)
print("Is num_1 not equal to numb_2? (!=) :", num_1 != numb_2)
print("Is num_1 greater than or equal to numb_2? (>=) :", num_1 >= numb_2)
print("Is num_1 less than or equal to numb_2? (<=) :", num_1 <= numb_2)

# Logical Operators
print("\nLogical Operations:")
print("Is num_1 > 0 AND numb_2 > 0? (and) :", num_1 > 0 and numb_2 > 0)
print("Is num_1 > 0 OR numb_2 > 0? (or) :", num_1 > 0 or numb_2 > 0)
print("NOT(num_1 < 0)? (not) :", not(num_1 < 0))

# Bitwise Operators
print("\nBitwise Operations:")
print("Bitwise AND (&) :", num_1 & numb_2)
print("Bitwise OR (|) :", num_1 | numb_2)
print("Bitwise XOR (^) :", num_1 ^ numb_2)
print("Bitwise NOT (~) of num_1 :", ~num_1)
print("Bitwise Left Shift (<<) :", num_1 << 1)  # Shifts bits of num_1 to the left by 1
print("Bitwise Right Shift (>>) :", num_1 >> 1)  # Shifts bits of num_1 to the right by 1

# Membership Operators
num_list = [1, 2, 3, 4, 5]
print("\nMembership Operations:")
print("Is num_1 in the list? (in) :", num_1 in num_list)
print("Is numb_2 not in the list? (not in) :", numb_2 not in num_list)

# Identity Operators
print("\nIdentity Operations:")
print("Is num_1 the same object as numb_2? (is) :", num_1 is numb_2)
print("Is num_1 not the same object as numb_2? (is not) :", num_1 is not numb_2)
