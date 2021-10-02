# --------------------------------------------------------------------------------
# Tobias Haueter                                                        2021-09-27
# Chart plotting software for .csv files.
#
# One Chart Plot with 3 lines, legend and cursor
# --------------------------------------------------------------------------------


import matplotlib.pyplot as plt
import mplcursors
import csv

# Create axis arrays
x0 = []

y1 = []
y2 = []
y3 = []

# Open csv file and choose the delimiter.
with open('testDATA/dataframe.pycharts', 'r') as data_csv:
    plots = csv.reader(data_csv, delimiter=',')  # <TAB>: delimiter='\t'

    # Skip first line -> no errors if are string header placed
    next(plots)

    # Read data x / y
    for row in plots:
        # Convert x_time to float
        x0.append(float(row[1]))

        # Convert y_xxx to float
        y1.append(float(row[2]))
        y2.append(float(row[3]))
        y3.append(float(row[4]))

# Plot 01
plt.plot(
    x0, y1,
    color="g",
    label='y1_rpm'
)

# Plot 02
plt.plot(
    x0, y2,
    color="b",
    label="y2_power [kW]"
)

# Plot 03
plt.plot(
    x0, y3,
    color="#ff0000",
    label="y3_current [A]"
)

# Site properties
fig = plt.gcf()
fig.canvas.manager.set_window_title('ECU Current Measurement - pyCHARTs')
plt.xlabel('x_Time')
plt.ylabel('y_axis')

# Set background
ax = plt.gca()
ax.set_facecolor('#E3EBFF')
ax.grid(color='silver')

# Implement cursor value
mplcursors.cursor(hover=False)  # mplcursors.cursor(hover=True)

plt.show()
