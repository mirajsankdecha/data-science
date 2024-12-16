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
# It work on 1D array
dic = {
    "Name" : "Miraj Sankdecha",
    "Age" : 21,
    "Gender" : "Male"
}
s = pd.Series(dic)
print(f"Print the converted dic : \n{s}")
# Its works on rows and columns if we have 2D array
stu_nm = {
    "Students" : ["Darshit","Tanay","Kapil"]
}
ps = pd.DataFrame(stu_nm)
print(ps)

# Convert the 2D array into dataframe

info_data = [["Miraj",21,"Rajkot"],
             ["Vrushti",20,"Jalgaov"]]
df = pd.DataFrame(info_data,columns=["Name","Age","City"])
print(df)

