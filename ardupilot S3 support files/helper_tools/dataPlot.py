import matplotlib.pyplot as plt
import numpy as np  # Needed for the conversion of angles from degrees to radians

def read_csv_to_arrays(filename):
    """Reads a CSV file with distance and angle data, storing them in two arrays."""
    distances = []  # Array to store distances
    angles = []     # Array to store angles
    
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 2:
                distance, angle = values
                distances.append(float(distance))
                angles.append(float(angle))
    
    return distances, angles

def plot_polar_data(angles, distances):
    """Plots distances on a circular (polar) plot with angles."""
    # Convert angles from degrees to radians for plotting
    angles_radians = np.radians(angles)
    
    # Create a polar subplot
    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111, polar=True)
    ax.scatter(angles_radians, distances)
    
    ax.set_title('Polar Plot of Distance vs. Angle')
    ax.set_theta_zero_location('N')  # Setting the 0 degrees at the top
    ax.set_theta_direction(-1)  # Setting the direction of angles to clockwise
    ax.set_xlabel('Angles (radians)')
    ax.set_ylabel('Distance')
    ax.grid(True)
    
    plt.show()

if __name__ == "__main__":
    filename = 'REVX.txt'  # Make sure to replace this with your actual file name
    distances, angles = read_csv_to_arrays(filename)
    plot_polar_data(angles, distances)

