import pandas as pd

data = {
    'Name' : ["Miraj","Janvi","Darshit","Tanay"],
    'Age'   : [21,20,21,21],
    'City' : ["Rajkot","Rajkot","Babra","Babra"]
}
df = pd.DataFrame(data)
df.set_index("Name",inplace=False) # It will do the modification in the object
print(df)

