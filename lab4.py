import numpy as np
import matplotlib.pyplot as plt

###Euler method

# parameters
T = 5
h = 0.1

# x' = ax
a = 1
initial_x = 1

t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (1 * x[i])

plt.plot(t, x, 'o')
plt.xlabel('t', fontsize=14)
plt.ylabel('x', fontsize=14)
plt.show()

#1 Looking at the Euler method above create your own function that takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (2p)
#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (2p)
#2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'
#3