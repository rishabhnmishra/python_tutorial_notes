# Assignment- 3 

# Q1: Leap Year: Write a simple program to 
# determine if a given year is a leap year 
# using user input.

# leap year condition: 
# 4 divisible & 100 not divisible 
# 400 divisible

# user input 
year = int(input("Enter a Year (e.g. 2024): "))

# checking leap year
if (year % 4 == 0 and year % 100 != 0) or \
    (year % 400 == 0):
    print(f"{year} is leap year") 
else:
    print(f"{year} is not leap year") 

# Q2: Login Authentication using conditional statement. 
# Assume you have a predefined username and password. 
# Write a program that prompts the user to enter a username and password and checks whether they match. 
# Provide appropriate messages for the following cases:
# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

# predefined username and password
predefined_username = 'Madhav'
predefined_password = 'Pass101'

# prompts the user to enter a username and password 
username = input("Enter your username: ")
password = input("Enter your password: ")

# # username and password match 
if username == predefined_username:
    if password == predefined_password:
        print("Welcome! Login was successful.")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Username!")


# Q3: Admission Eligibility: A university has the following 
# eligibility criteria for admission:
# Marks in Mathematics >= 65
# Marks in Physics >= 55
# Marks in Chemistry >= 50
# Total marks in all three subjects >= 180 OR- 
# -Total marks in Mathematics and Physics >= 140
# Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission.

# user input 
print("Enter PCM marks out of 100")
physics_marks = int(input("Enter Physics marks: "))
Chemistry_marks = int(input("Enter Chemistry marks: "))
Maths_marks = int(input("Enter Maths marks: "))

# Eligibility checks
if (Maths_marks >= 65 and 
    physics_marks >= 55 and 
    Chemistry_marks >= 50 and 
    (Maths_marks + physics_marks + Chemistry_marks) >= 180 ) or \
    (Maths_marks + physics_marks) >= 140:
    print("You're eligible!")
else: 
    print("You're not eligible!")