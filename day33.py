#!/usr/bin/env python3

# We can use the with statement to make working with files more cleaner and readable
with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
    for line in in_file:
        # for each line in the original file, we will write it
        # twice to the output file.
        out_file.write(line * 2)


# the files will be closed automatically once the with block finishes
