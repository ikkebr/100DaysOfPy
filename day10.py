#!/usr/bin/env python3

# creating an empty dictionary using dict()
an_empty_dictionary = dict()

# creating an empty dictionary using {}
my_dictionary = {}

# adding a key to a dictionary
my_dictionary["name"] = "ikkebr"
print(my_dictionary["name"])

# checking to see if a key is in a dictionary
if "name" in my_dictionary:
    print(f"The name is {my_dictionary['name']}")

# my_dictionary["age"] = 30
if "age" in my_dictionary:
    print(f"The age is {my_dictionary['age']}")
else:
    print("The key age is not in my_dictionary")

# creating a dictionary with pre-set values
another_dict = {0: "Zero", 1: "One", "name": "ikkebr"}

# printing the all the keys
print(another_dict.keys())

# printing all the values
print(another_dict.values())

# printing all (key, values)
print(another_dict.items())
