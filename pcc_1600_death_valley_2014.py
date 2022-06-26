# Chapter 16: Error Checking

import csv
import matplotlib.pyplot as plt

filename = 'pcc_death_valley_2014_rev.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file.
    highs = []
    for row in reader:
        # Added error checking to handle missing data.
        try:
            high = int(row[1])
        except ValueError:
            print(f"Missing data for highs index[{highs.index(high)}]")
        else:
            highs.append(high)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures for Death Valley during 2014", fontsize=18)
plt.xlabel('', fontsize=14)
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
