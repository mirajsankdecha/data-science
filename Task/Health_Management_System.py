# Design and implement a fully digital hopital management system using python yto simple the mangement of 10 patients and 5 doctor across 5 department : OPD , Dental , Eye , Gynocology and Child.

# The system should be able to:
# 1. Add Patient
# 2. Display All Patients
# 3. Find Patient by ID
# 4. List Patients by Department
# 5. Update Patient Details
# 6. Delete Patient
# 7. Check if Patient ID Exists
# 8. Copy Patient Dictionary
# 9. Add Doctor
# 10. Display All Doctors
# 11. Find Doctor by ID
# 12. List Doctors by Department
# 13. Update Doctor Details
# 14. Delete Doctor
# 15. Check if Doctor ID Exists
# 16. Copy Doctor Dictionary
# 17. Merge Patient and Doctor Dictionaries
# 18. Create Dictionary from Lists (IDs and Names)
# 19. Add New Field to Patient Record
# 20. Add New Field to Doctor Record
# 21. Exit


Health_Management_System = {}

while True:
    print("\n--- Health Management System ---")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Find Patient by ID")
    print("4. List Patients by Department")
    print("5. Update Patient Details")
    print("6. Delete Patient")
    print("7. Check if Patient ID Exists")
    print("8. Copy Patient Dictionary")
    print("9. Add Doctor")
    print("10. Display All Doctors")
    print("11. Find Doctor by ID")
    print("12. List Doctors by Department")
    print("13. Update Doctor Details")
    print("14. Delete Doctor")
    print("15. Check if Doctor ID Exists")
    print("16. Copy Doctor Dictionary")
    print("17. Merge Patient and Doctor Dictionaries")
    print("18. Create Dictionary from Lists (IDs and Names)")
    print("19. Add New Field to Patient Record")
    print("20. Add New Field to Doctor Record")
    print("21. Exit")

    choice = input("Enter your choice (1-21): ")

    if choice == "1":  # Add Patient
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        department = input("Enter Department: ")
        age = input("Enter Age: ")
        symptoms = input("Enter Symptoms: ")
        Health_Management_System[patient_id] = {"Name": name, "Department": department, "Age": age, "Symptoms": symptoms}
        
        print("Patient Added Successfully!")
    elif choice == "2":
        for patient_id, details in Health_Management_System.items():
            print(f"ID: {patient_id}, Name: {details['Name']}, Department: {details['Department']}, Age: {details['Age']}, Symptoms: {details['Symptoms']}")    
            
    elif choice == "3":
        patient_id = input("Enter Patient ID to search: ")
        if patient_id in Health_Management_System:
            print(f"ID: {patient_id}, Details: {Health_Management_System[patient_id]}")
        else:
            print("Patient not found.")        