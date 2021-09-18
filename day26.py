#!/usr/bin/env python3

numbers = [1, 3, 5, 9]

while numbers:
    number = numbers.pop()

    if number % 2 == 0:
        print(f"{number} is even")
        break
else:
    # the else statement will only be executed if the break condition is not reached
    # and if the while condition becomes False. In this case, when numbers is empty
    # it will evaluate to False and the else statement will be executed.
    print("I didn't find any even numbers in the list")
