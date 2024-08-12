# Pratice While Loop Simple Example

# Even Numbers
print("Even Numbers")
i = 1 
while(i<=20) :
    if(i%2==0) :
        print(i, end=", ")
    i+=1    
# Odd Numbers 
print("Odd Numbers")
i=1
while(i<=20) :
    if(i%2!=0) :
        print(i, end=", ")
    i+=1
# Both Numbers
i = 1
while(i<=20) :
        if(i%2==0) :
             print("\nIt is Even",i)
        elif(i%2!=0) :
             print("\nIt is Odd",i)
        i+=1              
