#!/usr/bin/env python3

print("This is a literal")
print("This is another literal")
print("""This is yet another literal!""")

# Printing an object
variable = 5
print(variable)

# Using string concatenation:
print("The number is " + str(variable))

# Using str.format
print("The number is {}".format(variable))

# Using printf-style
print("The number is %i" % variable)
print("The number is %.2f" % variable)

# Using f-strings (since Py 3.6)
print(f"The number is {variable}")

# Printing multiple objects
another_variable = 0
print(variable, another_variable)  # prints 5 0
print(variable, another_variable, sep=" -*- ")  # prints 5 -*- 0
print(1, 2, 3, sep=" -*- ")  # prints 1 -*- 2 -*- 3
