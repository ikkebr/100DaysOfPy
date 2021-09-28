#!/usr/bin/env python3

def to_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@to_upper
def say(message = 'Hi', times = 1):
    return message * times


print(say("Henrique ", 3)) # HENRIQUE HENRIQUE HENRIQUE