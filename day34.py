#!/usr/bin/env python3

# Using a finally on a try .. except block will change the flow of execution of a function
# before the return is executed, the finally block is triggered and takes precedence
def divide(x, n):
    try:
        number = x/n
        print(f"The result is {number}")
        return number
    except ZeroDivisionError:
        print("I cannot divide by 0!")
        return -1
    finally:
        print("This will get returned regardless if we hit exceptions or not.")
        # uncomment the next line and the function will always return -2
        # return -2


divide(1, 0)