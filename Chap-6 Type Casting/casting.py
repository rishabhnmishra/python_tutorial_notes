# casting in python

a = 1               # int type
print(type(a))

b = "1"             # str type
print(type(b))

c = int(b)          # convert str to int type
print(type(c))

print(a+int(b)) 

# all str type can't be casted into numerical type
# name = "Madhav"
# newname = int(name) 

# all numerical type can be cast into str 
mynum = 26              # int type
mynum2 = str(mynum)     # convert int to str type
print(type(mynum2))

f1 = 22.56          # float type
f2 = int(f1)        # convert float to int type
print(f2)
print(type(f2)) 

in1 = 26 
print(type(float(in1))) 

# type casting types:

# 1. implicit type casting - python automatically convert data type
var1 = 10   #int type
var2 = 15.5 #float type
var3 = var1+var2
print(var3)
print(type(var3)) 

# 2. explicit type casting - programmer need to manually convert data type
int_num = 101           # int type
str_num = str(int_num)  # convert to str type
print(type(str_num)) 

a0 = bool(0)  # boolean type - False
print(a0)
print(type(a0))

a1 = bool(1)  # boolean type - True
print(a1)
print(type(a1))