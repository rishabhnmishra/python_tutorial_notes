# Simple calculator using Python

# Function to Add two numbers
def add(num1, num2):
	return num1 + num2

# Function to Subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to Multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to Divide two numbers
def divide(num1, num2):
	if num2 == 0:
		return "Cannot divide by zero"
	return num1 / num2 

# Function to find Average of two numbers
def avg(num1, num2):
	return (num1 + num2)/2 

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n"  \
		"5. Average\n" )


# Take input from the user
select = int(input("Select operation from 1, 2, 3, 4, 5: "))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=", divide(number_1, number_2))
	
elif select == 5:
	print(number_1, "+", number_2, "/2", "=", avg(number_1, number_2))
else:
	print("Invalid Operation") 