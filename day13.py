#!/usr/bin/env python3

start = 0
stop = 10

# We can generate a sequence containing all values in [start, stop[ with the range function
# In Python 3, range will return a sequence but only one element at a time.
# If we want all of the elements at once, we can build a list from it.
count = range(start, stop)
print(list(count))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# We don't have to enter a start value. If we don't it will default to 0.
count = range(stop)
print(list(count))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# We can also use a set step
odd = range(1, 21, 2)  # generating all odd integers between [1 and 20]
print(list(odd))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

even = range(0, 21, 2)  # generating all even integers between [0 and 20]
print(list(even))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# We can also do it backwards!
decreasing_odd = range(20, -1, -2)
print(list(decreasing_odd))  # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
