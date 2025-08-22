#  Set is an unordered collection of unique elements.
# 1. Unordered : Sets do not maintain any order of elements
# 2. Mutable : Sets can be modified after creation
# 3. Unique : Sets do not allow duplicate elements
# ================Common Operation===============
# 1. Adding elements : my_set.add(4) adds an element to the set
# 2. Removing elements : my_set.remove(2) removes an element from the set
# 3. Union : set1.union(set2) combines two sets
# 4. Intersection : set1.intersection(set2) finds common elements in two sets
# 5. Difference : set1.difference(set2) finds elements in set1 not in set2
# ========================USE Cases=================
# 1. Removing duplicates from a list
# 2. Membership testing
# 3. Mathematical set operations

my = {1,2,3}
print(my, type(my))

numbers = {1,2,2,3,4,5}
print(numbers)


numbers.add(0)
numbers.add(6)
numbers.add(7)
numbers.add(8)
print(numbers)


# Remove iss used to remove a number
numbers.remove(2)
print("*"*9)  

print(numbers)



print("*"*9)
# Discard is used to discard a nuber if is present but if is not present dont bring an error
numbers.discard(10)
print(numbers)



print("*"*20)
a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
print(b.difference(a))