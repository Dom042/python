# loops 
# Loops are used to execute a block of code repeatedly.
# Python has two primitive loop commands:
# FOR LOOP
# WHILE LOOP



# Using FOR LOOP to print each fruit in the list
fruits = ["apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)




word = "Python"

for letter in word:
    print(letter)


# FOR LOOP
# Using FOR LOOP TO GIVE A NUMBER FROM 10 TO 0
for i in range(10, 0, -1):
    print(i)


for i in range(5):
    print(i)







# WHILE  LOOP
# Using WHILE LOOP to print numbers from 1 to 5

count = 1
while count <=5:
    print("count is:", count)
    count +=1


num = 10
while num >=1:
    print(num)
    num-=1


for i in range(10):
    if i == 5:
        break
    print(i)





numbers = [2, 3, 4, 5, 6, 7]
total = 2

for num in numbers:
    total *= num
    print("Total sum:", total) 
    


Student = {
    "name" : "Alice",
    "age" : 23,
    "grade" : "A",
    "Courses" : ["Math", "English"]
}


for key in Student:
    print(key, ":", Student[key])



number = []

for i in range (1, 7):
    number.append(i)

    print(number)






# Using continue statement 
# to skip an iteration
# Example: Skipping a specific number in a loop
for i in range(10):
    if i == 5:
        continue
    print(i)



    for i in range(5):
        if i == 2:
            continue
        print(i)


    print("*"*9)
    for numb in range(1,6):
        if numb == 3:
            continue
        print(numb)

    
    print("*"*9)
    for num in range(1,11):
        if num % 2 != 0:
            continue
        print(num)


print("*"*9)
# Using continue statement to skip an iteration
# Example: Skipping a specific number in a loop
foods = ["rice", "beans", "green-beans", "Okpa"]

for food in foods:
    if food == "green-beans":
        continue
    print("I like", food)




# The else Statement
# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



# Looping Through a String
for char in "Hello":
    print(char)




# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)




# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")



# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")



# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass