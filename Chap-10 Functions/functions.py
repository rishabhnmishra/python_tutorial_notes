# functions in python

#create function without parameter 
def greetings():
    print("Welcome to the python course by Rishabh!") 

#call function (use function)
greetings() 

# create a function to add 2 numbers using parameter
def add2numbers(a,b):   #parameter (a,b)
    result = a + b 
    print("The sum is: ", result) 

#call above sum function
add2numbers(5,3)    #arguments (5,3) 

add2numbers(a=10, b=100) 

add2numbers(b=50, a=10) 

# create a function to add 3 numbers 
def add3numbers(a,b,c):   #parameter (a,b,c)
    result = a + b + c
    print("The sum is: ", result) 

#call above sum function
add3numbers(5,3, 100)    #arguments (5,3,100) 


function with return statement 
def add2num(a,b):
    return a+b 
    # return a-b    after return statement function ends 

sum2num = add2num(10,1)
print(sum2num)  

# function to convert celsius to Fahrenheit- return statement 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 

#call function 
temp_f = celsius_to_fahrenheit(25) 
print(temp_f)
print("with return: ", type(temp_f))

# function to convert celsius to Fahrenheit- without return
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    print(fahrenheit)  

#call function 
temp_f2 = celsius_to_fahrenheit(50) 
print("without return: ", type(temp_f2)) 

# pass statement 
def kuchbhi(): 
    pass 

def top_right_CTA_button_type():    # code to be updated later
    pass 

print("Hello!")