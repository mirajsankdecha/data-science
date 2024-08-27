# Let's work with a string to explore some common string functions in Python.
name = "Miraj Sankdecha"

# First, we want to check the type of our variable
print("1. Type of 'name':", type(name))  # This tells us that 'name' is a string

# Next, we find out how long our string is
print("2. Length of 'name':", len(name))  # This gives us the number of characters in 'name'

# Let's look at individual characters in our string
print("3. First character:", name[0])    # Output will be 'M'
print("4. Second character:", name[1])   # Output will be 'i'
print("5. Last character:", name[-1])    # Output will be 'a' (last character)

# We can also slice our string to get a part of it
print("6. Sliced string [0:5]:", name[0:5])  # This extracts 'Miraj'
print("7. Full string [:]:", name[:])        # This gives us the entire string 'Miraj Sankdecha'

# Now let's explore some useful string methods
print("8. Lowercase:", name.lower())  # Converts the entire string to lowercase
print("9. Uppercase:", name.upper())  # Converts the entire string to uppercase
print("10. Title case:", name.title())  # Capitalizes the first letter of each word

# We can find where a substring is located
print("11. Find 'Miraj':", name.find("Miraj"))  # Shows where 'Miraj' starts, which is index 0

# Let's split our string into a list of words
print("12. Split by space:", name.split(" "))  # Splits the string into ['Miraj', 'Sankdecha']

# Adding more string methods to show
print("13. Replace 'Sankdecha' with 'Patel':", name.replace("Sankdecha", "Patel"))  # Replaces 'Sankdecha' with 'Patel'
print("14. Starts with 'Miraj':", name.startswith("Miraj"))  # Checks if the string starts with 'Miraj'
print("15. Ends with 'Decha':", name.endswith("Decha"))  # Checks if the string ends with 'Decha'
print("16. Count of 'a':", name.count("a"))  # Counts how many times 'a' appears in the string

# Removing spaces from the start and end
print("17. Strip leading and trailing spaces:", "  " + name + "  ".strip())  # Removes extra spaces around the string

# Justifying the text in different ways
print("18. Right justify to 20 characters:", name.rjust(20, '*'))  # Adds '*' to the left to make the string 20 characters wide
print("19. Left justify to 20 characters:", name.ljust(20, '*'))   # Adds '*' to the right to make the string 20 characters wide
print("20. Center to 20 characters:", name.center(20, '*'))  # Centers the string with '*' padding on both sides

# Checking if the string is alphanumeric, alphabetic, or numeric
print("21. Is alphanumeric:", name.isalnum())  # Checks if all characters are letters or numbers
print("22. Is alphabetic:", name.isalpha())  # Checks if all characters are letters
print("23. Is numeric:", name.isdigit())  # Checks if all characters are digits

# A few more examples
text = "Python programming is fun!"
print("24. Replace 'fun' with 'awesome':", text.replace("fun", "awesome"))  # Replaces 'fun' with 'awesome'
print("25. Uppercase text:", text.upper())  # Converts the text to uppercase
print("26. Title case text:", text.title())  # Capitalizes the first letter of each word in the text
