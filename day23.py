#!/usr/bin/env python3

# Since we are talking about functions, zip is another very useful one.
# zip will take 2 or more sequences and group together elements by index.
# It will stop once one of the sequences is empty
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
numbers = [1, 2, 3, 4, 5]

for month, number in zip(months, numbers):
    print(f"{month} is month #{number}")

# zip with 3 sequences
for month, number, value in zip(months, numbers, range(10, 10000, 20)):
    print(f"{month} is month #{number} and it is worth ${value}")

# you can use zip to look at the next or previous element in a sequence when iterating
for current, next in zip(months, months[1:]):
    print(f"The current month is {current} and the next is {next}") 