#!/usr/bin/env python3

# We want to find the first number that is divisible by 3, 5, 7 and 13
# We can use a break if we don't want to keep searching after we found that number
# 1365 is the first number that matches that condition
for number in range(1, 10000):
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0 and number % 13 == 0:
        print(f"{number} matches the condition.")
        break
        # If you remove the break it will print all numbers in [1, 10000[
        # that satisfy the condition, namely 1365, 2730, 4095, 5460, 6825, 8190 and 9555

# Another loop modifier is the continue. A continue will skip the rest of the loop body and
# continue with the next item (or with the else clause if there is no item available)
# Let's say we want to print all values that are not multiples of 20
for value in [10, 20, 30, 40, 50, 60]:
    if not value % 20:
        continue

    print(value)  # this print will only be reached when value is 10, 30 or 50.
