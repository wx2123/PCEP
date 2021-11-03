# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:12:16 2021

@author: Wujian
"""
# 3.1.1.2 Making decisions in Python: Equality: the equal to operator (==)
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)


# 
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# 3.1.1.9 Making decisions in Python

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


# 3.1.1.10 LAB: Comparison operators and conditional execution
x = input()
if (x == 'Spathiphyllum'): print("Yes - Spathiphyllum is the best plant ever")
elif (x == 'spathiphyllum'): print("No, I want a big Spathiphyllum!")
else : print("Spathiphyllum! Not", x)

# 3.1.1.11 LAB: Essentials of the if-else statement

income = float(input("Enter the annual income: "))

#
# Write your code here.
#

if income <= 85528 : tax = (income) * .18 - 556.02
else : tax = 14839 + (income - 85528) * .32

tax = round(tax, 0)
if (tax < 0) : tax = 0.0

print("The tax is:", tax, "thalers")

# 3.1.1.12 LAB: Essentials of the if-elif-else statement

year = int(input("Enter a year: "))

#
# Write your code here.
#	
if year <= 1582 : print("Not within the Gregorian calendar period")
elif year %   4 != 0: print("common year")
elif year % 100 != 0: print('leap year')
elif year % 400 != 0: print('common year')
else : print ("leap year")


# 3.1.1.14 SECTION SUMMARY (2/2)
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")



# 3.2.1.1 Loops in Python | while
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

# 3.2.1.2 Loops in Python | while
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


