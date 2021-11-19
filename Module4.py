# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:32:33 2021

@author: Wujian
"""

def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# 4.2.1.2 How functions communicate with their environment
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

# 4.2.1.3 How functions communicate with their environment
def message(what, number):
    print("Enter", what, "number", number)

# invoke the function
message("telephone", 11)
message("price", 5)
message("number", "number")

# 4.2.1.4 How functions communicate with their environment

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# 4.2.1.5 Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# 4.2.1.7 How functions communicate with their environment
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction()


# 4.3.1.1 Returning a result from a function
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")

happy_new_year()
happy_new_year(False)


def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)


def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


# 4.3.1.2 Returning a result from a function
value = None
if value is None:
    print("Sorry, you don't carry any value")

# 4.3.1.3 Returning a result from a function
def strange_function(n):
    if(n % 2 == 0):
        return True
    
print(strange_function(2))
print(strange_function(1))


# 4.3.1.4 Returning a result from a function
def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
print(list_sum([5, 4, 3]))

# print(list_sum(5))


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))



# 4.3.1.6 LAB: A leap year: writing your own functions
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#    if (year % 4 == 0) and (year % 100) != 0: 
#        return True
#
# put your code here
#
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
    


# 4.3.1.7 LAB: How many days: writing and using your own functions
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month==2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4,6,8,9,11]:
        return 30
    else:
        return None
#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")    
    
# 4.3.1.8 LAB: Day of the year: writing and using your own functions
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month==2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4,6,8,9,11]:
        return 30
    else:
        return None
#
# Your code from LAB 4.3.1.7.
#

def day_of_year(year, month, day):
#    if is_year_leap(year) == True :return 366
#    else: return 365
    
    total = 0  # initializing the total variable to add results
    # create loop to add only days in the months before the month in the input/test data
    for i in range(1, month):
        result = days_in_month(year, i)
        total += result
    day_num = total + day  # add the value of the day argument to get day of the year
    return day_num
#
# Write your new code here.
#

print(day_of_year(2000, 12, 31))
print(day_of_year(1999, 12, 31))
print(day_of_year(2021, 7, 29))    


# 4.3.1.9 LAB: Prime numbers - how to find them
def is_prime(num):
# Write your code here.
    if num < 2:
        return False
    elif num == 2:
        return True  
    for n in range(2, num):
        if num % n ==0:
            return False
    return True

for i in range(1, 30):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
    
# 4.3.1.10 LAB: Converting fuel consumption
def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784  
    mile   = 100/ 1.609344 
    return mile/gallon    
#
# Write your code here.
#

def miles_gallon_to_liters_100km(miles):
    km = miles * 1.609344
    liters = 3.785411784
    return 100 * liters/ km
#
# Write your code here
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# 4.3.1.11 SECTION SUMMARY

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)
hi_everybody(["Adam", "John", "Lucy"])

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

# Exercise 1
def hi():
    return
    print("Hi!")

hi()

# Exercise 2
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

# 4.4.1.2 Scopes in Python
def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

def my_function():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)


# 4.4.1.3 Scopes in Python | global
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)

# 4.5.1.2 Creating functions | two-parameter functions
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2


print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

# 4.5.1.3 Creating functions | three-parameter functions
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# 4.5.1.4 Creating functions | testing triangles

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')



def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
print(is_a_right_triangle(3, 5, 4))


# 4.5.1.5 Creating functions | right-angle triangles
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))



# 4.5.1.6 Creating functions | factorials
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 10):  # testing
    print(n, factorial_function(n))

# 4.5.1.7 Creating functions | Fibonacci numbers
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

# 4.5.1.8 Creating functions | recursion

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))

# 4.5.1.9 SECTION SUMMARY

# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24


# 4.6.1.1 Tuples and dictionaries
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

# 4.6.1.2 Tuples and dictionaries
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    
    
# 4.6.1.3 Tuples and dictionaries
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)


# 4.6.1.5 Tuples and dictionaries

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


# 4.6.1.6 Tuples and dictionaries | methods

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])
    
# 4.6.1.7 Tuples and dictionaries | methods  
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)
    
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for french in dictionary.values():
    print(french)
    
    
# 4.6.1.8 Tuples and dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['cat'] = 'minou'
print(dictionary)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['swan'] = 'cygne'
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
del dictionary['dog']
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}


# 4.6.1.9 Tuples and dictionaries
school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)