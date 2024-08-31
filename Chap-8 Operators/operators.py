# operators 

# 1. Arithmetic Operators 
a = 5 
b = 3 
print(a+b)   # addition operator 
print(a-b)   # substraction operator 
print(a*b)   # multiplication operator  
print(a%b)   # modulus operator

# 2. Comparison operators - output is a boolean value (T/F)
a = 5 
b = 3
print(a > b)   #greater than operator 
print(a < b)   #less than operator 
print(a == b)   # equal operator 
print(a != b)   # not equal operator 

# 3. Assignment Operators 
a = 5 # assignment Operator

# 4. Logical Operators - and, or, not
# Rule for 'and' operator
# 1. True + True = True 
# 2. True + False = False
# 3. False + False = False

a = 10 
b = 20
print(a>10 and b<10) # and operator
print(a==10 and b==20)
print(a==10 or b<10) # or operator 

# Rule for 'or' operator
True + False = True 

# 'not' operator
print(not(a==10 and b==20))

# 5. Identity operators - is, is not 
x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)   # is operator 
print(x is z)

print(x is not z) # is not operator

# 6. Membership operators - in, not in 
my_list = ['apple', 'orange', 'watermelon']
print('apple' in my_list) # in operator
print('apple2' in my_list)
print('apple2' not in my_list) # not in operator 

# # 7. Bitwise operators - AND &, OR |, XOR ^, NOT ~, etc 
a = 5           # 5 in binary- 0101 
b = 3           # 3 in binary- 0011 
print(a & b)    # 1 in binary- 0001 

# Rule for AND '&' operator
# 1. True + True = True 
# 2. True + False = False
# 3. False + False = False 

# Rule for OR '|' operator
# True + False = True 