#!/usr/bin/env python3

# Given an integer n greater than or equal to 0, return whether it is a power of two.


def power_of_two(n):
    return bin(n)[2:].count("1") == 1


print(power_of_two(2))  # True
print(power_of_two(3))  # False
print(power_of_two(512))  # True
print(power_of_two(4096))  # True
print(power_of_two(4094))  # False
