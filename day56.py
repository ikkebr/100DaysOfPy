#!/usr/bin/env python3

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. 
# If there is no such substring return -1.

from collections import Counter


def maxLengthBetweenEqualCharacters(s: str) -> int:
    counter = Counter(list(s))
    max_l = -1

    for key, value in counter.items():
        if value >= 2:
            initial = s.find(key)
            next = s.rfind(key)

            distance = next - initial - 1
            if distance > max_l:
                max_l = distance

    return max_l


print(maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv")) # prints 18
