import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Year': ['2021', '2022', '2023', '2024'],
    'Sales': [10000, 15000, 20000, 25000],
    'Profit': [3000, 4000, 5000, 6000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Calculate profit margin and add it as a new column
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

# Print updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# Plot sales and profit over years
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['Sales'], label='Sales', marker='o', linestyle='--')
plt.plot(df['Year'], df['Profit'], label='Profit', marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Amount (in $)')
plt.title('Sales and Profit Over Years')
plt.legend()

# Show the plot
plt.show()
