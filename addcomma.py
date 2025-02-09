#   input_file = 'g1874.txt'
#   output_file = 'test.csv'

## Define positions after which to add commas (column widths)
##column_positions = [4, 2, 2, 4, 8, 2, 2, 5, 5, 5, 5, 6, 6, 6, 6, 6]  # Adjust based on your data
#   column_positions = [4, 6, 8, 12, 20, 22, 24, 29, 34, 39, 44, 50, 56, 62, 68]

#   def add_commas(line, positions):
#       new_line = ""
#       last_pos = 0
#       for pos in positions:
#           new_line += line[last_pos:pos] + ","
#           last_pos = pos
#       new_line += line[last_pos:]  # Add the remaining part of the line
#       return new_line

## Process the file
#   with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#       for line in infile:
#           outfile.write(add_commas(line, column_positions))

import os

# Input and output directories
input_dir = 'NASA'
output_dir = 'NASAcsv'

# Define positions after which to add commas (column widths)
column_positions = [4, 6, 8, 12, 20, 22, 24, 29, 34, 39, 44, 50, 56, 62, 68]

def add_commas(line, positions):
    """Insert commas at the specified positions in a line."""
    new_line = ""
    last_pos = 0
    for pos in positions:
        new_line += line[last_pos:pos] + ","
        last_pos = pos
    new_line += line[last_pos:]
    return new_line

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):  # Only process .txt files
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.txt', '.csv'))

        # Read the input file and write the output file
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(add_commas(line, column_positions))

print(f"Conversion completed! CSV files are saved in: {output_dir}")


