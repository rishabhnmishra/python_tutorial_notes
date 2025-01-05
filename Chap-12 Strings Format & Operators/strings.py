# Strings in Python - PART 1

# strings- chars in single, double and triple quotes

name = "Madhav"     # creating a string
print(name)

print(type(name))   # checking data type

print("It's easy")
print("Hello World")

print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ") 


# Formatted Strings - insert variables or experssions
#1. Old style formatting - % operator 

name = "Madhav"
age = 16 
print("My name is %s and I'm %d" % (name, age)) 
# %s, %d are placeholders for the string and int 


#2. str.format() method 

name = "Madhav"
age = 16 
print("My name is {} and I'm {}".format(name, age)) 


# you can reference variables by index or keyword
print("My name is {0} and I'm {1}".format(name, age))
print("My name is {1} and I'm {0}".format(name, age))

print("My name is {name} and I'm {age}".format(name="Keshav", age="21"))


#3. f-strings - my fav

name = "Rishabh"
age = 24
print(f"My name is {name} and I'm {age}")

print(f"My age after 5 years will be {age + 5}") 


# Escape Characters - backslash with chars 
print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ")  # double quotes using \

print(" \'kw-single Quotes\' ") # single quote using \

print("Hello\nWorld")       # new line
print("Hello\tWorld")       # tab - space 


# String Operators in Python 
a = "Hello"
b = "Python"

print(a+b)      # concatenate 
print(a*2)      # multiple copies 
# [] - slice, [:] - range  -- scroll below

if "h" in a:
    print("Yess")
else:
    print("noo")

    
if "h" not in a:
    print("Yess")
else:
    print("noo") 

print(r"Hello\nWorld")  # Raw string: suppress the escape chars 


# String Indexing, Slicing and methods in PART 2 