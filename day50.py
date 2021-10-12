#!/usr/bin/env python3

# Given a list of integers nums, find the most frequently occurring element and
# return the number of occurrences of that element.

from collections import Counter

def solution(nums):
    if nums:
        counter = Counter(nums)
        most_common = counter.most_common(1)
        most_common_element, most_common_times = most_common[0]
        return most_common_element
    return 0



print(solution([1, 4, 1, 7, 1, 7, 1, 1])) # 1 (appears 5 times)
print(solution([1, 2, 3, 4, 5, 6, 7])) # 1 (appears 1 time)