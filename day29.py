#!/usr/bin/env python3

# We can use the raise expression to throw an exception
def countdown_to_zero(n):
    if n < 0:
        raise ValueError(f"n must be >= 0. Your n is {n}.")

    if n > 100:
        raise ValueError(f"n must be <= 100. Your n is {n}.")

    return ", ".join(map(str, range(n, -1, -1)))


print(countdown_to_zero(20))
print(countdown_to_zero(99999))
