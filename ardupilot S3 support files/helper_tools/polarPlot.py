import re
import matplotlib.pyplot as plt
import numpy as np
import os

# Regular expression pattern to extract distance and angle
pattern = re.compile(r"MSG, \d+, LIDAR: (\d+\.\d+), (\d+\.\d+)")

def extract_data_and_plot(file_path):
    distances = []  # Array to store distance values
    angles_degrees = []  # Array to store angle values

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                distance, angle = map(float, match.groups())
                distances.append(distance)
                angles_degrees.append(angle)
    
    # Convert angles from degrees to radians for plotting
    angles_radians = np.radians(angles_degrees)
    
    # Define the figure size and DPI
    # Here, we assume a typical screen resolution and size
    dpi = 100  # Dots per inch
    figure_width = 1920 / dpi  # Width in inches
    figure_height = 1080 / dpi  # Height in inches
    
    # Plotting with specified figure size
    plt.figure(figsize=(figure_width, figure_height), dpi=dpi)
    ax = plt.subplot(111, polar=True)
    ax.scatter(angles_radians, distances)
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    # Determine the output file name based on the input file name
    output_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.png'
    
    # Save the plot with the defined figure size and DPI
    plt.savefig(output_file_name, dpi=dpi)
    print(f"Graph saved as {output_file_name}")

# Replace 'path/to/your/data_file.txt' with the actual path to your text file
file_path = '/home/dk/projects/helper_tools/outputs/log1.txt'
extract_data_and_plot(file_path)

