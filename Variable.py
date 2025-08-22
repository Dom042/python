# VARIABLE AND DATA TYPE
# Variable is a name given to a value, valueable are used to store and manipulate data in a program
my_name = "Miracle"
print(my_name)

num1 = 34
print(num1)

# Data types: they are values that a variable can hold
# Types of data trpes:
# FLOAT: E.g 3.14, -0.5
# INTEGERS: e.g 1, 2, 3, 4, 5
# STRINGS: e.g "hello", "Welcome"
# LIST: e.g [1, 2, 3], ['a', 'b', 'c']
# BOOLEAN: e.g True or False
# TUPLE; e.g (1, 2, 3, 4), ('a', 'b', 'c')
# DICTIONARY: E.g {'name': 'john', 'age': 30}
# SET: e.g {1, 2, 3}, {'a', 'b', 'c'}
x = 10
y = -5
print("x:",x, "y:",y, "type of x:", type(x), "type of y:", type(y),)


# Float
pi = 3.14
e = -0.001
print("pi:",pi, "e:",e,  "type of pi:", type(pi), "type of e:", type(e),)


# Strings
my_second_name = "ebube"
print(my_second_name, type(my_second_name))


# Lists: are ordered collections of items that can be of any data type, including strings, integers, float and other list, thry are mutable
# We use .append to add a new list
fruits =  ["apple", "banana", "cherry" ] 
print(fruits )


# To append
fruits =  ["apple", "banana", "cherry" ] 
fruits.append("gray")
print(fruits )


# To insert
fruits =  ["apple", "banana", "cherry" ] 
fruits.append("gray")
fruits.insert(1, "milk")
print(fruits, type(fruits))

# You can append in an empty list
empty = []
empty.append("miracle")
print(empty)

# Tuples are ordered, immutable collections of items that can be of any data types, including strings, integers, floats, and other tuples.
corrd = (12, 20.0)
print(corrd, type(corrd))


# Boolean Type
is_valid = True
not_valid = False
print(is_valid, type(is_valid))
print(not_valid, type(not_valid))


# Set: are unordered collections of unique elements.
colors = {"red", "green", "white"}
print(colors, type(colors))


# Instead of using .Append to add extra we use .Add
colors = {"red", "green", "white"}
colors.add("yellow")
print(colors, type(colors))


# Dictionary: are unordered collection of key-value pairs
# we call Dictionary object in javascript


person = {
    "name": "Alice",
    "age":20,
    "city": "New york"
}

print(person)

# How to attach additional value pairs
person = {
    "name": "Alice",
    "age":20,
    "city": "New york"
}
person["Email"] = "udeohadom@gmail.com"
person["Phone_no"] = 8109086654
print(person)



# Complex Numbers: are numbers that have both a real and imaginary part
z = 2 + 3j
print(z)


# Types of conversion
# IMPLICIT Conversion:
x = 5
y = 2.0
print(x + y)


# EXPLICIT Conversion
x = '5'
y = int(x)
print(y)

name = "JOHN DOE"
age = 20
height = 35.9
subjects = ["Mats", "English", "Python"]

Scores = {
    "Maths" : 79,
    "English" : 80,
    "python": 78,
}
is_enrolled = True


print(name, type(name))
print(age, type(age))
print(height, type(height))
print()


# Arithimetic operators
# '+' (Additon)
# '-' ()
# 
# 
# 
# 


a = 10
b = 5
addition = a + b
print("addition =", addition)
subtraction = a-b 
print("Subtraction =", subtraction)


first_name ="Dave"
last_name = "Mark"
add = first_name + last_name
print(add)
double = add * 3
print(double)


# 2 Comparison Operators
a = 10
b = 5


greater_than = a > b 
print(greater_than)
mine = b > a
print(mine)
equal_to = a == b
print(equal_to)
not_equal_to = a != b
print(not_equal_to)


# Logical operators: are symbols or words used to connect two or more expressions and return a Boolean value (True or False).
# AND
# OR 
# NOT
a =  True
b = False

Logical_and = a and b
print(Logical_and)

Logical_or = a or b
print(Logical_or)

Logical_not = not a
print(Logical_not)

# Assignment Operator

# '=' (Assign)
# '+=' (Add and assign)
# '-=' (Subtract and assign)
# '*=' (Multiply and assign)
# '%=' (Modulus and assign)


a = 10


a += 5
print(a)

a -= 5
print(a)

a *= 2
print(a)


a /= 5
print(a)

a %= 5
print(a)


# Identity Operators
# 'is' (Identical)
# 'is' not (not identical)


a = 10
b = 10
c = [10]
d = [ 10]

identity = c is b
print(identity)

identity = a is b
print(identity)


# ASSIGNMENT QUESTION
# Given six numbers, 
# a = 12.5, b = 3.2, c = 2.1, d = 4.8, e = 5.3, and f = 2.9, calculate the following complex expression:

# (((a + b) * (c - d) / (e + f)) ** 2 + ((a * b) % (c + d)) / (e - f) * (a ** (b - c)))




# ASSIGNMENT ANSWERS
# Define the variables
a = 12.5
b = 3.2
c = 2.1
d = 4.8
e = 5.3
f = 2.9

# Calculate the complex expression
result = (((a + b) * (c - d) / (e + f)) ** 2 + ((a * b) % (c + d)) / (e - f) * (a ** (b - c)))

# Print the result
print(result) 


# Class work
# Write a Python function called addfive that takes one number as input and prints the result of adding 5 to that number, then call the function two times using the number 10 and 15
def addfive(number):
    result = number + 5
    print(result)


addfive(10)
addfive(15)

def add(a,b):
    return a + b
print(add(9,5))
print("*"*20)