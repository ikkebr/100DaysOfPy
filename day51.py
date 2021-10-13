#!/usr/bin/env python3

# Given an integer n, return a list with each number from 1 to n
# except if it's a multiple of 3 or has a 3, 6, or 9 in the number
# it should be the string "clap".


def weird3(i):
    result = []
    for x in range(1, i + 1):
        sx = str(x)
        if x % 3 == 0:
            result.append("clap")
            continue
        while x:
            if x % 10 in [3, 6, 9]:
                result.append("clap")
                break
            x //= 10
        else:
            result.append(sx)

    return result


print(
    weird3(16)
)  # ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]
