#!/usr/bin/env python3

# We can use finally to clean up after a try ... except block.
try:
    in_file = open("input.txt")
    number = int( in_file.read(10) )
    print(f"I have read the number {number}")
except ValueError:
    print("I couldn't read a number.")
except Exception as e:
    print("Something went wrong! " + e)
finally:
    print("This will get executed regardless if we hit an exception or not.")

    # let's make sure the file gets closed.
    in_file.close()