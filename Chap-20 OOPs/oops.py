# OOPs in Python 
# OOP- Object Oriented Programming

# using list - creating student records
# student details
student_1 = ['Madhav', 10] # Name, Grade
student_2 = ['Vishakha', 12] 
student_3 = 'Keshav'

student_1.append('A')
print(student_1)
print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')


# using OOPs- creating student records

# class - blueprint or template
# __init__ method - constructor, value initialize - fix
# self parameter - reference or connection build btw class and object - fix
class Student: # student class
    def __init__(self, name, grade, percentage):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class 
student1 = Student('Madhav', 11, 96)
print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99)
print(student2.name, student2.grade)

print(student1.percentage)
student1.student_details()
student2.student_details()

print(student1.__dict__) 

# modify object property
print(student1.percentage) 
student1.percentage = 100 # modify
print(student1.percentage)

# delete object property 
print(student1.__dict__) 
del student1.percentage
print(student1.__dict__) 

# delete object 
del student1
print(student1)



# class - blueprint or template
class Student: # student class
    def __init__(self, name, grade, percentage, team):  # method
        self.name = name  # attribute 
        self.grade = grade # attribute 
        self.percentage = percentage # attribute
        self.team = team

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}% and is in team {self.team}")

team1 = 'A'
team2 = 'B'

# object - instance of class 
student1 = Student('Madhav', 11, 96, team1)
# print(student1.name, student1.grade)

student2 = Student('Vishakha', 12, 99, team2)
# print(student2.name, student2.grade)

# print(student2.team)
student1.student_details()
student2.student_details()



# 4 features in OOPs 
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Abstraction 
# hiding unnecesary deatils from users through class, methods 

class Student: # student class
    def __init__(self, name, grade, percentage): 
        self.name = name  # attribute 
        self.grade = grade  
        self.percentage = percentage 

    def student_details(self): # method - abstraction
        print(f"{self.name} is in class {self.grade}, with {self.percentage+2}%") # hidden from users

# object - instance of class 
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

student2.student_details()


# Encapsulation 
# Restrict access to certain attributes or methods to protect data and enforce controlled access

class Student: # student class
    def __init__(self, name, grade, percentage): 
        self.name = name  # attribute 
        self.grade = grade  
        self.__percentage = percentage # double underscore limits access

    def get_percentage(self):
        return self.__percentage 

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%") 

# object - instance of class 
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 97)

print(student1.__percentage) # error
print(student1.percentage) # error
print(student2.get_percentage())


# Inheritance 
# allows one class (child) to reuse the prop and methods of another class (parent). 

# parent class - baap
class Student: # student class
    def __init__(self, name, grade, percentage): 
        self.name = name  # attribute 
        self.grade = grade  
        self.percentage = percentage 

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class 
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 99)

# child class - beta 
class GraduateStudent(Student): # Graduatestudent child class inherit prop and methods from Student Parent class
    def __init__(self, name, grade, percentage, stream): # old parameters from parent class and new parameters in child class
        super().__init__(name, grade, percentage) # call parent class init
        self.stream = stream # new attribute in child class 

    def student_details(self):
        super().student_details() # method inherit from parent class
        print(f'Stream is {self.stream}')

# object
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')
print(Grad_Student1.stream) 

Grad_Student1.student_details()


# Polymorphism
# allows methods in difft classes to have same name but difft behaviour depending on objects 

class Student: # student class
    def __init__(self, name, grade, percentage): 
        self.name = name  # attribute 
        self.grade = grade  
        self.percentage = percentage 

    def student_details(self): # method 
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")

# object - instance of class 
student1 = Student('Madhav', 11, 96)
student2 = Student('Vishakha', 12, 99)

# child class  
class GraduateStudent(Student): 
    def __init__(self, name, grade, percentage, stream): 
        super().__init__(name, grade, percentage) 
        self.stream = stream 

    def student_details(self): # method
        # print(f'{self.name} is in class {self.grade}, with {self.percentage}% and from stream {self.stream}')
        print('same method with difft o/p')

# object - Student class
student1 = Student('Madhav', 11, 96)

# object - GraduateStudent class
Grad_Student1 = GraduateStudent('Keshav', 12, 96, 'PCM')

student1.student_details()
Grad_Student1.student_details()

# download notes for defintions and more examples 