# Lists in Python 

# create list 

my_list = [1,2,3]
print(my_list) 

print(type(my_list)) 

my_list2 = [1, 'Madhav', 'Keshav', True, 3.14]
print(my_list2) 
print(type(my_list2)) 

my_list3 = [1,2, [3,4] ,True, [5,6,7] ]
print(my_list3) 
print(type(my_list3))  


# Access list - Indexing 
list1 = [10, 20, 30, 40, 50]
# index: 0   1   2   3   4
# index:-5  -4  -3   -2  -1

# first element
print(list1[0])

# second element
print(list1[1])

# last element
print(list1[-1])

# second last element
print(list1[-2])  


# list - slicing 

list2 = [10, 20, 30, 40, 50, 60, 100]
# index: 0   1   2   3   4   5    6
# index: -7 -6  -5  -4  -3   -2  -1

# slicing syntax 
# list_name[start : stop : step]

# start is inclusive, default is 0
# stop is exclusive, default is -1/last index value 
 
# first 3 elements 
print(list2[0:3:1])

# elements from index 1 to 4
print(list2[1:5])

# last 3 elements 
print(list2[-3:])

# alternative elements 
print(list2[::2]) #step is 2 

# reverse list 
print(list2[::-1]) #step is -1 


# list modify 

my_list = ['apple', 'banana', 'cherry']

print(my_list)

# replace element at index 1
my_list[1] = "blueberry"
print(my_list)

# add element in list 
my_list.append("Mango")
print(my_list)

# remove element from the list 
my_list.remove("cherry")
print(my_list)


# list methods 

# 1 append
fruits = ["apple", "banana", "orange"]
fruits.append("cherry") 
# fruits.append(108) 
print(fruits)  


#2 extend
fruits = ["apple", "orange"]
more_fruits = ["cherry", "mango"] # anaother list
fruits.extend(more_fruits)
print(fruits)  


#3 insert
fruits = ["apple", "orange"]
fruits.insert(1, "blueberry")
print(fruits) 


#4 remove
fruits = ["apple", "banana", "orange", "banana"]
fruits.remove("banana")
print(fruits)  


#5 clear
fruits = ["apple", "orange"]
fruits.clear()  # empty list
print(fruits) 


#6 finding index
fruits = ["apple", "banana", "cherry", "banana"]
index = fruits.index("banana")
print(index)  # Output: 1

# finding index - within a range
index = fruits.index("banana", 2)
print(index)  # Output: 3


#7 count elements
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)  # Output: 2


#8 Reverse list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  


# 9 sorting list
numbers = [40, 10, 30, 20]
numbers.sort() # default sort asc order
print(numbers) 

# sorting list in descending order
numbers.sort(reverse=True)
print(numbers)  

# Sorting strings in a list
fruits = ["cherry", "apple", "banana", 'blueberry']
fruits.sort() # default by chars asc order
print(fruits) 

# Sorting with a key
fruits.sort(key=len, reverse=True) # sort based on len 
print(fruits) 


# 10 pop with index value
numbers = [10, 20, 30, 40]
popped = numbers.pop(2)
print(popped)    # Output: pop 2nd index value 30
print(numbers)   

# pop with defualt
last = numbers.pop()
print(last)      # Output: pop last value by default 40
print(numbers)   


#11 copying list
fruits = ["apple", "banana", "cherry"]
copy_fruits = fruits.copy() # shallow copy
print(copy_fruits)  

# copying list - Modifying the copy does not affect the original list 
copy_fruits.append("mango")
print(copy_fruits) 
print(fruits)        
 

# Join Lists  

list1 = [1,2,3]
list2 = ['a', 'b']

# using + operator 
final_list = list1 + list2 
print(final_list)

# using append method 
for x in list2:
    list1.append(x)
print(list1)

# using extend method 
list1.extend(list2)
print(list1)


# List comprehensions 

# syntax: 
# list_name = [expressions for item in iterable if condition] 

# 3 main components of list comprehension 
# expression, for clasue, if condition 

# Create a list of squares
squares = [x**2 for x in range(1,6)]
print(squares)

# filter even numbers 
even_list = [x for x in range(1,20) if x%2 == 0]
print(even_list)

# apply function to each element of a list  
my_list = ['apple', 'mango', 'cherry'] 

my_name = "madhav"
print(my_name)
print(my_name.upper()) 

print(my_list)
# print(my_list.upper()) # wrong way  

uppercase_list = [lst.upper() for lst in my_list]
print(uppercase_list) 

# flatten a nested list using list comp 
nested_list = [[1,2], [3,4], [5,6]] 

result = [item for sublist in nested_list for item in sublist] 
print(result)

# first, [1,2] -> 1,2
# second, [3,4] -> 3,4
# third, [5,6] -> 5,6

def flatten_list(lst):
    return [item for sublist in lst for item in sublist] 

final_list = flatten_list(nested_list)
print(final_list)


# List iterations 

fruits = ['apple', 'mango', 'cherry'] 

# using for loop
for fruit in fruits:
    print(fruit)  

print("length of list", len(fruits))

# while loop
index = 0
while index < len(fruits):
    print(fruits[index]) 
    index += 1 


# list functions examples: 
list1 = [1, 9, 11]

print(len(list1))   # find length of list - total element count
print(min(list1))   # find min value in list
print(max(list1))   # find max value in list
print(sum(list1))   # sum of all list elements 


# complete the assignment-6 :)

