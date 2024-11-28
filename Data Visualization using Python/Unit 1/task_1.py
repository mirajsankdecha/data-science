import numpy as np 

marks = np.random.randint(20,100,(5,4,2))
print(f"Mark are : {marks}")

marks[marks < 35] = 35

print("Mark of student 2th and 4th\n",marks[[1,3],:,:])

print("Mean of student is : ", np.mean(marks,axis=(1,2)))

print("Mean of subject is : ",np.mean(marks,axis=(0,2)))
