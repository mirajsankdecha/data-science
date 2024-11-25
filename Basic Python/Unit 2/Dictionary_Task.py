emp = {
    1: {"name": "John", "age": 25, "department": "HR", "salary": 50000},
    2: {"name": "Smith", "age": 30, "department": "IT", "salary": 60000},
    3: {"name": "Alice", "age": 35, "department": "Finance", "salary": 70000},
    4: {"name": "Bob", "age": 40, "department": "HR", "salary": 80000},
    5: {"name": "Cathy", "age": 45, "department": "IT", "salary": 90000},
    6: {"name": "David", "age": 50, "department": "Finance", "salary": 100000},
    7: {"name": "Eva", "age": 55, "department": "HR", "salary": 110000},
    8: {"name": "Frank", "age": 60, "department": "IT", "salary": 120000},
    9: {"name": "George", "age": 65, "department": "Finance", "salary": 130000},
    10: {"name": "Harry", "age": 70, "department": "HR", "salary": 140000},
}

# Problem 1
# for i,j in emp.items():
#     print(i," ",j)

# Problem 2
# iid = int(input("Enter the Employee ID : "))
# for i in emp:
#     if emp[i]["id"] == iid:
#         print(emp[i])
#         break
#     else:
#         print("Employee Not Found")

# Problem 3
for i in emp:
    if emp[i]["department"] == "HR":
        print(emp[i])

# Problem 4
emp["emp1"].update(
    {
        "name" : "Miraj",
        "age" : 21,
        "department" : "IT",
        "salary" : 5000000000000
    }
)
print(emp.get("emp1"))