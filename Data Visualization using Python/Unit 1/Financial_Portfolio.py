import numpy as np

# Task 1 : Create a Array
stock_price = np.random.randint(100,500, size=((5,7)))
print(f"Price of Company :\n {stock_price}")

#Task 2 : Find the Shape of Array
shape = stock_price.shape
print(f"Shape of Array is : {shape}")

#Task 3 : Access the price of 3rd company on fourth day

access_price = stock_price[2,3]
print(f"The Price of 3rd Company on 4th Day is : {access_price}")

#Task 4 : Slice the price of first two company for first three days

slice_price = stock_price[:2,:3]
print(f"Price of first two company on 3 days is :\n {slice_price}")

#Task 5 : Find the price of company that are greater than 300 
greater_price = stock_price[stock_price > 300]
print(f"The company which price have greater than 300 are :\n {greater_price}")

#Task 6 : Calculate the daily return for first company
daily_returns_company1 = (stock_price[0,1:] - stock_price[0,:-1]) / stock_price[0,:-1]
print(f"Daily Return of 1st company is :\n {daily_returns_company1}")

#Task 7 : Find the sum of all stock price
sum_price = stock_price.sum()
print(f"Sum of Price of Compnies is : {sum_price}")

#Task 8 : Calculate the mean of stock price for each company
mean_each_company = stock_price.mean(axis=1)
print(f"Mean of stock price of each company is :\n {mean_each_company}")

#Task 9 : Finding the standard deviation of stock prices for each company
std_per_day = stock_price.std(axis=0)
print(f"Standard Deviation of stock price for each day is :\n {std_per_day}")

#Task 10 : Finding the minimum and maximum price for each company
min_price = stock_price.min(axis=1)
max_price = stock_price.max(axis=1)
print(f"Minimum price for each company : {min_price}")
print(f"Maximum price of each company is : {max_price}")

#Task 11 : Add a 1D array of transaction costs
transaction_costs = np.array([5,5,5,5,5,5,5])
adjusted_price = stock_price + transaction_costs
print(f"Stock prices after adding transaction costs : \n{adjusted_price}")

#Task 12 : 

# Task 13 : finding the co-variance matrix of stock price
cov_var = np.cov(stock_price)
print(f"Co-Variance Matrix is :\n {cov_var}")

#Task 14 : Sort the data of stock prices for the 4th company
sorted_price = np.sort(stock_price[3])
print(f"Sorted stock price for the 4th company :\n {sorted_price}")

#Task 15 : Generate random weight for a portfolio of 5 stock that sum to 1
weights = np.random.random(5)
weights /= weights.sum()
print(f"Random Portfolio weights : {weights}")

#Task 16 : Find the index of the highest price for each company
max_price_indices = stock_price.argmax(axis=1)
print(f"Indices of the highest price for each company : {max_price_indices}")

