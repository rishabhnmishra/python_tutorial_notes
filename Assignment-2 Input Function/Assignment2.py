# Assignment - 2
# Write a program to input student name & marks of 3 subjects. 
# Print name & percentage in output. 

student_name = input("Enter your name: ")
hindi_marks = input("Enter Hindi Marks: ")
maths_marks = input("Enter Maths Marks: ")
science_marks = input("Enter Science Marks: ") 

# calcualating percentage 
percentage = ((int(hindi_marks) + int(maths_marks) + int(science_marks))/300)*100

# # print result 
print(f"The result of {student_name} is {int(percentage)}%. Well done!!")

# optimized solution
print("Percentage Calculator")
student_name = input("Enter your name: ")
hindi_marks = int(input("Enter Hindi Marks: "))
maths_marks = int(input("Enter Maths Marks: "))
science_marks = int(input("Enter Science Marks: "))

# # calcualating percentage 
percentage = ((hindi_marks + maths_marks + science_marks)/300)*100

# # print result 
print(f"The result of {student_name} is {int(percentage)}%. Well done!!")


# Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.

#  initializing a dictionary
user_data = {} 

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)