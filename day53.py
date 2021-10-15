#!/usr/bin/env python3

# Given a string s representing a number in base 3 (consisting only of 0, 1, or 2)
# return its decimal integer equivalent.

# short version using the built-in int function
def to_base3(s):
    return int(s, 3)

# long version using proper base conversion
def to_base3_long(s):
    res = 0
    for i, v in enumerate(reversed(list(s))):
        res += pow(3,i) * int(v)

    return res

print(to_base3("10"))  # prints 3
print(to_base3_long("21"))  # prints 7
print(to_base3_long("1112220")) # prints 1131
assert( to_base3_long("1110002120") == to_base3("1110002120") )

