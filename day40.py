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

# Treasure_Chest inherits from Box
# This means that any Treasure_Chest instance will have access to the store method
# and to the __init__ constructor.
class Treasure_Chest(Box):
    def open(self):
        treasure = self.storage[:]
        self.storage.clear()
        return treasure


chest = Treasure_Chest("Amazing Chest", 3)
chest.store('Weekend')
chest.store(1337)
chest.store('Pizza')

treasure = chest.open()
print(treasure) # prints ['Weekend', 1337, 'Pizza']
print(chest.storage) # prints []

