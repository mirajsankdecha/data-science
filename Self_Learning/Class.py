# Creating the Class
class Animal :
    def cow(self) :
        print("Ohhhhhoooo")
    def elephant(self) :
        print("hmmmmmmmmmm")
animal = Animal()
output = animal.cow()
print(f"Its Sounds like {output}")


#  Creating the Constructor

class Calculation :
    def __init__(self,X,Y) :
        self.x = X
        self.y = Y
        sum = X + Y
        print(f"Sum of Two Number is : {sum}")
    def sub(self) :
        result = self.x - self.y
        print(f"Substraction of Two Number is : {result}")  
    def mul(self) :
        result = self.x * self.y
        print(f"Multiplication of Two Number is : {result}")
    def div(self) :
        result = self.x / self.y
        print(f"Division of Two Numbers is : {result}")
    def mod(self) :
        result = self.x % self.y
        print(f"The Modulo of Two Number is : {result}")
                   
cal = Calculation(X = 10, Y = 10)
cal.sub()
cal.mul()
cal.div()
cal.mod()

# Inheritance of Class

class mammal :
    def walk(self):
        print("Walking.....")
class Dog(mammal) :
    pass
class Cat() :
    def cat(self) :
        print("Meowwwwwwww")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.cat()