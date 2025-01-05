# Modules in Python 
# single py file 

# create a module mymodule.py file 
# use mymodule file 

import mymodule 
mymodule.say_hello('Madhav')
mymodule.say_bye('Rishabh') 

# import/use specific part of code
from mymodule import person1 
print(person1['age'])

# package: collection modules/py files + __init__.py

# library: collection of modules and packages 
# in-built lib
import math 

A = 36 
print(math.sqrt(A))

# import specific function from lib 
from math import factorial 
B = 4 
print(factorial(B)) 

# installed new/external modules/lib 
# pip install <library_name>
import pandas as pd 
import seaborn as sb
