# File Handling - place the example txt files out of this 'file-handling' folder
# mode: r - read, w - write, a - append 

# open file 
file = open('example.txt', 'r') # read mode

# # read file 
file = open('example.txt', 'r')
content = file.read() # read entire data
print(content)
file.close() # best practice

file = open('example.txt', 'r')
content = file.readline() # read first line
print(content)
file.close() 

file = open('example2.txt', 'r')
content = file.readlines() # list entire data
print(content)
file.close() 


# write to a file 
file = open('example2.txt', 'w') # write mode - overwrite
file.write("Namaste, kasie ho?")
file.close()

file = open('example2.txt', 'a') # append mode - incremental write
file.write("\nAgain Acha hu.")
file.close()


# close a file 
# using with statement 
with open('example2.txt', 'r') as file:
    content = file.readline()
    print(content) 

# exceptional handling when closing a file 
try:
    file = open('example2.txt', 'r')
    content = file.read()
    print(content)
finally:
    file.close() 

# HW: How can you handle multiple exceptions while performing operations on a file?
# error example: FileNotFound, ValueError, etc 