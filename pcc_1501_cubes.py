# Chapter 15: Try It Yourself. 15-01: Cubes

import matplotlib.pyplot as plt

x_values1 = range(1, 6)
y_values1 = [x1**3 for x1 in x_values1]
x_values2 = range(1, 5001)
y_values2 = [x2**3 for x2 in x_values2]

plt.subplot(2, 1, 1)
plt.plot(x_values1, y_values1, color='red')

plt.subplot(2, 1, 2)
plt.plot(x_values2, y_values2, color='blue')

plt.show()
