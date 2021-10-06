#!/usr/bin/env python3

# In python we can use 'magic methods' to implement behaviours in our classes
# magic methods will start and end with double underscores.
class Temperature(object):
    def __init__(self, temperature=0, unit="Celsius"):
        self.temperature = temperature
        self.unit = unit

    # we can define how an instance is converted to str
    def __str__(self):
        return f"{self.temperature} degrees {self.unit}"

    # or even what happens if we add two Temperature objects together!
    def __add__(self, other):
        # we can only operate on Temperatures
        if not isinstance(other, Temperature):
            raise Exception("Both objects need to be temperatures...")

        # We can only operate if they have the same unit
        if self.unit != other.unit:
            raise ValueError("Both temperatures must be using the same unit...")

        # if all is good, we return a new Temperature instance
        return Temperature(self.temperature + other.temperature, unit=self.unit)


t1 = Temperature(27)  # some nice 27 degrees Celsius.
print(t1)

t2 = Temperature(-5)  # some cold -5 degrees Celsius
print(t2)

print(t1 + t2)  # some nice 22 degrees Celsius.
