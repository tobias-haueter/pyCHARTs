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

    # skip first line -> no errors if are string header placed
    next(plots)

    # Read data x / y
    for row in plots:
        # Convert x_time to float
        x0.append(float(row[1]))

        # Convert y_axis to float
        y1.append(float(row[2]))
        y2.append(float(row[3]))
        y3.append(float(row[4]))


# Add subplots
fig, axs = plt.subplots(3, sharex=True, sharey=False)
fig.suptitle('ECU Current Measurement')


# Plot 01
axs[0].plot(
            x0, y1,
            color="g",
            label="rpm [min-1]"
            )
axs[0].legend(loc="upper right")
axs[0].set_ylabel("y1_rpm")
axs[0].set_facecolor('#E3EBFF')
axs[0].grid(color='silver')


# Plot 02
axs[1].plot(
            x0, y2,
            color="b",
            label="power [kW]"
            )
axs[1].legend(loc="upper right")
axs[1].set_ylabel("y2_power")
axs[1].set_facecolor('#E3EBFF')
axs[1].grid(color='silver')


# Plot 03
axs[2].plot(
            x0, y3,
            color="#ff0000",
            label="current [A]"
            )
axs[2].legend(loc="upper right")
axs[2].set_ylabel("y3_current")
axs[2].set_facecolor('#E3EBFF')
axs[2].grid(color='silver')


# Site properties
fig.canvas.manager.set_window_title('pyCHARTs - ECU Current Measurement')
plt.xlabel('x0_time = daily seconds - 10Hz')


# Implement cursor value
mplcursors.cursor(hover=False)  # mplcursors.cursor(hover=True)


plt.show()
