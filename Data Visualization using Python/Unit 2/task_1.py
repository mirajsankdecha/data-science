import pandas as pd

titanic = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/titanic.csv")
print(titanic) #Print the first and last rows  of dataset
print(titanic.head) #Print the first 5 rows of dataset
print(titanic.tail) #Print the last 5 rows of dataset
print(type(titanic)) #Print the type of dataset
print(titanic.columns) #Print all the columns of dataset
print(len(titanic)) #Print all the rows of dataset
print(titanic.shape) #Print the shape of dataset
print(titanic.info) #Print the inforamtion of dataset
print(titanic.dtypes) #Print all the columns datatype in dataset
print(f"Minimum Value is :\n {titanic.min()}")
print(f"Maximum Value is :\n {titanic.max()}")
print(f"Sum Value is :\n {titanic.sum()}")
print(f"Filter the numeric value is :\n {titanic.sum(numeric_only=True)}")
