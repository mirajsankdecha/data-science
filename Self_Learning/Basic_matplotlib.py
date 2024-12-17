import matplotlib.pyplot as plt

# Bargraph
# Sample data
year = ['2021', '2022', '2023', '2024']
values = [10, 25, 15, 30]

plt.bar(year, values)

# Corrected labels
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Bar Graph Example')

plt.show()
