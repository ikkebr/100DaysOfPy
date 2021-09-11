#!/usr/bin/env python3

# Functions are sequences of instructions that perform a specific task.
# Python comes with a series of built-in functions, but you are also able to create your own!

# Let's say we want to return the cube of a number
def cube(number):
    return number * number * number


# We invoke a function by calling its identifier and passing the required arguments
result = cube(5)
print(result)

# We can also have functions with no return statement
# These functions are called void (and they implicitly return None at the end)
def print_cube(number):
    print(f"Calculating the cube of {number}:", end=" ")
    print(cube(number))


print_cube(10)

# Functions can have no arguments
def hi():
    return "Hi"


print(hi())

# or they can have multiple arguments, and even default values
def many_times(message, times=1):
    return message * times


# we can pass all of the arguments
hehe = many_times("He", 10)  # prints HeHeHeHeHeHeHeHeHeHe
print(hehe)

# or just some
print(many_times("Ha"))  # prints Ha
