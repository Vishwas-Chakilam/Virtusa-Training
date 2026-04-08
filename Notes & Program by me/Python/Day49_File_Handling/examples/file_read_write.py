filename = "log.txt"

# Writing to file
with open(filename, 'w') as f:
    f.write("Line 1: Log Started\n")
    f.write("Line 2: Processing Data\n")

# Reading from file
with open(filename, 'r') as f:
    print(f.read())