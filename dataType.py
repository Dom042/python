# INTEGER
num = 10
print(type(num), num)


y = -5

m = 123456789




# FLOAT
a = 3.12

m = -86.9

user = 0.0
print(type(user), user)

d= 1.3e4
print(type(d), d)





# Complex Number
give = 3 + 4j
print(type(give),give)


add = 9j + 4
print(type(add), add)




# MATH Method
import math
ads_value = abs(-10)
print("Absolute value ", ads_value)

round_value = round(3.13467, 2)
print(round_value)

sqrt_value = math.sqrt(16)
print(sqrt_value)

cos_value = math.cos(40)
print(cos_value)

tan_value = math.tan(13)
print(tan_value)



# Strings Indexing
name1 = 'miraclce'
change1 = name1[0]
print(type(change1), change1)

name = "miracle"
change = name[1]
print(type(change), change)

name2 = """"Peter"""
change3 = name2[2]
print(type(change3), change3)

peter = name2[1:4]
print(peter)



# String Length
length = len(name2)
print(length)


# Changing Case
upper_case = name2.upper()
print(upper_case)
# Lowerupper_case
# tittle()

lower_case = name2.lower()
print(lower_case)



# Formatted String
myname = "john"
age = "30"
formatted_str = f"my name is {myname}, i am {age} years old"
print(formatted_str)


replace = formatted_str.replace("years", "months").replace("old", "born")
print(replace)




# List Method
my_list = [1,2,3,4,5,6,7,8,9]

my_list.append(60)

my_list.insert(1,35)

my_list.remove(35)
print((my_list), my_list)


my_list1 = [10, 11, 12, 13, 14, 15, 16, 17]
combine_list = my_list + my_list1
print(combine_list)




# List Slicing
print(my_list1[2:5])

# Reverse method
my_list1.reverse()
print(my_list1)


# Nested 

nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(nested_list)

print(nested_list[1])

print(nested_list[1] [1])

print(nested_list[2] [1])



copy_list = nested_list.copy()
print(copy_list)



# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
# 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# The values in dictionary items can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)


Student ={
    "name" : "Alice",
    "age" : 23,
    "grade" : "A",
    "Course" : ["Math", "English"]
}

print(Student)
print(Student.keys())
print(Student.values())


# Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


# There is also a method called get() that will give you the same result:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)





