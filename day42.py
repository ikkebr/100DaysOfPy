#!/usr/bin/env python3

# In python we don't have true "Private" instance variables
# we have a convention that names prefixed with _ should be treated as non-public
# and we can use name mangling (__) to make the variables hard to find
# but you can get around that.
class Temperature(object):
    def __init__(self, temperature=0):
        self.temperature = temperature
        # let's say we are keeping track of the units in the Temperature instance
        self.__unit = "Celsius"


t1 = Temperature(27)  # some nice 27 degrees Celsius.

print(t1.temperature)  # 27
# print(t1.__unit) # fails as __unit has been mangled
print(
    t1._Temperature__unit
)  # but if you know where to look, you can still access it...
