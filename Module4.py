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