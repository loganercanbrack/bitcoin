def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# Replace 'yourfile.txt' with the name of your file
filename = 'master_addresses.txt'
line_count = count_lines(filename)
print(f"The file {filename} has {line_count} lines.")

