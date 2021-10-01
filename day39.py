#!/usr/bin/env python3

class Box(object):
    def __init__(self, name='MyBox', capacity = 1):
        self.capacity = capacity
        self.name = name
        self.storage = []

    def store(self, object):
        if len(self.storage) >= self.capacity:
            print("Storage is Full.")
            return -1

        self.storage.append(object)
        return len(self.storage) - 1
    
my_box = Box("My First Box", capacity = 0)
my_box.store("abc") # should print Storage is Full

my_other_box = Box("My second box", capacity = 5)
my_other_box.store("abc") # should be ok
