#!/usr/bin/env python3

# Functions can be very simple or very complex
def square(x):
    return x * x


# Functions can take other functions as arguments
def apply(function, operand):
    return function(operand)


print(apply(square, 10))  # prints 100


# Some functions can take many arguments
def sum_all(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


print(sum_all(1, 2, 3, 4, 5))  # prints 15
print(sum_all(*range(11)))  # prints 55
