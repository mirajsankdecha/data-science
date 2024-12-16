import pandas as pd

#Print from CSV file
# states = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/states.csv")
# print(states)

#Print from Excel file
kc = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/kc_house_data.csv")
print(kc) # Print first and last 5 rows and columns
print(kc.head()) # print the first 5 rows
print(type(kc)) # Print the type of dataframe
print(kc.columns) # Print all the columns
print(f"Total Rows in dataset : {len(kc)}")
print(kc.shape)
print(f"size of dataset is : {kc.size}") # Print the size of dataset
print(f"Data of first 200 rows : {kc.head(200)}") #Print the first 200 rows
print(f"{kc.tail()}")
print(f"{kc.tail(-1)}") # print negative indexing in the dataset
print(kc.info) # Print all the inforamtion of dataset