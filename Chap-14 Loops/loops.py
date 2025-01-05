# Loops in Python - while & for loop 

# while loop 

count = 0 

while count < 5: #condition 
    print(count)
    count = count + 1


# print numbers from 1 to 5 using while loop
count = 1 
while count < 6: #condition 
    print(count)
    # count = count + 1
    count += 1 


count = 5 
while count > 0: #condition 
    print(count)
    # count = count + 1
    count -= 1 
else:
    print("while loop ended")


# while True:
#     print("again and again!!") 
# check conditions to avoid infinite loop


#for loop 

language = 'Python' # sequence 

for x in language:
    print(x) 

# range function
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(5):  # stop argument
    print(i)

for i in range(5,10):     # start, stop argument
    print(i)

for i in range(1,10,3):  # start, stop, step argument
    print(i)

for i in range(5):
    print(i)
else:
    print("for loop ended")


# loop control statements 
# 1. pass statement 

for i in range(5):
    # mann nahi hai 
    pass 

count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 


#2. break statement 

for i in range(5):
    if i == 3:
        break 
    print(i) 

print("---------")


#3. continue statement 

for i in range(5):
    if i == 3:
        continue 
    print(i) 


# pass statment vs continue statement
count = 5 
while count > 0:
    if count == 3:
        pass 
    else:
        print(count)
    count -= 1 

# continue statement: don't try - infinite loop
count = 5 
while count > 0:
    if count == 3:
        # continue 
    else:
        print(count)
    count -= 1 


# validate user input: controlled infinite while loop using break statement
while True:
    user_input = input("Enter 'exit' to STOP: ")
    if user_input == 'exit':
        print("congarts! You guessed it right!")
        break 
    print("sorry, you entered: ", user_input)  