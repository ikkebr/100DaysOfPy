#!/usr/bin/env python3

class Box(object):
    _boxes = 0 # boxes is a class attribute

    def __init__(self, name='MyBox', capacity = 1):
        self.capacity = capacity
        self.name = name
        self.storage = []

        # we will increment the number of boxes by one
        Box._boxes += 1 

    @classmethod
    def how_many(cls):
        return cls._boxes
    
my_box = Box("My First Box", capacity = 0)
print(Box.how_many()) # 1

my_other_box = Box("My second box", capacity = 5)
print(Box.how_many()) # 2

third_box = Box("Third")
print(Box.how_many()) # 3