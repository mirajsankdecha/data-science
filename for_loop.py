# Pratice Of Asterisk Using For Loop Pattern 

# Simple
for i in range(1,6,1) :
    for j in range(1,i+1) :
        print("* ",end="")
    print()
# Reverse
for i in range(5,0,-1) :
    for j in range(i) :
        print("* ",end="")
    print()     