import sys
import os
import re

def append_suffix_to_lines(input_file_path, output_file_path):
    counter = 0
    marker_positions = {}
    lines = []

    # First pass: Assign line numbers and identify markers
    with open(input_file_path, 'r') as infile:
        for line in infile:
            stripped_line = line.strip()
            # Skip lines that start with '#' or are empty
            if stripped_line.startswith('#') or len(stripped_line) == 0:
                lines.append(line)
            elif re.match(r'^\[.*\]', stripped_line):
                # Line contains a marker at the beginning
                marker_name = stripped_line.split()[0]
                marker_name = marker_name[1:-1]  # Remove the square brackets
                marker_positions[marker_name] = counter
                # Write the line without the marker name, add to lines
                rest_of_line = ' '.join(stripped_line.split()[1:])
                lines.append(f"{counter} {rest_of_line}\n")
                counter += 1
            else:
                # Add the counter before the line
                lines.append(f"{counter} {line}")
                counter += 1

    # Second pass: Replace marker references with corresponding line numbers
    updated_lines = []
    marker_pattern = re.compile(r'\[(.*?)\]')
    for line in lines:
        def replace_marker(match):
            marker_name = match.group(1)
            return str(marker_positions.get(marker_name, match.group(0)))

        updated_line = marker_pattern.sub(replace_marker, line)
        updated_lines.append(updated_line)

    # Write updated lines to output file
    with open(output_file_path, 'w') as outfile:
        outfile.writelines(updated_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file_path> [output_file_path]")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else input_file_path

    append_suffix_to_lines(input_file_path, output_file_path)
    print(f"Processing completed. Modified content saved to {output_file_path}")
