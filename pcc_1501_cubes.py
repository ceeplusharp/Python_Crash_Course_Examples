# Chapter 15: Try It Yourself. 15-01: Cubes

import matplotlib.pyplot as plt

x_values1 = range(1, 6)
y_values1 = [x1**3 for x1 in x_values1]
x_values2 = range(1, 5001)
y_values2 = [x2**3 for x2 in x_values2]

fig = plt.figure()
fig.suptitle("Plot of Cubic Numbers", fontsize=16)

ax = plt.subplot(211)
ax.set_title("First 5 Cubic Numbers")
ax.plot(x_values1, y_values1)

ax = plt.subplot(212)
ax.set_title("First 5,000 Cubic Numbers")
ax.plot(x_values2, y_values2)

plt.subplots_adjust(hspace=0.5)
plt.show()
