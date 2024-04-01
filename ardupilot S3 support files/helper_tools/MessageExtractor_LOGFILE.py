import re

# Define the pattern to match lines similar to the given example
pattern = r"MSG, \d+, LIDAR: \d+\.\d+, \d+\.\d+\n"
matches_found = 0
# File paths
input_file_path = '/home/dk/projects/ArdupilotLogFolders/log5.log'
output_file_path = '/home/dk/projects/helper_tools/outputs/log5.txt'


# Open the input file and read lines
with open(input_file_path, 'r') as input_file, open(output_file_path, 'a') as output_file:
    for line in input_file:
        # Check if the line matches the pattern
        if re.match(pattern, line):
             output_file.write(line)
            # Write the matching line to the output file
             matches_found += 1

print(f"Extraction complete. {matches_found} matches were found and written to the output file.")
