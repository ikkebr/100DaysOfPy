#!/usr/bin/env python3

import math

circle_radius = 3
circle_area = circle_radius * math.pi
print(circle_area) # prints 9.4247...

# we can monkey patch the value of pi!
math.pi = 3 # because why not?!
circle_area = circle_radius * math.pi
print(circle_area) # prints 9