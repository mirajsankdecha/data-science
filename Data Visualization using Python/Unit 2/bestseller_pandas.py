import pandas as pd

# Load the CSV file
df = pd.read_csv("E:/python/Data Visualization using Python/Unit 2/bestsellers.csv")

# 1. Basic Information
print("1. Shape:", df.shape)
print("2. Columns:", df.columns)
print("3. Index:", df.index)
print("4. Data types:\n", df.dtypes)
print("5. First 5 rows:\n", df.head())
print("6. Last 5 rows:\n", df.tail())
print("7. DataFrame info:\n")
df.info()
print("8. Summary statistics:\n", df.describe())

# 2. Data Selection
print("9. Select 'Name' column:\n", df['Name'])
print("10. Select first 5 rows using iloc:\n", df.iloc[:5])
print("11. Select rows where Year > 2015:\n", df[df['Year'] > 2015])

# 3. Data Cleaning
print("12. Check for null values:\n", df.isnull().sum())
df_cleaned = df.dropna()  # Dropping rows with missing values
print("13. Fill missing values:\n", df.fillna(0).head())
df_no_duplicates = df.drop_duplicates()  # Dropping duplicate rows
print("14. Remove duplicates:\n", df_no_duplicates.shape)

# 4. Data Manipulation
df['New_Column'] = df['Price'] * 0.9  # Add a new column
print("15. Add a new column:\n", df.head())
df = df.rename(columns={'Name': 'Book_Title'})  # Rename column
print("16. Rename a column:\n", df.columns)
df = df.drop(columns=['New_Column'])  # Drop a column
print("17. Drop a column:\n", df.head())
df_sorted = df.sort_values(by='Price', ascending=False)  # Sort rows
print("18. Sorted by Price:\n", df_sorted.head())

# 5. Statistical and Mathematical Operations
print("19. Mean Price:", df['Price'].mean())
print("20. Sum of Reviews:", df['Reviews'].sum())
print("21. Maximum Price:", df['Price'].max())
print("22. Minimum Price:", df['Price'].min())
print("23. Median Year:", df['Year'].median())
print("24. Variance of Reviews:", df['Reviews'].var())
print("25. Standard deviation of Reviews:", df['Reviews'].std())

# 6. Grouping and Aggregation
grouped = df.groupby('Year')['Price'].mean()
print("26. Average Price per Year:\n", grouped)
print("27. Count of Books per Year:\n", df.groupby('Year')['Name'].count())

# 7. Merging and Joining
df2 = pd.DataFrame({'Year': [2020, 2021], 'Discount': [10, 15]})
merged = pd.merge(df, df2, on='Year', how='left')
print("28. Merged DataFrame:\n", merged.head())

# 8. Handling Index
df_reset = df.reset_index(drop=True)  # Reset index
print("29. Reset index:\n", df_reset.head())
df_set_index = df.set_index('Book_Title')  # Set index
print("30. Set 'Book_Title' as index:\n", df_set_index.head())

# 9. Filtering
print("31. Filter rows where Price > 15:\n", df[df['Price'] > 15])

# 10. Value Counts and Unique Values
print("32. Unique Years:\n", df['Year'].unique())
print("33. Value counts of Year:\n", df['Year'].value_counts())

# 11. Advanced Selection
print("34. Selecting specific rows and columns:\n", df.loc[0:4, ['Name', 'Price']])

# 12. Transformation
df['Price'] = df['Price'].apply(lambda x: x * 1.1)  # Apply function
print("35. Transformed Prices:\n", df.head())

# 13. Pivot and Crosstab
pivot = df.pivot_table(values='Price', index='Year', aggfunc='mean')
print("36. Pivot Table:\n", pivot)
crosstab = pd.crosstab(df['Year'], df['Genre'])
print("37. Crosstab of Year and Genre:\n", crosstab)

# 14. Concatenation and Appending
concatenated = pd.concat([df, df2], axis=1)
print("38. Concatenated DataFrame:\n", concatenated.head())
appended = df.append(df2, ignore_index=True)
print("39. Appended DataFrame:\n", appended.tail())

# 15. Missing Value Handling
df_filled = df.fillna(method='ffill')
print("40. Forward Fill for Missing Values:\n", df_filled.head())

# 16. Exporting
df.to_csv("output.csv", index=False)
print("41. Exported DataFrame to CSV file.")

# 17. Memory Usage
print("42. Memory usage of DataFrame:\n", df.memory_usage())

# 18. Mathematical Functions
print("43. Correlation:\n", df.corr())
print("44. Covariance:\n", df.cov())

# 19. Advanced String Operations
df['Author_Upper'] = df['Author'].str.upper()  # Convert to uppercase
print("45. Uppercase Author Names:\n", df[['Author', 'Author_Upper']].head())
df['Author_Length'] = df['Author'].str.len()  # Length of strings
print("46. Length of Author Names:\n", df[['Author', 'Author_Length']].head())

# 20. Advanced Indexing
print("47. Check if index is unique:", df.index.is_unique)
print("48. Index Names:", df.index.names)

# 21. Visualization Helper
print("49. Plot of Year counts:")
df['Year'].value_counts().plot(kind='bar')

# 22. Boolean Mask
mask = df['Price'] > 15
print("50. Boolean Mask for Price > 15:\n", mask.head())
