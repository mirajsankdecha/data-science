import numpy as np

# Numpy Array Integer
monthly_sales = np.array([10,20,15,30,25,18])
total_sales = np.sum(monthly_sales)
print(total_sales)
average = np.mean(monthly_sales)
print(average)
mask = (monthly_sales > 20 )
print(monthly_sales[mask])

# String Operation
product_data_array = np.array(["Headphone","Mobile","Pendrive","Tablet","Laptop","PC"])
lower_array = np.char.lower(product_data_array)
print(f"Lower of product array is : {lower_array}")
check = np.isin("Table",lower_array).all()
if check == False :
    print("Table is not available in array")
else : 
    print("Table is available in array")   

total_number = len("".join(product_data_array))
print(f"Total number of character present in array : {total_number}")

product_data_array[1] = "Smartphone"
print(f"Product List is: {product_data_array}")     