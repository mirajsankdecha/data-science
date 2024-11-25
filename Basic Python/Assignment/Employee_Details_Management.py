# Employee Details Management
employees = {}

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee Details")
    print("2. Display All Employees")
    print("3. Find Employee by ID")
    print("4. List Employees by Department")
    print("5. Update Employee Details")
    print("6. Delete Employee")
    print("7. Check if Employee ID Exists")
    print("8. Copy Employee Dictionary")
    print("9. Merge Employee Dictionaries")
    print("10. Create Dictionary from Lists (IDs and Salaries)")
    print("11. Add New Field to Employee Record")
    print("12. Exit")

    choice = input("Enter your choice (1-12): ")
    
    if choice == "1":  # Add Employee
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")
        employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
        print("Employee added.")
    
    elif choice == "2":  # Display All Employees
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}, Salary: {details['salary']}")
    
    elif choice == "3":  # Find Employee by ID
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in employees:
            print(f"ID: {emp_id}, Details: {employees[emp_id]}")
        else:
            print("Employee not found.")
    
    elif choice == "4":  # List Employees by Department
        department = input("Enter Department: ")
        for emp_id, details in employees.items():
            if details['department'] == department:
                print(f"ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}")
    
    elif choice == "5":  # Update Employee Details
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in employees:
            print("What to update? (name/age/department/salary)")
            field = input("Enter field: ")
            if field in employees[emp_id]:
                new_value = input(f"Enter new {field}: ")
                employees[emp_id][field] = new_value
                print(f"{field.capitalize()} updated.")
            else:
                print("Invalid field.")
        else:
            print("Employee not found.")
    
    elif choice == "6":  # Delete Employee
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted.")
        else:
            print("Employee not found.")
    
    elif choice == "7":  # Check if Employee ID Exists
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee ID exists.")
        else:
            print("Employee ID does not exist.")
    
    elif choice == "8":  # Copy Employee Dictionary
        employees_copy = employees.copy()
        print("Employee dictionary copied.")
    
    elif choice == "9":  # Merge Employee Dictionaries
        other_employees = {}
        num_entries = int(input("Enter number of employees for the second dictionary: "))
        for i in range(num_entries):
            emp_id = input(f"Enter Employee ID {i+1}: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            department = input("Enter Department: ")
            salary = input("Enter Salary: ")
            other_employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
        employees.update(other_employees)
        print("Employee dictionaries merged.")
    
    elif choice == "10":  # Create Dictionary from Lists
        ids = input("Enter Employee IDs (comma-separated): ").split(",")
        salaries = input("Enter Salaries (comma-separated): ").split(",")
        new_dict = dict(zip(ids, salaries))
        print("New dictionary created:", new_dict)
    
    elif choice == "11":  # Add New Field to Employee
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            field = input("Enter new field (e.g., phone number): ")
            value = input(f"Enter value for {field}: ")
            employees[emp_id][field] = value
            print(f"Added {field} to Employee ID {emp_id}.")
        else:
            print("Employee not found.")
    
    elif choice == "12":  # Exit
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
