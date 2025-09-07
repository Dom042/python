# Conditional statement allow your program to make decisions and excute different code blocks depending on whether a condition is True or False

# The if Statement: runs a block of code only if the condition is true

x = 10
if x > 5:
    print("x is greater than 5")



# The if-else Statement: Provides an alternative path when the condition is false

x = 2
if x > 5:
    print("x is grater than 5")
else:
    print("x is not gretaer than 5")


# The if-elif-else Statement: used for multiple conditions

x = 0
if x > 0:
    print("positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")


# Nested if Statement: You can put one if inside another

x = 20
if x > 10:
    if x % 2 == 0:
        print("x is greater than 10 ane even")



# Using and, or, not (Logical Operator): combine conditions

age = 25
if age > 18 and age < 30:
    print("Young adult")
if age < 18 or age > 60:
    print("Special age group")
if not age == 20:
    print("Age is not 20")



# Conditional Statements with membership operator: in and not in

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("banana is in the list")
if "orange" not in fruits:
    print("Orange is not in the list")



# conditiional Statements with identity Operator: is and is not

x = None
if x is None:
    print("x is None")
if x is not None:
    print("x has a value")




# Multiple Conditions in one line:
x = 12
if 10 < x < 20:
    print("x is between 10 and 20")





# Practical Example

score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade) 