# Assignment-5 on Loops 

#1: print in the same line

print("Hello", "Madhav1", sep = "*" , end = " * ")
print("Madhav") 

# while loop to print the output in the same line
i = 1
while i < 4:
    print(f"Hello Madhav {i}", end = " ")
    i += 1

i = 1
while i < 4:
    print(f"Hello{i}", "Madhav", sep = "*", end = " ")
    i += 1


#2: star pattern 

#2.a: Triangle Pattern 
# nested loop to print triangle pattern
n = 5 # number of rows

for i in range(1, n+1): # outer loop no. of rows (1 to 5)
    for j in range(1, i+1):  # inner loop for columns (1 to i)
        print("*", end = " ") # print star without new line
    print() # move to the nest line after each row/iteration

# shortcut method
for i in range(1, n+1):
        print("* " * i) 

#2.b: inverted triangle 
n = 5 

# nested loop to print inverted triangle pattern
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()

#shortcut method 
for i in range(n, 0, -1):
        print("* " * i)   

#2.c: pyramid pattern 
n = 5 # no. of rows 

for i in range(1, n+1): # loop for no. of rows 
    print(' ' * (n - i), end = "") # spaces to center the stars
    print("*" * (2 * i - 1)) # print stars

# 2n-1 
# 1 3 5 7   

# shortcut using single print function
for i in range(1, n+1): # loop for no. of rows 
    print(' ' * (n - i) + "*" * (2 * i - 1)) # print stars


#3: Factorial of a number 

def factorial(n):
    result = 1
    while n > 0:
        result *= n 
        # result = result * n  # 5*1, 5*4, 20*3, 60*2 
        n -= 1 
    return result 

print(factorial(5))
# 5! = 5 * 4 * 3 * 2 * 1  


#4: Count vowels in a string 
my_string = "Python by Rishabh Mishra" 
vowels = "aeiou"
count = 0 

for char in my_string:
    if char.lower() in vowels:
        count += 1 
print("Number of vowels are", count)    


#5: Longest word in a string 
sentence = "Python by Rishabh Mishra" 
words = sentence.split() 
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word 
print("The longest word is:", longest_word)


#6: do-while loop in python 

while True:
    num = int(input("Enter a number greater than 10: "))

    if num > 10:
        print(f"Valid number entered: {num}") 
        break # exit the loop when condition is satisfied
    else:
        print("Number is not greater than 10, try again!") 


#7: Fibonacci Sequence 

def fibonacci(n):
    a,b = 0,1 
    count = 0
    while count < n:
        print(a)    # 0 1 1 2 3
        a,b = b, a+b 
        count += 1 # 0 1 2 3 4 

fibonacci(10)
