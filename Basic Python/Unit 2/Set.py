new_set = {1, 2, 3, 4, 5}
print(new_set)  # This will print the set
new_set.add(6)  # This will add 6 to the set
print(new_set)
new_set.remove(2)  # This will remove 2 from the set
print(new_set)
new_set.discard(7)  # This will discard 7 from the set
print(new_set)
new_set.clear()  # This will clear the set
print(new_set)

# Remove the Duplicate Elements from a List by Converting it to a Set
new_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
new_set = set(new_list)
print(new_set)  # This will print the set
