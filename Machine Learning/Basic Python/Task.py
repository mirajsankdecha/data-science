
# list1 = ["Hi","Hello"]
# print(list1)
# print(list1[0])
# print(list1[1])

# list2 = ["H","I","H","E","L","L","O"]
# print(list2)
# for i in range(0, len(list2), 1):
#     print(list2[i], end="")
# print()

# list3 = "Hello How Are You"
# print(list3.split(" ")[0])
# print(list3.split(" ")[1])
# print(list3.split(" ")[2])
# print(list3.split(" ")[3])

# for i in range(0, len(list3.split(" ")), 1):
#     print(list3.split(" ")[i], end="")

# list4 = list(list3.split(" "))
# print(list4)

#Task 5 : Distinoary Malipulation
# Given dictionaries
dict1 = {'a': 10, 'b': [20, 30], 'c': 40, 'd': 60}
dict2 = {'p': 100, 'q': [40, 80], 'a': 20, 'b': [80, 20], 'd': 70}

# Merging dictionaries
merged_dict = {}

# Combine keys from both dictionaries
for key in set(dict1) | set(dict2):
    if key in dict1 and key in dict2:
        # Convert to list if needed and merge without duplicates
        val1 = dict1[key] if isinstance(dict1[key], list) else [dict1[key]]
        val2 = dict2[key] if isinstance(dict2[key], list) else [dict2[key]]
        merged_dict[key] = list(set(val1 + val2))  # Remove duplicates
    elif key in dict1:
        merged_dict[key] = dict1[key] if isinstance(dict1[key], list) else [dict1[key]]
    else:
        merged_dict[key] = dict2[key] if isinstance(dict2[key], list) else [dict2[key]]

print("Merged Dictionary:", merged_dict)
