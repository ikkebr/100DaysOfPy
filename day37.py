#!/usr/bin/env python3

class Box(object):
    def __init__(self, name='MyBox'):
        self.name = name
        self.storage = []
    
my_box = Box("My First Box")
my_box.storage.append("abc")
my_box.storage.append("cde")

print(my_box.storage) # prints ['abc', 'cde']
