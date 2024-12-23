import pandas as pd

# Original Data
student = {
    "Name" : ["Miraj","Darshit","Tanay"],
    "Age" : [21,21,21],
    "City" : ["Rajkot","Babra","Babra"]
}
df = pd.DataFrame(student)
print(f"Student Data is : {df}")

# Appending the Key and Values
address = ["Gujarat","Gujarat","Gujarat"]
df['Address'] = address
print(df)

