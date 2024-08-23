# Check the Year weather the year is leap year or not in Python

year = int(input("Enter the Year : "))

if (year%400==0) or (year%4==0 and year%100!=0)  :
    print("It is Leap Year")
else :
    print("It is not Leap Year")     