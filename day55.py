#!/usr/bin/env python3

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


def is_pos_mono(nums):
    return all(x >= y for x, y in zip(nums, nums[1:]))


def is_neg_mono(nums):
    return all(x <= y for x, y in zip(nums, nums[1:]))


def is_monotonic(nums):
    return is_pos_mono(nums) or is_neg_mono(nums)


print(is_monotonic([1, 3, 2]))  # False
print(is_monotonic([1, 2, 4, 5]))  # True
print(is_monotonic([6, 5, 4, 4]))  # True
