import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/titanic.csv")

# Print the first and last rows of the dataset
print(titanic)  
print(titanic.head())  # Print the first 5 rows of the dataset
print(titanic.tail())  # Print the last 5 rows of the dataset
print(type(titanic))  # Print the type of the dataset
print(titanic.columns)  # Print all the columns of the dataset
print(len(titanic))  # Print the number of rows in the dataset
print(titanic.shape)  # Print the shape of the dataset
print(titanic.info())  # Print information about the dataset
print(titanic.dtypes)  # Print the datatypes of all columns in the dataset

# Perform calculations on the dataset
print(f"Minimum Value is:\n{titanic.min()}")
print(f"Maximum Value is:\n{titanic.max()}")
print(f"Sum Value is:\n{titanic.sum()}")
print(f"Filter the numeric value is:\n{titanic.sum(numeric_only=True)}")

# Fetch and print the particluar column
print(f"Names :\n{titanic['name']}")
print(f"Age :\n{titanic['age']} ")
