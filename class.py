# ============================CLASS============================
# class is a blueprint for creating objects, it allows you bundle data and functionality together. Classes defines the properties (called attribute) and behaviors (called methods) of the objects you create from them.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):

        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 30)
p1.greet()






class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"The {self.brand} {self.model} is starting.")

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
        

car1.start()
car2.start()






class king:
    pass


class TeddyBear:
    color = "red"
    size = "big"

my_toy = TeddyBear()
print(type(my_toy), my_toy.color, my_toy.size)




class Car:
    model = 25
    color = "blue"
    wheels = 4

print("*"*9)
my_car = Car()
print(my_car.model)
print(my_car.color)
print(my_car.wheels)




class Car:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def mycar(self):
        print("This is my car")


my_car = Car("red", 4)
print(my_car.color)
print(my_car.wheels)
my_car.mycar()
print(type(my_car))




class Car:
    def __init__(self, name, color, wheels):
        self.color = color
        self.wheels = wheels
        self.name = name

    def mycar(self):
        print("This is my car and it is a", self.name)

my_car = Car("BMW", "red", 4)
my_car.mycar()



# Create a class called Dog with name and age.
# Make a method called bark that print "Woof!"
# 
class Dog:
    def __init__(self, name,shelf, age):
        self.name = name
        self.shelf = shelf
        self.age = age
    def bark(self):
        print("Woof! Woof!")
    def info(self):
        print(f"My dog's name is {self.name} and {self.shelf} he is {self.age} years old.")

my_dog = Dog("Buddy", "Shephard", 3)
my_dog.bark()
my_dog.info()



# Correction

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("woof")

dog1 = Dog("rex", 5)
dog2 = Dog("rex", 23)


dog1.bark()
dog2.bark()



# ==============INHERITANCE===================
# Is a way to create a new class (called child class or subclass) that inherit attribute and method from an existing class (called parent class or base class)

# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):   # Overriding method
        print("Woof! Woof!")

# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        print("Meow!")

# Objects
a = Animal()
a.speak()   # Output: This animal makes a sound

d = Dog()
d.speak()   # Output: Woof! Woof!

c = Cat()
c.speak()   # Output: Meow!





# ==============TYPE INHERITANCE============
# SINGLE INHERITANCE
class Parent:
    pass

class Child(Parent):
    pass


# MULTIPLE INHERITANCE
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    def skills(self):
        super().skills()   # Calls Father first (Method Resolution Order)
        Mother.skills(self)

c = Child()
c.skills()  
# Output: Gardening
#         Cooking


# multi-level inheritance
class Grandparent:
    def house(self):
        print("Big house")

class Parent(Grandparent):
    def car(self):
        print("Family car")

class Child(Parent):
    def bike(self):
        print("Sports bike")

c = Child()
c.house()  # From Grandparent
c.car()    # From Parent
c.bike()   # From Child


# HIERARCHICAL INHERITANCE
class Parent:
    def work(self):
        print("Parent works hard")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.work()
c2.work()


# HYBRID INHERITANCE
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)  # Calls parent constructor
        self.school = school

s = Student("Dominic", "UNN")
print(s.name)     # Dominic
print(s.school)   # UNN






class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} make a sound")


class Man(Animal):
    def walk(self):
        print(f"{self.name} walks")

man = Man("miracle")
man.walk()





class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class info(Animal):
    def bark(self):
        print(f"My dog name is {self.name}, she is {self.age} years old")

go =info("lex", 19)
go.bark()




class Company:
    def __init__(self, name, year):
        self.name = name
        self.year = year

my_company = Company("nissan , nssn2", 2015)

class Car(Company):  
    def __init__(self, name, year, model):
        super().__init__(name, year)
        self.model = model

    def display_info(self):
        print(f"Company: {self.name}, Year: {self.year}, Model: {self.model}")

my_car = Car("Tesla", 2022, "Model S")
my_car.display_info()



#   classwork: Create a class called Company with attributes name,year
# inherite from Company and a class call car and give it a default init of model= cammry, color= red, wheels= 4
# and print the attributes of the car
  



class Company:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Car(Company):
    def __init__(self, name, year, model="Camry", color="Red", wheels=4):
        super().__init__(name, year) 
        self.model = model
        self.color = color
        self.wheels = wheels

    def show_details(self):
        print(f"Company: {self.name}")
        print(f"Established Year: {self.year}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Wheels: {self.wheels}")



my_car = Car("Toyota", 1937)
my_car.show_details()

# Multileval inheritance

class Grandparent():
    def show_ep(self):
        print("i am the Parent")

class Parent(Grandparent):
    def show_p(self):
        print("I am the child")

class Child(Parent):
    def show_c(self):
        ("I am the child")

c = Child()
c.show_ep()
c.show_p()

class shape:
    def draw(self):
        print("Drawing shap")


class Rectangle(shape):
    def square_info(self):
        print("this is a rectangle")


class Checking:
    def __init__(self, name, score):
    
        self.name = name
        self.score = score

    def check_pass(self):
        if self.score >= 50:
            print(self.name, " passed.")
        else:
            print(self.name, " failed.")

student1 = Checking("john", 40)
student2 = Checking("john", 80)


student1.check_pass()
student2.check_pass()



# Multiple inheritance
class Mother:
    def cook(self):
        print("father is in the palour")

class Father:
    def parlour(self):
        print("Father is in the palour")

class Child(Mother, Father):
    def child_me(self):
        print("I have both blood")


print("*"*9)
d= Child()
d.cook()
d.parlour()
d.child_me()   


class Mother_Father:
    def parent(self):
        print("we the Father and Mother")

class Me(Mother_Father):
    def child(self):
        print("We the children")

class Brother(Mother_Father):
    def child(self):
        print("We the children")

class Sister(Mother_Father):
    def child(self):
        print("We the children")


us = Me()
us.parent()
us.child()

sis = Sister()
sis.parent()
sis.child()

bro = Brother()
bro.parent()
bro.child()






# Class work: Using class and function check if a user is 18 or above print his name and he is 18 else print the person name and is a child after it create a two class and inherite from them using Multileval inheritance
# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Function to check age
    def check_age(self):
        if self.age >= 18:
            print(f"{self.name} is 18 or above.")
        else:
            print(f"{self.name} is a child.")

# First derived class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

# Second derived class (multilevel inheritance)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age, student_id)
        self.course = course

    def display_course(self):
        print(f"Course: {self.course}")


# Example usage
# Base check
p1 = Person("John", 20)
p1.check_age()

p2 = Person("Alice", 15)
p2.check_age()

# Using multilevel inheritance
grad = GraduateStudent("Mike", 22, "ST123", "Computer Science")
grad.check_age()       
grad.display_student() 
grad.display_course() 


# How to use or manipulate Loops in our Class

class student_1:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Hello, i am ", self.name)

names = [student_1("king"), student_1("jnr"), student_1("sam")]

for my in names:
    my.hello()

class Num:
    def numbers(self):
        for i in range(1, 6):
            print(i)

n = Num()
n.numbers()

class numbers:
    def print_even(self):
        for i in range(1, 100):
            if i % 2 == 0:
                print(i)

kin = numbers()
kin.print_even()

