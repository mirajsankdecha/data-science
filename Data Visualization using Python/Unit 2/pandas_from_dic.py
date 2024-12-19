import pandas as pd

data = {
    'Name' : ["Miraj","Janvi","Darshit","Tanay"],
    'Age'   : [21,20,21,21],
    'City' : ["Rajkot","Rajkot","Babra","Babra"]
}
df = pd.DataFrame(data)
df.set_index("Name",inplace=False) # It will do the modification in the object(inplace=)
print(df)


# Rename the index
df.rename(index={0:'A',1:'B',2:'C'}, inplace=True) # When we use false we get the new object with the modification while the leaving the orginal object unchanged
# Display dataframe after index is renamed
print(f"Modified Dataframe : {df}") # No new object is return 



