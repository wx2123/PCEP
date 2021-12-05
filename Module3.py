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

# 3.1.1.3 Making decisions in Python
n = int(input("please enter a number: "))
print(n >= 100)


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


n = input("enter a plant name: ")
if n == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif n == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else :
    print("Spathiphyllum! Not", n)

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


# 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Input a number
number = int(input("Enter a number: "))

# If the number is not equal to -1, continue.
while number != secret_number:
    # If the number chosen by the user is different than the magician's secret number
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Enter a number again: "))

# Print the largest number.
print("Well done, muggle! You are free now.")


power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# 3.2.1.4 Loops in Python | for
for i in range(10):
    print("The value of i is currently", i)


# 3.2.1.5 Loops in Python | for

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2




# 3.2.1.6 LAB: Essentials of the for loop - counting mississippily
import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.

for i in range(1,6):
    print(i,"Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

# 3.2.1.7 Loop control in Python | break and continue
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")    
    
# 3.2.1.8 Loop control in Python | break and continue

# break
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# continue    
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

# 3.2.1.9 LAB: The break statement - Stuck in a loop
secret_word = "chupacabra"

# Input a word
number = input("Enter a word: ")

# If the number is not equal to -1, continue.
while number != secret_word:
    # If the number chosen by the user is different than the magician's secret number
    print("Ha ha! You're stuck in my loop!")
    number = input("Enter a word again: ")

# Print the largest number.
print("You've successfully left the loop.")    

# 3.2.1.10 LAB: The continue statement - the Ugly Vowel Eater
# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A" : continue
    elif  letter == "E": continue
    elif  letter == "I": continue
    elif  letter == "O": continue
    elif  letter == "U": continue
    print(letter)




# 3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater
user_word = input("Enter a word: ")
word_without_vowels = ""
user_word = user_word.upper()
# Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the loop.
    if letter == "A" : continue
    elif  letter == "E": continue
    elif  letter == "I": continue
    elif  letter == "O": continue
    elif  letter == "U": continue
    else : word_without_vowels += letter


# Print the word assigned to word_without_vowels.
print(word_without_vowels)


# 3.2.1.12 Python loops | else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    

# 3.2.1.13 Python loops | else
    
for i in range(5):
    print(i)
else:
    print("else:", i)
    
    
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
    
    
# 3.2.1.14 LAB: Essentials of the while loop
  
blocks = int(input("Enter the blocks : "))

i=1
layer=1
height=0

while i < blocks + 1:
    height += layer
    if height > blocks:
        print("he height of the pyramid:", layer-1)
        break
    i += 1
    layer += 1
    

# 3.2.1.15 LAB: Collatz's hypothesis

c0 = int(input("Enter the c0 : "))

i = 0
while c0 != 1.0:
    if c0 % 2 == 0 : c0 = c0/2
    else: c0 = 3 * c0 + 1
    print(c0)
    i += 1
print('steps=',i)


# 3.2.1.16 SECTION SUMMARY (1/2)

# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# 3
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

# 4
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

# 3.2.1.17 SECTION SUMMARY (2/2)
"""
Exercise 1
Create a for loop that counts from 0 to 10, 
and prints odd numbers to the screen. Use the skeleton below:
"""
for i in range(1, 11):
    if i % 2 != 0:   print(i)
    
"""
Exercise 2
Create a while loop that counts from 0 to 10,
 and prints odd numbers to the screen. Use the skeleton below:
"""

x = 1
while x < 11:
    if x % 2 != 0:   
        print(x)
    x += 1
    
"""
Exercise 3
Create a program with a for loop and a break statement. 
The program should iterate over characters in an email address, 
exit the loop when it reaches the @ symbol, 
and print the part before @ on one line. Use the skeleton below:
"""    
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
    
"""
Exercise 4
Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, 
replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:
"""
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

    
"""
Exercise 5
Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, 
replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:
"""

# 3.3.1.2 Logic and bit operations in Python | and, or, not

# Example 1:
var = 1
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

i = 1
j = not not i
print(j) # True


i = 0
j = not not i
print(j) # False



#3.3.1.3 Logic and bit operations in Python
i = 15
j = 22
log = i and j  # 22
bit = i &   j  # 6
logneg = not i # False
bitneg = ~i    #-16


print(log)

x = 3
y = 7

if (y > 1 and y > x) : print("y is greater than 1 AND x")

z = x & y
print(z)

# 3.3.1.5 Logic and bit operations in Python | Bit shifting
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)


# 3.3.1.6 SECTION SUMMARY

#Exercise 1
#What is the output of the following snippet?

x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

#Exercise 2
#What is the output of the following snippet?

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)


x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)


# 3.4.1.2 Lists - collections of data | Indexing
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.

# 3.4.1.3 Lists - collections of data | Indexing
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.


# 3.4.1.4 Lists - collections of data | Operations on lists

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###


# 3.4.1.5 Lists - collections of data | Operations on lists
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
print(numbers[-4])

# 3.4.1.6 LAB: The basics of lists
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
number = int(input("Enter a number : "))

hat_list[2] = number

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)

# 3.4.1.8 Lists - collections of data | list methods
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

# 3.4.1.9 Lists - collections of data | list methods
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list2 = []  # Creating an empty list.

for j in range(5):
    my_list2.insert(0, j + 1)

print(my_list2)


# 3.4.1.10 Lists - collections of data | lists and loops
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# 3.4.1.11 Lists - collections of data | lists and loops
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
print(variable_1,variable_2)

# 3.4.1.12 Lists - collections of data | lists and loops
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


# 3.4.1.13 LAB: The basics of lists - the Beatles
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in ['Stu Sutcliffe', 'Pete Best']:
    beatles.append(i)
print("Step 3:", beatles)

# step 4
del beatles[3]
del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))


# 3.5.1.2 Sorting simple lists - the bubble sort algorithm
my_list = [8, 10, 6, 2, 4]  # list to sort
for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.


my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)


# 3.5.1.3 Sorting simple lists - the bubble sort algorithm

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("\nSorted:")
print(my_list)

# 3.6.1.1 Operations on lists

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2) # need to remember!!!!


# 3.6.1.2 Operations on lists | slices
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# 3.6.1.5 Operations on lists | slices, del
my_list = [10, 8, 6, 4, 2]
del my_list
#print(my_list)

# 3.6.1.6 Operations on lists | in, not in
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# 3.6.1.8 Lists - more details

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


# 3.6.1.9 LAB: Operating with lists - basics

# https://www.youtube.com/watch?v=pKccpZujYqU
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
new_list = []
for i in my_list:
    if  i not in new_list:
        new_list.append(i)
        
print("The list with unique elements only:")
print(my_list)
print(new_list)


# 3.7.1.1 Lists in advanced applications
squares = [x ** 2 for x in range(10)]
squares

twos = [2 ** i for i in range(8)]
twos

odds = [x for x in squares if x % 2 != 0 ]
odds


# 3.7.1.3 Lists in advanced applications | Arrays
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)


temps = [[0.0 for h in range(24)] for d in range(31)]


# 3.7.1.6 SECTION SUMMARY
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'



# Module 3 quiz
nums =  []
vals = nums
vals.append(5)
print(len(nums))
print(len(vals))


nums =  []
vals = nums[:]
vals.append(5)
print(len(nums))
print(len(vals))


# Module 3 test
# 1
vals = [0,1,2]
vals.insert(0,1)
del vals[1]
vals


# 9
z =10
y = 0
x = y < z and z > y or y > z and z < y
x

# 15
my_list = [[0,1,2,3] for i in range(2)]
print(my_list[2][0])

# 18
my_list = [1,2,3,4]
print(my_list[-3:-2])


var = 1
while var < 10:
    print("#")
    var = var << 1
    
    
for i in range(1):
    print("#")
else:
    print("#")
    