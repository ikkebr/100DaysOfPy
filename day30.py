#!/usr/bin/env python3

first_number = input("Enter an integer: ")
second_number = input("Enter another integer: ")


try:
    division_result = int(first_number) / int(second_number)
    print(f"The division of the first number by the second one is {division_result}")

except ZeroDivisionError:
    # this will get executed if we get a division by zero
    # meaning that second_number is 0
    print(f"It was not possible to divide by zero")
except ValueError as e:
    # this will get executed if one of the two numbers fails
    # to be converted to an integer
    print(f"One of the things you entered was not an integer: ", end="")
    print(e)
except Exception as e:
    # this will get executed if we get some other error
    print("Something else went wrong: ", end="")
    print(e)
