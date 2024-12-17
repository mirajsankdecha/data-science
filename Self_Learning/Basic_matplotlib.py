import matplotlib.pyplot as plt

# Sample data
year = ['2021','2022','2023','2024']
values = [10,25,15,30]

plt.bar(year,values)

plt.xlable('year')
plt.ylable('values')
plt.title('Bar Graph Example')

plt.show()