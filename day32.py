#!/usr/bin/env python3

# we will open an input.txt file as in_file
# we use the 'r' mode to make it read-only
in_file = open("input.txt", "r")

# we will open an output.txt file as out_file
# the 'w' mode will create the file if it is not there
# or empty it if it exists.
out_file = open("output.txt", "w")

# we can go over each individual line from the input file
# using a for statement
for line in in_file:
    # for each line in the original file, we will write it
    # twice to the output file.
    out_file.write(line * 2)

# never forget to close your files!
in_file.close()
out_file.close()
