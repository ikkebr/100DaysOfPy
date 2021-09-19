#!/usr/bin/env python3

numbers = [1, 3, 5, 9, 8]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
        break
else:
    # we can have else statements following for loops
    # the else statement will only execute if we don't reach the break statement
    # once we reach the end of the iterator
    print("I didn't find any even numbers in the list")
