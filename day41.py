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
class Treasure_Chest(Box):
    def open(self):
        treasure = self.storage[:]
        self.storage.clear()
        return treasure

# Infinite_Storage also inherits from Box
class Infinite_Storage(Box):
    def store(self, object):
        # we can store an infinite amount of things in the cest
        self.storage.append(object)
        return len(self.storage) - 1

# Infinite Chest inherits from Treasure_Chest and Infinite_Storage
# meaning it wil have both the TC.open and the custom IS.store methods
# resulting in an openable box with infinite storage
class Infinite_Chest(Treasure_Chest, Infinite_Storage):
    pass

chest = Infinite_Chest("Amazing Chest", 0)
chest.store('Weekend')
chest.store(1337)
chest.store('Pizza')

treasure = chest.open()
print(treasure) # prints ['Weekend', 1337, 'Pizza']
print(chest.storage) # prints []

