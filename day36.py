#!/usr/bin/env python3


# Creates a decorator that manipulates the return value of a function
def to_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

# We use @ to place the decorator
@to_upper
def say(message = 'Hi', times = 1):
    return message * times


# the result of the say function is now in uppercase
print(say("Henrique ", 3)) # HENRIQUE HENRIQUE HENRIQUE