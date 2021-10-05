#!/usr/bin/env python3

# In python we don't have true "Private" instance variables
# we have a convention that names prefixed with _ should be treated as non-public
class Temperature(object):
    def __init__(self, temperature=0):
        self._temperature = temperature
        self.__unit = "Celsius"

    # we can use the built-in property decorator to achieve getters and setters behaviour
    # this will become the getter
    @property
    def temperature(self):
        return self._temperature

    # and this the setter
    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    # or use the property function
    def set_unit(self, unit):
        self.__unit = unit

    def get_unit(self):
        return self.__unit

    unit = property(get_unit, set_unit)


t1 = Temperature(27)  # some nice 27 degrees Celsius.

print(t1.temperature)  # 27
print(t1.unit)  # prints Celsius

t1.temperature = 60
t1.unit = "Fahrenheit"

print(t1.temperature)  # 60
print(t1.unit)  # prints Fahrenheit
