# Installation, preparation: https://www.youtube.com/watch?v=2y2F7x2TPPA
from decimal import *

print("Hello Matthew!")

x = 1
y = 10

print(x/y)
#how to add the description?
print(f"X/Y: {x/y}")
#how to do decimal roundings?
print(f"{x/y:.2f}")
print(f"{x/y:.4f}")
print(f"{x/y:.50f}")
#went wrong? This is casued by approximation in calculations. How to fix this?
getcontext().prec = 50
x = Decimal(x)
y = Decimal(y)
print(f"{x/y:.50f}")

print('-'*20)

#loops - repeating the operation automatically
#print numbers from 0 to 4
for i in range(5):
    print(i)

print('-' * 20)

#range of numbers from 10 to 15
for i in range(10, 16):
    print(i)

print('-' * 20)

#print revision numbers
for i in range(5):
    print("Revision number", i + 1)

print('-'*20)
#print exponential values for y = 2^x
for i in range(5):
    print(2**i)

print('-'*20)

#functions
def exponentialOf2(x):
    return 2**x
#print exponential values for y = 2^x using predefined function exponentialOf2
for i in range(5):
    print(exponentialOf2(i))

print('-'*20)

print('Insert your value here:')
x = int(input())
print('The inserted value times 2 is', 2 * x)

print('-'*20)

#tables

y = [0, 1, 2, 3, 4]
print(y)
print(len(y))

print('-'*20)


#TASKS (8p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (1p)
#2 ask the user for a number and print its factorial (2p)
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (4p)
#4 upload the solution as a Github repo. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (1p)
#Ad 4 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.