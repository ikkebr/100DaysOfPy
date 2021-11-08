#!/usr/bin/env python3

# Given a list of integers nums and an integer k, 
# return the maximum possible i where nums[0] + nums[1] + ...  + nums[i] ≤ k. 
# Return -1 if no valid i exists.

def k_prefix(nums: list, k: int) -> int:
    result = -1

    if not nums:
        return result
    #elif nums[0] > k:
    #    return result

    result = sum = 0
    while sum <= k:
        current = nums.pop(0)
        sum += current
        result += 1

        if not nums:
            break

    else:
        return result-1
 
    return result-2


print(k_prefix([3, -5, 4, 1, 6], 4))