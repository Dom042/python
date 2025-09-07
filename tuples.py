# Tuples are immutable, so you can't reverse a tuple in-place. However you can create a new tuple with the elements in reverse order using slicing
# ===============Characters=================
# 1. Ordered : Tuples maintain the order of elements
# 2. Immutable : Tuples cannot be modified after creation
# 3. Indexed : Tuples are indexed, allowing access to elements by index
# ================Common Operation===============
# 1. Indexing : my_tuple[0] returns the first element
# 2. SLICING : my_tuple[1 : 3] returns a subset of element
# 3. Concatenation : my_tuple * 2 create a new tuple with repeated element
# 4. Repeatition : my_tuple * 2 create a new tuple with repeated elements 

# ========================USE Cases=================
# 1. Representing records
# 2. Returning multiple values
# 3. Immutable data

# 1. Representing records
student_record = ("John Doe", 20, "Computer Science")
print(student_record[0])  # Accessing name

print(student_record[1])  # Accessing age

# 2. Returning multiple values
def get_student_info():
    return ("Alice", 22, "Mathematics")


my_tuples = (1,2,3,4,5)
print(my_tuples, type(my_tuples))



# 3. Immutable data
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # This will raise an error because tuples are immutable


# 4. Storing multiple values
data = (42, "Hello", 3.14)
print(data)


# How to create a tuple
empty_tuple = ()
single_element_tuple = (1,)

fruits = ("apple", "banana", "cherry")

info = ("John", 23, 5.7, True)
print(info[1])
print(info[-1])
# How to Select items using Tuples
print(info[1:4])


new_fruits = fruits + ("Orange",)
print(new_fruits)


Student_Courses = ("Maths", "English", "Biology", "Chemistry", "Physics")
print(Student_Courses)
print(Student_Courses[::-1])
print(Student_Courses[1:5])


# ======================LIST=============

# Meat
# Vegetable
# Corn Flour


name1 = "Kamsy"
name2 = "justina"
name3 = "Despina"


classNames = ["Kamsy","justina", "despina"]
print(len(classNames))
# prints the values according to the index
print(classNames [0])
print(classNames [1])
print(classNames [2])


name1 = input("Enter your name: ")
height = input("Enter your height: ")
gender = input("Enter your gender: ")
isMarried = input("Are you married? (true/false): ")
myDetails = ["Kamsy", 5.6, "false", False]

print(type(myDetails))
con = list((name1, height, gender, isMarried))


# method
myDetails.append


# finction
print(type(con))












thislist = ["apple", "banana", "cherry"]
print(len(thislist))



list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]



# Assignment is on List and Tuple 

