# Strings in Python - PART 2 -- Scroll down to String Indexing

# strings- chars in single, double and triple quotes

name = "Madhav"     # creating a string
print(name)

print(type(name))   # checking data type

print("It's easy")
print("Hello World")

print(''' "kw-double Quotes" ''') 

print(" \"kw-double Quotes\" ") 


# Formatted Strings - insert variables or experssions
# 1. Old style formatting - % operator 

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


# String Indexing

my_name = "MADHAV"
# index:   012345

print(my_name[0])       # first character of str 
print(my_name[1])       # second character of str 
print(my_name[2])       # third character of str 
print(my_name[3])       # fourth character of str 
print(my_name[4])       # fifth character of str 
print(my_name[5])       # sixth character of str 
print(my_name[-1]) 

name2   =  "Hello World"
# index:    012345678910
# -ve index:1110987654321 -
print(name2[5])     # blank space is also a char
print(name2[-1])    # last char from str
print(name2[-3])    # 3rd last char from str 



# String Slicing  

# syntax: string[start : end : step]

my_name = "MADHAV"
# index:   012345 

print(my_name[0:3])     # default step = 1
print(my_name[0:3:1]) 

print(my_name[0:5:1]) 

print(my_name[3:5:1]) 

print(my_name[0:5:2])   # step = 2

print(my_name[0:5:3])   # step = 3

print(my_name[0:5:4])   # step = 4 

print(my_name[0:2])        # first 2 chars
print(my_name[0:3])        # first 3 chars
print(my_name[2:5])        # third to fifth chars
print(my_name[1:4])        # second to fourth chars
print(my_name[-1:])        # last char of str
print(my_name[5:])         # last char of str
print(my_name[-2:])        # last 2 char of str
print(my_name[-3:])        # last 3 char of str
print(my_name[0::2])       # every second char
print(my_name[:])          # all char
print(my_name[::])         # all char 
print(my_name[::-1])       # reverse the string 


# String Methods

word = "Hello, Madhav" 

#1. len()
print(len(word)) 

#2. upper()
print(word.upper())

#3. lower()
print(word.lower())

#4. count()
print(word.count('M')) 

#5. find()
print(word.find('e'))

#6. Split()
print(word.split(','))
print(word.split()) 

#7. Replace()
print(word.replace("Madhav", "Keshav")) 

#8. title()
print(word.title()) 

#9. strip()
word2 = "  Hello World   "
print(len(word2))
print(word2.strip()) 

#10. join()
zwords = ("Madhav", "is", "Great")
print(" ".join(zwords))
print("-".join(zwords))