# Assignment-4 on Strings

#1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359 

pi = 3.14159265359 

print(round(pi,2))

print("Value of pi is {}".format(pi))

# using f-function formating float numbers 
print("Value of pi is {:.1f}".format(pi))

print("{:.1f}".format(pi)) 

# f-strings
print(f"{pi:.2f} using f-string")




#2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.
my_string = "Python Course"

# string[start:stop:step]
print(my_string[2:8:2])




#3.  Slice to get only the middle character(s): For my_string = "Madhav", use slicing to extract the middle character(s).
my_string = "Madhav"    # 6 chars - even
# index:     012345
my_string2 = "Madhava"  # 7 chars - odd 
# index:      0123456

def mid_str(word):
    middle = int(len(word)/2)               #3
    if len(word) % 2 == 0:                  # even char len - 2 middle char
        return word[middle-1 : middle+1]    #2:4
    else:                                   # odd char len - 1 middle char
        return word[middle]

print(mid_str(my_string2))




#4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.

my_string = "Regression Analysis"

print(my_string[3:-3])




#5. Get the substring that starts 4 characters from the end to the last character: For my_string = "Classification", slice the string starting from the 4th character from the end to the last character.

my_string = "Classification"
print(my_string[-4:])




#6. How to Reverse a String Using Python String Methods? 
word = "Python"
print(word[::-1])       # step value = -1




#7. Write a Python function to check if a string is a palindrome using string methods.

word = "madam"
word2 = "madan"

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:   
        print(f"{s} is not a palindrome")

is_palindrome(word2)


#8 and 9 are homework :)

#8. Difference Between find() and index() in Python? 

#9. Efficient String Concatenation method: Why is using join() often more efficient than using + for string concatenation in a loop? 
