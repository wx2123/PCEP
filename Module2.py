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
