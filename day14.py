#!/usr/bin/env python3

# The for statement can be used to iterate over the elements of a sequence!
# Not quite the same as the while loop!

# We can iterate over the range sequence
for number in range(10):
    print(f"The number is {number}.")
    print(f"The square of {number} is {number*number}.")

# We can iterate over a list, one element at a time
for element in ["Pizza", 42, 3.50]:
    print(f"The element is {element}")
    print(type(element))

# We can iterate over strings, one character at a time
for char in "Henrique":
    print(char.upper())

# We can iterate over a list of fixed-size sequences
people = [("Henrique", 33), ("Paulo", 20), ("Rafael", 31), ("Carlos", 10)]
for name, age in people:
    # name will 'point' to the first element in the tuple
    # age will 'point' to the second element in the tuple
    if age > 18:
        print(f"{name} is older than 18", end=", ")
    else:
        print(f"{name} is younger than 18", end=", ")

    print(f"{name} is {age} years old.")
