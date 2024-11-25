import numpy as np
# Assignment 1
# Step 1 Creating the Array
stock_count = np.array([50,100,150,200,250])
price = np.array([20.5,35.0,15.0,50.0,80.0])
# Step 2 Calculating the Stock Value
stp1 = stock_count * price
print(f"Stock Value is : {stp1}")
# Step 3 Total inventory value
print(f"Total Inventory Value is : {stp1.sum()}")
# Step 4 Product with the highest stock value
print(f"The Highest Stock Value is : {stp1.max()}")

# Assignment 2
# Step 1 : Generating the Random Number for Daily Sales
randnum = np.random.randint(50,200, size=10)
# Step 2 : Calculating the Statistics
avg = randnum.mean()
print(f"Calculating the Avgerage of Sales : {avg}")
print(f"Calculating the Maximum of Sales : {randnum.max()}")
print(f"Calculating the Minumum of Sales : {randnum.min()}")
# Step 3 Calculating the Cumulative Sales
cum_sales = randnum.cumsum()
print(f"Calculating the Cumulative Sales : {cum_sales}")

