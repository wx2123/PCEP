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