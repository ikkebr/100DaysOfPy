#!/usr/bin/env python3

# Given a string s representing a number in base 3 (consisting only of 0, 1, or 2)
# return its decimal integer equivalent.


def to_base3(s):
    return int(s, 3)


print(to_base3("10"))  # prints 3
print(to_base3("21"))  # prints 7
