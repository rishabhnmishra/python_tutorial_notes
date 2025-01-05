# Loops in Python - Nested Loop

# loop inside another loop is Nested Loop
# syntax

# outer_loop:
#     inner_loop:
#         #block of code for inner loop 
# block of code for outer loop

# print numbers from 1 to 3 for 3 times 

for i in range(3):
    # print("Outer loop iteration no, ", i)
    for num in range(1,4):
        print(num) 
    print("- - -")

# print numbers from 1 to 3 for 3 times using while-for loop : nested loop 
i = 1

while i < 4:
    print("while loop iteration no.", i)
    for j in range(1,4):
        print(j)
    # print("- - -")
    i += 1 


# print prime numbers between range of 2 to 10 using nested loop:

for num in range(2,10):
    for i in range(2,num):
        if num % i == 0: 
            break 
    else:
        print(num) 