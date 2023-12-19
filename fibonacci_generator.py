# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:23:52 2023

@author: ANaz
"""
# list
def fib(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
print(fib(10))

#generator
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for i in fib(10):
    print(i)



    