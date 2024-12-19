import pandas as pd

# Original data
data = {
    'Name': ["Miraj", "Janvi", "Darshit", "Tanay"],
    'Age': [21, 20, 21, 21],
    'City': ["Rajkot", "Rajkot", "Babra", "Babra"]
}
df = pd.DataFrame(data)

# Example 1: Using set_index without inplace=False
df_with_name_index = df.set_index("Name")  # Returns a new object
print("DataFrame with 'Name' as index:")
print(df_with_name_index)

# Example 2: Creating a DataFrame with RangeIndex
df_with_range_index = pd.DataFrame(data, index=pd.RangeIndex(5, 9, name='index'))  # Correct range to match data length
print("\nDataFrame with RangeIndex:")
print(df_with_range_index)

# Rename the index of the DataFrame with RangeIndex
df_with_range_index.rename(index={5: 'A', 6: 'B', 7: 'C', 8: 'D'}, inplace=True)  # Correct keys
print("\nModified DataFrame after renaming index:")
print(df_with_range_index)
