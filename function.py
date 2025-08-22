# A function is a block of organized, reusuable code that perform a specific task
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Functions provide better modularity for your application and a high degree of code reusing.
# Python has many built-in functions that you can use, but you can also create your own functions.
# A function is defined using the def keyword, followed by the function name and parentheses.
# The parentheses may include parameters, which are values that the function can accept.
# The code block within every function starts with a colon (:) and is indented.



# Here is an example of a simple function that prints "Hello World":
def function_name():
    print("Hello World")

function_name() 


# Calling a Function
# To call a function, you simply use its name followed by parentheses.
def my_function():
  print("Hello from a function")

my_function()



# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# If you try to call the function with 1 or 3 arguments, you will get an error:
# EXAMPLE:
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")



# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



# Keyword Arguments
# You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Default Parameter Value
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")




def addtwo():
    print(2+2)
    print("Hello World")
    addtwo()




def name (my_name):
    print("my_name is ", my_name)
    name("Miracle")




def square(number,number2):
    print(number + number2)
    square(4, 5)




def ty(i, c=5):
    print(i + c)
ty(9)


def greet(name= "world"):
    print(f"hello, {name}! ")
greet()
greet("Alice")


def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweeden")
my_function("India")
my_function()
my_function("Brazil")