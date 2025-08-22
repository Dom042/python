

print('Hello world')

line = ""
line1 = "******************************"
line2 = "* WELCOME TO MY PYTHON CLASS FRIENDS *"
line3 = "******************************"


print(line)
print(line1)
print(line2)
print(line3)

price = 10
print (price) 

price = 10
price = 20
print (price)


print('*' * 100)

# # Imput
# name = input('What is your name? ')
# print('Hi ' + name)

# name = input('What is your name? ')
# favourite_color = input('What is your favourite color? ')
# print(name + ' likes ' + favourite_color)

# # Type conversion that ask and calculate our age
# birth_year = input('Birth year: ')
# # On the age line we have to convert birth-year string into an integer using int() function
# age = 2025 - int(birth_year)    
# print (age)


# # Ask a user their weight (in pounds), convert it to kilograms and print on the terminal
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.4
# print(weight_kg)

# # How to manipulate strings that have something inbetween
# course = ('Python for "Beginners"')
# print(course)

# course = ("Python's for Beginners")
# print(course)



# string for a multiple line message e.g Email message
# Three quotes to start and three to terminate the comment, it can be single or double quote
# email = '''
# Hi John,

# Here is our first email to you.

# Thank you,
# The support team.
# '''
# print(email)

#  index character start from 01234567 upward
# Positive index start from the front 012345
index_character = 'Python for Beginners'
print(index_character[0])

# Negative index -1 starts from the back whivh is the index of the last character
index_character = 'Python for Beginners'
print(index_character[-1])

# 
index_character = 'Python for Beginners'
print(index_character[0:3])


# Return initial index
index_character = 'Python for Beginners'
course = index_character[:]
print(course)

# Another way
name = 'Jennnifer'
print(name[0:-1])

# Len is used to calculate the number of characters 
course = 'Python for Beginners'
print(len(course))

# .pper case character
course = 'Python for Beginners'
print(course.upper())

# .lower case character
course = 'Python for Beginners'
print(course.lower())

# Find character method
course = 'Python for Beginners'
print(course.find('P'))


course = 'Python for Beginners'
print(course.find('o'))

course = 'Python for Beginners'
print(course.find('Beginners'))

# Method for replacing a character or a sequence of a charcter
course = 'Python for Beginners'
print(course.replace('Beginners', 'Absolute'))


# How to return if true or false from the characer
# Beware of case sensitive
course = 'Python for Beginners'
print('Beginners' in course)


course = 'Python for Beginners'
print('beginners' in course)

# # COURSES WE LEARN SO FAR
# # We use Len() to count a character
# len()
# # We learn Upper case, lower case, find and replace
# course.upper()
# course.lower()
# course.find()
# course.replace()
# # charcaters in a string
# '....' in course



# We have two types of Numbers 10, 6 numbers without a decimal point is called integer while one with a decimal point like 4.7, 3.234 is called Float
# OPERATOR
# Addition
print(4 + 6)

# Multiplication
print(4 * 3)

# Subtraction
print(18 - 5) 

# Two kind of division
print(10 / 3)

print(10 // 3)

# Modulus Retuen the remainder
print(10 % 3)

# Exponent Operator
print(10 ** 3)

# Augumented Assignment operator
y = 10
x = y + 3
print(x)

d = 10
d -= 3
print(d)


# 3 *  2 first before ADDING UP
x = 10 + 3 * 2
print(x)

# starts from 2 + 3, them multiply the outcome 5 with 10 and subtract 2 from it, parenthesis override the order
x = (2 + 3) * 10 - 2
print(x)


# print(math.ceil(2.9))

# print(math.floor(2.9))


# IF, ELIF AND ELSE STATEMENT
# If any of the statement is true, that's when it print the statement under it
# is_hott is True 
is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely Day")
    print("Enjoy your Day")


# is_cold is True
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely Day")

    print("Enjoy your Day")

# is_hot and is_cold were both false, so it will skip their statement and print It's a lovely Day and Enjoy your Day
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely Day")
    print("Enjoy your Day")

# A programme with this rules:
# Price of a house is $1m, if buyer has a good credit, they need to put 10% of the down payment otherwise they need to put 20% down payment
# SOLUTION
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down_payment: ${down_payment}")


# LOGICAL OPERATORS:
# AND: both condition
# OR: One condition
# NOT: Reverse any boolean value from true to false, false to true
# Another IF STATEMENT Question
# If applicant have high income and good credit, print he is eligible, and if the conditions are not met else statement follows
# SOLUTION

has_good_credit = True
has_high_income = False

if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Non Eligible")

# OR is a logical Statement it will show eligible if one of the condition is met
# If applicant have high income and good credit, print he is eligible, and if the conditions are not met OR Logical Statement will still print eligible for loan
# SOLUTION

has_good_credit = True
has_high_income = False

if has_good_credit or has_high_income:
    print("Eligible for loan")



# If applicant have good credit, and does'nt have criminal record
has_good_credit = True
has_criminal_record = False

if has_good_credit  and not has_criminal_record:
    print("Eligible for loan")



# COMPARISON OPERATORS
# > Operator
# < operator
# >= operator
# <= operator
# != operator
# == operator


# if temp is greater than 30 is a hot day, otherwise if is less than 10 is a cold day otherwise is neither hot or cold day 
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
    # outcome is "it's not a hot day cus 30 is no greater than 30, rather from 31 upwards"



# QUESTION
# If name is less than 3 character long output name must be at least 3 charcters, otherwise if it's more than 50 characters long output name can be a maximum of 50 characters, otherwise lastly name looks good
# SOLUTION
name = "j"

if len(name) < 3:
    print("Name must be at least 3 characters ")
elif len(name) > 50:
    print("Name must be a maximum of 50 charcters")
else:
    print("Name looks good!")



# Logic on How to calculate your weight in kilos or pounds
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')

# if unit.upper() == "L":
#     converted = weight * 0.4
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")


# Loops in Python are used to execute block of code repeatedly for a specified number of times. and two primary types are FOR Loops and WHILE Loops
# WHILE LOOP are used to execute a block of code as long as a certain condition is true
i = 0
while i < 5:
    print(i)
    i += 1



# # How to build a guessing game logic using WHILE LOOP
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print("Sorry you failed")



# # ASSIGNMENT
# # CAR ASSIMILATION GAME COMMAND, WHEN YOU TYPE START CAR STARTS, WHEN YOU TYPE STOP CAR STOP AND WHEN YOU TYPE QUITE TO QUITE THE GAME
# # SOLUTION
command = ""
started = False
while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car already started...")
        else:
         started =True
         print("Car Started...")
    

    elif command == "stop":
        if not started:
            print("Car already stopped...")
        else:
         started = False
        print("Car Stop.")


    elif command == "help":
        print("""
Start - to start the car
Stop - to stop the car
Quite - to quite the Game         
        """)
    elif command == "quite":
        break
    else:
        print("Sorry, I dont understand that")
    


# FOR LOOP are used to iterate over a sequence (such as a list, tuple, dictionary or string) and execute a block of code for each item.
# Loop control system: break terminates the loop entirely while continue skips the current iteration and moves on to the next one
# Syntax
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)




# Nested Loops: loops can be nested inside each other to creat more complete iteration
# Syntax
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")


        
