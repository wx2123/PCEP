# -*- coding: utf-8 -*-
"""

PCEP Module 2

Created on Fri Oct 29 19:28:50 2021

@author: Wujian

"""

# 2.1.1.1 Your very first program
print("Hello, World!")

# 2.1.1.6 LAB: The print() function
print("Hello, Python!")
print("David")
#print(david)

# 2.1.1.8 Your very first program
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

# 2.1.1.9 Your very first program
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

# 2.1.1.10 Your very first program
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

# 2.1.1.11 Your very first program
# print("\")
print("\\")

# 2.1.1.12 Your very first program: The print() function - using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")


# 2.1.1.13 Your very first program: The print() function - the positional way of passing the arguments
print("My name is", "Python.")
print("Monty Python.")

# 2.1.1.14 Your very first program: The print() function - the keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is", "Python.", end="\n")
print("Monty Python.")

# 2.1.1.15 Your very first program: The print() function - the keyword arguments
print("My name is ", end="")
print("Monty Python.")

print("My name is ", end="tttttttttttt")
print("Monty Python.")

# 2.1.1.16 Your very first program: The print() function – the keyword arguments
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", "Monty", "Python.", sep="**")


# 2.1.1.17 Your very first program: The print() function - the keyword arguments
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# 2.1.1.18 LAB: The print() function
print("Programming","Essentials","in")
print("Python")

print("Programming","Essentials","in",sep="***",end="...")
print("Python")

# 2.1.1.19 LAB: Formatting the output: LAB
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *")
print("   * ",end='*\n')
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# make the arrow twice as large (but keep the proportions)



# 2.2.1.2 Python literals: Literals - the data in itself
print("2")
print(2)

# 2.2.1.3 Python literals: Integers
print(1_111 + 2_222)

#2.2.1.4 Python literals: Integers: oct and hexadecimal numbers
print(0o123) # 八进制83
print(0x123) # 十六进制291

# 2.2.1.7 Python literals: Coding floats
print(0.0000000000000000000001)
6.62607E-34

# 2.2.1.8 Python literals: Strings
print("I like \"Monty Python\"")
print('I like "Monty Python"')

# 2.2.1.9 Python literals: Coding strings
print('I\'m Monty Python')
print("I'm Monty Python")

# 2.2.1.10 Python literals: Boolean values
print(True > False) 
print(True < False)

# 2.2.1.11 LAB: Python literals - strings
print('"I\'m"')
print('""learning""')
print('"""Python"""')

# 2.3.1.1 Operators - data manipulation tools: Python as a calculator
print(2+2)

# Arithmetic operators: exponentiation
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# 2.3.1.3 Arithmetic operators: multiplication
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# 2.3.1.4 Arithmetic operators: integer division
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

# 2.3.1.5 Operators: remainder (modulo)
print(14 % 4)

print(12 % 4.5)

# 2.3.1.6 Operators: The subtraction operator, unary and binary operators
print(-4. + 8)

print(-4 - 4)
print(4. - 8)
print(-1.1)

print(+2)

# 2.3.1.7 Operators and their priorities
print(9 % 6 % 2)

# 2.3.1.8 Operators and their bindings: exponentiation
print(2 ** 2 ** 3)

# 2.3.1.9 List of priorities
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

((25%13) + 100)/(2*13)


print(17%3)
print(14%3.5)

print(10%7%2)

# 2.4.1.2 Variables - data-shaped boxes: Correct and incorrect variable names
变量=1
变量/2

# 2.4.1.2 Variables - data-shaped boxes: Creating variables
var = 1
print(var)

# 2.4.1.4 Variables - data-shaped boxes: Assigning a new value to an already existing variable
var = 100
var = 200 + 300
print(var)

# 2.4.1.5 Variables - data-shaped boxes: Solving simple mathematical problems
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# 2.4.1.6 Variables - data-shaped boxes: LAB
john = 3
mary = 4
adam = 5
print("John:", john, "Mary: ", mary, "Adam: ", adam)

total_apple =  john + mary + adam
print("total_apple: ", total_apple )


# 2.4.1.9 Variables - data-shaped boxes: LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles *1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 2.4.1.10 Variables - data-shaped boxes: LAB
x =  -1 # hardcode your test data here
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x -1
# write your code here
print("y =", y)

# 2.4.1.11 SECTION SUMMARY


a = 6
b = 3
a /= 2 * b
print(a)


# 2.5.1.2 LAB: Comments
# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")
#here we should also print "Goodbye", but a programmer didn't have time to write any code
#this is the end of the program that computes the number of seconds in 3 hour

# 2.6.1.1 How to talk to a computer: The input() function
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# 2.6.1.1 How to talk to a computer: The input() function with an argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")


# 2.6.1.4 How to talk to a computer: Type casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# 2.6.1.5 How to talk to a computer: More about input() and type casting
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)


# 2.6.1.6 How to talk to a computer: string operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# 2.6.1.7 How to talk to a computer: Replication
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# 2.6.1.8 How to talk to a computer: string operators
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))


# 2.6.1.9 LAB: Simple input and output
# input a float value for variable a here
a = float(input("input a float value for variable a here: "))

# input a float value for variable b here
b = float(input("input b float value for variable a here: "))


# output the result of addition here
print("the addition is:", a + b)

# output the result of subtraction here
print("the subtraction is:", a - b)

# output the result of multiplication here
print("the multiplication is:", a * b)

# output the result of division here
print("the division is:", a / b)

print("\nThat's all, folks!")

# 2.6.1.10 LAB: Operators and expressions
x = float(input("Enter value for x: "))

# Write your code here.
x1 = x + 1 / x
x2 = x + 1 / x1
x3 = x + 1 / x2
y  = 1 / x3 

print("y =", y)





