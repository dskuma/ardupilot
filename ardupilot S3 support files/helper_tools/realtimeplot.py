import matplotlib.pyplot as plt
import numpy as np
import sys

# Setup polar plot for updating
plt.ion()  # Interactive mode on
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
sc = ax.scatter([], [])  # Initial empty scatter plot

# Lists to store all distances and angles
all_distances = []
all_angles = []

# Function to update the polar plot with new data
def update_polar_plot(new_distance, new_angle):
    """Update the polar plot with a new distance and angle (in degrees)."""
    all_distances.append(new_distance)
    all_angles.append(new_angle)

    # Convert all angles from degrees to radians for plotting
    angles_rad = np.radians(all_angles)

    # Update scatter plot data with all points
    sc.set_offsets(np.c_[angles_rad, all_distances])
    ax.relim()  # Recompute the ax.dataLim
    ax.autoscale_view()  # Automatic axis scaling
    plt.draw()
    plt.pause(0.1)  # Pause to ensure the plot updates

# Read from stdin in a loop
for line in sys.stdin:
    if line.strip():  # Make sure the line is not empty
        try:
            # Now expecting the format 'distance,angle'
            distance, angle = map(float, line.strip().split(','))
            update_polar_plot(distance, angle)
        except ValueError:
            print("Error: Invalid input format. Please ensure the input is 'distance,angle'.")
            continue

