#alternative way of reading inputs - using library:
#in terminal/command line write pip install cs50
#restart your IDE (Pycharm, VSCode, whatever it is)
#remember to use python3 in your project
#add "from cs50 import get_int" to the top of your file
# x = get_int("x: ")
# y = get_int("y: ")

print("x:")
x = int(input())
print("y:")
y = int(input())

print("-"*10)
print(x + y)
print("-"*10)

print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x modulo y: {x % y}")

xIsEven = x % 2 == 0
xIsEvenLog = 'X is even' if xIsEven else 'X is not even'
print(xIsEvenLog)


# TASKS (8p)- calculate & print:
#0 use alternative way of reading inputs - using library (0.5p)
#1 perimeter & field of circles with radius X & Y. (1p)
#2 find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
#3 check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (2p)
#Ad 3 Hint- use the "ternary operator" as we did in calculating xIsEvenLog above.
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
#5 Test your code. Check various edge cases. In other words: does your program (1, 3 & 4)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)