num = int(input("Enter the Number : "))
sum = 0

temp = num 

while temp > 0 :
    digit = temp % 10
    sum += digit  ** 3
    temp  //= 10

if num == sum :
    print("It is Amstrong Number")
else : 
    print("It is not Amstrong Number")
