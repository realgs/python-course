from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

plot([1,2,3,2,3,4,3,4,5])
show()
#
# x = linspace(0, 4.*pi, 100)
# y = sin(x)
# plot(x, y)
# show()
#
# x = linspace(-10., 10., 200)
# x2 = linspace(-10., 10., 200)
# y = sin(x) * exp(-(x/5.0)**2)
# y2 = cos(x2) * exp(-(x2/2.0)**2)
# figure(1, figsize = (6,4) )
# plot(x, y, 'b-', label='theory')
# plot(x2, y2, 'ro', label="data")
# xlabel('x')
# legend(loc='upper right')
# axhline(color = 'gray', zorder=-1)
# axvline(color = 'gray', zorder=-1)
# ylim(-1.3, 1.3)
# savefig('WavyPulse.pdf')
# show()

num_points = 20000
x_values = zeros(num_points)
y_values = zeros(num_points)

for i in range(num_points - 1):
    x_values[i + 1] = x_values[i] + randn()
    y_values[i + 1] = y_values[i] + randn()

point_numbers = range(num_points)
scatter(x_values, y_values, s=1, c=point_numbers, cmap=cm.Blues)
# pierwszy i ostatni punkt
scatter(x_values[0], y_values[0], c='green', edgecolors='none', s=70)
scatter(x_values[-1], y_values[-1], c='red', edgecolors='none', s=70)
# ukrycie osi
axis('off')
show()
figure(dpi=128, figsize=(7, 4))