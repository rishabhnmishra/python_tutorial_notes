# python program to create a simple calculator

# 3 steps to build calculator program
#   1. functions for operations 
#   2. user input 
#   3. print result 

# step-1: create functions:
# Function to add two numbers 
def add(num1,num2):
     return num1 + num2 

# Function to substract two numbers 
def sub(num1,num2):
     return num1 - num2 

# Function to multiply two numbers 
def multiply(num1,num2):
     return num1 * num2  

# Function to divide two numbers 
def divide(num1,num2):
     return num1 / num2 

# Function to average two numbers 
def avg(num1,num2):
     return (num1 + num2)/2  

#Step-2: user input 
print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n") 

select = int(input("Select a operation from 1,2,3,4,5: ")) 

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

#Step-3: Print the result 

if select == 1:
     print(number1, "+", number2, "= ", \
           add(number1, number2))
     
elif select == 2:
     print(number1, "-", number2, "= ", \
           sub(number1, number2)) 
     
elif select == 3:
     print(number1, "*", number2, "= ", \
           multiply(number1, number2))
     
elif select == 4:
     print(number1, "/", number2, "= ", \
           divide(number1, number2))

elif select == 5:
     print("(",number1, "+", number2, ")", "/", "2", "= ", \
           avg(number1, number2)) 
    
else:
     print("Invalid operation! Pls select again!")
     