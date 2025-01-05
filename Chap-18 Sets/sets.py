# Sets in Python 

# charaterstics of set 
#1. unique values/items 
#2. unordered - no indexing 
#3. mutable- add/remove elements
#4. Immuatable elements - replace/modify existing elements 

# create set using curly braces 
my_set = {1,2,3}
print(my_set)
print(type(my_set))

# create set using set constructor 
my_set2 = set([4,5,6]) 
print(my_set2)  

# set operations
#adding elements
numbers = {1,2,3,4} 
numbers.add(100)
print(numbers) 

# removing elements 
#remove 
fruits = {'apple', 'mango', 'banana'}
# fruits.remove('banana') # if element not present show error
print(fruits) 

#discard 
fruits.discard('apple') # doesn't show error
print(fruits)


# Set Methods
#1. union - combine elements from 2 sets 
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
# print(union_set) 

# union alternative 
union_set2 = set1 | set2 
# print(union_set2) 

#2. Intersection - common elements 
set1 = {1,2,3,4}
set2 = {3,4,5}
inter_set = set1.intersection(set2)
# print(inter_set) 

# intersection alternative 
inter_set2 = set1 & set2 
# print(inter_set2) 

#3. Difference - element present in first set only but not in second set 
set1 = {1,2,3,4}
set2 = {3,4,5}
diff_set = set1.difference(set2)
# print(diff_set) 

# Difference alternative 
diff_set2 = set1 - set2 
# print(diff_set2) 

#4. Symmertic Difference - element in either set but not in both 
set1 = {1,2,3,4}
set2 = {3,4,5,6}
sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)

# Symm Diff alternative 
sdiff_set2 = set1 ^ set2 
# print(sdiff_set2)


# Set Iterations
# for loop
numbers = {1,2,3,4,5}
for i in numbers:
    print(i)

# while loop - doesn't support 


# Set compreshesion 
squares = {x**3 for x in range(1,6)} 
print(squares)
