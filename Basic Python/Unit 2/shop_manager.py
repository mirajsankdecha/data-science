price_list = [129.99, 99.99, 49.99, 79.99, 149.99, 199.99, 299.99, 399.99, 499.99, 599.99]

lower_price = min(price_list)
higher_price = max(price_list)

print("The lowest price is: ", lower_price)
print("The highest price is: ", higher_price)

rounded_price = round(2 * sum(price_list) / len(price_list), 2) 

print("The Average price is: ", rounded_price)

price_list.sort()
print("The sorted price list is: ", price_list)
