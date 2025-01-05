# Dictionary in Python

#syntax: 
# my_dict = {'key1':'value1', 'key2':'value2', ...}

#Methods to create dictionary 
# method-1 create dictionary using curly braces 
cohort = {'course':'Python', 
          'Instructor':'Rishabh Mishra', 
          'Level': 'Benginner'} 

print(cohort)
print(type(cohort)) 

# Method-2 using dict() constructor 
person = dict(name= 'Madhav', age=20, grade = 'A')
print(person)
print(type(person)) 

# Method-3 using list of tuples 
person2 = dict([('name', 'Madhav'), ('age', 20), ('city', 'Mathura')])
print(person2)
print(type(person2)) 

# Access dictionary values 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

print(student)
print(type(student)) 

print(student['name'])
print(student['grade'])


# Dictionary Methods 
student = {
    1: 'Class-X',
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# keys
print(student.keys())

# values
print(student.values())

# items
print(student.items())

# get
print(student['name'])
print(student.get('email', 'Nahi hai')) 


# Add/modify items in dictionary 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# add item - assign operator
student['email'] = 'madhav@example.com'
print(student)

# modify/replace item - assign operator
student['grade'] = 'A+'
print(student) 

# remove items
# del to remove item 
del student['grade']
print(student)

# pop method
var1 = student.pop('email')
print(var1)
print(student)


# dictionary iteration 
student = {
    'name': 'Madhav',
    'grade': 'A',
    'city': 'Mathura'
}

# loop through keys 
for keys in student:
    print(keys)

# loop through values
for value in student:
    print(student[value]) 

# using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair  
for keys,value in student.items():
    print(keys, value) 


# Nested dictionary 

main_student = {

    'student1' : {'name': 'Madhav', 'age': 20},
    'student2' : {'name': 'Keshav', 'age': 25, 'grade': 'A'}
} 

print(main_student)

# access value 
print(main_student['student1'])

print(main_student['student1']['name'])
print(main_student['student2']['grade'])


# Dictionary comprehension 

# syntax 
# new_dict = 
# {key_exp : value_exp for item in iterable if condition}

my_dict = {x:x+x for x in range(1,6)}

print(my_dict) 


# Note: Solve Assignment-6 to practice dictionary questions :)