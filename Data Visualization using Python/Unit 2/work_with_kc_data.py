import pandas as pd

house = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/kc_house_data.csv")
print(f"Minimum value is :\n{house.min()}") #  Get the minimum value from dataset
print(f"Maximum value is :\n{house.max()}") # Get the maximum value from dataset
print(f"Sum of Value is :\n {house.sum()}") # Get the sum value from dataset
print(f"Filter the Numeric Value is :\n {house.sum(numeric_only=True)}") 