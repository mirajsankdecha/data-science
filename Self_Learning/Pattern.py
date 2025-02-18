


# for i in range(num, 0, -1):
#     print("*" * i)


for i in range(1, 8 ,1):
    print("*" * i)
for i in range(6, 0, -1):
    print("*" * i)


test = input("Enter the test : ")
test = test.replace("2", "@")
test = test.replace("3", "$")
test = test.replace("4", "#")
print(test)
