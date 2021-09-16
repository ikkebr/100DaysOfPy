#!/usr/bin/env python3

# Consider an unsorted list of numbers
numbers = [10, 2, 1, 3,2, 4, 5, 6, 7, 11, 32]

# We can easily sort it in ascending order by calling the sorted function
sorted_numbers = sorted(numbers)
print(sorted_numbers) # prints [1, 2, 2, 3, 4, 5, 6, 7, 10, 11, 32]

# We can also sort it in descending order with an extra argument
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers) # prints [32, 11, 10, 7, 6, 5, 4, 3, 2, 2, 1]

# Sorted will also work on lists and tuples
# By default, it will sort values according to the first element in the tuple
# In the next example, it will sort the list of months lexicographically
months = [ ('Mar', 3), ('Jan', 1), ('Apr', 4), ('May', 5), ('Feb', 2)]
sorted_months = sorted(months)
print(sorted_months) # prints [('Apr', 4), ('Feb', 2), ('Jan', 1), ('Mar', 3), ('May', 5)]

# If we don't want to sort it lexicographically, we can force sorted to use the second element
import operator
sorted_months = sorted(months, key=operator.itemgetter(1))
print(sorted_months) # prints [('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5)]