# Chapter 15: Try It Yourself. 15-03: Molecular Motion.
import matplotlib.pyplot as plt

from pcc_1500_random_walk import RandomWalk

# Keep making new plots, as long as the program is active.
while True:
    # Make a random plot.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    plt.plot(rw.x_values, rw.y_values, linewidth=0.5)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another plot? (y/n): ")
    if keep_running == 'n':
        break
