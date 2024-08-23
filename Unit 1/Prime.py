num = int(input("Enter The Number : "))

if num > 1 :
    for i in range(2,num) :
        if i % 2 == 0 :
            print("It is Not Prime Number")
            break
        else :
            print("It is Prime Number")
            
