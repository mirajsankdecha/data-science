import numpy as np

# Task 1 : Create a Array
stock_price = np.random.randint(100,500, size=((5,7)))
print(f"Price of Company : {stock_price}")

#Task 2 : Find the Shape of Array
shape = stock_price.shape
print(f"Shape of Array is : {shape}")

#Task 3 : Access the price of 3rd company on fourth day

access_price = stock_price[2,3]
print(f"The Price of 3rd Company on 4th Day is : {access_price}")

#Task 4 : Slice the price of first two company for first three days
