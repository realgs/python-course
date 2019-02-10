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