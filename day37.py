#!/usr/bin/env python3

# Let's create a Box class that has a name and some storage
class Box(object):
    def __init__(self, name='MyBox'):
        self.name = name
        self.storage = []
    
my_box = Box("My First Box")

# we can then insert things in the storage
my_box.storage.append("abc")
my_box.storage.append("cde")

# we can also show what is in storage
print(my_box.storage) # prints ['abc', 'cde']
