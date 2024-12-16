import pandas as pd
# Converting the list to series
data = [10,20,30,40,50]
my_series = pd.Series(data)
print(f"The Series of list is : {my_series}")
print(f"Filterout the values by indexing : {my_series[2]}")
new_data = [1,2,3]
s = pd.Series(new_data, index=["x","y","z"])
print(f"Filterout using the lables :\n {s} ")

# Converting the dictonary to series
dic = {
    "Name" : "Miraj Sankdecha",
    "Age" : 21,
    "Gender" : "Male"
}
s = pd.Series(dic)
print(f"Print the converted dic : \n{s}")
