# Arguments in Functions 

# 1. Required Arguments (single/multiple arguments)

def greetings(name):        # name is parameter
    print("Hello ", name, "!") 

greetings("Madhav")     # Madhav is argument 
greetings()       # required an argument to run code

def intro(course_name, instructor_name):
    print("Welcome to ", course_name, "course by", instructor_name)

intro("Python", "Rishabh")


# 2. Default Arguments 

def greetings(name = "World"):        # "World" is a default value
    print("Hello ", name, "!") 

greetings()     # runs without error using default value 
greetings("Rishabh")


# 3. Keyword Arguments (named argument)

def divide(a,b):
    return a/b

result1 = divide(100,20)        # positional argument
print(result1)

result2 = divide(b = 100,a = 20) 
print(result2)


# 4. Arbitrary Argument
# Arbitrary Positional Argument (*args)

# Note: stores arguments as tuple

def add2number(a,b):
    return a+b

result = add2number(10,11)
print(result)

def add3number(a,b,c):
    return a+b+c

result1 = add3number(10,11,1)
print(result1)

def add_numbers(*args):
    print(type(args))
    return sum(args)

op = add_numbers(1,2,3,4)   # variable no. of arguments
print(op)

def greetings2(*names):
    for name in names:
        print(f"Hello, {name}!") 

greetings2("Madhav", 'Rishabh', 'Visakha')


# Arbitrary Keyword Argument (**kwargs)

# Note: stores arguments as dictionary

def print_details(**kwargs):
    # print(type(kwargs))       # dictionary type
    for key, value in kwargs.items():
        print(f"{key}: {value}") 

# print_details(name = "Madhav", age = 26, city = "Delhi")

print_details(name = "Madhav", age = 26)