#!/usr/bin/env python3

# Given an integer n, return the number of 1 bits in n.


def count_1bits(n):
    return bin(n).count("1")


print(count_1bits(2))  # prints 1
print(count_1bits(3))  # prints 2
print(count_1bits(7))  # prints 3
print(count_1bits(15))  # prints 3
